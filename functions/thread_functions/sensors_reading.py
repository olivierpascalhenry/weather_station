import logging
import random
import datetime
import time
import psycopg2
import platform
from PyQt5 import QtCore
if platform.system() == 'Linux':
    import smbus2
    import bme280


class DataCollectingThread(QtCore.QThread):
    def __init__(self, connector, cursor, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DataCollectingThread - __init__')
        self.connector = connector
        self.cursor = cursor
        self.cal_params = None
        self.sensors_rate = int(config_dict.get('SYSTEM', 'sensors_rate'))
        self.place_altitude = int(config_dict.get('SYSTEM', 'place_altitude'))

    def run(self):
        logging.debug('gui - sensors_reading.py - DataCollectingThread - run')
        if platform.system() == 'Linux':
            self.cal_params = self.prepare_bme280_bus()
        while True:
            date_time = datetime.datetime.now().replace(microsecond=0)
            ext_tp = self.collect_ext_temp()
            int_tp, int_hd, int_ps = self.collect_int_temp_hum_pres()
            self.add_data_to_db(date_time, int_tp, ext_tp, int_hd, int_ps)
            time.sleep(self.sensors_rate)

    def add_data_to_db(self, dt, int_tp, ext_tp, int_hd, int_ps):
        try:
            self.cursor.execute('insert into int_temp (int_tp_time, int_tp_data) values (%s, %s)', (dt, int_tp))
            self.cursor.execute('insert into ext_temp (ext_tp_time, ext_tp_data) values (%s, %s)', (dt, ext_tp))
            self.cursor.execute('insert into int_hum (int_hd_time, int_hd_data) values (%s, %s)', (dt, int_hd))
            self.cursor.execute('insert into int_pres (int_ps_time, int_ps_data) values (%s, %s)', (dt, int_ps))
            self.connector.commit()
        except (psycopg2.InterfaceError, psycopg2.OperationalError):
            pass

    def collect_ext_temp(self):
        temp = None
        if platform.system() == 'Linux':
            f = open('/sys/bus/w1/devices/28-012059b3456d/w1_slave', 'r')
            lines = f.readlines()
            f.close()
            if lines[0].strip()[-3:] == 'YES':
                t_idx = lines[1].find('t=')
                if t_idx != -1:
                    temp = float(lines[1][t_idx + 2:]) / 1000.0
                    if temp > 50:
                        temp = -999
        else:
            temp = self.collect_test_data(25., 5)
        return round(temp, 1)

    def collect_int_temp_hum_pres(self):
        if platform.system() == 'Linux':
            data = bme280.sample(bus, address, calibration_params)
            temp = data.temperature
            hum = data.humidity
            pres = data.pressure

            pres = pres + ((pres * 9.80665 * self.place_altitude) /
                           (287.0531 * (273.15 + temp + (self.place_altitude / 400))))

            if temp > 50:
                temp = -999

        else:
            temp = self.collect_test_data(20., 5)
            hum = self.collect_test_data(65., 20)
            pres = self.collect_test_data(1013., 15)

        temp = round(temp, 1)
        hum = round(hum)
        pres = round(pres, 1)
        return temp, hum, pres

    @staticmethod
    def collect_test_data(num, limit):
        random.seed()
        temp = round(num + random.uniform(0, limit), 1)
        return temp

    @staticmethod
    def prepare_bme280_bus():
        return bme280.load_calibration_params(smbus2.SMBus(1), 0x77)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DataCollectingThread - stop')
        self.terminate()


class DBDataDisplayThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)

    def __init__(self, cursor, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DBDataDisplayThread - __init__')
        self.cursor = cursor
        self.display_rate = int(config_dict.get('SYSTEM', 'display_rate'))

    def run(self):
        logging.debug('gui - sensors_reading.py - DBDataDisplayThread - run')
        time.sleep(self.display_rate / 2.)

        q_temp_norm_in = 'SELECT int_tp_data FROM int_temp ORDER BY id DESC LIMIT 1'
        q_temp_minmax_in = 'SELECT MIN (int_tp_data), MAX (int_tp_data) FROM int_temp'
        q_temp_norm_out = 'SELECT ext_tp_data FROM ext_temp ORDER BY id DESC LIMIT 1'
        q_temp_minmax_out = 'SELECT MIN (ext_tp_data), MAX (ext_tp_data) FROM ext_temp'
        q_hum_norm_in = 'SELECT int_hd_data FROM int_hum ORDER BY id DESC LIMIT 1'
        # q_hum_minmax_in = 'SELECT MIN (int_hd_data), MAX (int_hd_data) FROM int_hum'
        q_pres_norm_in = 'SELECT int_ps_data FROM int_pres ORDER BY id DESC LIMIT 1'

        while True:
            temp_dict = {'temp_norm_in': None, 'temp_minmax_in': None, 'temp_norm_out': None, 'temp_minmax_out': None,
                         'hum_norm_in': None, 'pres_norm_in': None}
            try:
                self.cursor.execute(q_temp_norm_in)
                data = self.cursor.fetchone()
                temp_dict['temp_norm_in'] = data[0]
            except psycopg2.ProgrammingError:
                pass
            try:
                self.cursor.execute(q_temp_minmax_in)
                data = self.cursor.fetchone()
                temp_dict['temp_minmax_in'] = data
            except psycopg2.ProgrammingError:
                pass

            try:
                self.cursor.execute(q_temp_norm_out)
                data = self.cursor.fetchone()
                temp_dict['temp_norm_out'] = data[0]
            except psycopg2.ProgrammingError:
                pass
            try:
                self.cursor.execute(q_temp_minmax_out)
                data = self.cursor.fetchone()
                temp_dict['temp_minmax_out'] = data
            except psycopg2.ProgrammingError:
                pass

            try:
                self.cursor.execute(q_hum_norm_in)
                data = self.cursor.fetchone()
                temp_dict['hum_norm_in'] = data[0]
            except psycopg2.ProgrammingError:
                pass
            try:
                self.cursor.execute(q_pres_norm_in)
                data = self.cursor.fetchone()
                temp_dict['pres_norm_int'] = data[0]
            except psycopg2.ProgrammingError:
                pass

            self.db_data.emit(temp_dict)
            time.sleep(self.display_rate)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBDataDisplayThread - stop')
        self.terminate()
