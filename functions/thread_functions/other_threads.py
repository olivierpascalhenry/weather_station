import logging
import datetime
import time
import psycopg2
import requests
import pathlib
import socket
from distutils.version import LooseVersion
import numpy as np
from PyQt5 import QtCore
from functions.utils import set_size, mpl_hour_list, db_data_to_mpl_vectors


username = 'olivierpascalhenry'
token = '***REMOVED***'


class CleaningThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - other_threads.py - CleaningThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - other_threads.py - CleaningThread - run')
        while True:
            try:
                time_limit = datetime.datetime.now() - datetime.timedelta(hours=48)
                self.cursor.execute('DELETE FROM "BME280" WHERE date_time <= %s', (time_limit, ))
                self.cursor.execute('DELETE FROM "DS18B20" WHERE date_time <= %s', (time_limit,))
                self.connector.commit()
            except Exception as e:
                self.error.emit(['cleaning data', e])
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
        logging.debug('gui - other_threads.py - CheckUpdate - __init__')
        self.gui_version = gui_version
        self.url_dict = {}

    def run(self):
        logging.debug('gui - other_threads.py - CheckUpdate - run')
        url = 'https://api.github.com/repos/olivierpascalhenry/weather_station/releases'
        try:
            gh_session = requests.Session()
            gh_session.auth = (username, token)
            json_object = gh_session.get(url=url, timeout=5).json()[0]
            if LooseVersion(self.gui_version) < LooseVersion(json_object['tag_name']):
                self.url_dict['file'] = json_object['assets'][0]['name']
                self.url_dict['url'] = json_object['assets'][0]['url']
            self.finished.emit(self.url_dict)
        except Exception as e:
            self.error.emit(['update request', e])

    def stop(self):
        logging.debug('gui - other_threads.py - CheckUpdate - stop')
        self.terminate()


class DownloadFile(QtCore.QThread):
    download_update = QtCore.pyqtSignal(list)
    download_done = QtCore.pyqtSignal()
    download_failed = QtCore.pyqtSignal(list)

    def __init__(self, url, update_file):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - DownloadFile - __init__ - url ' + str(url))
        self.url = url
        self.update_file = update_file
        self.filename = pathlib.Path(update_file).name
        self.cancel = False

    def run(self):
        logging.debug('gui - other_threads.py - DownloadFile - run')
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
        try:
            socket.create_connection((self.ip_address, 53))
            self.connexion_alive.emit()
        except OSError:
            time.sleep(3)
            self.no_connexion.emit()

    def stop(self):
        logging.debug('gui - other_threads.py - DownloadFile - stop')
        self.terminate()


class RequestPlotDataThread(QtCore.QThread):
    success = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(list)

    def __init__(self, canvas_in, canvas_out, plot_in_1, plot_in_2, plot_out_1, plot_out_2, cursor):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - RequestPlotDataThread - __init__')
        self.canvas_in = canvas_in
        self.canvas_out = canvas_out
        self.plot_in_1 = plot_in_1
        self.plot_in_2 = plot_in_2
        self.plot_out_1 = plot_out_1
        self.plot_out_2 = plot_out_2
        self.cursor = cursor

    def run(self):
        try:
            color_1, color_2, color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
            hours_list = mpl_hour_list()
            now = datetime.datetime.now()
            limit = now - datetime.timedelta(hours=24)
            self.cursor.execute(f"select int_tp_time, int_tp_data from int_temp where "
                                f"int_tp_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY int_tp_time")
            temp_in_x, temp_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute(f"select ext_tp_time, ext_tp_data from ext_temp where "
                                f"ext_tp_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY ext_tp_time")
            temp_out_x, temp_out_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute(f"select int_hd_time, int_hd_data from int_hum where "
                                f"int_hd_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY int_hd_time")
            hum_in_x, hum_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute(f"select int_ps_time, int_ps_data from int_pres where "
                                f"int_ps_time>='{limit.strftime('%Y-%m-%d %H:%M:%S')}' ORDER BY int_ps_time")
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

            if np.min(temp_in_y) < 10:
                y_min = np.min(temp_in_y) - 5
            else:
                y_min = 10
            if np.max(temp_in_y) > 30:
                y_max = np.max(temp_in_y) + 5
            else:
                y_max = 30

            self.plot_in_1.set_ylim(y_min, y_max)
            self.plot_in_2.plot(hum_in_x, hum_in_y, color=color_2, linewidth=1.)
            self.plot_in_2.set_ylim(0, 100)
            self.plot_in_1.set_xlim(limit, now)
            self.plot_in_1.set_xticks(hours_list)
            self.plot_in_1.set_xticklabels(['-24h', '-20h', '-16h', '-12h', '-8h', '-4h', 'Now'])
            self.plot_out_1.plot(temp_out_x, temp_out_y, color=color_1, linewidth=1.)

            if np.min(temp_out_y) < 0:
                y_min = np.min(temp_out_y) - 5
            else:
                y_min = 0
            if np.max(temp_out_y) > 30:
                y_max = np.max(temp_out_y) + 5
            else:
                y_max = 30

            self.plot_out_1.set_ylim(y_min, y_max)
            self.plot_out_2.plot(pres_in_x, pres_in_y, color=color_3, linewidth=1.)

            if np.min(pres_in_y) < 990:
                y_min = np.min(pres_in_y) - 10
            else:
                y_min = 990
            if np.max(pres_in_y) > 1030:
                y_max = np.max(pres_in_y) + 10
            else:
                y_max = 1030

            self.plot_out_2.set_ylim(y_min, y_max)
            self.plot_out_1.set_xlim(limit, now)
            self.plot_out_1.set_xticks(hours_list)
            self.plot_out_1.set_xticklabels(['-24h', '-20h', '-16h', '-12h', '-8h', '-4h', 'Now'])
            self.canvas_in.draw()
            self.canvas_out.draw()
            self.success.emit()
        except Exception as e:
            self.error.emit(['plot data', e])

    def stop(self):
        logging.debug('gui - other_threads.py - RequestPlotDataThread - stop')
        self.terminate()
