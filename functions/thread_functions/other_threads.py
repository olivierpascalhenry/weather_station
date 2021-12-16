import logging
import datetime
import time
import psycopg2
import requests
import pathlib
import socket
from distutils.version import LooseVersion
from functions.utils import set_size
from PyQt5 import QtCore

username = 'olivierpascalhenry'
token = '***REMOVED***'


class CleaningThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, connector, cursor):
        QtCore.QThread.__init__(self)
        logging.debug('gui - other_threads.py - CleaningThread - __init__')
        self.connector = connector
        self.cursor = cursor

    def run(self):
        logging.debug('gui - other_threads.py - CleaningThread - run')
        while True:
            try:
                time_limit = datetime.datetime.now() - datetime.timedelta(days=2)
                self.cursor.execute('DELETE FROM int_temp WHERE int_tp_time <= %s', (time_limit, ))
                self.cursor.execute('DELETE FROM ext_temp WHERE ext_tp_time <= %s', (time_limit,))
                self.cursor.execute('DELETE FROM int_hum WHERE int_hd_time <= %s', (time_limit,))
                self.cursor.execute('DELETE FROM int_pres WHERE int_ps_time <= %s', (time_limit,))
                self.connector.commit()
            except Exception as e:
                self.error.emit(['update request', e])
            time.sleep(3600)

    def stop(self):
        logging.debug('gui - other_threads.py - CleaningThread - stop')
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



