import time
import socket
import logging
import pathlib
import datetime
import psycopg2
import requests
import platform
from distutils.version import LooseVersion
from numpy import min, max, linspace
from PyQt5 import QtCore
from functions.utils import set_size, mpl_hour_list, db_data_to_mpl_vectors, check_postgresql_server


username = 'olivierpascalhenry'
token = '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'


class CleaningThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CleaningThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - other_threads.py - CleaningThread - run')
        self.clean_db()

    def clean_db(self):
        logging.debug('gui - other_threads.py - CleaningThread - clean_db')
        while True:
            try:
                time_limit = datetime.datetime.now() - datetime.timedelta(hours=48)
                for table in ['BME280_TEST', 'DS18B20_TEST', 'AQARA_THP_TEST']:
                    self.cursor.execute(f'DELETE FROM "{table}" WHERE date_time <= %s', (time_limit,))
                self.connector.commit()
            except Exception:
                logging.exception('gui - other_threads.py - CleaningThread - clean_db - an exception '
                                  'occurred when cleaning db')
            time.sleep(3600)

    def stop(self):
        logging.debug('gui - other_threads.py - CleaningThread - stop')
        self.connector.close()
        self.terminate()


class CheckUpdate(QtCore.QThread):
    finished = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, gui_version):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CheckUpdate - __init__')
        self.gui_version = gui_version
        self.url_dict = {}

    def run(self):
        logging.debug('gui - other_threads.py - CheckUpdate - run')
        self.update_request()

    def update_request(self):
        logging.debug('gui - other_threads.py - CheckUpdate - update_request')
        url = 'https://api.github.com/repos/olivierpascalhenry/weather_station/releases'
        try:
            gh_session = requests.Session()
            gh_session.auth = (username, token)
            json_object = gh_session.get(url=url, timeout=5).json()[0]
            if LooseVersion(self.gui_version) < LooseVersion(json_object['tag_name']):
                self.url_dict['file'] = json_object['assets'][0]['name']
                self.url_dict['url'] = json_object['assets'][0]['url']
            self.finished.emit(self.url_dict)
        except Exception:
            logging.exception('gui - other_threads.py - CheckUpdate - update_request - an exception occurred when '
                              'requesting update')

    def stop(self):
        logging.debug('gui - other_threads.py - CheckUpdate - stop')
        self.terminate()


class DownloadFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal(list)

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
        download_text = 'Downloading %s at %s'
        pre_download_text = 'Downloading %s'
        self.download_update.emit([0, pre_download_text % self.filename])
        opened_file = open(self.update_file, 'wb')
        try:
            headers = {"Authorization": 'token ' + token, "Accept": 'application/octet-stream'}
            gh_session = requests.Session()
            gh_session.auth = (username, token)
            opened_url = gh_session.get(self.url, timeout=5, headers=headers, stream=True)
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
                    download_speed = '0b/s'
                self.download_update.emit([round(file_size * 100 / total_file_size),
                                           download_text % (self.filename, download_speed)])
            opened_file.close()
            if not self.cancel:
                logging.debug('gui - other_threads.py - DownloadFile - run - download finished')
                self.download_done.emit()
            else:
                logging.debug('gui - other_threads.py - DownloadFile - run - download canceled')
        except Exception as e:
            logging.exception('gui - other_threads.py - DownloadFile - run - connexion issue ; self.url '
                              + self.url)
            opened_file.close()
            self.download_failed.emit(['download thread', e])

    def cancel_download(self):
        logging.debug('gui - other_threads.py - DownloadFile - cancel_download')
        self.cancel = True

    def stop(self):
        logging.debug('gui - other_threads.py - DownloadFile - stop')
        self.terminate()


class CheckInternetConnexion(QtCore.QThread):
    connexion_alive = QtCore.pyqtSignal()
    no_connexion = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CheckInternetConnexion - __init__')
        self.ip_address = '1.1.1.1'

    def run(self):
        logging.debug('gui - other_threads.py - CheckInternetConnexion - run')
        try:
            socket.create_connection((self.ip_address, 53))
            self.connexion_alive.emit()
        except OSError:
            time.sleep(3)
            self.no_connexion.emit()

    def stop(self):
        logging.debug('gui - other_threads.py - CheckInternetConnexion - stop')
        self.terminate()


class CheckPostgresqlConnexion(QtCore.QThread):
    results = QtCore.pyqtSignal(list)

    def __init__(self, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - CheckPostgresqlConnexion - __init__')
        self.sensor_dict = sensor_dict

    def run(self):
        logging.debug('gui - other_threads.py - CheckPostgresqlConnexion - run')

        installed, database, tables = False, False, False
        if platform.system() == 'Linux':
            res = subprocess.run(['which', 'psql'])
            if res.returncode == 0:
                installed = True
            else:
                logging.error('gui - other_threads.py - CheckPostgresqlConnexion - which -s psql returned 1, '
                              'postgresql is not installed')
        else:
            installed = True
        if installed:
            try:
                connector = psycopg2.connect(user='weather_station', password='31weather64', host='127.0.0.1',
                                             database='weather_station_db', connect_timeout=1)
                database = True
                connector.close()
            except psycopg2.OperationalError:
                logging.error('gui - other_threads.py - CheckPostgresqlConnexion - database is not installed')

        if installed and database:
            ds18_dict = self.sensor_dict['DS18B20']
            bme280_dict = self.sensor_dict['BME280']
            mqtt_dict = self.sensor_dict['MQTT']['devices']
            table_list = []
            connector = psycopg2.connect(user='weather_station', password='31weather64', host='127.0.0.1',
                                         database='weather_station_db', connect_timeout=1)
            cursor = connector.cursor()
            cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
            for table in cursor.fetchall():
                table_list = table[0]

            for device, ddict in mqtt_dict.items():
                if device not in table_list:
                    query = (f'CREATE TABLE IF NOT EXISTS public."{device}" (date_time timestamp without time zone NOT '
                             f'NULL, temperature real, humidity real, pressure real, battery real, signal real, '
                             f'CONSTRAINT "{device}_pkey" PRIMARY KEY (date_time)) TABLESPACE pg_default;'
                             f'ALTER TABLE public."{device}" OWNER to weather_station;')
                    cursor.execute(query)
                    connector.commit()
            cursor.close()
            connector.close()
        self.results.emit([installed, database])

    def stop(self):
        logging.debug('gui - other_threads.py - CheckPostgresqlConnexion - stop')
        self.terminate()


class RequestPlotDataThread(QtCore.QThread):
    success = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal()

    def __init__(self, canvas_in, canvas_out, plot_in_1, plot_in_2, plot_out_1, plot_out_2, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - RequestPlotDataThread - __init__')
        self.canvas_in = canvas_in
        self.canvas_out = canvas_out
        self.plot_in_1 = plot_in_1
        self.plot_in_2 = plot_in_2
        self.plot_out_1 = plot_out_1
        self.plot_out_2 = plot_out_2
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - run')
        self.request_plot_data()

    def request_plot_data(self):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - request_plot_data')
        try:
            color_1, color_2, color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
            ticks_labels = ['-24h', '', ' ', '', '-20h', '', ' ', '', '-16h', '', ' ', '', '-12h', '', ' ',
                            '', '-8h', '', ' ', '', '-4h', '', ' ', '', 'Now']

            hours_list = mpl_hour_list()
            now = datetime.datetime.now()
            limit = now - datetime.timedelta(hours=24)
            self.cursor.execute(f'select date_time, temperature from "BME280"  where '
                                f"date_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY date_time")
            temp_in_x, temp_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute(f'select date_time, temperature from "AQARA_THP" where '
                                f"date_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY date_time")
            temp_out_x, temp_out_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute(f'select date_time, humidite from "BME280" where '
                                f"date_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY date_time")
            hum_in_x, hum_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute(f'select date_time, pressure from "AQARA_THP" where '
                                f"date_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY date_time")
            pres_in_x, pres_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())

            self.plot_in_1.clear()
            self.plot_in_2.clear()
            self.plot_out_1.clear()
            self.plot_out_2.clear()
            self.plot_in_1.set_ylabel('Température (°C)', color=color_1)
            self.plot_in_1.tick_params(axis='y', labelcolor=color_1)
            self.plot_in_2.set_ylabel('Humidité (%)', color=color_2)
            self.plot_in_2.tick_params(axis='y', labelcolor=color_2)
            self.plot_out_1.set_ylabel('Température (°C)', color=color_1)
            self.plot_out_1.tick_params(axis='y', labelcolor=color_1)
            self.plot_out_2.set_ylabel('Pression (hPa)', color=color_3)
            self.plot_out_2.tick_params(axis='y', labelcolor=color_3)
            self.plot_in_1.plot(temp_in_x, temp_in_y, color=color_1, linewidth=1.)

            if min(temp_in_y) < 10:
                y_min = min(temp_in_y) - 5
            else:
                y_min = 10
            if max(temp_in_y) > 30:
                y_max = max(temp_in_y) + 5
            else:
                y_max = 30

            self.plot_in_1.set_ylim(y_min, y_max)
            self.plot_in_2.plot(hum_in_x, hum_in_y, color=color_2, linewidth=1.)
            self.plot_in_2.set_ylim(0, 100)
            self.plot_in_1.set_xlim(limit, now)
            self.plot_in_1.set_xticks(hours_list)
            self.plot_in_1.set_xticklabels(ticks_labels)
            self.plot_out_1.plot(temp_out_x, temp_out_y, color=color_1, linewidth=1.)

            if min(temp_out_y) < 0:
                y_min = min(temp_out_y) - 5
            else:
                y_min = 0
            if max(temp_out_y) > 30:
                y_max = max(temp_out_y) + 5
            else:
                y_max = 30

            self.plot_out_1.set_ylim(y_min, y_max)
            self.plot_out_2.plot(pres_in_x, pres_in_y, color=color_3, linewidth=1.)

            if min(pres_in_y) < 990:
                y_min = min(pres_in_y) - 10
            else:
                y_min = 990
            if max(pres_in_y) > 1030:
                y_max = max(pres_in_y) + 10
            else:
                y_max = 1030

            self.plot_out_2.set_ylim(y_min, y_max)
            self.plot_out_1.set_xlim(limit, now)
            self.plot_out_1.set_xticks(hours_list)
            self.plot_out_1.set_xticklabels(ticks_labels)

            self.plot_in_2.set_yticks(linspace(self.plot_in_2.get_yticks()[0], self.plot_in_2.get_yticks()[-1],
                                               len(self.plot_in_1.get_yticks())))
            self.plot_out_2.set_yticks(linspace(self.plot_out_2.get_yticks()[0], self.plot_out_2.get_yticks()[-1],
                                                len(self.plot_out_1.get_yticks())))

            self.plot_in_1.grid(linestyle='-', linewidth=0.5, color='grey', alpha=0.5)
            self.plot_out_1.grid(linestyle='-', linewidth=0.5, color='grey', alpha=0.5)

            self.canvas_in.draw()
            self.canvas_out.draw()
            self.connector.close()
            self.success.emit()
        except Exception:
            logging.exception('gui - other_threads.py - RequestPlotDataThread - request_plot_data - an exception '
                              'occurred when ploting data')
            self.connector.close()
            self.error.emit()

    def stop(self):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - stop')
        self.connector.close()
        self.terminate()
