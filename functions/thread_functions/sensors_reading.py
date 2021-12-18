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


class DS18B20DataCollectingThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, connector, cursor, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - __init__')
        self.connector = connector
        self.cursor = cursor
        self.sensors_rate = int(config_dict.get('SYSTEM', 'sensors_rate'))

    def run(self):
        while True:
            dtime = datetime.datetime.now().replace(microsecond=0)
            try:
                temp = self.collect_data()
                self.add_data_to_db(dtime, temp)
                time.sleep(self.sensors_rate)
            except Exception as e:
                self.error.emit(['DS18B20 data collecting', e])
                self.add_data_to_db(dtime, None)

    def add_data_to_db(self, dt, tp):
        try:
            self.cursor.execute('insert into "DS18B20" (date_time, temperature) values (%s, %s)', (dt, tp))
            self.connector.commit()
        except (psycopg2.InterfaceError, psycopg2.OperationalError):
            pass

    def collect_data(self):
        temp = None
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            try:
                f = open('/sys/bus/w1/devices/28-012059b3456d/w1_slave', 'r')
                lines = f.readlines()
                f.close()
                if lines[0].strip()[-3:] == 'YES':
                    t_idx = lines[1].find('t=')
                    if t_idx != -1:
                        temp = round(float(lines[1][t_idx + 2:]) / 1000.0, 1)
                        if temp > 50:
                            temp = None
            except:
                temp = None
        else:
            temp = self.collect_test_data(25., 5)
        return temp

    @staticmethod
    def collect_test_data(num, limit):
        random.seed()
        if random.randrange(1, 7, 1) == 1:
            return None
        else:
            return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - stop')
        self.terminate()


class BME280DataCollectingThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, connector, cursor, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - __init__')
        self.connector = connector
        self.cursor = cursor
        self.sensors_rate = int(config_dict.get('SYSTEM', 'sensors_rate'))
        self.cal_params = None
        self.bus = None
        self.address = None
        if config_dict.get('SYSTEM', 'place_altitude'):
            self.place_altitude = int(config_dict.get('SYSTEM', 'place_altitude'))
        else:
            self.place_altitude = None

    def run(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - run')
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            try:
                self.bus = smbus2.SMBus(1)
                self.address = 0x77
                self.cal_params = self.prepare_bme280_bus()
            except Exception as e:
                self.error.emit(['BME280 data collecting', e])
        while True:
            date_time = datetime.datetime.now().replace(microsecond=0)
            try:
                temp, hum, pres, pres_msl = self.collect_data()
                self.add_data_to_db(date_time, temp, hum, pres, pres_msl)
                time.sleep(self.sensors_rate)
            except Exception as e:
                self.error.emit(['BME280 data collecting', e])
                self.add_data_to_db(date_time, None, None, None, None)

    def collect_data(self):
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            data = bme280.sample(self.bus, self.address, self.cal_params)
            temp = data.temperature
            hum = data.humidity
            pres = data.pressure
            if self.place_altitude is not None:
                pres_msl = pres + ((pres * 9.80665 * self.place_altitude) /
                                   (287.0531 * (273.15 + temp + (self.place_altitude / 400))))
                pres_msl = round(pres_msl, 1)
            else:
                pres_msl = None
            pres = round(pres, 1)
            temp = round(temp, 1)
            hum = round(hum)
            if temp > 50:
                temp = None
        else:
            temp = self.collect_test_data(20., 5)
            hum = self.collect_test_data(65., 20)
            pres = self.collect_test_data(1013., 15)
            pres_msl = self.collect_test_data(1013., 15)
        return temp, hum, pres, pres_msl

    def add_data_to_db(self, dt, tp, hm, ps, ps_msl):
        try:
            self.cursor.execute('insert into "BME280" (date_time, temperature, humidite, pression, pression_msl) '
                                'values (%s, %s, %s, %s, %s)', (dt, tp, hm, ps, ps_msl))
            self.connector.commit()
        except (psycopg2.InterfaceError, psycopg2.OperationalError):
            pass

    def prepare_bme280_bus(self):
        return bme280.load_calibration_params(self.bus, self.address)

    @staticmethod
    def collect_test_data(num, limit):
        random.seed()
        if random.randrange(1, 7, 1) == 1:
            return None
        else:
            return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - stop')
        self.terminate()


class DBDataDisplayThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, cursor, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DBDataDisplayThread - __init__')
        self.cursor = cursor
        self.display_rate = int(config_dict.get('SYSTEM', 'display_rate'))

    def run(self):
        logging.debug('gui - sensors_reading.py - DBDataDisplayThread - run')
        time.sleep(self.display_rate / 2.)

        temp_in = 'SELECT date_time, temperature FROM "BME280" ORDER BY date_time DESC LIMIT 1'
        temp_minmax_in = 'SELECT MIN (temperature), MAX (temperature) FROM "BME280"'
        temp_out = 'SELECT temperature FROM "DS18B20" ORDER BY date_time DESC LIMIT 1'
        temp_minmax_out = 'SELECT MIN (temperature), MAX (temperature) FROM "DS18B20"'
        hum_in = 'SELECT humidite FROM "BME280" ORDER BY date_time DESC LIMIT 1'
        pres_in = 'SELECT pression FROM "BME280" ORDER BY date_time DESC LIMIT 1'
        presmsl_in = 'SELECT pression_msl FROM "BME280" ORDER BY date_time DESC LIMIT 1'

        while True:
            try:
                temp_dict = {'temp_in': None, 'temp_minmax_in': None, 'temp_out': None,
                             'temp_minmax_out': None, 'hum_in': None, 'pres_in': None,
                             'presmsl_in': None, 'datetime': None}
                try:
                    self.cursor.execute(temp_in)
                    data = self.cursor.fetchone()
                    temp_dict['temp_in'] = data[1]
                    temp_dict['datetime'] = data[0]
                except psycopg2.ProgrammingError:
                    temp_dict['temp_in'] = None
                    temp_dict['datetime'] = None
                try:
                    self.cursor.execute(temp_minmax_in)
                    data = self.cursor.fetchone()
                    temp_dict['temp_minmax_in'] = data
                except psycopg2.ProgrammingError:
                    temp_dict['temp_minmax_in'] = None
                try:
                    self.cursor.execute(temp_out)
                    data = self.cursor.fetchone()
                    temp_dict['temp_out'] = data[0]
                except psycopg2.ProgrammingError:
                    temp_dict['temp_out'] = None
                try:
                    self.cursor.execute(temp_minmax_out)
                    data = self.cursor.fetchone()
                    temp_dict['temp_minmax_out'] = data
                except psycopg2.ProgrammingError:
                    temp_dict['temp_minmax_out'] = None
                try:
                    self.cursor.execute(hum_in)
                    data = self.cursor.fetchone()
                    temp_dict['hum_in'] = data[0]
                except psycopg2.ProgrammingError:
                    temp_dict['hum_in'] = None
                try:
                    self.cursor.execute(pres_in)
                    data = self.cursor.fetchone()
                    temp_dict['pres_in'] = data[0]
                except psycopg2.ProgrammingError:
                    temp_dict['pres_in'] = None
                try:
                    self.cursor.execute(presmsl_in)
                    data = self.cursor.fetchone()
                    temp_dict['presmsl_in'] = data[0]
                except psycopg2.ProgrammingError:
                    temp_dict['presmsl_in'] = None
                self.db_data.emit(temp_dict)
            except Exception as e:
                self.error.emit(['data display', e])
            time.sleep(self.display_rate)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBDataDisplayThread - stop')
        self.terminate()


class MqttToDbThread(QtCore.QThread):

    def __init__(self, connector, cursor, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - other_threads.py - MqttToDbThread - __init__')
        self.connector = connector
        self.cursor = cursor

    def run(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - run')


    def stop(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - stop')
        self.terminate()