import io
import sys
import copy
import math
import time
import pickle
import platform
import logging
import pathlib
import configparser
import datetime
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from ui.version import gui_version
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utils import (days_months_dictionary, stylesheet_creation_function, shadow_creation_function,
                             icon_creation_function, battery_value_icon_dict, link_value_icon_dict,
                             weather_to_pictogrammes, define_time_ticks)
from functions.window_functions.option_window import MyOptions
from functions.window_functions.weather_windows import My1hFCDetails, My6hFCDetails, My1dFCDetails
from functions.window_functions.other_windows import (MyAbout, MyExit, MyWarning, MyWarningUpdate,
                                                      MyConnexion, MyBatLink, MyPressure, MyTempHum, MyInfo,
                                                      MyUpdateProcess)
from functions.thread_functions.sensors_reading import (DS18B20DataCollectingThread, BME280DataCollectingThread,
                                                        DBInDataThread, DBOutDataThread, MqttToDbObject,
                                                        DS18B20DataCollectingTestThread, MqttToDbTestThread,
                                                        BME280DataCollectingTestThread)
from functions.thread_functions.forecast_request import MFForecastRequest, OWForecastRequest
from functions.thread_functions.other_threads import (CleaningThread, CheckInternetConnexion, CheckUpdate,
                                                      RequestPlotDataThread, CheckPostgresqlConnexion, DBTableManager,
                                                      ComputeEphemerisThread)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, user_path, config_dict, sensor_dict, parent=None):
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.gui_path = path
        self.user_path = user_path
        self.config_dict = config_dict
        self.sensor_dict = sensor_dict
        self.setupUi(self)
        if platform.system() == 'Linux':
            self.showFullScreen()
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.BlankCursor)
        self.menu_layout.setAlignment(QtCore.Qt.AlignTop)
        self.db_dict = {'user': config_dict.get('DATABASE', 'username'),
                        'password': config_dict.get('DATABASE', 'password'),
                        'host': config_dict.get('DATABASE', 'host'),
                        'database': config_dict.get('DATABASE', 'database'),
                        'port': config_dict.get('DATABASE', 'port')}
        self.place_object = None
        self.database_ok = False
        self.connector = None
        self.cursor = None
        self.reboot = False
        self.shutdown = False
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
        self.query_forecast_thread = None
        self.display_in_data_thread = None
        self.display_out_data_thread = None
        self.db_cleaning_thread = None
        self.check_update_thread = None
        self.request_plot_thread = None
        self.compute_ephemeris_thread = None
        self.forecast_data = None
        self.check_internet = None
        self.check_posgresql = None
        self.table_manager = None
        self.update_url = None
        self.timer = None
        self.in_temperature = None
        self.in_old = None
        self.in_temperature_min_max = None
        self.in_humidity = None
        self.in_pressure = None
        self.in_pressure_msl = None
        self.in_battery = None
        self.in_signal = None
        self.out_temperature = None
        self.out_old = None
        self.out_temperature_min_max = None
        self.out_humidity = None
        self.out_pressure = None
        self.out_pressure_msl = None
        self.out_battery = None
        self.out_signal = None
        self.first_plot = True
        self.color_1, self.color_2, self.color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
        self.forecast_service_dispatcher = {'openweather': OWForecastRequest, 'meteofrance': MFForecastRequest}
        self.sunrise_6days = []
        self.sunset_6days = []
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
        fc_buttons = self.forecast_1h_stack.findChildren(QtWidgets.QToolButton)
        for button in fc_buttons:
            button.clicked.connect(self.display_1h_forecast_details)
        fc_buttons = self.page_5.findChildren(QtWidgets.QToolButton)
        for button in fc_buttons:
            button.clicked.connect(self.display_6h1d_forecast_details)
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
        self.setup_plot_area()
        self.launch_ephemeris_thread()
        self.check_postgresql_connection()
        self.check_internet_connection()

    def check_postgresql_connection(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_postgresql_connection')
        self.check_posgresql = CheckPostgresqlConnexion(self.db_dict)
        self.check_posgresql.postgresql_ok.connect(self.launch_table_manager)
        self.check_posgresql.postgresql_failed.connect(self.postgresql_failed)
        self.check_posgresql.start()

    def launch_table_manager(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_table_manager')
        self.table_manager = DBTableManager(self.db_dict, self.sensor_dict)
        self.table_manager.work_done.connect(self.start_database_services)
        self.table_manager.work_failed.connect(self.postgresql_failed)
        self.table_manager.start()

    def postgresql_failed(self, string):
        logging.debug('gui - mainwindow.py - MainWindow - postgresql_failed')
        info_window = MyInfo(string, self)
        info_window.exec_()

    def start_database_services(self):
        logging.debug('gui - mainwindow.py - MainWindow - start_database_services')
        self.database_ok = True
        self.launch_clean_thread()
        self.collect_sensors_data()
        self.display_sensors_data()

    def check_internet_connection(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_internet_connection')
        self.check_internet = CheckInternetConnexion(self.config_dict)
        self.check_internet.connexion_alive.connect(self.start_internet_services)
        if self.config_dict.getboolean('SYSTEM', 'auto_check_connexion'):
            self.check_internet.no_connexion.connect(self.display_no_data)
        else:
            self.check_internet.no_connexion.connect(self.no_internet_message)
        self.check_internet.start()

    def start_internet_services(self):
        logging.debug('gui - mainwindow.py - MainWindow - start_internet_services')
        if getattr(sys, 'frozen', False) and self.config_dict.getboolean('SYSTEM', 'check_update'):
            self.check_update()
        self.launch_weather_request()

    def no_internet_message(self):
        logging.warning('gui - mainwindow.py - MainWindow - no_internet_message - there is no connexion to the '
                        'outside world !')
        self.display_no_data()
        connexion_window = MyConnexion(self)
        connexion_window.exec_()
        if connexion_window.retry:
            self.check_internet_connection()

    def load_place_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - load_place_data')
        place_file = pathlib.Path(self.user_path).joinpath('place_object.dat')
        if self.config_dict.getboolean('API', 'user_place') and place_file.exists():
            f = open(pathlib.Path(self.user_path).joinpath('place_object.dat'), 'rb')
            self.place_object = pickle.load(f)
            f.close()
        else:
            logging.warning('gui - mainwindow.py - MainWindow - load_place_data - user_place is False or '
                            'place_object.dat doesn\'t exist')

    def launch_ephemeris_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_ephemeris_thread')
        if self.place_object is not None:
            self.compute_ephemeris_thread = ComputeEphemerisThread(self.place_object['longitude'],
                                                                   self.place_object['latitude'])
            self.compute_ephemeris_thread.work_done.connect(self.display_ephemeris)
            self.compute_ephemeris_thread.start()

    def display_ephemeris(self, data_dict):
        logging.debug(f'gui - mainwindow.py - MainWindow - display_ephemeris - data_dict: {data_dict}')
        self.sunrise_6days = data_dict['sunrise_6days']
        self.sunset_6days = data_dict['sunset_6days']
        self.day_box.setTitle(data_dict['day_box_title'])
        self.day_lb_1.setText(data_dict['day_year'])
        self.day_lb_2.setText(data_dict['week_nbr'])
        self.day_lb_3.setText(data_dict['season'])
        self.sun_lb_1.setText(data_dict['sun_text'])
        self.sun_lb_2.setText(data_dict['sun_live'])
        self.moon_lb_1.setText(data_dict['moon_text'])
        self.moon_lb_3.setPixmap(data_dict['moon_phase'])

    def launch_clean_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_clean_thread')
        self.db_cleaning_thread = CleaningThread(self.db_dict, self.sensor_dict)
        self.db_cleaning_thread.start()

    def collect_sensors_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - collect_sensors_data')
        alt = None
        if self.config_dict.get('SYSTEM', 'place_altitude'):
            alt = float(self.config_dict.get('SYSTEM', 'place_altitude'))
        if platform.system() == 'Linux':
            for _, ddict in self.sensor_dict['DS18B20'].items():
                if ddict['table']:
                    self.ds18b20_data_threads.append(DS18B20DataCollectingThread(self.db_dict, ddict))
            for _, ddict in self.sensor_dict['BME280'].items():
                if ddict['table']:
                    self.bme280_data_threads.append(BME280DataCollectingThread(self.db_dict, ddict, alt))
            if (self.sensor_dict['MQTT'] and self.sensor_dict['MQTT']['username'] and
                    self.sensor_dict['MQTT']['password'] and self.sensor_dict['MQTT']['address'] and
                    self.sensor_dict['MQTT']['main_topic'] and self.sensor_dict['MQTT']['devices']):
                self.collect_mqtt_data_thread = [MqttToDbObject(self.db_dict, self.sensor_dict['MQTT'], alt)]
        else:
            self.ds18b20_data_threads.append(DS18B20DataCollectingTestThread(self.db_dict))
            self.bme280_data_threads.append(BME280DataCollectingTestThread(self.db_dict))
            self.collect_mqtt_data_thread = [MqttToDbTestThread(self.db_dict)]

        for thread in self.ds18b20_data_threads + self.bme280_data_threads:
            thread.start()

        for thread in self.collect_mqtt_data_thread:
            try:
                thread.connect_to_mqtt()
            except AttributeError:
                thread.start()

    def display_sensors_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_sensors_data')
        if self.config_dict.get('DISPLAY', 'in_temperature'):
            self.display_in_data_thread = DBInDataThread(self.config_dict, self.sensor_dict)
            self.display_in_data_thread.db_data.connect(self.refresh_in_display)
            self.display_in_data_thread.start()
        if self.config_dict.get('DISPLAY', 'out_temperature'):
            self.display_out_data_thread = DBOutDataThread(self.config_dict, self.sensor_dict)
            self.display_out_data_thread.db_data.connect(self.refresh_out_display)
            self.display_out_data_thread.start()

    def launch_weather_request(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_weather_request')
        if self.config_dict.get('API', 'api_used') and self.place_object is not None:
            fc_thread = self.forecast_service_dispatcher[self.config_dict.get('API', 'api_used')]
            self.query_forecast_thread = fc_thread(self.place_object, self.config_dict)
            self.query_forecast_thread.fc_data.connect(self.parse_forecast_data)
            self.query_forecast_thread.no_forecast.connect(self.display_no_data)
            self.query_forecast_thread.start()
        else:
            logging.warning('gui - mainwindow.py - MainWindow - launch_weather_request : no API registered in options'
                            ' and/or self.place_object is None')

    def check_update(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_update')
        self.check_update_thread = CheckUpdate(gui_version)
        self.check_update_thread.finished.connect(self.display_gui_update_button)
        self.check_update_thread.start()

    def refresh_in_display(self, data_dict):
        logging.debug(f'gui - mainwindow.py - MainWindow - refresh_in_display - data_dict: {data_dict}')
        self.in_temperature = data_dict['temp']
        self.in_old = data_dict['old']
        self.in_temperature_min_max = data_dict['temp_minmax']
        self.in_humidity = data_dict['hum']
        self.in_pressure = data_dict['pres']
        self.in_pressure_msl = data_dict['pres_msl']
        self.in_battery = data_dict['bat']
        self.in_signal = data_dict['sig']
        if self.in_temperature is not None:
            self.in_temperature_label.setText(f'{self.in_temperature} °C')
        else:
            self.in_temperature_label.setText('No data')
        if self.in_old:
            self.in_old_data.setText('(donnée ancienne)')
        else:
            self.in_old_data.clear()
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
                    break
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
                    break
        else:
            self.in_signal_bt.setEnabled(False)
            icon = 'none_icon.png'
        self.in_signal_bt.setIcon(icon_creation_function(icon))

    def refresh_out_display(self, data_dict):
        logging.debug(f'gui - mainwindow.py - MainWindow - refresh_out_display - data_dict: {data_dict}')
        self.out_temperature = data_dict['temp']
        self.out_old = data_dict['old']
        self.out_temperature_min_max = data_dict['temp_minmax']
        self.out_humidity = data_dict['hum']
        self.out_pressure = data_dict['pres']
        self.out_pressure_msl = data_dict['pres_msl']
        self.out_battery = data_dict['bat']
        self.out_signal = data_dict['sig']
        if self.out_temperature is not None:
            self.out_temperature_label.setText(f'{self.out_temperature} °C')
        else:
            self.out_temperature_label.setText('No data')
        if self.out_old:
            self.out_old_data.setText('(donnée ancienne)')
        else:
            self.out_old_data.clear()
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

    def request_plot_data(self):
        logging.debug(f'gui - mainwindow.py - MainWindow - request_plot_data - database_ok: {self.database_ok}')
        if self.database_ok:
            self.request_plot_thread = RequestPlotDataThread(self.config_dict, self.sensor_dict)
            self.request_plot_thread.success.connect(self.plot_time_series)
            self.request_plot_thread.error.connect(self.request_plot_data_error)
            self.request_plot_thread.start()
        else:
            msg = 'Un problème avec la base de données\nempêche l\'affichage des séries temporelles'
            self.request_plot_data_error(msg)

    def plot_time_series(self, val_dict):
        logging.debug(f'gui - mainwindow.py - MainWindow - plot_time_series')
        tick_list, label_list = define_time_ticks(val_dict['temp_in'][0][-1])
        if self.first_plot:
            self.plot_in.plot(val_dict['temp_in'][0], val_dict['temp_in'][1], color=self.color_1, linewidth=1.)
            self.plot_in_2.plot(val_dict['hum_in'][0], val_dict['hum_in'][1], color=self.color_2, linewidth=1.)
            self.plot_out.plot(val_dict['temp_out'][0], val_dict['temp_out'][1], color=self.color_1, linewidth=1.)
            self.plot_out_2.plot(val_dict['pres_out'][0], val_dict['pres_out'][1], color=self.color_3, linewidth=1.)
            self.first_plot = False
        else:
            self.plot_in.lines.pop(0)
            self.plot_in.plot(val_dict['temp_in'][0], val_dict['temp_in'][1], color=self.color_1, linewidth=1.)
            self.plot_in_2.lines.pop(0)
            self.plot_in_2.plot(val_dict['hum_in'][0], val_dict['hum_in'][1], color=self.color_2, linewidth=1.)
            self.plot_out.lines.pop(0)
            self.plot_out.plot(val_dict['temp_out'][0], val_dict['temp_out'][1], color=self.color_1, linewidth=1.)
            self.plot_out_2.lines.pop(0)
            self.plot_out_2.plot(val_dict['pres_out'][0], val_dict['pres_out'][1], color=self.color_3, linewidth=1.)
        self.plot_in.set_xlim(tick_list[0], tick_list[-1])
        self.plot_out.set_xlim(tick_list[0], tick_list[-1])
        self.plot_in.set_xticks(tick_list)
        self.plot_out.set_xticks(tick_list)
        self.plot_in.set_xticklabels(label_list)
        self.plot_out.set_xticklabels(label_list)
        self.canvas_in.draw()
        self.canvas_out.draw()

    def request_plot_data_error(self, msg):
        logging.debug('gui - mainwindow.py - MainWindow - request_plot_data_error')
        text_kwargs1 = dict(ha='center', va='center', fontsize=20, color='#2d2d2d', fontfamily='Source Sans Pro',
                            backgroundcolor='#E2F0D9')
        text_kwargs2 = dict(ha='center', va='center', fontsize=20, color='#2d2d2d', fontfamily='Source Sans Pro',
                            backgroundcolor='#FBE5D6')
        self.plot_in.text(0.5, 0.5, msg, transform=self.plot_in.transAxes, **text_kwargs1)
        self.plot_out.text(0.5, 0.5, msg, transform=self.plot_out.transAxes, **text_kwargs2)
        self.canvas_in.draw()
        self.canvas_out.draw()

    def setup_plot_area(self):
        logging.debug('gui - mainwindow.py - MainWindow - setup_plot_area')
        self.figure_in = plt.figure(facecolor='#E2F0D9')
        self.canvas_in = FigureCanvas(self.figure_in)
        NavigationToolbar(self.canvas_in, self).hide()
        self.plot_in = self.figure_in.add_subplot(1, 1, 1)
        self.plot_in_2 = self.plot_in.twinx()
        self.plot_in.spines['top'].set_visible(False)
        self.plot_in_2.spines['top'].set_visible(False)
        self.plot_in.set_facecolor('None')
        self.plot_in.set_ylabel('Température (°C)', color=self.color_1)
        self.plot_in.tick_params(axis='y', labelcolor=self.color_1)
        self.plot_in_2.set_ylabel('Humidité (%)', color=self.color_2)
        self.plot_in_2.tick_params(axis='y', labelcolor=self.color_2)
        self.figure_in.subplots_adjust(left=0.08, right=0.92, bottom=0.06, top=0.95)
        self.figure_out = plt.figure(facecolor='#FBE5D6')
        self.canvas_out = FigureCanvas(self.figure_out)
        NavigationToolbar(self.canvas_out, self).hide()
        self.plot_out = self.figure_out.add_subplot(1, 1, 1)
        self.plot_out_2 = self.plot_out.twinx()
        self.plot_out.spines['top'].set_visible(False)
        self.plot_out_2.spines['top'].set_visible(False)
        self.plot_out.set_ylabel('Température (°C)', color=self.color_1)
        self.plot_out.tick_params(axis='y', labelcolor=self.color_1)
        if self.config_dict.getboolean('TIMESERIES', 'msl_pressure'):
            ylabel = 'Pression SL (hPa)'
        else:
            ylabel = 'Pression (hPa)'
        self.plot_out_2.set_ylabel(ylabel, color=self.color_3)
        self.plot_out_2.tick_params(axis='y', labelcolor=self.color_3)
        self.figure_out.subplots_adjust(left=0.08, right=0.92, bottom=0.06, top=0.95)
        self.plot_out.set_facecolor('None')
        self.plot_in_2.set_ylim(0, 100)
        self.plot_in.set_ylim(10, 30)
        self.plot_in_2.set_yticks(range(0, 110, 10))
        self.plot_in.set_yticks(range(10, 32, 2))
        self.plot_in.grid(linestyle='-', linewidth=0.5, color='grey', alpha=0.5)
        self.plot_out_2.set_ylim(980, 1030)
        self.plot_out.set_ylim(-10, 40)
        self.plot_out_2.set_yticks(range(980, 1035, 5))
        self.plot_out.set_yticks(range(-10, 45, 5))
        self.plot_out.grid(linestyle='-', linewidth=0.5, color='grey', alpha=0.5)
        self.plot_layout_1.addWidget(self.canvas_in)
        self.plot_layout_3.addWidget(self.canvas_out)
        self.canvas_in.draw()
        self.canvas_out.draw()

    def parse_forecast_data(self, fc_data):
        logging.debug(f'gui - mainwindow.py - MainWindow - parse_forecast_data - fc_data: {fc_data}')
        if fc_data:
            self.forecast_data = fc_data
            self.display_fc_1h()
            self.display_fc_6h()
            if fc_data['warning']:
                self.warning_button.setObjectName('warning_function')
                self.warning_button.setIcon(icon_creation_function('weather_warning_icon.svg'))

    def display_fc_1h(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_fc_1h')
        if self.forecast_data:
            i = 1
            for t, forecast in self.forecast_data['hourly'].items():
                hour = str(t.hour) + 'h'
                if hour == '0h':
                    hour = 'Minuit'
                elif hour == '12h':
                    hour = 'Midi'
                hour_lb = self.forecast_1h_stack.findChild(QtWidgets.QLabel, f'fc_hour_lb_{i}')
                weat_bt = self.forecast_1h_stack.findChild(QtWidgets.QToolButton, f'fc_weat_bt_{i}')
                temp_lb = self.forecast_1h_stack.findChild(QtWidgets.QLabel, f'fc_temp_lb_{i}')
                hour_lb.setText(hour)
                weat_bt.setIcon(weather_to_pictogrammes(forecast['weather'], t, self.sunrise_6days, self.sunset_6days))
                temp_lb.setText(str(round(forecast['temp'])) + '°C')
                i += 1

    def display_fc_6h(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_fc_6h')
        if self.forecast_data:
            if self.forecast_data['api'] == 'meteofrance':
                for i in [0, 4, 8, 12, 16]:
                    dt_list = list(self.forecast_data['quaterly'].keys())[i: i + 4]
                    weather = self.forecast_data['quaterly'][dt_list[0]]['weather12h']
                    temp_list = self.forecast_data['quaterly'][dt_list[0]]['temp_min_max']
                    date = days_months_dictionary()['day'][dt_list[2].weekday() + 1] + ' ' + str(dt_list[2].day)
                    temp = f'{round(temp_list["min"])}°C / {round(temp_list["max"])}°C'
                    date_lb = self.page_5.findChild(QtWidgets.QLabel, f'fc_day_lb_{int(i / 4) + 1}')
                    weat_bt = self.page_5.findChild(QtWidgets.QToolButton, f'fc_dweat_bt_{int(i / 4) + 1}')
                    temp_lb = self.page_5.findChild(QtWidgets.QLabel, f'fc_mmtemp_lb_{int(i / 4) + 1}')
                    date_lb.setText(date)
                    weat_bt.setIcon(weather_to_pictogrammes(weather))
                    weat_bt.setText(str(i))
                    temp_lb.setText(temp)
            elif self.forecast_data['api'] == 'openweather':
                i = 0
                for dt, fc in self.forecast_data['quaterly'].items():
                    date = days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day)
                    weather = fc['weather']
                    temp = f'{round(fc["temp"]["min"])}°C / {round(fc["temp"]["max"])}°C'
                    date_lb = self.page_5.findChild(QtWidgets.QLabel, f'fc_day_lb_{i + 1}')
                    weat_bt = self.page_5.findChild(QtWidgets.QToolButton, f'fc_dweat_bt_{i + 1}')
                    temp_lb = self.page_5.findChild(QtWidgets.QLabel, f'fc_mmtemp_lb_{i + 1}')
                    date_lb.setText(date)
                    weat_bt.setIcon(weather_to_pictogrammes(weather))
                    temp_lb.setText(temp)
                    i += 1

    def display_no_data(self):
        logging.debug(f'gui - mainwindow.py - MainWindow - display_no_data')
        icon = icon_creation_function('no_data_icon')
        weat_bts = self.forecast_1h_stack.findChildren(QtWidgets.QToolButton, QtCore.QRegExp('^fc_weat_bt_'))
        weat_bts += self.page_5.findChildren(QtWidgets.QToolButton, QtCore.QRegExp('^fc_dweat_bt_'))
        weat_lbs = self.forecast_1h_stack.findChildren(QtWidgets.QLabel, QtCore.QRegExp('^fc_hour_lb_'))
        weat_lbs += self.forecast_1h_stack.findChildren(QtWidgets.QLabel, QtCore.QRegExp('^fc_temp_lb_'))
        weat_lbs += self.page_5.findChildren(QtWidgets.QLabel, QtCore.QRegExp('^fc_day_lb_'))
        weat_lbs += self.page_5.findChildren(QtWidgets.QLabel, QtCore.QRegExp('^fc_mmtemp_lb_'))
        for button in weat_bts:
            button.setIcon(icon)
        for label in weat_lbs:
            label.clear()

    def display_1h_forecast_details(self):
        logging.debug(f'gui - mainwindow.py - MainWindow - display_1h_forecast_details')
        if self.forecast_data:
            idx = int(self.sender().objectName()[11:]) - 1
            forecast = self.forecast_data['hourly'][list(self.forecast_data['hourly'].keys())[idx]]
            details_window = My1hFCDetails(forecast, self.sunrise_6days, self.sunset_6days, self)
            details_window.exec_()

    def display_6h1d_forecast_details(self):
        logging.debug(f'gui - mainwindow.py - MainWindow - display_6h1d_forecast_details')
        if self.forecast_data:
            idx1 = int(self.sender().objectName()[12:])
            if self.forecast_data['api'] == 'meteofrance':
                idx2 = int(self.sender().text())
                dt_list = list(self.forecast_data['quaterly'].keys())[idx2: idx2 + 4]
                forecast = []
                for dt in dt_list:
                    forecast.append([dt, self.forecast_data['quaterly'][dt]])
                details_window = My6hFCDetails(forecast, self.sunrise_6days[idx1], self.sunset_6days[idx1], self)
                details_window.exec_()
            elif self.forecast_data['api'] == 'openweather':
                dt = list(self.forecast_data['quaterly'].keys())[idx1 - 1]
                fc = self.forecast_data['quaterly'][dt]
                data = {'temp': f'{round(fc["temp"]["min"])}°C / {round(fc["temp"]["max"])}°C', 'date': dt,
                        'weather': fc['weather'], 'cover': fc['cover'], 'pres': fc['pres'],
                        'rain': fc['rain'], 'w_spd': fc['w_spd'], 'w_dir': fc['w_dir'], 'w_gst': fc['w_gst']}
                details_window = My1dFCDetails(data, self)
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
                install_path = pathlib.Path(self.gui_path)
                update_window = MyUpdateProcess(self.update_url, install_path, self)
                update_window.exec_()
                if update_window.success:
                    self.reboot = True
                    self.close()
        elif self.warning_button.objectName() == 'warning_function':
            warning_window = MyWarning(self.forecast_data['warning'], self)
            warning_window.exec_()

    def open_options(self):
        logging.debug('gui - mainwindow.py - MainWindow - open_options')
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0)
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        option_window = MyOptions(config_dict_copy, copy.deepcopy(self.sensor_dict), self.user_path, self)
        option_window.available_update.connect(self.force_gui_update_button)
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

    def force_gui_update_button(self, url_dict):
        logging.debug(f'gui - mainwindow.py - MainWindow - force_gui_update_button - url_dict: {url_dict}')
        self.warning_button.setObjectName('no_function')
        self.display_gui_update_button(url_dict)

    def display_gui_update_button(self, url_dict):
        logging.debug(f'gui - mainwindow.py - MainWindow - display_gui_update_button - url_dict: {url_dict}')
        if url_dict:
            self.update_url = url_dict
            if self.warning_button.objectName() == 'no_function':
                self.warning_button.setObjectName('update_function')
                self.warning_button.setIcon(icon_creation_function('weather_station_update.svg'))

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

    def set_stack_widget_page(self, idx):
        logging.debug(f'gui - mainwindow.py - MainWindow - set_stack_widget_page - idx: {idx}')
        for button in self.button_list:
            button.setStyleSheet(stylesheet_creation_function('qtoolbutton_menu'))
        self.button_list[idx].setStyleSheet(stylesheet_creation_function('qtoolbutton_menu_activated'))
        self.main_stacked_widget.setCurrentIndex(idx)
        if idx == 2:
            self.request_plot_data()

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

    def exit_menu(self):
        logging.debug('gui - mainwindow.py - MainWindow - exit_menu')
        if platform.system() == 'Windows':
            self.close_gui()
        else:
            exit_window = MyExit(self)
            exit_window.exec_()
            if not exit_window.cancel:
                if exit_window.exit:
                    self.close_gui()
                elif exit_window.reboot:
                    self.reboot = True
                    self.close_gui()
                elif exit_window.shutdown:
                    self.shutdown = True
                    self.close_gui()

    def close_gui(self):
        logging.info('gui - mainwindow.py - MainWindow - close_gui')
        if self.ds18b20_data_threads is not None:
            for thread in self.ds18b20_data_threads:
                thread.stop()
        if self.bme280_data_threads is not None:
            for thread in self.bme280_data_threads:
                thread.stop()
        if self.collect_mqtt_data_thread is not None:
            for thread in self.collect_mqtt_data_thread:
                try:
                    thread.disconnect_from_mqtt()
                except AttributeError:
                    thread.stop()
        if self.db_cleaning_thread is not None:
            self.db_cleaning_thread.stop()
        if self.display_in_data_thread is not None:
            self.display_in_data_thread.stop()
        if self.display_out_data_thread is not None:
            self.display_out_data_thread.stop()
        if self.compute_ephemeris_thread is not None:
            self.compute_ephemeris_thread.stop()
        if self.query_forecast_thread is not None:
            self.query_forecast_thread.stop()
        self.timer.stop()
        time.sleep(0.5)
        logging.info('**********************************')
        logging.info('WEATHER STATION ' + gui_version + ' is closing ...')
        logging.info('**********************************')
        if self.reboot:
            os.system('sudo shutdown -r now')
        elif self.shutdown:
            os.system('sudo shutdown -h now')
        else:
            self.close()
