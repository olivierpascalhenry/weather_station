import os
import math
import stat
import time
import ephem
import shutil
import socket
import logging
import pathlib
import datetime
import psycopg2
import requests
import platform
import numpy as np
from zipfile import ZipFile
from distutils.version import LooseVersion
from PyQt5 import QtCore, QtGui
from functions.utils import (set_size, mpl_hour_list, angle_moon_phase, get_season, days_months_dictionary,
                             define_time_ticks)


class CleaningThread(QtCore.QThread):

    def __init__(self, db_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CleaningThread - __init__')
        self.running = False
        self.sensor_dict = sensor_dict
        self.routine_rate = 3600 * 1000
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.clean_db)
        self.started.connect(self.start_routine)
        # self.start()

    def start_routine(self):
        logging.debug(f'gui - other_threads.py - CleaningThread - start_routine')
        self.running = True
        self.clean_db()
        self.thread_timer.start(self.routine_rate)

    def clean_db(self):
        logging.debug('gui - other_threads.py - CleaningThread - clean_db')
        try:
            time_limit = datetime.datetime.now() - datetime.timedelta(hours=48)
            if platform.system() == 'Windows':
                for table in ['BME280_TEST', 'DS18B20_TEST', 'AQARA_THP_TEST']:
                    self.cursor.execute(f'DELETE FROM "{table}" WHERE date_time <= %s', (time_limit,))

            for device, ddict in self.sensor_dict['DS18B20'].items():
                table = ddict['table']
                time_limit = datetime.datetime.now() - datetime.timedelta(hours=int(ddict['store']))
                self.cursor.execute(f'DELETE FROM "{table}" WHERE date_time <= %s', (time_limit,))

            for device, ddict in self.sensor_dict['BME280'].items():
                table = ddict['table']
                time_limit = datetime.datetime.now() - datetime.timedelta(hours=int(ddict['store']))
                self.cursor.execute(f'DELETE FROM "{table}" WHERE date_time <= %s', (time_limit,))

            for device, ddict in self.sensor_dict['MQTT']['devices'].items():
                time_limit = datetime.datetime.now() - datetime.timedelta(hours=int(ddict['store']))
                self.cursor.execute(f'DELETE FROM "{device}" WHERE date_time <= %s', (time_limit,))

            self.connector.commit()
        except Exception:
            logging.exception('gui - other_threads.py - CleaningThread - clean_db - an exception '
                              'occurred when cleaning db')

    def stop(self):
        logging.debug('gui - other_threads.py - CleaningThread - stop')
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug(f'gui - other_threads.py - CleaningThread - stop - qtimer stopped / db closed')
        self.running = False
        self.exit()


class CheckUpdate(QtCore.QThread):
    finished = QtCore.pyqtSignal(dict)

    def __init__(self, gui_version):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CheckUpdate - __init__')
        self.gui_version = gui_version
        self.url_dict = {}

    def run(self):
        logging.debug('gui - other_threads.py - CheckUpdate - run')
        self.update_request()
        self.stop()

    def update_request(self):
        logging.debug('gui - other_threads.py - CheckUpdate - update_request')
        url = 'https://api.github.com/repos/olivierpascalhenry/weather_station/releases'
        try:
            json_object = requests.get(url=url, timeout=5).json()[0]
            if LooseVersion(self.gui_version) < LooseVersion(json_object['tag_name']):
                self.url_dict['file'] = json_object['assets'][0]['name']
                self.url_dict['url'] = json_object['assets'][0]['url']
            self.finished.emit(self.url_dict)
        except Exception:
            logging.exception('gui - other_threads.py - CheckUpdate - update_request - an exception occurred when '
                              'checking update')

    def stop(self):
        logging.debug('gui - other_threads.py - CheckUpdate - stop')
        self.exit()


class DownloadFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(dict)
    download_done = QtCore.pyqtSignal(dict)
    download_failed = QtCore.pyqtSignal()
    objectName = 'DownloadFile'

    def __init__(self, url, update_file):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - other_threads.py - DownloadFile - __init__ - url: {url}')

        self.url = url
        self.update_file = update_file
        self.filename = pathlib.Path(update_file).name
        self.cancel = False

    def run(self):
        logging.debug('gui - other_threads.py - DownloadFile - run')
        self.download_request()

    def download_request(self):
        logging.debug('gui - other_threads.py - DownloadFile - download_request')
        update_dict = {'bar_value': 0, 'bar_text': f'Downloading {self.filename}',
                       'browser_text': f'Téléchargement du fichier de mise à jour :\n      {self.filename}'}
        self.download_update.emit(update_dict)
        opened_file = open(self.update_file, 'wb')
        try:
            headers = {"Accept": 'application/octet-stream'}
            opened_url = requests.get(self.url, timeout=5, headers=headers, stream=True)
            total_file_size = int(opened_url.headers['Content-length'])
            buffer_size = 8192
            file_size = 0
            start = time.time()
            for chunk in opened_url.iter_content(chunk_size=buffer_size):
                if self.cancel:
                    opened_file.close()
                    break
                opened_file.write(chunk)
                file_size += len(chunk)
                try:
                    download_speed = set_size(file_size / (time.time() - start)) + '/s'
                except ZeroDivisionError:
                    download_speed = '0 B/s'
                update_dict = {'bar_value': round(file_size * 100 / total_file_size),
                               'bar_text': f'Downloading {self.filename} at {download_speed}',
                               'browser_text': None}
                self.download_update.emit(update_dict)
            opened_file.close()
            if not self.cancel:
                logging.debug('gui - other_threads.py - DownloadFile - run - download finished')
                update_dict = {'bar_value': 100,
                               'bar_text': 'Download finished',
                               'browser_text': 'Le fichier de mise à jour a été téléchargé'}
                self.download_done.emit(update_dict)
            else:
                logging.debug('gui - other_threads.py - DownloadFile - run - download canceled')
        except Exception as e:
            logging.exception(f'gui - other_threads.py - DownloadFile - run - connexion issue - self.url: {self.url}')
            opened_file.close()
            self.download_failed.emit()

    def cancel_process(self):
        logging.debug('gui - other_threads.py - DownloadFile - cancel_process')
        self.cancel = True

    def stop(self):
        logging.debug('gui - other_threads.py - DownloadFile - stop')
        self.exit()


class UnzipFile(QtCore.QThread):
    unzip_update = QtCore.pyqtSignal(dict)
    unzip_done = QtCore.pyqtSignal(dict)
    unzip_failed = QtCore.pyqtSignal()
    objectName = 'UnzipFile'

    def __init__(self, update_file, temp_folder):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - other_threads.py - UnzipFile - __init__ - update_file: {update_file} ; '
                     f'temp_folder: {temp_folder}')
        self.temp_folder = temp_folder
        self.update_file = update_file
        self.filename = pathlib.Path(update_file).name
        self.cancel = False
        self.archive = None

    def run(self):
        logging.debug('gui - other_threads.py - UnzipFile - run')
        update_dict = {'bar_value': 0, 'bar_text': f'Extracting {self.filename}',
                       'browser_text': f'Décompression du fichier de mise à jour :\n      {self.filename}'}
        self.unzip_update.emit(update_dict)
        try:
            self.archive = ZipFile(self.update_file)
            members = self.archive.infolist()
            mem_nbr = len(members)
            for i, file in enumerate(members):
                update_dict = {'bar_value': round(((i + 1) / mem_nbr) * 100),
                               'bar_text': f'Extracting {pathlib.Path(file.filename).name}',
                               'browser_text': None}
                self.archive.extract(file, path=self.temp_folder)
                self.unzip_update.emit(update_dict)
                if self.cancel:
                    break
            self.archive.close()
            if not self.cancel:
                logging.debug('gui - other_threads.py - UnzipFile - run - unzip finished')

                update_dict = {'bar_value': 100,
                               'bar_text': 'Extracting finished',
                               'browser_text': 'Le fichier de mise à jour a été décompressé'}
                self.unzip_done.emit(update_dict)
            else:
                logging.debug('gui - other_threads.py - UnzipFile - run - unzip canceled')
        except Exception as e:
            logging.exception(f'gui - other_threads.py - UnzipFile - run - an issue occured during extracting')
            self.archive.close()
            self.unzip_failed.emit()

    def cancel_process(self):
        logging.debug('gui - other_threads.py - UnzipFile - cancel_process')
        self.cancel = True

    def stop(self):
        logging.debug('gui - other_threads.py - UnzipFile - stop')
        self.exit()


class InstallFile(QtCore.QThread):
    install_update = QtCore.pyqtSignal(dict)
    install_done = QtCore.pyqtSignal(dict)
    install_failed = QtCore.pyqtSignal()
    objectName = 'InstallFile'

    def __init__(self, temp_folder, dest_folder):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - other_threads.py - InstallFile - __init__ - temp_folder: {temp_folder} ; '
                     f'dest_folder: {dest_folder}')
        self.temp_folder = temp_folder
        self.dest_folder = dest_folder
        self.cancel = False

    def run(self):
        logging.debug('gui - other_threads.py - InstallFile - run')
        update_dict = {'bar_value': 0, 'bar_text': f'Installing update',
                       'browser_text': f'Installation de la mise à jour'}
        self.install_update.emit(update_dict)
        try:
            for filename in os.listdir(self.dest_folder):
                file_path = os.path.join(self.dest_folder, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            if self.temp_folder.joinpath('weather_station').exists():
                self.temp_folder = self.temp_folder.joinpath('weather_station')
            file_list = sorted(self.temp_folder.glob('**/*'))
            file_nbr = len(file_list)
            for i, file in enumerate(file_list):
                update_dict = {'bar_value': round(((i + 1) / file_nbr) * 100),
                               'bar_text': f'Installing {file.name}',
                               'browser_text': None}
                orig_file = str(file)
                dest_file = orig_file.replace(str(self.temp_folder), str(self.dest_folder))
                logging.info(f'PATHLIB : file {file} ; dest_file {dest_file}')
                if file.is_dir():
                    if not pathlib.Path(dest_file).exists():
                        pathlib.Path(dest_file).mkdir(exist_ok=True)
                else:
                    shutil.copy2(orig_file, dest_file)
                    if pathlib.Path(dest_file).name == 'weather_station':
                        st = os.stat(dest_file)
                        os.chmod(dest_file, st.st_mode | stat.S_IEXEC)
                self.install_update.emit(update_dict)
            logging.debug('gui - other_threads.py - InstallFile - run - install finished')
            update_dict = {'bar_value': 100,
                           'bar_text': 'Installation finished',
                           'browser_text': 'La mise à jour a été installée'}
            self.install_done.emit(update_dict)
        except Exception as e:
            logging.exception(f'gui - other_threads.py - InstallFile - run - an issue occured during installation')
            self.install_failed.emit()

    def stop(self):
        logging.debug('gui - other_threads.py - InstallFile - stop')
        self.exit()


class RebootingThread(QtCore.QThread):
    reboot_update = QtCore.pyqtSignal(dict)
    reboot_done = QtCore.pyqtSignal(dict)

    def __init__(self):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - RebootingThread - __init__')

    def run(self):
        logging.debug('gui - other_threads.py - RebootingThread - run')
        update_dict = {'bar_value': 0, 'bar_text': 'Rebooting in 5s',
                       'browser_text': f'Redémarrage du Raspberry Pi dans 5 secondes'}
        self.reboot_update.emit(update_dict)
        j = 5
        for i in range(5):
            update_dict = {'bar_value': i * 20, 'bar_text': f'Rebooting in {j}s', 'browser_text': None}
            self.reboot_update.emit(update_dict)
            time.sleep(1)
            j -= 1
        update_dict = {'bar_value': 100, 'bar_text': 'Rebooting now',
                       'browser_text': f'Redémarrage du Raspberry Pi'}
        self.reboot_done.emit(update_dict)

    def stop(self):
        logging.debug('gui - other_threads.py - RebootingThread - stop')
        self.exit()


class CheckInternetConnexion(QtCore.QThread):
    connexion_alive = QtCore.pyqtSignal()
    no_connexion = QtCore.pyqtSignal()
    time_dict = {'secondes': 1, 'minutes': 60, 'hours': 3600}

    def __init__(self, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CheckInternetConnexion - __init__')
        self.config_dict = config_dict
        self.ip_address = '1.1.1.1'

    def run(self):
        logging.debug('gui - other_threads.py - CheckInternetConnexion - run')
        if self.config_dict.getboolean('SYSTEM', 'auto_check_connexion'):
            time_factor = self.time_dict[self.config_dict.get('SYSTEM', 'auto_connexion_unit')]
            time_sleep = int(self.config_dict.get('SYSTEM', 'auto_connexion_value')) * time_factor
            while True:
                try:
                    socket.create_connection((self.ip_address, 53))
                    self.connexion_alive.emit()
                    break
                except OSError:
                    logging.exception('no connectivity detected')
                    self.no_connexion.emit()
                time.sleep(time_sleep)
        else:
            try:
                socket.create_connection((self.ip_address, 53))
                self.connexion_alive.emit()
            except OSError:
                logging.exception('no connectivity detected')
                self.no_connexion.emit()

    def stop(self):
        logging.debug('gui - other_threads.py - CheckInternetConnexion - stop')
        self.exit()


class CheckPostgresqlConnexion(QtCore.QThread):
    postgresql_ok = QtCore.pyqtSignal()
    postgresql_failed = QtCore.pyqtSignal(str)

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CheckPostgresqlConnexion - __init__')
        self.db_dict = db_dict

    def run(self):
        logging.debug('gui - other_threads.py - CheckPostgresqlConnexion - run')
        try:
            connector = psycopg2.connect(user=self.db_dict['user'], password=self.db_dict['password'],
                                         host=self.db_dict['host'], database=self.db_dict['database'],
                                         port=self.db_dict['port'], connect_timeout=1)
            connector.close()
            logging.debug('gui - other_threads.py - CheckPostgresqlConnexion - postgresql connexion is ok')
            self.postgresql_ok.emit()
        except psycopg2.OperationalError as e:
            logging.exception('gui - other_threads.py - CheckPostgresqlConnexion - issue with postgresql')
            if 'Connection refused' in str(e):
                msg = ('La connection à PostgreSQL a été explicitement refusée. Veuillez vérifier  son installation et '
                       'son fonctionnement, ainsi que les paramètres de connexion (adresse et port).')
            elif f'database "{self.db_dict["database"]}"' in str(e):
                msg = (f'La base de données {self.db_dict["database"]} n\'a pas été trouvée. Veuillez vérifier qu\'elle'
                       ' existe et les paramètres de connexion (nom de la base de données)')
            elif f'password authentication failed for user "{self.db_dict["user"]}"' in str(e):
                msg = (f'La connexion a PostgreSQL a été refusée pour l\'utilisateur {self.db_dict["user"]}. Veuillez '
                       f'vérifier qu\'il existe et les paramètres de connexion (nom d\'utilisateur et mot de passe)')
            elif f'could not translate host name "{self.db_dict["host"]}" to address' in str(e):
                msg = ('La connection à PostgreSQL a été explicitement refusée. Veuillez vérifier les paramètres de '
                       'connexion (adresse et port).')
            elif 'timeout expired' in str(e):
                msg = ('La connexion à PostgreSQL a échoué. Veuillez vérifier les paramètres de connexion '
                       '(adresse et port).')
            elif 'no password supplied' in str(e):
                msg = ('La connexion à PostgreSQL a échoué. Veuillez vérifier les paramètres de connexion '
                       '(adresse, port, utilisateur et mot de passe).')
            else:
                msg = 'La connexion à PostgreSQL a échoué. Veuillez lire le log pour obtenir des détails sur cet échec.'
            self.postgresql_failed.emit(msg)
        except:
            logging.exception('gui - other_threads.py - CheckPostgresqlConnexion - issue with postgresql')
            msg = 'La connexion à PostgreSQL a échoué. Veuillez lire le log pour obtenir des détails sur cet échec.'
            self.postgresql_failed.emit(msg)

    def stop(self):
        logging.debug('gui - other_threads.py - CheckPostgresqlConnexion - stop')
        self.exit()


class DBTableManager(QtCore.QThread):
    work_done = QtCore.pyqtSignal()
    work_failed = QtCore.pyqtSignal(str)

    def __init__(self, db_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - DBTableManager - __init__')
        self.db_dict = db_dict
        self.sensor_dict = sensor_dict

    def run(self):
        logging.debug('gui - other_threads.py - DBTableManager - run')
        try:
            ds18_dict = self.sensor_dict['DS18B20']
            bme280_dict = self.sensor_dict['BME280']
            mqtt_dict = self.sensor_dict['MQTT']['devices']
            table_list = []
            connector = psycopg2.connect(user=self.db_dict['user'], password=self.db_dict['password'],
                                         host=self.db_dict['host'], database=self.db_dict['database'],
                                         port=self.db_dict['port'], connect_timeout=1)
            cursor = connector.cursor()
            cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
            db_table_list = [table[0] for table in cursor.fetchall()]
            fl_table_list = []
            for device, _ in mqtt_dict.items():
                fl_table_list.append(device)
                if device not in table_list:
                    query = (f'CREATE TABLE IF NOT EXISTS public."{device}" (date_time timestamp without time zone NOT '
                             f'NULL, temperature real, humidity real, pressure real, pressure_msl real, battery real, '
                             f'signal real, CONSTRAINT "{device}_pkey" PRIMARY KEY (date_time)) TABLESPACE pg_default;'
                             f'ALTER TABLE public."{device}" OWNER to weather_station;')
                    cursor.execute(query)
                    connector.commit()

            for device, ddict in ds18_dict.items():
                fl_table_list.append(ddict['table'])
                if ddict['table'] and ddict['table'] not in table_list:
                    query = (f'CREATE TABLE IF NOT EXISTS public."{ddict["table"]}" (date_time timestamp without '
                             f'time zone NOT NULL, temperature real, humidity real, pressure real, pressure_msl real,'
                             f' battery real, signal real, CONSTRAINT "{ddict["table"]}_pkey" PRIMARY KE'
                             f'Y (date_time)) TABLESPACE pg_default; ALTER TABLE public."{ddict["table"]}" OWNER to '
                             f'weather_station;')
                    cursor.execute(query)
                    connector.commit()

            for device, ddict in bme280_dict.items():
                fl_table_list.append(ddict['table'])
                if ddict['table'] and ddict['table'] not in table_list:
                    query = (f'CREATE TABLE IF NOT EXISTS public."{ddict["table"]}" (date_time timestamp without '
                             f'time zone NOT NULL, temperature real, humidity real, pressure real, pressure_msl real,'
                             f'CONSTRAINT "{ddict["table"]}_pkey" PRIMARY KEY (date_time)) TABLESPACE '
                             f'pg_default; ALTER TABLE public."{ddict["table"]}" OWNER to weather_station;')
                    cursor.execute(query)
                    connector.commit()

            for table in db_table_list:
                if table not in fl_table_list and 'TEST' not in table:
                    query = f'drop TABLE public."{table}";'
                    cursor.execute(query)
                    connector.commit()

            cursor.close()
            connector.close()
            self.work_done.emit()
        except:
            logging.exception('gui - other_threads.py - CheckPostgresqlConnexion - issue with postgresql')
            msg = ('La gestion des tables des différents capteurs a échoué. Veuillez lire le log pour obtenir des '
                   'détails sur cet échec.')
            self.work_failed.emit(msg)

    def stop(self):
        logging.debug('gui - other_threads.py - CheckPostgresqlConnexion - stop')
        self.exit()


class RequestPlotDataThread(QtCore.QThread):
    success = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(str)

    def __init__(self, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - RequestPlotDataThread - __init__')
        self.config_dict = config_dict
        self.sensor_dict = sensor_dict
        self.now = datetime.datetime.now()
        self.limit = self.now - datetime.timedelta(hours=24)
        self.connector = psycopg2.connect(user=self.config_dict.get('DATABASE', 'username'),
                                          password=self.config_dict.get('DATABASE', 'password'),
                                          host=self.config_dict.get('DATABASE', 'host'),
                                          database=self.config_dict.get('DATABASE', 'database'),
                                          port=self.config_dict.get('DATABASE', 'port'))
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - run')
        try:
            in_temp_table, in_hum_table = self.get_device_table('in')
            out_temp_table, out_pres_table = self.get_device_table('out')
            data_dict = {'temp_in': self.query_table_for_data('temperature', in_temp_table, self.limit),
                         'temp_out': self.query_table_for_data('temperature', out_temp_table, self.limit),
                         'hum_in': self.query_table_for_data('humidity', in_hum_table, self.limit)}
            if self.config_dict.getboolean('TIMESERIES', 'msl_pressure'):
                data_dict['pres_out'] = self.query_table_for_data('pressure_msl', out_pres_table, self.limit)
            else:
                data_dict['pres_out'] = self.query_table_for_data('pressure_msl', out_pres_table, self.limit)
            self.cursor.close()
            self.connector.close()
            self.success.emit(data_dict)
        except:
            logging.exception('gui - other_threads.py - RequestPlotDataThread - plot_data - an exception occurred '
                              'when ploting data')
            self.error.emit('Une erreur lors de la requête empêche\nl\'affichage des séries temporelles')
            self.cursor.close()
            self.connector.close()

    def get_device_table(self, zone):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - get_device_table')
        zone_dict = {'in': {'table_1': 'in_temperature', 'table_2': 'in_humidity'},
                     'out': {'table_1': 'out_temperature', 'table_2': 'out_pressure'}}
        table_1, table_2 = None, None
        if self.config_dict.get('TIMESERIES', zone_dict[zone]['table_1']):
            table_1 = self.get_table(self.config_dict.get('TIMESERIES', zone_dict[zone]['table_1']))
        if self.config_dict.get('TIMESERIES', zone_dict[zone]['table_2']):
            table_2 = self.get_table(self.config_dict.get('TIMESERIES', zone_dict[zone]['table_2']))
        return table_1, table_2

    def get_table(self, device_name):
        logging.debug(f'gui - other_threads.py - RequestPlotDataThread - get_table - device_name: {device_name}')
        table = None
        if platform.system() == 'Windows':
            table = device_name
        else:
            for _, ddict in self.sensor_dict['DS18B20'].items():
                if device_name == ddict['name']:
                    table = ddict['table']
                    break
            if table is None:
                for _, ddict in self.sensor_dict['BME280'].items():
                    if device_name == ddict['name']:
                        table = ddict['table']
                        break
            if table is None:
                for device, _ in self.sensor_dict['MQTT']['devices'].items():
                    if device_name == device:
                        table = device
                        break
        return table

    def query_table_for_data(self, column, table, time_limit):
        logging.debug(f'gui - other_threads.py - RequestPlotDataThread - query_table_for_data - column: {column} ; '
                      f'table: {table} ; time_limit: {time_limit} ;')
        data_x, data_y = None, None
        self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'")
        column_list = [column[0] for column in self.cursor.fetchall()]
        if column in column_list:
            self.cursor.execute(f'select date_time, {column} from "{table}"  where '
                                f"date_time>='{time_limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY date_time")
            data = self.cursor.fetchall()
            data_x = np.asarray([x[0] for x in data])
            data_y = np.asarray([x[1] for x in data], dtype=np.float32)
        return data_x, data_y

    def stop(self):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - stop')
        self.cursor.close()
        self.connector.close()
        self.exit()


class PlotDataThread(QtCore.QThread):
    success = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(str)

    def __init__(self, plot_in, plot_in_2, plot_out, plot_out_2, canvas_in, canvas_out, val_dict, first_plot):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - PlotDataThread - __init__')
        self.plot_in = plot_in
        self.plot_in_2 = plot_in_2
        self.plot_out = plot_out
        self.plot_out_2 = plot_out_2
        self.canvas_in = canvas_in
        self.canvas_out = canvas_out
        self.val_dict = val_dict
        self.first_plot = first_plot

    def run(self):
        logging.debug('gui - other_threads.py - PlotDataThread - run')
        try:
            color_1, color_2, color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
            tick_list, label_list = define_time_ticks(self.val_dict['temp_in'][0][-1])
            if self.first_plot:
                self.plot_in.plot(self.val_dict['temp_in'][0], self.val_dict['temp_in'][1], color=color_1,
                                  linewidth=1.)
                self.plot_in_2.plot(self.val_dict['hum_in'][0], self.val_dict['hum_in'][1], color=color_2,
                                    linewidth=1.)
                self.plot_out.plot(self.val_dict['temp_out'][0], self.val_dict['temp_out'][1], color=color_1,
                                   linewidth=1.)
                self.plot_out_2.plot(self.val_dict['pres_out'][0], self.val_dict['pres_out'][1], color=color_3,
                                     linewidth=1.)
                self.first_plot = False
            else:
                self.plot_in.lines.pop(0)
                self.plot_in.plot(self.val_dict['temp_in'][0], self.val_dict['temp_in'][1], color=color_1,
                                  linewidth=1.)
                self.plot_in_2.lines.pop(0)
                self.plot_in_2.plot(self.val_dict['hum_in'][0], self.val_dict['hum_in'][1], color=color_2,
                                    linewidth=1.)
                self.plot_out.lines.pop(0)
                self.plot_out.plot(self.val_dict['temp_out'][0], self.val_dict['temp_out'][1], color=color_1,
                                   linewidth=1.)
                self.plot_out_2.lines.pop(0)
                self.plot_out_2.plot(self.val_dict['pres_out'][0], self.val_dict['pres_out'][1], color=color_3,
                                     linewidth=1.)
            self.plot_in.set_xlim(tick_list[0], tick_list[-1])
            self.plot_out.set_xlim(tick_list[0], tick_list[-1])
            self.plot_in.set_xticks(tick_list)
            self.plot_out.set_xticks(tick_list)
            self.plot_in.set_xticklabels(label_list)
            self.plot_out.set_xticklabels(label_list)
            self.canvas_in.draw()
            self.canvas_out.draw()

            self.success.emit()
        except:
            logging.exception('gui - other_threads.py - PlotDataThread - run - an error occured when plotting data')
            self.error.emit('Une erreur lors du traçage des données\nempêche l\'affichage des séries temporelles')

    def stop(self):
        logging.debug('gui - other_threads.py - PlotDataThread - stop')
        self.exit()


class ComputeEphemerisThread(QtCore.QThread):
    work_done = QtCore.pyqtSignal(dict)

    def __init__(self, longitude, latitude):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - ComputeEphemerisThread - __init__')
        self.longitude = str(longitude)
        self.latitude = str(latitude)
        self.running = False
        self.computation_rate = 60 * 30 * 1000
        self.observer, self.moon, self.sun = ephem.Observer(),  ephem.Moon(), ephem.Sun()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.compute_data)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - other_threads.py - ComputeEphemerisThread - start_routine')
        self.running = True
        self.compute_data()
        self.thread_timer.start(self.computation_rate)

    def compute_data(self):
        logging.debug('gui - other_threads.py - ComputeEphemerisThread - run')
        try:
            current_date = datetime.datetime.now()
            sunrise_6days, sunset_6days = [], []
            self.observer.lat, self.observer.lon, self.observer.date = self.latitude, self.longitude, current_date
            self.sun.compute(self.observer)
            self.moon.compute(self.observer)
            sunlon = ephem.Ecliptic(self.sun).lon / math.pi * 180.0
            moonlon = ephem.Ecliptic(self.moon).lon / math.pi * 180.0
            if sunlon >= moonlon:
                angle = sunlon - moonlon
            else:
                angle = 360. + (sunlon - moonlon)
            angle_dict = angle_moon_phase()
            angle_list = [a for a in angle_dict]
            svg = None
            for i in range(len(angle_list) - 1):
                if angle_list[i] <= angle < angle_list[i + 1]:
                    svg = angle_dict[angle_list[i]]
                    break

            next_date = current_date
            for i in range(0, 6):
                sunrise = ephem.localtime(self.observer.next_rising(self.sun, start=next_date.strftime('%Y/%m/%d')))
                sunset = ephem.localtime(self.observer.next_setting(self.sun, start=next_date.strftime('%Y/%m/%d')))
                sunrise_6days.append(sunrise)
                sunset_6days.append(sunset)
                next_date += datetime.timedelta(days=1)

            sunlive = sunset_6days[0] - sunrise_6days[0]
            moonrise = ephem.localtime(self.observer.next_rising(self.moon, start=current_date.strftime('%Y/%m/%d')))
            moonset = ephem.localtime(self.observer.next_setting(self.moon, start=current_date.strftime('%Y/%m/%d')))
            h, m = str(sunlive.seconds // 3600), str((sunlive.seconds // 60) % 60)
            if len(h) == 1:
                h = '0' + h
            if len(m) == 1:
                m = '0' + m
            day_box_title = (f'{days_months_dictionary()["day"][current_date.weekday() + 1]} '
                             f'{current_date.day} '
                             f'{days_months_dictionary()["month"][current_date.month]} '
                             f'{current_date.year}')
            if current_date.timetuple().tm_yday == 1:
                day_year = f'{current_date.timetuple().tm_yday}er jour de l’année'
            else:
                day_year = f'{current_date.timetuple().tm_yday}ème jour de l’année'
            data_dict = {'day_box_title': day_box_title,
                         'day_year': day_year,
                         'week_nbr': f'Semaine {current_date.isocalendar()[1]}',
                         'season': get_season(current_date),
                         'sun_text': (f'Le Soleil se lève à {sunrise_6days[0].strftime("%Hh%M")} '
                                      f'et se couche à {sunset_6days[0].strftime("%Hh%M")}'),
                         'sun_live': f'Durée d’ensoleillement: {h}h{m}',
                         'moon_text': (f'La Lune se lève à {moonrise.strftime("%Hh%M")} '
                                       f'et se couche à {moonset.strftime("%Hh%M")}'),
                         'moon_phase': QtGui.QPixmap(f'graphic_materials/pictogrammes/moon_phases/{svg}'),
                         'sunrise_6days': sunrise_6days, 'sunset_6days': sunset_6days}
            self.work_done.emit(data_dict)
        except:
            logging.exception('gui - other_threads.py - ComputeEphemerisThread - run - an exception '
                              'occurred when computing ephemeris data')

    def stop(self):
        logging.debug('gui - other_threads.py - ComputeEphemerisThread - stop')
        self.thread_timer.stop()
        self.running = False
        self.exit()
