import io
import os
import copy
import json
import math
import time
import ephem
import pickle
import platform
import logging
import pathlib
import configparser
import tempfile
import shutil
import datetime
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from pyqtspinner.spinner import WaitingSpinner
from ui.version import gui_version
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utils import (days_months_dictionary, stylesheet_creation_function, clear_layout,
                             shadow_creation_function, icon_creation_function, battery_value_icon_dict,
                             link_value_icon_dict, angle_moon_phase, get_season)
from functions.window_functions.option_window import MyOptions
from functions.window_functions.weather_windows import My1hFCDetails, My6hFCDetails, My1dFCDetails
from functions.window_functions.other_windows import (MyAbout, MyExit, MyDownload, MyWarning, MyWarningUpdate,
                                                      MyConnexion, MyBatLink, MyPressure, MyTempHum, MyInfo)
from functions.thread_functions.sensors_reading import (DS18B20DataCollectingThread, BME280DataCollectingThread,
                                                        MqttToDbThread, DBInDataThread, DBOutDataThread,
                                                        DS18B20DataCollectingTestThread, MqttToDbTestThread,
                                                        BME280DataCollectingTestThread)
from functions.thread_functions.forecast_request import MFForecastRequest, OWForecastRequest
from functions.thread_functions.other_threads import (CleaningThread, CheckUpdate, CheckInternetConnexion,
                                                      RequestPlotDataThread, CheckPostgresqlConnexion)
from functions.gui_functions import (add_1h_forecast_widget, add_6h_forecast_widget, clean_1h_forecast_widgets,
                                     clean_6h_forecast_widgets)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, user_path, config_dict, sensor_dict, parent=None):
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.gui_path = path
        self.user_path = user_path
        self.config_dict = config_dict
        self.sensor_dict = sensor_dict
        self.place_object = None
        self.database_ok = False
        self.connector = None
        self.cursor = None
        QtGui.QFontDatabase.addApplicationFont(f'{self.gui_path}/fonts/SourceSansPro-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont(f'{self.gui_path}/fonts/SourceSansPro-SemiBold.ttf')
        self.setupUi(self)
        if platform.system() == 'Linux':
            self.showFullScreen()
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BlankCursor)
        self.menu_layout.setAlignment(QtCore.Qt.AlignTop)
        self.current_date = None
        self.figure_in = None
        self.figure_out = None
        self.canvas_in = None
        self.canvas_out = None
        self.plot_in = None
        self.plot_in_2 = None
        self.plot_out = None
        self.plot_out_2 = None
        self.spinner = None
        self.h_spin_lay = None
        self.ds18b20_data_threads = []
        self.bme280_data_threads = []
        self.collect_ds18b20_data_thread = None
        self.collect_bme180_data_thread = None
        self.collect_mqtt_data_thread = None
        self.display_sensors_data_thread = None
        self.query_mf_forecast_thread = None
        self.query_ow_forecast_thread = None
        self.display_in_data_thread = None
        self.display_out_data_thread = None
        self.db_cleaning_thread = None
        self.check_update_thread = None
        self.request_plot_thread = None
        self.forecast_data = None
        self.check_internet = None
        self.check_posgresql = None
        self.update_url = None
        self.timer = None
        self.in_temperature = None
        self.in_temperature_min_max = None
        self.in_humidity = None
        self.in_pressure = None
        self.in_pressure_msl = None
        self.in_battery = None
        self.in_signal = None
        self.out_temperature = None
        self.out_temperature_min_max = None
        self.out_humidity = None
        self.out_pressure = None
        self.out_pressure_msl = None
        self.out_battery = None
        self.out_signal = None
        self.sunrise = None
        self.sunset = None
        self.fc_1h_vert_lay_1 = []
        self.fc_1h_lb_1 = []
        self.fc_1h_lb_2 = []
        self.fc_1h_bt_1 = []
        self.fc_1h_fr_1 = []
        self.fc_1h_nbr1 = 0
        self.fc_6h_vert_lay_1 = []
        self.fc_6h_lb_1 = []
        self.fc_6h_lb_2 = []
        self.fc_6h_bt_1 = []
        self.fc_6h_fr_1 = []
        self.fc_6h_nbr1 = 0
        self.warning_button.setObjectName('no_function')
        self.exit_button.clicked.connect(self.exit_menu)
        self.about_button.clicked.connect(self.about_weather_station)
        self.option_button.clicked.connect(self.open_options)
        self.warning_button.clicked.connect(self.warning_update_dispatch)
        self.in_out_bt.clicked.connect(lambda: self.set_stack_widget_page(0))
        self.ephemeride_bt.clicked.connect(lambda: self.set_stack_widget_page(1))
        self.time_series_bt.clicked.connect(lambda: self.set_stack_widget_page(2))
        self.h1_prev_bt.clicked.connect(lambda: self.set_stack_widget_page(3))
        self.h6_prev_bt.clicked.connect(lambda: self.set_stack_widget_page(4))
        self.left_ts_button.clicked.connect(self.set_ts_stack_left)
        self.right_ts_button.clicked.connect(self.set_ts_stack_right)
        self.left_fc_button.clicked.connect(self.set_fc_stack_left)
        self.right_fc_button.clicked.connect(self.set_fc_stack_right)
        self.out_battery_bt.clicked.connect(self.show_bat_link_details)
        self.out_signal_bt.clicked.connect(self.show_bat_link_details)
        self.in_battery_bt.clicked.connect(self.show_bat_link_details)
        self.in_signal_bt.clicked.connect(self.show_bat_link_details)
        self.in_pressure_bt.clicked.connect(self.show_pressure_details)
        self.out_pressure_bt.clicked.connect(self.show_pressure_details)
        self.in_humidity_bt.clicked.connect(self.show_hum_temp_details)
        self.out_humidity_bt.clicked.connect(self.show_hum_temp_details)
        self.button_list = [self.in_out_bt, self.ephemeride_bt, self.time_series_bt, self.h1_prev_bt, self.h6_prev_bt]
        self.in_out_bt.setStyleSheet(stylesheet_creation_function('qtoolbutton_menu_activated'))
        self.time_label.setGraphicsEffect(shadow_creation_function(1, 5))
        self.in_temperature_label.setGraphicsEffect(shadow_creation_function(2, 5))
        self.out_temperature_label.setGraphicsEffect(shadow_creation_function(2, 5))
        self.in_humidity_bt.setGraphicsEffect(shadow_creation_function(1, 5))
        self.in_pressure_bt.setGraphicsEffect(shadow_creation_function(1, 5))
        self.out_humidity_bt.setGraphicsEffect(shadow_creation_function(1, 5))
        self.out_pressure_bt.setGraphicsEffect(shadow_creation_function(1, 5))
        self.time_label.setText(QtCore.QTime.currentTime().toString('hh:mm:ss'))
        self.show_date()
        self.set_time_date()
        self.load_place_data()
        self.compute_ephemerides()
        self.check_postgresql_connection()
        self.check_internet_connection()

    def check_postgresql_connection(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_postgresql_connection')
        db_dict = {'user': self.config_dict.get('DATABASE', 'username'),
                   'password': self.config_dict.get('DATABASE', 'password'),
                   'host': self.config_dict.get('DATABASE', 'host'),
                   'database': self.config_dict.get('DATABASE', 'database'),
                   'port': self.config_dict.get('DATABASE', 'port')}
        self.check_posgresql = CheckPostgresqlConnexion(db_dict, self.sensor_dict)
        self.check_posgresql.results.connect(self.parse_posgresql_check)
        self.check_posgresql.start()

    def check_internet_connection(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_internet_connection')
        self.check_internet = CheckInternetConnexion()
        self.check_internet.connexion_alive.connect(self.start_internet_services)
        self.check_internet.no_connexion.connect(self.no_internet_message)
        self.check_internet.start()

    def parse_posgresql_check(self, results):
        logging.debug(f'gui - mainwindow.py - MainWindow - parse_posgresql_check - results: {results}')
        if results[0] and results[1]:
            self.database_ok = True
            self.launch_clean_thread()
            self.collect_sensors_data()
            self.display_sensors_data()
        else:
            if not results[0]:
                text = ('La station météo n\'a pas trouvé PostgreSQL. Veuillez l\'installer ou vérifier son '
                        'installation. PostgreSQL est obligatoire pour gérer la base de données des capteurs.')
            else:
                text = ('La station météo n\'a pas pu se connecter à la base de données ou celle-ci n\'existe pas. '
                        'Veuillez vérifier la présence de la base de données et d\'un utilisateur pouvant s\'y '
                        'connecter.')
            info_window = MyInfo(text, self)
            info_window.exec_()

    def start_internet_services(self):
        logging.debug('gui - mainwindow.py - MainWindow - start_internet_services')
        self.check_update()
        self.launch_weather_request()

    def load_place_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - load_place_data')
        if self.config_dict.getboolean('API', 'user_place'):
            try:
                f = open(pathlib.Path(self.user_path).joinpath('place_object.dat'), 'rb')
                self.place_object = pickle.load(f)
                f.close()
            except FileNotFoundError:
                logging.exception('gui - mainwindow.py - MainWindow - load_place_data - place_object.dat has not been '
                                  'found')
        else:
            logging.warning('gui - mainwindow.py - MainWindow - load_place_data - no user_place, self.place_object is '
                            'None')

    def set_stack_widget_page(self, idx):
        logging.debug(f'gui - mainwindow.py - MainWindow - set_stack_widget_page - idx: {idx}')
        for button in self.button_list:
            button.setStyleSheet(stylesheet_creation_function('qtoolbutton_menu'))
        self.button_list[idx].setStyleSheet(stylesheet_creation_function('qtoolbutton_menu_activated'))
        self.main_stacked_widget.setCurrentIndex(idx)
        if idx == 1:
            self.compute_ephemerides()
        elif idx == 2:
            self.plot_time_series_start()
        elif idx == 3:
            self.display_fc_1h()
        elif idx == 4:
            self.display_fc_6h()

    def set_ts_stack_left(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_ts_stack_left')
        idx = self.time_series_stack.currentIndex()
        if idx != 0:
            self.time_series_stack.setCurrentIndex(idx - 1)
            self.set_ts_stack_icon()

    def set_ts_stack_right(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_ts_stack_right')
        idx = self.time_series_stack.currentIndex()
        if idx != 1:
            self.time_series_stack.setCurrentIndex(idx + 1)
            self.set_ts_stack_icon()

    def set_fc_stack_left(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_fc_stack_left')
        idx = self.forecast_1h_stack.currentIndex()
        if idx != 0:
            self.forecast_1h_stack.setCurrentIndex(idx - 1)
            self.set_fc_stack_icon()

    def set_fc_stack_right(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_fc_stack_right')
        idx = self.forecast_1h_stack.currentIndex()
        if idx != 1:
            self.forecast_1h_stack.setCurrentIndex(idx + 1)
            self.set_fc_stack_icon()

    def set_ts_stack_icon(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_ts_stack_icon')
        idx = self.time_series_stack.currentIndex() + 1
        for button in self.findChildren(QtWidgets.QToolButton, QtCore.QRegExp('ts_page_marker*')):
            if idx == int(button.objectName()[-1:]):
                button.setIcon(icon_creation_function('filled_circle_icon.svg'))
            else:
                button.setIcon(icon_creation_function('empty_circle_icon.svg'))

    def set_fc_stack_icon(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_fc_stack_icon')
        idx = self.forecast_1h_stack.currentIndex() + 1
        for button in self.findChildren(QtWidgets.QToolButton, QtCore.QRegExp('fc_page_marker*')):
            if idx == int(button.objectName()[-1:]):
                button.setIcon(icon_creation_function('filled_circle_icon.svg'))
            else:
                button.setIcon(icon_creation_function('empty_circle_icon.svg'))

    def set_time_date(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_time_date')
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.show_time_date)
        self.timer.start(1000)

    def show_time_date(self):
        self.time_label.setText(QtCore.QTime.currentTime().toString('hh:mm:ss'))
        self.show_date()

    def show_date(self):
        if QtCore.QDate.currentDate() != self.current_date:
            self.current_date = QtCore.QDate.currentDate()
            week_day = days_months_dictionary()['day'][self.current_date.dayOfWeek()]
            day = str(self.current_date.day())
            month = days_months_dictionary()['month'][self.current_date.month()]
            year = str(self.current_date.year())
            self.date_label.setText(f'{week_day} {day}\n{month} {year}')

    def compute_ephemerides(self):
        logging.debug('gui - mainwindow.py - MainWindow - compute_ephemerides')
        if self.place_object and self.place_object is not None:
            if self.config_dict.get('API', 'api_used') == 'meteofrance':
                lon = str(self.place_object.longitude)
                lat = str(self.place_object.latitude)
            else:
                lon = str(self.place_object.lon)
                lat = str(self.place_object.lat)
            date = self.current_date.toPyDate()
            observer = ephem.Observer()
            observer.lat, observer.lon, observer.date = lat, lon, date
            moon, sun = ephem.Moon(), ephem.Sun()
            sun.compute(observer)
            moon.compute(observer)
            sunlon = ephem.Ecliptic(sun).lon / math.pi * 180.0
            moonlon = ephem.Ecliptic(moon).lon / math.pi * 180.0
            if sunlon >= moonlon:
                angle = sunlon - moonlon
            else:
                angle = 360 - sunlon - moonlon
            angle_dict = angle_moon_phase()
            angle_list = [a for a in angle_dict]
            svg = None
            for i in range(len(angle_list) - 1):
                if angle_list[i] <= angle < angle_list[i + 1]:
                    svg = angle_dict[angle_list[i]]
                    break
            self.sunrise = ephem.localtime(observer.next_rising(sun, start=date.strftime('%Y/%m/%d')))
            self.sunset = ephem.localtime(observer.next_setting(sun, start=date.strftime('%Y/%m/%d')))
            sunlive = self.sunset - self.sunrise
            moonrise = ephem.localtime(observer.next_rising(moon, start=date.strftime('%Y/%m/%d')))
            moonset = ephem.localtime(observer.next_setting(moon, start=date.strftime('%Y/%m/%d')))
            yday = date.timetuple().tm_yday
            nweek = date.isocalendar()[1]
            season = get_season(date)
            week_day = days_months_dictionary()['day'][self.current_date.dayOfWeek()]
            day = str(self.current_date.day())
            month = days_months_dictionary()['month'][self.current_date.month()]
            year = str(self.current_date.year())
            self.day_box.setTitle(f'{week_day} {day} {month} {year}')
            if yday == 1:
                self.day_lb_1.setText(f'{yday}er jour de l’année')
            else:
                self.day_lb_1.setText(f'{yday}ème jour de l’année')
            self.day_lb_2.setText(f'Semaine {nweek}')
            self.day_lb_3.setText(season)
            self.sun_lb_1.setText(f'Le Soleil se lève à {self.sunrise.strftime("%Hh%M")} et se couche à '
                                  f'{self.sunset.strftime("%Hh%M")}')
            h = str(sunlive.seconds//3600)
            if len(h) == 1:
                h = '0' + h
            m = str((sunlive.seconds//60) % 60)
            if len(m) == 1:
                m = '0' + m
            self.sun_lb_2.setText(f'Durée d’ensoleillement: {h}h{m}')
            self.moon_lb_1.setText(f'La Lune se lève à {moonrise.strftime("%Hh%M")} et se couche à '
                                   f'{moonset.strftime("%Hh%M")}')
            self.moon_lb_3.setPixmap(QtGui.QPixmap(f'graphic_materials/pictogrammes/moon_phases/{svg}'))

    def launch_clean_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_clean_thread')
        db_dict = {'user': self.config_dict.get('DATABASE', 'username'),
                   'password': self.config_dict.get('DATABASE', 'password'),
                   'host': self.config_dict.get('DATABASE', 'host'),
                   'database': self.config_dict.get('DATABASE', 'database'),
                   'port': self.config_dict.get('DATABASE', 'port')}
        self.db_cleaning_thread = CleaningThread(db_dict, self.sensor_dict)
        self.db_cleaning_thread.error.connect(self.log_thread_error)
        self.db_cleaning_thread.start()

    def collect_sensors_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - collect_sensors_data')
        db_dict = {'user': self.config_dict.get('DATABASE', 'username'),
                   'password': self.config_dict.get('DATABASE', 'password'),
                   'host': self.config_dict.get('DATABASE', 'host'),
                   'database': self.config_dict.get('DATABASE', 'database'),
                   'port': self.config_dict.get('DATABASE', 'port')}
        if self.config_dict.get('SYSTEM', 'place_altitude'):
            alt = float(self.config_dict.get('SYSTEM', 'place_altitude'))
        else:
            alt = None
        if platform.system() == 'Linux':
            for _, ddict in self.sensor_dict['DS18B20'].items():
                if ddict['table']:
                    self.ds18b20_data_threads.append(DS18B20DataCollectingThread(db_dict, ddict))
            for _, ddict in self.sensor_dict['BME280'].items():
                if ddict['table']:
                    self.bme280_data_threads.append(BME280DataCollectingThread(db_dict, ddict, alt))
            if (self.sensor_dict['MQTT'] and self.sensor_dict['MQTT']['username'] and
                    self.sensor_dict['MQTT']['password'] and self.sensor_dict['MQTT']['address'] and
                    self.sensor_dict['MQTT']['main_topic'] and self.sensor_dict['MQTT']['devices']):
                self.collect_mqtt_data_thread = MqttToDbThread(db_dict, self.sensor_dict['MQTT'], alt)
                self.collect_mqtt_data_thread.error.connect(self.log_thread_error)
                self.collect_mqtt_data_thread.start()
        else:
            self.ds18b20_data_threads.append(DS18B20DataCollectingTestThread(db_dict))
            self.bme280_data_threads.append(BME280DataCollectingTestThread(db_dict))
            self.collect_mqtt_data_thread = MqttToDbTestThread(db_dict)
            self.collect_mqtt_data_thread.error.connect(self.log_thread_error)
            self.collect_mqtt_data_thread.start()

        for thread in self.ds18b20_data_threads + self.bme280_data_threads:
            thread.error.connect(self.log_thread_error)
            thread.start()

    def display_sensors_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_sensors_data')
        if self.config_dict.get('DISPLAY', 'in_sensor'):
            self.display_in_data_thread = DBInDataThread(self.config_dict, self.sensor_dict)
            self.display_in_data_thread.db_data.connect(self.refresh_in_data)
            self.display_in_data_thread.error.connect(self.log_thread_error)
            self.display_in_data_thread.start()
        else:
            data_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'pres_msl': None, 'bat': None,
                         'sig': None}
            self.refresh_in_data(data_dict)
        if self.config_dict.get('DISPLAY', 'out_sensor'):
            self.display_out_data_thread = DBOutDataThread(self.config_dict, self.sensor_dict)
            self.display_out_data_thread.db_data.connect(self.refresh_out_data)
            self.display_out_data_thread.error.connect(self.log_thread_error)
            self.display_out_data_thread.start()
        else:
            data_dict = {'temp': None, 'temp_minmax': None, 'hum': None, 'pres': None, 'pres_msl': None, 'bat': None,
                         'sig': None}
            self.refresh_out_data(data_dict)

    def no_internet_message(self):
        logging.warning('gui - mainwindow.py - MainWindow - no_internet_message - there is no connexion to the '
                        'outside world !')
        connexion_window = MyConnexion(self)
        connexion_window.exec_()
        if connexion_window.retry:
            self.check_internet_connection()

    def launch_weather_request(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_weather_request')
        if self.config_dict.get('API', 'api_used') and self.place_object is not None:
            if self.config_dict.get('API', 'api_used') == 'meteofrance':
                self.launch_mf_request_thread()
            elif self.config_dict.get('API', 'api_used') == 'openweather':
                self.launch_ow_request_thread()
        else:
            logging.warning('gui - mainwindow.py - MainWindow - launch_weather_request : no API registered in options'
                            ' and/or  self.place_object is None')

    def launch_mf_request_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_fc_request_thread')
        self.query_mf_forecast_thread = MFForecastRequest(self.place_object, self.config_dict)
        self.query_mf_forecast_thread.fc_data.connect(self.parse_forecast_data)
        self.query_mf_forecast_thread.error.connect(self.log_thread_error)
        self.query_mf_forecast_thread.start()

    def launch_ow_request_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_ow_request_thread')
        self.query_ow_forecast_thread = OWForecastRequest(self.place_object, self.config_dict)
        self.query_ow_forecast_thread.fc_data.connect(self.parse_forecast_data)
        self.query_ow_forecast_thread.error.connect(self.log_thread_error)
        self.query_ow_forecast_thread.start()

    def check_update(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_update')
        self.check_update_thread = CheckUpdate(gui_version)
        self.check_update_thread.finished.connect(self.display_gui_update_button)
        self.check_update_thread.error.connect(self.log_thread_error)
        self.check_update_thread.start()

    def refresh_in_data(self, data_dict):
        logging.debug('gui - mainwindow.py - MainWindow - refresh_in_data')
        self.in_temperature = data_dict['temp']
        self.in_temperature_min_max = data_dict['temp_minmax']
        self.in_humidity = data_dict['hum']
        self.in_pressure = data_dict['pres']
        self.in_pressure_msl = data_dict['pres_msl']
        self.in_battery = data_dict['bat']
        self.in_signal = data_dict['sig']
        self.refresh_in_display()

    def refresh_out_data(self, data_dict):
        logging.debug('gui - mainwindow.py - MainWindow - refresh_out_data')
        self.out_temperature = data_dict['temp']
        self.out_temperature_min_max = data_dict['temp_minmax']
        self.out_humidity = data_dict['hum']
        self.out_pressure = data_dict['pres']
        self.out_pressure_msl = data_dict['pres_msl']
        self.out_battery = data_dict['bat']
        self.out_signal = data_dict['sig']
        self.refresh_out_display()

    def refresh_in_display(self):
        logging.debug('gui - mainwindow.py - MainWindow - refresh_in_display')
        if self.in_temperature is not None:
            self.in_temperature_label.setText(f'{self.in_temperature} °C')
        else:
            self.in_temperature_label.setText('No data')
        if self.in_temperature_min_max is not None and self.in_temperature_min_max[0] is not None:
            self.in_label_3.setText(f'{self.in_temperature_min_max[0]} °C / {self.in_temperature_min_max[1]} °C')
        else:
            self.in_label_3.setText('No data / No data')
        if self.in_humidity is not None:
            self.in_humidity_bt.setEnabled(True)
            self.in_humidity_bt.setText(f'Humidité : {round(self.in_humidity)} %')
        else:
            self.in_humidity_bt.setEnabled(False)
            self.in_humidity_bt.setText('')
        if self.in_pressure is not None:
            self.in_pressure_bt.setEnabled(True)
            if self.in_pressure_msl is not None and self.config_dict.getboolean('DISPLAY', 'in_msl_pressure'):
                self.in_pressure_bt.setText(f'Pression SL : {round(self.in_pressure_msl)} hPa')
            else:
                self.in_pressure_bt.setText(f'Pression : {round(self.in_pressure)} hPa')
        else:
            self.in_pressure_bt.setEnabled(False)
            self.in_pressure_bt.setText('')

        if self.in_battery is not None:
            self.in_battery_bt.setEnabled(True)
            icon = 'batterie_0-5_icon.svg'
            bat_list = sorted(list(battery_value_icon_dict().keys()))
            for i, val in enumerate(bat_list[: -1]):
                if bat_list[i] <= self.in_battery < bat_list[i + 1]:
                    icon = battery_value_icon_dict()[val]
        else:
            self.in_battery_bt.setEnabled(False)
            icon = 'none_icon.png'
        self.in_battery_bt.setIcon(icon_creation_function(icon))

        if self.in_signal is not None:
            self.in_signal_bt.setEnabled(True)
            icon = 'signal_0-5_icon.svg'
            link_list = sorted(list(link_value_icon_dict().keys()))
            for i, val in enumerate(link_list[: -1]):
                if link_list[i] <= self.in_signal < link_list[i + 1]:
                    icon = link_value_icon_dict()[val]
        else:
            self.in_signal_bt.setEnabled(False)
            icon = 'none_icon.png'
        self.in_signal_bt.setIcon(icon_creation_function(icon))

    def refresh_out_display(self):
        logging.debug('gui - mainwindow.py - MainWindow - refresh_out_display')
        if self.out_temperature is not None:
            self.out_temperature_label.setText(f'{self.out_temperature} °C')
        else:
            self.out_temperature_label.setText('No data')
        if self.out_temperature_min_max is not None and self.out_temperature_min_max[0] is not None:
            self.out_label_3.setText(f'{self.out_temperature_min_max[0]} °C / {self.out_temperature_min_max[1]} °C')
        else:
            self.out_label_3.setText('No data / No data')
        if self.out_humidity is not None:
            self.out_humidity_bt.setEnabled(True)
            self.out_humidity_bt.setText(f'Humidité : {round(self.out_humidity)} %')
        else:
            self.out_humidity_bt.setEnabled(False)
            self.out_humidity_bt.setText('')
        if self.out_pressure is not None:
            self.out_pressure_bt.setEnabled(True)
            if self.out_pressure_msl is not None and self.config_dict.getboolean('DISPLAY', 'out_msl_pressure'):
                self.out_pressure_bt.setText(f'Pression SL : {round(self.out_pressure_msl)} hPa')
            else:
                self.out_pressure_bt.setText(f'Pression : {round(self.out_pressure)} hPa')
        else:
            self.out_pressure_bt.setEnabled(False)
            self.out_pressure_bt.setText('')
        if self.out_battery is not None:
            self.out_battery_bt.setEnabled(True)
            icon = 'batterie_0-5_icon.svg'
            bat_list = sorted(list(battery_value_icon_dict().keys()))
            for i, val in enumerate(bat_list[: -1]):
                if bat_list[i] <= self.out_battery < bat_list[i + 1]:
                    icon = battery_value_icon_dict()[val]
        else:
            self.out_battery_bt.setEnabled(False)
            icon = 'none_icon.png'
        self.out_battery_bt.setIcon(icon_creation_function(icon))

        if self.out_signal is not None:
            self.out_signal_bt.setEnabled(True)
            icon = 'signal_0-5_icon.svg'
            link_list = sorted(list(link_value_icon_dict().keys()))
            for i, val in enumerate(link_list[: -1]):
                if link_list[i] <= self.out_signal < link_list[i + 1]:
                    icon = link_value_icon_dict()[val]
        else:
            self.out_signal_bt.setEnabled(False)
            icon = 'none_icon.png'
        self.out_signal_bt.setIcon(icon_creation_function(icon))

    def plot_time_series_start(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_time_series_start')
        self.time_series_stack.setCurrentIndex(0)
        clear_layout(self.plot_layout_1)
        clear_layout(self.plot_layout_3)
        self.setup_plot_area()
        self.h_spin_lay = QtWidgets.QHBoxLayout()
        self.h_spin_lay.setObjectName('h_spin_lay')
        self.spinner = WaitingSpinner(self, roundness=40., opacity=15., fade=70., radius=24., lines=16,
                                      line_length=26., line_width=6., speed=1., color=(75, 75, 75))
        self.h_spin_lay.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding,
                                                      QtWidgets.QSizePolicy.Minimum))
        self.h_spin_lay.addWidget(self.spinner)
        self.h_spin_lay.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding,
                                                      QtWidgets.QSizePolicy.Minimum))
        self.plot_layout_1.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                         QtWidgets.QSizePolicy.Expanding))
        self.plot_layout_1.addLayout(self.h_spin_lay)
        self.plot_layout_1.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                         QtWidgets.QSizePolicy.Expanding))
        self.spinner.start()
        if self.database_ok:
            self.request_plot_thread = RequestPlotDataThread(self.canvas_in, self.canvas_out, self.plot_in,
                                                             self.plot_in_2, self.plot_out, self.plot_out_2,
                                                             self.config_dict, self.sensor_dict)
            self.request_plot_thread.success.connect(self.plot_time_series_end)
            self.request_plot_thread.error.connect(self.plot_time_series_error)
            self.request_plot_thread.start()
        else:
            self.plot_time_series_error()

    def plot_time_series_end(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_time_series_end')
        self.spinner.stop()
        clear_layout(self.plot_layout_1)
        clear_layout(self.plot_layout_3)
        self.plot_layout_1.addWidget(self.canvas_in)
        self.plot_layout_3.addWidget(self.canvas_out)
        self.plot_layout_1.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                         QtWidgets.QSizePolicy.Fixed))
        self.plot_layout_3.addItem(QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum,
                                                         QtWidgets.QSizePolicy.Fixed))

    def plot_time_series_error(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_time_series_error')
        self.spinner.stop()
        clear_layout(self.plot_layout_1)
        clear_layout(self.plot_layout_3)

    def setup_plot_area(self):
        logging.debug('gui - mainwindow.py - MainWindow - setup_plot_area')
        color_1, color_2, color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
        self.figure_in = plt.figure(facecolor='#E2F0D9')
        self.canvas_in = FigureCanvas(self.figure_in)
        NavigationToolbar(self.canvas_in, self).hide()
        self.plot_in = self.figure_in.add_subplot(1, 1, 1)
        self.plot_in_2 = self.plot_in.twinx()
        self.plot_in.spines['top'].set_visible(False)
        self.plot_in_2.spines['top'].set_visible(False)
        self.plot_in.set_facecolor('None')
        self.plot_in.set_ylabel('Température (°C)', color=color_1)
        self.plot_in.tick_params(axis='y', labelcolor=color_1)
        self.plot_in_2.set_ylabel('Humidité (%)', color=color_2)
        self.plot_in_2.tick_params(axis='y', labelcolor=color_2)
        self.figure_in.subplots_adjust(left=0.08, right=0.89, bottom=0.06, top=0.95)
        self.figure_out = plt.figure(facecolor='#FBE5D6')
        self.canvas_out = FigureCanvas(self.figure_out)
        NavigationToolbar(self.canvas_out, self).hide()
        self.plot_out = self.figure_out.add_subplot(1, 1, 1)
        self.plot_out_2 = self.plot_out.twinx()
        self.plot_out.spines['top'].set_visible(False)
        self.plot_out_2.spines['top'].set_visible(False)
        self.plot_out.set_ylabel('Température (°C)', color=color_1)
        self.plot_out.tick_params(axis='y', labelcolor=color_1)
        self.plot_out_2.set_ylabel('Pression MSL (hPa)', color=color_3)
        self.plot_out_2.tick_params(axis='y', labelcolor=color_3)
        self.figure_out.subplots_adjust(left=0.08, right=0.89, bottom=0.06, top=0.95)
        self.plot_out.set_facecolor('None')

    def parse_forecast_data(self, fc_data):
        logging.debug('gui - mainwindow.py - MainWindow - parse_forecast_data')
        if fc_data:
            self.forecast_data = fc_data
            if fc_data['warning']:
                self.warning_button.setObjectName('warning_function')
                self.warning_button.setIcon(icon_creation_function('weather_warning_icon.svg'))

    def display_fc_1h(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_fc_1h')
        if self.forecast_data:
            clean_1h_forecast_widgets(self)
            lim = 0
            for t, forecast in self.forecast_data['hourly'].items():
                hour = str(t.hour)
                weather = forecast['weather']
                temp = str(round(forecast['temp']))
                if 0 <= lim < 6:
                    horizontal_layout = self.prev1h_layout_1
                elif 6 <= lim < 12:
                    self.right_fc_button.click()
                    horizontal_layout = self.prev1h_layout_2
                elif 12 <= lim < 18:
                    horizontal_layout = self.prev1h_layout_3
                else:
                    horizontal_layout = self.prev1h_layout_4
                add_1h_forecast_widget(self, hour, weather, temp, t, horizontal_layout)
                lim += 1
            self.left_fc_button.click()

    def display_fc_6h(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_fc_6h')
        if self.forecast_data:
            clean_6h_forecast_widgets(self)

            logging.debug(f'gui - mainwindow.py - MainWindow - display_fc_6h - objects '
                          f'{len(self.forecast_data["quaterly"])}')
            if self.forecast_data['api'] == 'meteofrance':
                for i in [0, 4, 8, 12, 16]:
                    dt_list = list(self.forecast_data['quaterly'].keys())[i: i + 4]
                    dt = dt_list[2]
                    weather = self.forecast_data['quaterly'][dt]['weather']
                    temp_list = [self.forecast_data['quaterly'][t]['temp'] for t in dt_list]
                    date = days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day)
                    temp = f'{round(min(temp_list))}°C / {round(max(temp_list))}°C'
                    if i < 12:
                        horizontal_layout = self.prev6h_layout_1
                    else:
                        horizontal_layout = self.prev6h_layout_2
                    add_6h_forecast_widget(self, date, weather, temp, dt_list, horizontal_layout)
            else:
                i = 0
                for dt, fc in self.forecast_data['quaterly'].items():
                    date = days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day)
                    weather = fc['weather']
                    temp = f'{round(fc["temp"]["min"])}°C / {round(fc["temp"]["max"])}°C'
                    if i < 3:
                        horizontal_layout = self.prev6h_layout_1
                    else:
                        horizontal_layout = self.prev6h_layout_2
                    data = {'temp': temp, 'date': dt, 'weather': weather, 'cover': fc['cover'], 'pres': fc['pres'],
                            'rain': fc['rain'], 'w_spd': fc['w_spd'], 'w_dir': fc['w_dir']}
                    add_6h_forecast_widget(self, date, weather, temp, data, horizontal_layout=horizontal_layout,
                                           api='openweather')
                    i += 1

    def display_1h_forecast_details(self, full_dt):
        logging.debug('gui - mainwindow.py - MainWindow - display_1h_forecast_details')
        forecast = self.forecast_data['hourly'][full_dt]
        details_window = My1hFCDetails(forecast, self)
        details_window.exec_()

    def display_1d_forecast_details(self, data):
        logging.debug('gui - mainwindow.py - MainWindow - display_1h_forecast_details')
        details_window = My1dFCDetails(data, self)
        details_window.exec_()

    def display_6h_forecast_details(self, dt_list):
        logging.debug('gui - mainwindow.py - MainWindow - display_6h_forecast_details')
        forecast = []
        for dt in dt_list:
            forecast.append([dt, self.forecast_data['quaterly'][dt]])
        details_window = My6hFCDetails(forecast, self)
        details_window.exec_()

    def show_bat_link_details(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_bat_link_details')
        if 'in' in self.sender().objectName():
            bat, sig = self.in_battery, self.in_signal
        else:
            bat, sig = self.out_battery, self.out_signal
        bat_link = MyBatLink(bat, sig, self)
        bat_link.exec_()

    def show_pressure_details(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_pressure_details')
        if self.sender().objectName() == 'out_pressure_bt':
            pres = int(round(self.out_pressure, 0))
            presmsl = int(round(self.out_pressure_msl, 0))
        else:
            pres = int(round(self.in_pressure, 0))
            presmsl = int(round(self.in_pressure_msl, 0))
        if pres is None:
            pres = 'No data'
        if presmsl is None:
            presmsl = 'No data'
        if self.config_dict.get('SYSTEM', 'place_altitude'):
            alt = int(self.config_dict.get('SYSTEM', 'place_altitude'))
        else:
            alt = 'No data'
        pres_window = MyPressure(pres, presmsl, alt, self)
        pres_window.exec_()

    def show_hum_temp_details(self):
        logging.debug('gui - mainwindow.py - MainWindow - show_hum_temp_details')
        if self.sender().objectName() == 'in_humidity_bt':
            temp = self.in_temperature
            hum = self.in_humidity
        else:
            temp = self.out_temperature
            hum = self.out_humidity
        a, b = 17.27, 237.7
        temp_ros = ((b * (((a * temp) / (b + temp)) + math.log(hum / 100.))) / (a - (((a * temp) / (b + temp)) +
                                                                                     math.log(hum / 100.))))
        temp_window = MyTempHum(hum, temp, round(temp_ros, 1), self)
        temp_window.exec_()

    def warning_update_dispatch(self):
        logging.debug('gui - mainwindow.py - MainWindow - warning_update_dispatch')
        if self.warning_button.objectName() == 'update_function':
            update_window = MyWarningUpdate(self)
            update_window.exec_()
            if not update_window.cancel:
                temp_folder = tempfile.gettempdir()
                download_window = MyDownload(self.update_url, temp_folder, self)
                download_window.exec_()
                if download_window.success:
                    install_path = pathlib.Path(self.gui_path)
                    shutil.copy(str(install_path.joinpath('functions/unzip_update.py')), temp_folder)
                    script_path = pathlib.Path(temp_folder).joinpath('unzip_update.py')
                    update_path = pathlib.Path(temp_folder).joinpath(self.update_url['file'])
                    logging.debug(f'gui - mainwindow.py - MainWindow - warning_update_dispatch - '
                                  f'install_path:{install_path} ; script_path: {script_path} '
                                  f'; update_path: {update_path}')
                    os.system(f'lxterminal -e python3 {script_path} {update_path} {install_path}')
                    time.sleep(1.5)
                    self.close()
        elif self.warning_button.objectName() == 'warning_function':
            warning_window = MyWarning(self.mf_forecast_data['warning'], self)
            warning_window.exec_()

    def open_options(self):
        logging.debug('gui - mainwindow.py - MainWindow - open_options')
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0)
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        option_window = MyOptions(config_dict_copy, copy.deepcopy(self.sensor_dict), self.user_path, self)
        option_window.exec_()
        if not option_window.cancel:
            self.sensor_dict = option_window.sensor_dict
            self.sensor_dict['modification_date'] = datetime.datetime.now().strftime('%d/%m/%Y')
            f = open(pathlib.Path(self.user_path).joinpath('sensor_file.json'), 'w')
            json.dump(self.sensor_dict, f, indent=4)
            f.close()
            self.config_dict = option_window.config_dict
            ini_file = open(pathlib.Path(self.user_path).joinpath('weather_station.ini'), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            if self.config_dict.getboolean('API', 'user_place'):
                self.place_object = option_window.place_object
                f = open(pathlib.Path(self.user_path).joinpath('place_object.dat'), 'wb')
                pickle.dump(self.place_object, f)
                f.close()

    def about_weather_station(self):
        logging.debug('gui - mainwindow.py - MainWindow - about_weather_station')
        text = (f'<p align=\"justify\">La Station Météo v{gui_version} a été développée à partir de Python et de '
                f'PyQt.</p>')
        about_window = MyAbout(text, self.gui_path, self)
        about_window.exec_()

    def display_gui_update_button(self, url_dict):
        logging.debug('gui - mainwindow.py - MainWindow - display_gui_update_button')
        if url_dict:
            self.update_url = url_dict
            if self.warning_button.objectName() == 'no_function':
                self.warning_button.setObjectName('update_function')
                self.warning_button.setIcon(icon_creation_function('weather_station_update.svg'))

    @staticmethod
    def log_thread_error(e_list):
        logging.exception(f'gui - mainwindow.py - MainWindow - log_thread_error - '
                          f'ERROR: {e_list[0]} | {str(e_list[1])}')

    def exit_menu(self):
        logging.debug('gui - mainwindow.py - MainWindow - exit_menu')
        if platform.system() == 'Windows':
            self.close()
        else:
            exit_window = MyExit(self)
            exit_window.exec_()
            if not exit_window.cancel:
                if exit_window.exit:
                    self.close()
                elif exit_window.reboot:
                    os.system('sudo shutdown -r now')
                elif exit_window.shutdown:
                    os.system('sudo shutdown -h now')

    def closeEvent(self, event):
        logging.debug('gui - mainwindow.py - MainWindow - closeEvent')
        for thread in self.ds18b20_data_threads + self.bme280_data_threads:
            thread.stop()
        if self.collect_mqtt_data_thread is not None:
            self.collect_mqtt_data_thread.stop()
        if self.db_cleaning_thread is not None:
            self.db_cleaning_thread.stop()
        if self.display_in_data_thread is not None:
            self.display_in_data_thread.stop()
        if self.display_out_data_thread is not None:
            self.display_out_data_thread.stop()
        self.timer.stop()
        logging.info('**********************************')
        logging.info('WEATHER STATION ' + gui_version + ' is closing ...')
        logging.info('**********************************')
        event.accept()
