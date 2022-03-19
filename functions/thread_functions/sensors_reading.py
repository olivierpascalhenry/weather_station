import os
import json
import time
import random
import logging
import pathlib
import datetime
import platform
import psycopg2
from PyQt5 import QtCore
if platform.system() == 'Linux':
    import smbus2
    import bme280
    import paho.mqtt.client as mqtt


class DS18B20DataCollectingThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DS18B20DataCollectingThread - __init__')
        self.sensors_rate = int(sensor_dict['refresh'])
        self.sensor_file = pathlib.Path(f'/sys/bus/w1/devices/{sensor_dict["id"]}/w1_slave')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - run')
        if self.check_sensor():
            while True:
                dtime = datetime.datetime.now().replace(microsecond=0)
                temp = self.collect_data()
                self.add_data_to_db(dtime, temp)
                time.sleep(self.sensors_rate)
        else:
            logging.info('gui - sensors_reading.py - DS18B20DataCollectingThread - run - no sensor detected')

    def add_data_to_db(self, dt, tp):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread - add_data_to_db _ dt: {dt} ; tp: {tp}')
        try:
            self.cursor.execute('insert into "DS18B20" (date_time, temperature) values (%s, %s)', (dt, tp))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - DS18B20DataCollectingThread - collect_data - an issue '
                              'occurred when adding data to db')

    def collect_data(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - collect_data')
        temp = None
        try:
            f = open(self.sensor_file, 'r')
            lines = f.readlines()
            f.close()
            if lines[0].strip()[-3:] == 'YES':
                t_idx = lines[1].find('t=')
                if t_idx != -1:
                    temp = round(float(lines[1][t_idx + 2:]) / 1000.0, 1)
                    if temp > 50:
                        temp = None
        except Exception:
            logging.exception('gui - sensors_reading.py - DS18B20DataCollectingThread - collect_data - an issue '
                              'occurred when collecting data')
            temp = None
        return temp

    def check_sensor(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - check_sensor')
        if self.sensor_file.exists():
            return True
        else:
            return False

    def stop(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingThread - stop')
        self.connector.close()
        self.terminate()


class DS18B20DataCollectingTestThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DS18B20DataCollectingTestThread - __init__')
        self.sensors_rate = 30
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingTestThread - run')
        while True:
            dtime = datetime.datetime.now().replace(microsecond=0)
            temp = self.collect_data_test()
            self.add_data_to_db(dtime, temp)
            time.sleep(self.sensors_rate)

    def add_data_to_db(self, dt, tp):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingTestThread - add_data_to_db _ dt: {dt} ; tp:'
                      f' {tp}')
        try:
            self.cursor.execute('insert into "DS18B20_TEST" (date_time, temperature) values (%s, %s)', (dt, tp))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - DS18B20DataCollectingThread - collect_data - an issue '
                              'occurred when adding data to db')

    @staticmethod
    def collect_data_test():
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingTestThread - collect_data_test')
        random.seed()
        return round(25. + random.uniform(0, 5), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingTestThread - stop')
        self.connector.close()
        self.terminate()


class BME280DataCollectingThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - BME280DataCollectingThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.sensors_rate = int(config_dict.get('SENSOR', 'sensors_rate'))
        self.cal_params = None
        self.bus = None
        self.address = None

    def run(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - run')
        if self.set_bme280_parameters():
            while True:
                date_time = datetime.datetime.now().replace(microsecond=0)
                temp, hum, pres = self.collect_data()
                self.add_data_to_db(date_time, temp, hum, pres)
                time.sleep(self.sensors_rate)

    def collect_data(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - collect_data')
        try:
            data = bme280.sample(self.bus, self.address, self.cal_params)
            temp = round(data.temperature, 1)
            hum = round(data.humidity, 1)
            pres = round(data.pressure, 1)
            if temp > 50:
                temp = None
        except Exception:
            logging.exception('gui - sensors_reading.py - BME280DataCollectingThread - set_bme280_parameters - an '
                              'exception occurred when collecting bme280 data')
            temp, hum, pres = None, None, None
        return temp, hum, pres

    def add_data_to_db(self, dt, tp, hm, ps):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread - add_data_to_db - dt: {dt} ; tp: {tp} ; '
                      f'hm: {hm} ; ps: {ps}')
        try:
            self.cursor.execute('insert into "BME280" (date_time, temperature, humidity, pressure) '
                                'values (%s, %s, %s, %s)', (dt, tp, hm, ps))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - BME280DataCollectingThread - set_bme280_parameters - an '
                              'exception occurred when adding data to db')

    def set_bme280_parameters(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - set_bme280_parameters')
        try:
            self.bus = smbus2.SMBus(1)
            self.address = 0x77
            self.cal_params = bme280.load_calibration_params(self.bus, self.address)
            return True
        except OSError:
            logging.info('gui - sensors_reading.py - BME280DataCollectingThread - run - no sensor detected')
            return False
        except Exception:
            logging.exception('gui - sensors_reading.py - BME280DataCollectingThread - set_bme280_parameters - an '
                              'exception occurred when setting bme280 parameters')
            return False

    @staticmethod
    def collect_test_data(num, limit):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - collect_test_data')
        random.seed()
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingThread - stop')
        self.connector.close()
        self.terminate()


class BME280DataCollectingTestThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - BME280DataCollectingTestThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.sensors_rate = 30

    def run(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingTestThread - run')
        while True:
            date_time = datetime.datetime.now().replace(microsecond=0)
            temp, hum, pres = self.collect_data_test()
            self.add_data_to_db(date_time, temp, hum, pres)
            time.sleep(self.sensors_rate)

    def collect_data_test(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingTestThread - collect_data_test')
        temp = self.collect_test_data(20., 5)
        hum = self.collect_test_data(65., 20)
        pres = self.collect_test_data(1013., 15)
        return temp, hum, pres

    def add_data_to_db(self, dt, tp, hm, ps):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingTestThread - add_data_to_db - dt: {dt} ; tp:'
                      f' {tp} ; hm: {hm} ; ps: {ps}')
        try:
            self.cursor.execute('insert into "BME280_TEST" (date_time, temperature, humidity, pressure) '
                                'values (%s, %s, %s, %s)', (dt, tp, hm, ps))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - BME280DataCollectingTestThread - set_bme280_parameters - an '
                              'exception occurred when adding data to db')

    @staticmethod
    def collect_test_data(num, limit):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingTestThread - collect_test_data')
        random.seed()
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingTestThread - stop')
        self.connector.close()
        self.terminate()


class MqttToDbThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, mqtt_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - MqttToDbThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()
        self.mqtt_dict = mqtt_dict
        self.mqtt_client = None

    def run(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - run')
        self.mqtt_client = mqtt.Client('weather_station_thread')
        self.mqtt_client.on_message = self.parse_data
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.username_pw_set(username=self.mqtt_dict['username'], password=self.mqtt_dict['password'])
        self.mqtt_client.connect(self.mqtt_dict['address'])
        topics_list = [(f'{self.mqtt_dict["main_topic"]}/{device}', 0) for device in self.mqtt_dict['devices']]
        self.mqtt_client.subscribe(topics_list)
        self.mqtt_client.loop_forever()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        logging.info(f'gui - sensors_reading.py - MqttToDbThread - connected to broker with connect code: {rc}')

    @staticmethod
    def on_disconnect(client, userdata, rc):
        logging.info(f'gui - sensors_reading.py - MqttToDbThread - disconnected from broker with disconnect code: {rc}')

    def parse_data(self, client, userdata, message):
        message = str(message.payload.decode('utf-8'))
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - parse data - message received : {message} ; '
                      f'from {message.topic}')
        date_time = datetime.datetime.now()
        data = json.loads(message)
        database = os.path.basename(message.topic)
        try:
            temperature = round(data['temperature'], 1)
        except KeyError:
            temperature = None
        try:
            humidity = round(data['humidity'], 1)
        except KeyError:
            humidity = None
        try:
            pressure = round(data['pressure'], 1)
        except KeyError:
            pressure = None
        try:
            battery = data['battery']
        except KeyError:
            battery = None
        try:
            signal = data['linkquality']
        except KeyError:
            signal = None
        self.add_data_to_db(date_time, temperature, humidity, pressure, battery, signal, database)

    def add_data_to_db(self, dt, tp, hm, ps, bt, lk, db):
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - add_data_to_db - data : {dt} | {tp} | {hm} | {ps} '
                      f'| {bt} | {lk} | {db}')
        try:
            self.cursor.execute(f'insert into "{db}" (date_time, temperature, humidity, pressure, battery, '
                                f'signal) values (%s, %s, %s, %s, %s, %s)',
                                (dt, tp, hm, ps, bt, lk))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - MqttToDbThread - set_mqtt_client - an exception occurred '
                              'when adding data to db')

    @staticmethod
    def collect_test_data(num, limit):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - collect_test_data')
        random.seed()
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - stop')
        if platform.system() == 'Linux':
            self.mqtt_client.disconnect()
        self.connector.close()
        self.terminate()


class MqttToDbTestThread(QtCore.QThread):
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - MqttToDbTestThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - MqttToDbTestThread - run')
        while True:
            database = 'AQARA_THP_TEST'
            date_time = datetime.datetime.now().replace(microsecond=0)
            temperature = self.collect_test_data(20., 5)
            humidity = self.collect_test_data(65., 20)
            pressure = self.collect_test_data(1013., 15)
            batterie = 75.
            signal = 97.
            self.add_data_to_db(date_time, temperature, humidity, pressure, batterie, signal, database)
            time.sleep(60)

    def add_data_to_db(self, dt, tp, hm, ps, bt, lk, db):
        logging.debug(f'gui - sensors_reading.py - MqttToDbTestThread - add_data_to_db - data : {dt} | {tp} | {hm} | {ps} '
                      f'| {bt} | {lk} | {db}')
        try:
            self.cursor.execute(f'insert into "{db}" (date_time, temperature, humidity, pressure, battery, '
                                f'signal) values (%s, %s, %s, %s, %s, %s)',
                                (dt, tp, hm, ps, bt, lk))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - MqttToDbTestThread - set_mqtt_client - an exception occurred '
                              'when adding data to db')

    @staticmethod
    def collect_test_data(num, limit):
        logging.debug('gui - sensors_reading.py - MqttToDbTestThread - collect_test_data')
        random.seed()
        return round(num + random.uniform(0, limit), 1)

    def stop(self):
        logging.debug('gui - sensors_reading.py - MqttToDbTestThread - stop')
        if platform.system() == 'Linux':
            self.mqtt_client.disconnect()
        self.connector.close()
        self.terminate()


class DBInDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DBInDataThread - __init__')
        self.sensor_dict = sensor_dict
        self.device_name = config_dict.get('DISPLAY', 'in_sensor')
        self.display_rate = int(config_dict.get('DISPLAY', 'in_display_rate'))
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - run')
        self.request_data()

    def request_data(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - request_data')
        table = None
        if platform.system() == 'Windows':
            table = self.device_name
        else:
            if self.device_name:
                for _, ddict in self.sensor_dict['DS18B20'].items():
                    if self.device_name == ddict['name']:
                        table = ddict['table']
                        break
                if table is None:
                    for _, ddict in self.sensor_dict['BME280'].items():
                        if self.device_name == ddict['name']:
                            table = ddict['table']
                            break
                if table is None:
                    for device, _ in self.sensor_dict['MQTT']['devices'].items():
                        if self.device_name == device:
                            table = device
                            break
        if table is not None:
            req_dict = {'temp': {'query': f'SELECT temperature FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'temperature'},
                        'temp_minmax': {'query': f'SELECT MIN (temperature), MAX (temperature) FROM "{table}"',
                                        'column': 'temperature'},
                        'hum': {'query': f'SELECT humidity FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'humidity'},
                        'pres': {'query': f'SELECT pressure FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'pressure'},
                        'bat': {'query': f'SELECT battery FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'battery'},
                        'sig': {'query': f'SELECT signal FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'signal'}}
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'")
            column_list = [column[0] for column in self.cursor.fetchall()]
            while True:
                var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'bat': None, 'sig': None}
                for var, req in req_dict.items():
                    try:
                        if req['column'] in column_list:
                            self.cursor.execute(req['query'])
                            data = self.cursor.fetchone()
                            if var == 'temp_minmax':
                                var_dict[var] = data
                            else:
                                var_dict[var] = data[0]
                    except Exception:
                        logging.error(f'gui - sensors_reading.py - DBInDataThread - request_data - an exception '
                                      f'occurred when requesting {var} from {table}')
                self.db_data.emit(var_dict)
                time.sleep(self.display_rate)
        else:
            logging.error('gui - sensors_reading.py - DBInDataThread - request_data - no sensor in config file to '
                          'display in data or the sensor doesnt exist in sensor dict')

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - stop')
        self.connector.close()
        self.terminate()


class DBOutDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, db_dict, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DBOutDataThread - __init__')
        self.sensor_dict = sensor_dict
        self.device_name = config_dict.get('DISPLAY', 'out_sensor')
        self.display_rate = int(config_dict.get('DISPLAY', 'in_display_rate'))
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - run')
        self.request_data()

    def request_data(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - request_data')
        table = None
        if platform.system() == 'Windows':
            table = self.device_name
        else:
            if self.device_name:
                for _, ddict in self.sensor_dict['DS18B20'].items():
                    if self.device_name == ddict['name']:
                        table = ddict['table']
                        break
                if table is None:
                    for _, ddict in self.sensor_dict['BME280'].items():
                        if self.device_name == ddict['name']:
                            table = ddict['table']
                            break
                if table is None:
                    for device, _ in self.sensor_dict['MQTT']['devices'].items():
                        if self.device_name == device:
                            table = device
                            break
        if table is not None:
            req_dict = {'temp': {'query': f'SELECT temperature FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'temperature'},
                        'temp_minmax': {'query': f'SELECT MIN (temperature), MAX (temperature) FROM "{table}"',
                                        'column': 'temperature'},
                        'hum': {'query': f'SELECT humidity FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'humidity'},
                        'pres': {'query': f'SELECT pressure FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'pressure'},
                        'bat': {'query': f'SELECT battery FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'battery'},
                        'sig': {'query': f'SELECT signal FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'signal'}}
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'")
            column_list = [column[0] for column in self.cursor.fetchall()]
            while True:
                var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'bat': None, 'sig': None}
                for var, req in req_dict.items():
                    try:
                        if req['column'] in column_list:
                            self.cursor.execute(req['query'])
                            data = self.cursor.fetchone()
                            if var == 'temp_minmax':
                                var_dict[var] = data
                            else:
                                var_dict[var] = data[0]
                    except Exception:
                        logging.error(f'gui - sensors_reading.py - DBOutDataThread - request_data - an exception '
                                      f'occurred when requesting {var} from {table}')
                self.db_data.emit(var_dict)
                time.sleep(self.display_rate)
        else:
            logging.error('gui - sensors_reading.py - DBOutDataThread - request_data - no sensor in config file to '
                          'display in data or the sensor doesnt exist in sensor dict')

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - stop')
        self.connector.close()
        self.terminate()
