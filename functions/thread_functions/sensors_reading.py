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
    def __init__(self, db_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - sensors_reading.py - DS18B20DataCollectingThread - __init__ - sensor_dict: {sensor_dict}')
        self.name = sensor_dict['id']
        self.sensor_dict = sensor_dict
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - run')
        if self.check_sensor():
            while True:
                dtime = datetime.datetime.now().replace(microsecond=0)
                temp = self.collect_data()
                self.add_data_to_db(dtime, temp)
                time.sleep(int(self.sensor_dict['refresh']))
        else:
            logging.info(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - run - '
                         f'no sensor detected')

    def add_data_to_db(self, dt, tp):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - add_data_to_db _ dt: '
                      f'{dt} ; tp: {tp}')
        try:
            self.cursor.execute(f'insert into "{self.sensor_dict["table"]}" (date_time, temperature) values (%s, %s)',
                                (dt, tp))
            self.connector.commit()
        except Exception:
            logging.exception(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - collect_data - '
                              f'an issue occurred when adding data to db')

    def collect_data(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - collect_data')
        temp = None
        try:
            f = open(pathlib.Path(f'/sys/bus/w1/devices/{self.sensor_dict["id"]}/w1_slave'), 'r')
            lines = f.readlines()
            f.close()
            if lines[0].strip()[-3:] == 'YES':
                t_idx = lines[1].find('t=')
                if t_idx != -1:
                    temp = round(float(lines[1][t_idx + 2:]) / 1000.0, 1)

                    if self.sensor_dict['cal_methode']:
                        if self.sensor_dict['cal_methode'] == 'offset':
                            temp += float(self.sensor_dict['cal_value'])

                    if temp > 50:
                        temp = None
        except Exception:
            logging.exception(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - collect_data - '
                              f'an issue occurred when collecting data')
            temp = None
        return temp

    def check_sensor(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - check_sensor')
        if pathlib.Path(f'/sys/bus/w1/devices/{self.sensor_dict["id"]}/w1_slave').exists():
            return True
        else:
            return False

    def stop(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - stop')
        self.connector.close()
        self.terminate()


class DS18B20DataCollectingTestThread(QtCore.QThread):

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DS18B20DataCollectingTestThread - __init__')
        self.sensors_rate = 30
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingTestThread - run')
        random.seed()
        while True:
            self.add_data_to_db(datetime.datetime.now().replace(microsecond=0), round(25. + random.uniform(0, 5), 1))
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

    def stop(self):
        logging.debug('gui - sensors_reading.py - DS18B20DataCollectingTestThread - stop')
        self.connector.close()
        self.terminate()


class BME280DataCollectingThread(QtCore.QThread):
    def __init__(self, db_dict, sensor_dict, altitude):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - sensors_reading.py - BME280DataCollectingThread - __init__ - sensor_dict: {sensor_dict} '
                     f'; altitude: {altitude}')
        self.name = sensor_dict['id']
        self.sensor_dict = sensor_dict
        self.address = int(sensor_dict['id'][sensor_dict['id'].find('0x'):], 16)
        self.bus = smbus2.SMBus(sensor_dict['bus'])
        self.cal_params = None
        self.alt = altitude
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - run')
        if self.set_bme280_parameters():
            while True:
                date_time = datetime.datetime.now().replace(microsecond=0)
                temp, hum, pres, pres_msl = self.collect_data()
                self.add_data_to_db(date_time, temp, hum, pres, pres_msl)
                time.sleep(int(self.sensor_dict['refresh']))

    def collect_data(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - collect_data')
        try:
            # bus = smbus2.SMBus(self.bus)
            data = bme280.sample(self.bus, self.address, self.cal_params)
            temp = round(data.temperature, 1)
            hum = round(data.humidity, 1)
            pres = round(data.pressure, 1)

            if self.sensor_dict['cal_methode']:
                if self.sensor_dict['cal_methode'] == 'offset':
                    temp += float(self.sensor_dict['cal_value'])

            if self.alt is not None:
                pres_msl = pres + ((pres * 9.80665 * self.alt) / (287.0531 * (273.15 + temp + (self.alt / 400))))
                pres_msl = round(pres_msl, 1)
            else:
                pres_msl = pres

            if temp > 50:
                temp = None
        except Exception:
            logging.exception(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - '
                              f'collect_data - an exception occurred when collecting bme280 data')
            temp, hum, pres, pres_msl = None, None, None, None
        return temp, hum, pres, pres_msl

    def add_data_to_db(self, dt, tp, hm, ps, ps_sl):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - add_data_to_db - '
                      f'dt: {dt} ; tp: {tp} ; hm: {hm} ; ps: {ps} ; ps_sl: {ps_sl}')
        try:
            self.cursor.execute(f'insert into "{self.sensor_dict["table"]}" (date_time, temperature, humidity, '
                                f'pressure, pressure_msl) values (%s, %s, %s, %s, %s)', (dt, tp, hm, ps, ps_sl))
            self.connector.commit()
        except Exception:
            logging.exception(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} -'
                              f' add_data_to_db - an exception occurred when adding data to db')

    def set_bme280_parameters(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - set_bme280_parameters - '
                      f'bus: {self.bus} ; address: {self.address}')
        try:
            self.cal_params = bme280.load_calibration_params(self.bus, self.address)
            return True
        except OSError:
            logging.info(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - run - '
                         f'no sensor detected')
            return False
        except Exception:
            logging.exception(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - '
                              f'set_bme280_parameters - an exception occurred when setting bme280 parameters')
            return False

    def stop(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - stop')
        self.connector.close()
        self.bus.close()
        self.terminate()


class BME280DataCollectingTestThread(QtCore.QThread):
    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - BME280DataCollectingTestThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.sensors_rate = 30

    def run(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingTestThread - run')
        random.seed()
        while True:
            self.add_data_to_db(datetime.datetime.now().replace(microsecond=0),
                                round(20 + random.uniform(0, 5), 1),
                                round(65 + random.uniform(0, 20), 1),
                                round(1013 + random.uniform(0, 15), 1),
                                round(1013 + random.uniform(0, 15), 1))
            time.sleep(self.sensors_rate)

    def add_data_to_db(self, dt, tp, hm, ps, ps_sl):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingTestThread - add_data_to_db - dt: {dt} ; tp:'
                      f' {tp} ; hm: {hm} ; ps: {ps} ; ps_sl: {ps_sl}')
        try:
            self.cursor.execute('insert into "BME280_TEST" (date_time, temperature, humidity, pressure, pressure_msl) '
                                'values (%s, %s, %s, %s, %s)', (dt, tp, hm, ps, ps_sl))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - BME280DataCollectingTestThread - set_bme280_parameters - an '
                              'exception occurred when adding data to db')

    def stop(self):
        logging.debug('gui - sensors_reading.py - BME280DataCollectingTestThread - stop')
        self.connector.close()
        self.terminate()


class MqttToDbThread(QtCore.QThread):
    def __init__(self, db_dict, mqtt_dict, altitude):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - sensors_reading.py - MqttToDbThread - __init__ - mqtt_dict: {mqtt_dict} ; altitude: '
                     f'{altitude}')
        self.alt = altitude
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
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
        self.mqtt_client.loop_start()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - connected to broker with connect code: {rc}')

    @staticmethod
    def on_disconnect(client, userdata, rc):
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - disconnected from broker with disconnect code:'
                      f' {rc}')

    def parse_data(self, client, userdata, message):
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - parse data - message received : '
                      f'{str(message.payload.decode("utf-8"))} ; from {message.topic}')
        date_time = datetime.datetime.now()
        data = json.loads(str(message.payload.decode('utf-8')))
        database = os.path.basename(message.topic)
        try:
            temperature = round(data['temperature'], 1)
            if self.mqtt_dict['devices'][database]['cal_methode']:
                if self.mqtt_dict['devices'][database]['cal_methode'] == 'offset':
                    temperature += float(self.mqtt_dict['devices'][database]['cal_value'])
            humidity = round(data['humidity'], 1)
            pressure = round(data['pressure'], 1)
            if self.alt is not None and temperature is not None:
                pressure_msl = pressure + ((pressure * 9.80665 * self.alt) /
                                           (287.0531 * (273.15 + temperature + (self.alt / 400))))
                pressure_msl = round(pressure_msl, 1)
            else:
                pressure_msl = pressure
            battery = data['battery']
            signal = data['linkquality']
        except:
            logging.exception(f'gui - sensors_reading.py - MqttToDbThread - parse data - issue with data')
            temperature, humidity, pressure, pressure_msl, battery, signal = None, None, None, None, None, None
        self.add_data_to_db(date_time, temperature, humidity, pressure, pressure_msl, battery, signal, database)

    def add_data_to_db(self, dt, tp, hm, ps, ps_sl, bt, lk, db):
        logging.debug(f'gui - sensors_reading.py - MqttToDbThread - add_data_to_db - data : {dt} | {tp} | {hm} | {ps} '
                      f'| {ps_sl} | {bt} | {lk} | {db}')
        try:
            self.cursor.execute(f'insert into "{db}" (date_time, temperature, humidity, pressure, pressure_msl, '
                                f'battery, signal) values (%s, %s, %s, %s, %s, %s, %s)',
                                (dt, tp, hm, ps, ps_sl, bt, lk))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - MqttToDbThread - set_mqtt_client - an exception occurred '
                              'when adding data to db')

    def stop(self):
        logging.debug('gui - sensors_reading.py - MqttToDbThread - stop')
        if platform.system() == 'Linux':
            self.mqtt_client.disconnect()
            self.mqtt_client.loop_stop()
        self.connector.close()
        self.terminate()


class MqttToDbTestThread(QtCore.QThread):
    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - MqttToDbTestThread - __init__')
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()

    def run(self):
        logging.debug('gui - sensors_reading.py - MqttToDbTestThread - run')
        random.seed()
        while True:
            self.add_data_to_db(datetime.datetime.now().replace(microsecond=0),
                                round(20 + random.uniform(0, 5), 1), round(65 + random.uniform(0, 15), 1),
                                round(1013 + random.uniform(0, 10), 1), round(1013 + random.uniform(0, 20), 1),
                                75, 97, 'AQARA_THP_TEST')
            time.sleep(60)

    def add_data_to_db(self, dt, tp, hm, ps, ps_sl, bt, lk, db):
        logging.debug(f'gui - sensors_reading.py - MqttToDbTestThread - add_data_to_db - data : {dt} | {tp} | {hm} '
                      f'| {ps} | {ps_sl} | {bt} | {lk} | {db}')
        try:
            self.cursor.execute(f'insert into "{db}" (date_time, temperature, humidity, pressure, pressure_msl, '
                                f'battery, signal) values (%s, %s, %s, %s, %s, %s, %s)',
                                (dt, tp, hm, ps, ps_sl, bt, lk))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - MqttToDbTestThread - set_mqtt_client - an exception occurred '
                              'when adding data to db')

    def stop(self):
        logging.debug('gui - sensors_reading.py - MqttToDbTestThread - stop')
        if platform.system() == 'Linux':
            self.mqtt_client.disconnect()
        self.connector.close()
        self.terminate()


class DBInDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)

    def __init__(self, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DBInDataThread - __init__')
        self.sensor_dict = sensor_dict
        self.device_name = config_dict.get('DISPLAY', 'in_sensor')
        self.display_rate = int(config_dict.get('DISPLAY', 'in_display_rate'))
        self.connector = psycopg2.connect(user=config_dict.get('DATABASE', 'username'),
                                          password=config_dict.get('DATABASE', 'password'),
                                          host=config_dict.get('DATABASE', 'host'),
                                          database=config_dict.get('DATABASE', 'database'),
                                          port=config_dict.get('DATABASE', 'port'))
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
        logging.debug(f'gui - sensors_reading.py - DBInDataThread - request_data - table: {table}')
        if table is not None:
            req_dict = {'temp': {'query': f'SELECT temperature FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'temperature'},
                        'temp_minmax': {'query': f'SELECT MIN (temperature), MAX (temperature) FROM "{table}"',
                                        'column': 'temperature'},
                        'hum': {'query': f'SELECT humidity FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'humidity'},
                        'pres': {'query': f'SELECT pressure FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'pressure'},
                        'pres_msl': {'query': f'SELECT pressure_msl FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                     'column': 'pressure_msl'},
                        'bat': {'query': f'SELECT battery FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'battery'},
                        'sig': {'query': f'SELECT signal FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'signal'}}
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'")
            column_list = [column[0] for column in self.cursor.fetchall()]
            while True:
                var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'pres_msl': None,
                            'bat': None, 'sig': None}
                for var, req in req_dict.items():
                    try:
                        if req['column'] in column_list:
                            self.cursor.execute(req['query'])
                            data = self.cursor.fetchone()
                            if data is not None:
                                if var == 'temp_minmax':
                                    var_dict[var] = data
                                else:
                                    var_dict[var] = data[0]
                    except Exception:
                        logging.exception(f'gui - sensors_reading.py - DBInDataThread - request_data - an exception '
                                          f'occurred when requesting {var} from {table}')
                logging.debug(f'gui - sensors_reading.py - DBInDataThread - request_data - var_dict: {var_dict}')
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

    def __init__(self, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DBOutDataThread - __init__')
        self.sensor_dict = sensor_dict
        self.device_name = config_dict.get('DISPLAY', 'out_sensor')
        self.display_rate = int(config_dict.get('DISPLAY', 'in_display_rate'))
        self.connector = psycopg2.connect(user=config_dict.get('DATABASE', 'username'),
                                          password=config_dict.get('DATABASE', 'password'),
                                          host=config_dict.get('DATABASE', 'host'),
                                          database=config_dict.get('DATABASE', 'database'),
                                          port=config_dict.get('DATABASE', 'port'))
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
        logging.debug(f'gui - sensors_reading.py - DBOutDataThread - request_data - table: {table}')
        if table is not None:
            req_dict = {'temp': {'query': f'SELECT temperature FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'temperature'},
                        'temp_minmax': {'query': f'SELECT MIN (temperature), MAX (temperature) FROM "{table}"',
                                        'column': 'temperature'},
                        'hum': {'query': f'SELECT humidity FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'humidity'},
                        'pres': {'query': f'SELECT pressure FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                 'column': 'pressure'},
                        'pres_msl': {'query': f'SELECT pressure_msl FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                     'column': 'pressure_msl'},
                        'bat': {'query': f'SELECT battery FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'battery'},
                        'sig': {'query': f'SELECT signal FROM "{table}" ORDER BY date_time DESC LIMIT 1',
                                'column': 'signal'}}
            self.cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name='{table}'")
            column_list = [column[0] for column in self.cursor.fetchall()]
            while True:
                var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'pres_msl': None,
                            'bat': None, 'sig': None}
                for var, req in req_dict.items():
                    try:
                        if req['column'] in column_list:
                            self.cursor.execute(req['query'])
                            data = self.cursor.fetchone()
                            if data is not None:
                                if var == 'temp_minmax':
                                    var_dict[var] = data
                                else:
                                    var_dict[var] = data[0]
                    except Exception:
                        logging.exception(f'gui - sensors_reading.py - DBOutDataThread - request_data - an exception '
                                          f'occurred when requesting {var} from {table}')
                logging.debug(f'gui - sensors_reading.py - DBOutDataThread - request_data - var_dict: {var_dict}')
                self.db_data.emit(var_dict)
                time.sleep(self.display_rate)
        else:
            logging.error('gui - sensors_reading.py - DBOutDataThread - request_data - no sensor in config file to '
                          'display in data or the sensor doesnt exist in sensor dict')

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - stop')
        self.connector.close()
        self.terminate()
