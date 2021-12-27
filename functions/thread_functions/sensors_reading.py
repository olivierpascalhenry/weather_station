import logging
import random
import datetime
import time
import json
import psycopg2
import platform
from PyQt5 import QtCore
if platform.system() == 'Linux':
    import smbus2
    import bme280
    import paho.mqtt.client as mqtt


class DS18B20DataCollectingThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - __init__')
        self.sensors_rate = int(config_dict.get('SYSTEM', 'out_sensors_rate'))
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - run')
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
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - stop')
        self.connector.close()
        self.terminate()


class BME280DataCollectingThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.sensors_rate = int(config_dict.get('SYSTEM', 'in_sensors_rate'))
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
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - stop')
        self.connector.close()
        self.terminate()


class MqttToDbThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - MqttToDbThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.mqtt_client = None
        if config_dict.get('SYSTEM', 'place_altitude'):
            self.place_altitude = int(config_dict.get('SYSTEM', 'place_altitude'))
        else:
            self.place_altitude = None

    def run(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - run')
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            try:
                self.mqtt_client = mqtt.Client('weather_station_thread')
                self.mqtt_client.on_message = self.parse_data
                self.mqtt_client.on_connect = self.on_connect
                self.mqtt_client.on_disconnect = self.on_disconnect
                self.mqtt_client.username_pw_set(username='weather', password='mqtt_weather_password')
                self.mqtt_client.connect('127.0.0.1')
                self.mqtt_client.subscribe('zigbee2mqtt/Aqara_T_H_P_sensor', qos=0)
                self.mqtt_client.loop_forever()
            except Exception as e:
                self.error.emit(['MQTT data collecting', e])
                date_time = datetime.datetime.now().replace(microsecond=0)
                self.add_data_to_db(date_time, None, None, None, None, None, None)
        else:
            while True:
                date_time = datetime.datetime.now().replace(microsecond=0)
                temp = self.collect_test_data(20., 5)
                hum = self.collect_test_data(65., 20)
                pres = self.collect_test_data(1013., 15)
                pres_msl = self.collect_test_data(1013., 15)
                bat = 75.
                link = 97.
                self.add_data_to_db(date_time, temp, hum, pres, pres_msl, bat, link)
                time.sleep(600)

    def on_connect(self, client, userdata, flags, rc):
        logging.info(f'gui - sensors_reading.py - MqttToDbThread - connected to broker with connect code: {rc}')

    def on_disconnect(self, client, userdata, flags, rc):
        logging.info(f'gui - sensors_reading.py - MqttToDbThread - disconnected from broker with disconnect code: {rc}')

    def parse_data(self, client, userdata, message):
        message = str(message.payload.decode('utf-8'))
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - parse data - message received : {message}')
        date_time = datetime.datetime.now()
        data = json.loads(message)
        temp = data['temperature']
        hum = data['humidity']
        pres = data['pressure']
        bat = data['battery']
        link = data['linkquality']
        if self.place_altitude is not None:
            pres_msl = pres + ((pres * 9.80665 * self.place_altitude) /
                               (287.0531 * (273.15 + temp + (self.place_altitude / 400))))
            pres_msl = round(pres_msl, 1)
        else:
            pres_msl = None
        pres = round(pres, 1)
        temp = round(temp, 1)
        hum = round(hum)
        self.add_data_to_db(date_time, temp, hum, pres, pres_msl, bat, link)

    def add_data_to_db(self, dt, tp, hm, ps, ps_msl, bt, lk):
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - add_data_to_db - data : {dt} | {tp} | {hm} | {ps} '
                      f'| {ps_msl} | {bt} | {lk} |')
        try:
            self.cursor.execute('insert into "AQARA_THP" (date_time, temperature, humidite, pression, pression_msl, '
                                'batterie, qualite) values (%s, %s, %s, %s, %s, %s, %s)',
                                (dt, tp, hm, ps, ps_msl, bt, lk))
            self.connector.commit()
        except Exception as e:
            self.error.emit(['MQTT add data to db', e])

    @staticmethod
    def collect_test_data(num, limit):
        random.seed()
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - stop')
        self.self.mqtt_client.disconnect()
        self.connector.close()
        self.terminate()


class DBInDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DBInDataThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.display_rate = int(config_dict.get('SYSTEM', 'in_display_rate'))

    def run(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - run')
        database = 'BME280'
        req_dict = {'temp': f'SELECT temperature FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'temp_minmax': f'SELECT MIN (temperature), MAX (temperature) FROM "{database}"',
                    'hum': f'SELECT humidite FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'pres': f'SELECT pression FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'presmsl': f'SELECT pression_msl FROM "{database}" ORDER BY date_time DESC LIMIT 1'}
        while True:
            var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'presmsl': None}
            for var, req in req_dict.items():
                try:
                    self.cursor.execute(req)
                    data = self.cursor.fetchone()
                    if var == 'temp_minmax':
                        var_dict[var] = data
                    else:
                        var_dict[var] = data[0]
                except psycopg2.ProgrammingError:
                    var_dict[var] = None
                except Exception as e:
                    self.error.emit(['data in display', e])
            self.db_data.emit(var_dict)
            time.sleep(self.display_rate)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - stop')
        self.connector.close()
        self.terminate()


class DBOutDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.debug('gui - sensors_reading.py - DBOutDataThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.display_rate = int(config_dict.get('SYSTEM', 'out_display_rate'))

    def run(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - run')
        database = 'AQARA_THP'
        req_dict = {'temp': f'SELECT temperature FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'temp_minmax': f'SELECT MIN (temperature), MAX (temperature) FROM "{database}"',
                    'hum': f'SELECT humidite FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'pres': f'SELECT pression FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'presmsl': f'SELECT pression_msl FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'bat': f'SELECT batterie FROM "{database}" ORDER BY date_time DESC LIMIT 1',
                    'link': f'SELECT qualite FROM "{database}" ORDER BY date_time DESC LIMIT 1'}
        while True:
            var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'presmsl': None, 'bat': None,
                        'link': None}
            for var, req in req_dict.items():
                try:
                    self.cursor.execute(req)
                    data = self.cursor.fetchone()
                    if var == 'temp_minmax':
                        var_dict[var] = data
                    else:
                        var_dict[var] = data[0]
                except psycopg2.ProgrammingError:
                    var_dict[var] = None
                except Exception as e:
                    self.error.emit(['data out display', e])
            self.db_data.emit(var_dict)
            time.sleep(self.display_rate)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - stop')
        self.connector.close()
        self.terminate()
