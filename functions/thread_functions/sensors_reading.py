import os
import json
import random
import logging
import pathlib
import datetime
import platform
import psycopg2
from PyQt5 import QtCore
import paho.mqtt.client as mqtt
if platform.system() == 'Linux':
    import smbus2
    import bme280


class DS18B20DataCollectingThread(QtCore.QThread):
    def __init__(self, db_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - sensors_reading.py - DS18B20DataCollectingThread - __init__ - sensor_dict: {sensor_dict}')
        self.name = sensor_dict['id']
        self.running = False
        self.sensor_dict = sensor_dict
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.acquisition_routine)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - start_routine')
        self.running = True
        if self.check_sensor():
            self.thread_timer.start(int(self.sensor_dict['refresh']) * 1000)
        else:
            logging.info(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - run - no sensor '
                         f'detected')
            self.stop()

    def acquisition_routine(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - acquisition_routine')
        dtime = datetime.datetime.now().replace(microsecond=0)
        temp = self.collect_data()
        self.add_data_to_db(dtime, temp)

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
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingThread/{self.name} - stop - qtimer stopped / '
                      f'db closed')
        self.running = False
        self.exit()


class DS18B20DataCollectingTestThread(QtCore.QThread):

    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DS18B20DataCollectingTestThread - __init__')
        self.sensors_rate = 30
        self.running = False
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.acquisition_routine)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingTestThread - start_routine')
        self.running = True
        random.seed()
        self.thread_timer.start(self.sensors_rate * 1000)

    def acquisition_routine(self):
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingTestThread - acquisition_routine')
        self.add_data_to_db(datetime.datetime.now().replace(microsecond=0), round(25. + random.uniform(0, 5), 1))

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
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug(f'gui - sensors_reading.py - DS18B20DataCollectingTestThread - stop - qtimer stopped / '
                      f'db closed')
        self.running = False
        self.exit()


class BME280DataCollectingThread(QtCore.QThread):
    def __init__(self, db_dict, sensor_dict, altitude):
        QtCore.QThread.__init__(self)
        logging.info(f'gui - sensors_reading.py - BME280DataCollectingThread - __init__ - sensor_dict: {sensor_dict} '
                     f'; altitude: {altitude}')
        self.name = sensor_dict['id']
        self.sensor_dict = sensor_dict
        self.address = int(sensor_dict['id'][sensor_dict['id'].find('0x'):], 16)
        self.bus = smbus2.SMBus(sensor_dict['bus'])
        self.running = False
        self.cal_params = None
        self.alt = altitude
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.acquisition_routine)
        self.started.connect(self.start_routine)


    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - start_routine')
        self.running = True
        if self.set_bme280_parameters():
            self.thread_timer.start(int(self.sensor_dict['refresh']) * 1000)
        else:
            logging.info(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - run - no sensor '
                         f'detected')
            self.stop()

    def acquisition_routine(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - acquisition_routine')
        date_time = datetime.datetime.now().replace(microsecond=0)
        temp, hum, pres, pres_msl = self.collect_data()
        self.add_data_to_db(date_time, temp, hum, pres, pres_msl)

    def collect_data(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - collect_data')
        try:
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
        self.thread_timer.stop()
        self.bus.close()
        self.cursor.close()
        self.connector.close()
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingThread/{self.name} - stop - qtimer stopped / '
                      f'db closed / bus closed')
        self.running = False
        self.exit()


class BME280DataCollectingTestThread(QtCore.QThread):
    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - BME280DataCollectingTestThread - __init__')
        self.sensors_rate = 30
        self.running = False
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.acquisition_routine)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingTestThread - start_routine')
        self.running = True
        random.seed()
        self.thread_timer.start(self.sensors_rate * 1000)

    def acquisition_routine(self):
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingTestThread - acquisition_routine')
        self.add_data_to_db(datetime.datetime.now().replace(microsecond=0),
                            round(20 + random.uniform(0, 5), 1),
                            round(65 + random.uniform(0, 20), 1),
                            round(1013 + random.uniform(0, 15), 1),
                            round(1013 + random.uniform(0, 15), 1))

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
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug(f'gui - sensors_reading.py - BME280DataCollectingTestThread - stop - qtimer stopped / '
                      f'db closed / bus closed')
        self.running = False
        self.exit()


class MqttToDbObject(QtCore.QObject):
    def __init__(self, db_dict, mqtt_dict, altitude, parent=None):
        super(MqttToDbObject, self).__init__(parent)
        logging.info(f'gui - sensors_reading.py - MqttToDbObject - __init__ - mqtt_dict: {mqtt_dict} ; altitude: '
                     f'{altitude}')
        self.alt = altitude
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.mqtt_dict = mqtt_dict
        self.mqtt_client = mqtt.Client('weather_station_thread')
        self.mqtt_client.on_message = self.parse_data
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.username_pw_set(username=self.mqtt_dict['username'], password=self.mqtt_dict['password'])

    @QtCore.pyqtSlot()
    def connect_to_mqtt(self):
        logging.debug(f'gui - sensors_reading.py - MqttToDbObject - connect_to_mqtt')
        self.mqtt_client.connect(self.mqtt_dict['address'])
        topics_list = [(f'{device_dict["main_topic"]}/{device}', 0) for device, device_dict in
                       self.mqtt_dict['devices'].items()]
        self.mqtt_client.subscribe(topics_list)
        self.mqtt_client.loop_start()

    @QtCore.pyqtSlot()
    def disconnect_from_mqtt(self):
        logging.debug('gui - sensors_reading.py - MqttToDbObject - disconnect_from_mqtt')
        self.mqtt_client.disconnect()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        logging.debug(f'gui - sensors_reading.py - MqttToDbObject - connected to broker with connect code: {rc}')

    @staticmethod
    def on_disconnect(client, userdata, rc):
        logging.debug(f'gui - sensors_reading.py - MqttToDbObject - disconnected from broker with disconnect code:'
                      f' {rc}')
        client.loop_stop()

    def parse_data(self, client, userdata, message):
        logging.debug(f'gui - sensors_reading.py - MqttToDbObject - parse data - message received : '
                      f'{str(message.payload.decode("utf-8"))} ; from {message.topic}')
        date_time = datetime.datetime.now()
        data = json.loads(str(message.payload.decode('utf-8')))
        database = os.path.basename(message.topic)
        try:
            temperature = round(data['temperature'], 1)
            if self.mqtt_dict['devices'][database]['cal_methode']:
                if self.mqtt_dict['devices'][database]['cal_methode'] == 'offset':
                    temperature += float(self.mqtt_dict['devices'][database]['cal_value'])
            try:
                humidity = round(data['humidity'], 1)
            except KeyError:
                humidity = None
            try:
                pressure = round(data['pressure'], 1)
            except KeyError:
                pressure = None
            if self.alt is not None and temperature is not None and pressure is not None:
                pressure_msl = pressure + ((pressure * 9.80665 * self.alt) /
                                           (287.0531 * (273.15 + temperature + (self.alt / 400))))
                pressure_msl = round(pressure_msl, 1)
            else:
                pressure_msl = pressure
            try:
                battery = data['battery']
            except KeyError:
                battery = None
            try:
                signal = data['linkquality']
            except KeyError:
                signal = None
        except:
            logging.exception(f'gui - sensors_reading.py - MqttToDbObject - parse data - issue with data')
            temperature, humidity, pressure, pressure_msl, battery, signal = None, None, None, None, None, None
        self.add_data_to_db(date_time, temperature, humidity, pressure, pressure_msl, battery, signal, database)

    def add_data_to_db(self, dt, tp, hm, ps, ps_sl, bt, lk, db):
        logging.debug(f'gui - sensors_reading.py - MqttToDbObject - add_data_to_db - data : {dt} | {tp} | {hm} | {ps} '
                      f'| {ps_sl} | {bt} | {lk} | {db}')
        try:
            self.cursor.execute(f'insert into "{db}" (date_time, temperature, humidity, pressure, pressure_msl, '
                                f'battery, signal) values (%s, %s, %s, %s, %s, %s, %s)',
                                (dt, tp, hm, ps, ps_sl, bt, lk))
            self.connector.commit()
        except Exception:
            logging.exception('gui - sensors_reading.py - MqttToDbObject - set_mqtt_client - an exception occurred '
                              'when adding data to db')


class MqttToDbTestThread(QtCore.QThread):
    def __init__(self, db_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - MqttToDbTestThread - __init__')
        self.running = False
        self.sensors_rate = 60
        self.connector = psycopg2.connect(user=db_dict['user'], password=db_dict['password'], host=db_dict['host'],
                                          database=db_dict['database'], port=db_dict['port'])
        self.cursor = self.connector.cursor()
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.acquisition_routine)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - MqttToDbTestThread - start_routine')
        self.running = True
        random.seed()
        self.thread_timer.start(self.sensors_rate * 1000)

    def acquisition_routine(self):
        logging.debug(f'gui - sensors_reading.py - MqttToDbTestThread - acquisition_routine')
        self.add_data_to_db(datetime.datetime.now().replace(microsecond=0),
                            round(20 + random.uniform(0, 5), 1), round(65 + random.uniform(0, 15), 1),
                            round(1013 + random.uniform(0, 10), 1), round(1013 + random.uniform(0, 20), 1),
                            75, 97, 'AQARA_THP_TEST')

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
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug(f'gui - sensors_reading.py - MqttToDbTestThread - stop - qtimer stopped / db closed')
        self.running = False
        self.exit()


class DBInDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)

    def __init__(self, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DBInDataThread - __init__')
        self.running = False
        self.sensor_dict = sensor_dict
        self.request_dict = {}
        self.temp_device = config_dict['DISPLAY']['in_temperature']
        self.hum_device = config_dict['DISPLAY']['in_humidity']
        self.pres_device = config_dict['DISPLAY']['in_pressure']
        self.sig_bat_device = config_dict['DISPLAY']['in_bat_signal']
        self.display_rate = int(config_dict['DISPLAY']['in_display_rate']) * 1000
        self.connector = psycopg2.connect(user=config_dict['DATABASE']['username'],
                                          password=config_dict['DATABASE']['password'],
                                          host=config_dict['DATABASE']['host'],
                                          database=config_dict['DATABASE']['database'],
                                          port=config_dict['DATABASE']['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.request_data)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - DBInDataThread - start_routine')
        self.running = True
        self.request_dict = self.prepare_request()
        if self.request_dict:
            self.request_data()
            self.thread_timer.start(self.display_rate)
        else:
            logging.error('gui - sensors_reading.py - DBInDataThread - request_data - no sensor in config file to '
                          'display in data or the sensor doesnt exist in sensor dict')
            self.stop()

    def prepare_request(self):
        temp_table, hum_table, pres_table, sig_bat_table = None, None, None, None
        req_dict = {}
        sensor_list = {ddict['name']: ddict['table'] for _, ddict in self.sensor_dict['DS18B20'].items()}
        sensor_list.update({ddict['name']: ddict['table'] for _, ddict in self.sensor_dict['BME280'].items()})
        sensor_list.update({device: device for device, _ in self.sensor_dict['MQTT']['devices'].items()})
        if self.temp_device:
            temp_table = sensor_list[self.temp_device]
        if self.hum_device:
            hum_table = sensor_list[self.hum_device]
        if self.pres_device:
            pres_table = sensor_list[self.pres_device]
        if self.sig_bat_device:
            sig_bat_table = sensor_list[self.sig_bat_device]

        logging.debug(f'gui - sensors_reading.py - DBInDataThread - request_data - temp_table: {temp_table} ; '
                      f'hum_table: {hum_table} ; pres_table: {pres_table}')

        if temp_table is not None:
            req_dict.update({'temp': f'SELECT temperature, date_time FROM "{temp_table}" ORDER BY date_time DESC '
                                     f'LIMIT 1',
                             'temp_minmax': f'SELECT MIN (temperature), MAX (temperature) FROM "{temp_table}"'})
        if hum_table is not None:
            req_dict.update({'hum': f'SELECT humidity FROM "{hum_table}" ORDER BY date_time DESC LIMIT 1'})
        if pres_table is not None:
            req_dict.update({'pres': f'SELECT pressure FROM "{pres_table}" ORDER BY date_time DESC LIMIT 1',
                             'pres_msl': f'SELECT pressure_msl FROM "{pres_table}" ORDER BY date_time DESC LIMIT 1'})
        if sig_bat_table is not None:
            req_dict.update({'bat': f'SELECT battery FROM "{sig_bat_table}" ORDER BY date_time DESC LIMIT 1',
                             'sig': f'SELECT signal FROM "{sig_bat_table}" ORDER BY date_time DESC LIMIT 1'})
        return req_dict

    def request_data(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - request_data')
        var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'pres_msl': None,
                    'bat': None, 'sig': None, 'old': False}
        for var, req in self.request_dict.items():
            try:
                self.cursor.execute(req)
                data = self.cursor.fetchone()
                if data is not None:
                    if var == 'temp_minmax':
                        var_dict[var] = data
                    else:
                        if var == 'temp':
                            if (datetime.datetime.now() - data[1]).total_seconds() > 7200:
                                var_dict['old'] = True
                        var_dict[var] = data[0]
            except Exception:
                logging.exception(f'gui - sensors_reading.py - DBInDataThread - request_data - an exception '
                                  f'occurred when requesting {var} with request {req}')
        logging.debug(f'gui - sensors_reading.py - DBInDataThread - request_data - var_dict: {var_dict}')
        self.db_data.emit(var_dict)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBInDataThread - stop')
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug('gui - sensors_reading.py - DBInDataThread - stop - qtimer stopped / db closed')
        self.running = False
        self.exit()


class DBOutDataThread(QtCore.QThread):
    db_data = QtCore.pyqtSignal(dict)

    def __init__(self, config_dict, sensor_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - sensors_reading.py - DBOutDataThread - __init__')
        self.running = False
        self.sensor_dict = sensor_dict
        self.request_dict = {}
        self.temp_device = config_dict['DISPLAY']['out_temperature']
        self.hum_device = config_dict['DISPLAY']['out_humidity']
        self.pres_device = config_dict['DISPLAY']['out_pressure']
        self.sig_bat_device = config_dict['DISPLAY']['out_bat_signal']
        self.display_rate = int(config_dict['DISPLAY']['out_display_rate']) * 1000
        self.connector = psycopg2.connect(user=config_dict['DATABASE']['username'],
                                          password=config_dict['DATABASE']['password'],
                                          host=config_dict['DATABASE']['host'],
                                          database=config_dict['DATABASE']['database'],
                                          port=config_dict['DATABASE']['port'])
        self.cursor = self.connector.cursor()
        self.thread_timer = QtCore.QTimer(self)
        self.thread_timer.moveToThread(self)
        self.thread_timer.timeout.connect(self.request_data)
        self.started.connect(self.start_routine)

    def start_routine(self):
        logging.debug(f'gui - sensors_reading.py - DBOutDataThread - start_routine')
        self.running = True
        self.request_dict = self.prepare_request()
        if self.request_dict:
            self.request_data()
            self.thread_timer.start(self.display_rate)
        else:
            logging.error('gui - sensors_reading.py - DBOutDataThread - request_data - no sensor in config file to '
                          'display in data or the sensor doesnt exist in sensor dict')
            self.stop()

    def prepare_request(self):
        temp_table, hum_table, pres_table, sig_bat_table = None, None, None, None
        req_dict = {}
        sensor_list = {ddict['name']: ddict['table'] for _, ddict in self.sensor_dict['DS18B20'].items()}
        sensor_list.update({ddict['name']: ddict['table'] for _, ddict in self.sensor_dict['BME280'].items()})
        sensor_list.update({device: device for device, _ in self.sensor_dict['MQTT']['devices'].items()})
        if self.temp_device:
            temp_table = sensor_list[self.temp_device]
        if self.hum_device:
            hum_table = sensor_list[self.hum_device]
        if self.pres_device:
            pres_table = sensor_list[self.pres_device]
        if self.sig_bat_device:
            sig_bat_table = sensor_list[self.sig_bat_device]

        logging.debug(f'gui - sensors_reading.py - DBOutDataThread - request_data - temp_table: {temp_table} ; '
                      f'hum_table: {hum_table} ; pres_table: {pres_table}')
        if temp_table is not None:
            req_dict.update({'temp': f'SELECT temperature, date_time FROM "{temp_table}" ORDER BY date_time DESC '
                                     f'LIMIT 1',
                             'temp_minmax': f'SELECT MIN (temperature), MAX (temperature) FROM "{temp_table}"'})
        if hum_table is not None:
            req_dict.update({'hum': f'SELECT humidity FROM "{hum_table}" ORDER BY date_time DESC LIMIT 1'})
        if pres_table is not None:
            req_dict.update({'pres': f'SELECT pressure FROM "{pres_table}" ORDER BY date_time DESC LIMIT 1',
                             'pres_msl': f'SELECT pressure_msl FROM "{pres_table}" ORDER BY date_time DESC LIMIT 1'})
        if sig_bat_table is not None:
            req_dict.update({'bat': f'SELECT battery FROM "{sig_bat_table}" ORDER BY date_time DESC LIMIT 1',
                             'sig': f'SELECT signal FROM "{sig_bat_table}" ORDER BY date_time DESC LIMIT 1'})
        return req_dict

    def request_data(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - request_data')
        var_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'pres_msl': None,
                    'bat': None, 'sig': None, 'old': False}
        for var, req in self.request_dict.items():
            try:
                self.cursor.execute(req)
                data = self.cursor.fetchone()
                if data is not None:
                    if var == 'temp_minmax':
                        var_dict[var] = data
                    else:
                        if var == 'temp':
                            if (datetime.datetime.now() - data[1]).total_seconds() > 7200:
                                var_dict['old'] = True
                        var_dict[var] = data[0]
            except Exception:
                logging.exception(f'gui - sensors_reading.py - DBOutDataThread - request_data - an exception '
                                  f'occurred when requesting {var} with request {req}')
        logging.debug(f'gui - sensors_reading.py - DBOutDataThread - request_data - var_dict: {var_dict}')
        self.db_data.emit(var_dict)

    def stop(self):
        logging.debug('gui - sensors_reading.py - DBOutDataThread - stop')
        self.thread_timer.stop()
        self.cursor.close()
        self.connector.close()
        logging.debug('gui - sensors_reading.py - DBOutDataThread - stop - qtimer stopped / db closed')
        self.running = False
        self.exit()
