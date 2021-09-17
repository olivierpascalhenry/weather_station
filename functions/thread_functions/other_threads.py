import logging
import datetime
import time
import psycopg2
from PyQt5 import QtCore


class CleaningThread(QtCore.QThread):

    def __init__(self, connector, cursor):
        QtCore.QThread.__init__(self)
        logging.debug('gui - other_threads.py - CleaningThread - __init__')
        self.connector = connector
        self.cursor = cursor

    def run(self):
        logging.debug('gui - other_threads.py - CleaningThread - run')
        while True:
            time_limit = datetime.datetime.now() - datetime.timedelta(days=2)
            # query = 'DELETE FROM {table} WHERE {time} <= %s;'

            self.cursor.execute('DELETE FROM int_temp WHERE int_tp_time <= %s', (time_limit, ))
            self.cursor.execute('DELETE FROM ext_temp WHERE ext_tp_time <= %s', (time_limit,))
            self.cursor.execute('DELETE FROM int_hum WHERE int_hd_time <= %s', (time_limit,))

            # self.cursor.execute('insert into int_temp (int_tp_time, int_tp_data) values (%s, %s)', (dt, int_tp))
            # self.cursor.execute('insert into ext_temp (ext_tp_time, ext_tp_data) values (%s, %s)', (dt, ext_tp))
            # self.cursor.execute('insert into int_hum (int_hd_time, int_hd_data) values (%s, %s)', (dt, int_hd))
            self.connector.commit()

            time.sleep(3600)

    def stop(self):
        logging.debug('gui - other_threads.py - CleaningThread - stop')
        self.terminate()