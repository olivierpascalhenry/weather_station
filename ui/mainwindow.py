import collections
import io
import os
import sys
import pickle
import platform
import logging
import pathlib
import configparser
import datetime
import psycopg2
import requests
import tempfile
import shutil
import time
import numpy as np
from ui.version import gui_version, python_version, pyqt5_version
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from ui.Ui_mainwindow import Ui_MainWindow
from functions.utils import (days_months_dictionary, stylesheet_creation_function, clear_layout, mpl_hour_list,
                             shadow_creation_function, icon_creation_function, db_data_to_mpl_vectors)
from functions.window_functions.other_windows_functions import (MyAbout, MyOptions, MyExit, My1hFCDetails, MyDownload,
                                                                My6hFCDetails, MyWarning, MyWarningUpdate, MyConnexion,
                                                                MyWait)
from functions.thread_functions.sensors_reading import DataCollectingThread, DBDataDisplayThread
from functions.thread_functions.forecast_request import MFForecastRequest
from functions.thread_functions.other_threads import CleaningThread, CheckUpdate, DownloadFile, CheckInternetConnexion
from functions.gui_functions import (add_1h_forecast_widget, add_6h_forecast_widget, clean_1h_forecast_widgets,
                                     clean_6h_forecast_widgets, set_mainwindow_icons)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, path, user_path, config_dict, parent=None):
        logging.debug('gui - mainwindow.py - MainWindow - __init__')
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.gui_path = path
        self.user_path = user_path
        self.config_dict = config_dict
        self.place_object = None
        self.old_place_object = None
        self.connector = None
        self.cursor = None
        QtGui.QFontDatabase.addApplicationFont(f'{self.gui_path}/fonts/SourceSansPro-Regular.ttf')
        QtGui.QFontDatabase.addApplicationFont(f'{self.gui_path}/fonts/SourceSansPro-SemiBold.ttf')
        self.setupUi(self)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.showFullScreen()
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        set_mainwindow_icons(self)
        self.current_date = None
        self.figure_in = None
        self.figure_out = None
        self.canvas_in = None
        self.canvas_out = None
        self.plot_in = None
        self.plot_in_2 = None
        self.plot_out = None
        self.plot_out_2 = None
        self.collect_sensors_data_thread = None
        self.display_sensors_data_thread = None
        self.query_mf_forecast_thread = None
        self.db_cleaning_thread = None
        self.check_update_thread = None
        self.mf_forecast_data = None
        self.check_internet = None
        self.update_url = None
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
        self.time_series_bt.clicked.connect(lambda: self.set_stack_widget_page(1))
        self.h1_prev_bt.clicked.connect(lambda: self.set_stack_widget_page(2))
        self.h6_prev_bt.clicked.connect(lambda: self.set_stack_widget_page(3))
        self.left_ts_button.clicked.connect(self.set_ts_stack_left)
        self.right_ts_button.clicked.connect(self.set_ts_stack_right)
        self.left_fc_button.clicked.connect(self.set_fc_stack_left)
        self.right_fc_button.clicked.connect(self.set_fc_stack_right)
        self.button_list = [self.in_out_bt, self.time_series_bt, self.h1_prev_bt, self.h6_prev_bt]
        self.in_out_bt.setStyleSheet(stylesheet_creation_function('qtoolbutton_menu_activated', self.gui_path))

        if self.config_dict.getboolean('METEOFRANCE', 'user_place'):
            f = open(self.user_path + '/place_object.dat', 'rb')
            self.place_object = pickle.load(f)
            self.old_place_object = self.place_object
            f.close()

        self.time_label.setGraphicsEffect(shadow_creation_function(1, 5))
        self.in_temperature_label.setGraphicsEffect(shadow_creation_function(2, 5))
        self.out_temperature_label.setGraphicsEffect(shadow_creation_function(2, 5))
        self.in_humidity_label_1.setGraphicsEffect(shadow_creation_function(2, 5))
        self.out_pressure_label_1.setGraphicsEffect(shadow_creation_function(1, 5))
        self.time_label.setText(QtCore.QTime.currentTime().toString('hh:mm:ss'))
        self.show_date()
        self.setup_plot_area()
        self.set_time_date()

        self.database_connection()
        self.launch_clean_thread()
        self.collect_sensors_data()
        self.display_sensors_data()
        self.check_internet_connection()

    def set_stack_widget_page(self, idx):
        logging.debug('gui - mainwindow.py - MainWindow - set_stack_widget_page - idx ' + str(idx))
        self.main_stacked_widget.setCurrentIndex(idx)
        for button in self.button_list:
            button.setStyleSheet(stylesheet_creation_function('qtoolbutton_menu', self.gui_path))
        self.button_list[idx].setStyleSheet(stylesheet_creation_function('qtoolbutton_menu_activated', self.gui_path))
        if idx == 1:
            self.plot_time_series()
        elif idx == 2:
            self.display_fc_1h()
        elif idx == 3:
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
                button.setIcon(icon_creation_function('filled_circle_icon.svg', self.gui_path))
            else:
                button.setIcon(icon_creation_function('empty_circle_icon.svg', self.gui_path))

    def set_fc_stack_icon(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_fc_stack_icon')
        idx = self.forecast_1h_stack.currentIndex() + 1
        for button in self.findChildren(QtWidgets.QToolButton, QtCore.QRegExp('fc_page_marker*')):
            if idx == int(button.objectName()[-1:]):
                button.setIcon(icon_creation_function('filled_circle_icon.svg', self.gui_path))
            else:
                button.setIcon(icon_creation_function('empty_circle_icon.svg', self.gui_path))

    def set_time_date(self):
        logging.debug('gui - mainwindow.py - MainWindow - set_time_date')
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.show_time_date)
        timer.start(1000)

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

    def setup_plot_area(self):
        logging.debug('gui - mainwindow.py - MainWindow - setup_plot_area')
        color_1, color_2, color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
        self.figure_in = plt.figure(facecolor='#E2F0D9')
        self.canvas_in = FigureCanvas(self.figure_in)
        self.plot_layout_1.addWidget(self.canvas_in)
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
        self.figure_in.subplots_adjust(left=0.08, right=0.92, bottom=0.15, top=0.90)
        self.figure_out = plt.figure(facecolor='#FBE5D6')
        self.canvas_out = FigureCanvas(self.figure_out)
        self.plot_layout_3.addWidget(self.canvas_out)
        NavigationToolbar(self.canvas_out, self).hide()
        self.plot_out = self.figure_out.add_subplot(1, 1, 1)
        self.plot_out_2 = self.plot_out.twinx()
        self.plot_out.spines['top'].set_visible(False)
        self.plot_out_2.spines['top'].set_visible(False)
        self.plot_out.set_ylabel('Température (°C)', color=color_1)
        self.plot_out.tick_params(axis='y', labelcolor=color_1)
        self.plot_out_2.set_ylabel('Pression (hPa)', color=color_3)
        self.plot_out_2.tick_params(axis='y', labelcolor=color_3)
        self.figure_out.subplots_adjust(left=0.08, right=0.92, bottom=0.15, top=0.90)
        self.plot_out.set_facecolor('None')

    def database_connection(self):
        logging.debug('gui - mainwindow.py - MainWindow - database_connection')
        try:
            self.connector = psycopg2.connect(user='weather_station', password='31weather64', host='127.0.0.1',
                                              database='weather_station_db')
            self.cursor = self.connector.cursor()
        except:
            logging.exception('gui - mainwindow.py - MainWindow - database_connection - ERROR: impossible to connect '
                              'to the database')

    def launch_clean_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_clean_thread')
        self.db_cleaning_thread = CleaningThread(self.connector, self.cursor)
        self.db_cleaning_thread.error.connect(self.log_thread_error)
        self.db_cleaning_thread.start()

    def collect_sensors_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - collect_sensors_data')
        self.collect_sensors_data_thread = DataCollectingThread(self.connector, self.cursor, self.config_dict)
        self.collect_sensors_data_thread.error.connect(self.log_thread_error)
        self.collect_sensors_data_thread.start()

    def display_sensors_data(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_sensors_data')
        self.display_sensors_data_thread = DBDataDisplayThread(self.cursor, self.config_dict)
        self.display_sensors_data_thread.db_data.connect(self.refresh_in_out_display)
        self.display_sensors_data_thread.error.connect(self.log_thread_error)
        self.display_sensors_data_thread.start()

    def check_internet_connection(self):
        self.check_internet = CheckInternetConnexion()
        self.check_internet.connexion_alive.connect(self.start_internet_services)
        self.check_internet.no_connexion.connect(self.no_internet_message)
        self.check_internet.start()

    def start_internet_services(self):
        self.check_update()
        self.launch_fc_request_thread()

    def no_internet_message(self):
        logging.warning('gui - mainwindow.py - MainWindow - no_internet_message - there is no connexion to the '
                        'outside world !')
        connexion_window = MyConnexion(self.gui_path + '/', self)
        connexion_window.setGeometry(197, 160, 630, 280)
        connexion_window.exec_()
        if connexion_window.retry:
            self.check_internet_connection()

    def launch_fc_request_thread(self):
        logging.debug('gui - mainwindow.py - MainWindow - launch_fc_request_thread')
        if self.place_object is not None:
            self.query_mf_forecast_thread = MFForecastRequest(self.place_object, self.config_dict)
            self.query_mf_forecast_thread.fc_data.connect(self.parse_forecast_data)
            self.query_mf_forecast_thread.error.connect(self.log_thread_error)
            self.query_mf_forecast_thread.start()
        else:
            logging.warning('gui - mainwindow.py - MainWindow - launch_fc_request_thread : self.place_object is None')

    def check_update(self):
        logging.debug('gui - mainwindow.py - MainWindow - check_update')
        self.check_update_thread = CheckUpdate(gui_version)
        self.check_update_thread.finished.connect(self.display_gui_update_button)
        self.check_update_thread.error.connect(self.log_thread_error)
        self.check_update_thread.start()

    def refresh_in_out_display(self, data_dict):
        dt = data_dict['datetime']
        if (datetime.datetime.now() - dt).total_seconds() > 10800:
            in_temp = 'No data'
            in_minmax_temp = 'No data / No data'
            out_temp = 'No data'
            out_minmax_temp = 'No data / No data'
            humid = 'No data'
            pres = 'No data'
        else:
            in_temp = 'No data'
            in_minmax_temp = 'No data / No data'
            out_temp = 'No data'
            out_minmax_temp = 'No data / No data'
            humid = 'No data'
            pres = 'No data'
            if data_dict['temp_norm_in'] is not None:
                in_temp = str(data_dict['temp_norm_in']) + ' °C'
            if data_dict['temp_minmax_in'] is not None:
                in_minmax_temp = '{data_min} °C / {data_max} °C'.format(data_min=str(data_dict['temp_minmax_in'][0]),
                                                                        data_max=str(data_dict['temp_minmax_in'][1]))
            if data_dict['temp_norm_out'] is not None:
                out_temp = str(data_dict['temp_norm_out']) + ' °C'
            if data_dict['temp_minmax_out'] is not None:
                out_minmax_temp = '{data_min} °C / {data_max} °C'.format(data_min=str(data_dict['temp_minmax_out'][0]),
                                                                         data_max=str(data_dict['temp_minmax_out'][1]))
            if data_dict['hum_norm_in'] is not None:
                humid = str(data_dict['hum_norm_in']) + ' %'
            if data_dict['pres_norm_int'] is not None:
                pres = str(data_dict['pres_norm_int']) + ' hPa'

        self.in_temperature_label.setText('{in_temp}'.format(in_temp=in_temp))
        self.in_label_3.setText('{in_minmax_temp}'.format(in_minmax_temp=in_minmax_temp))
        self.out_temperature_label.setText('{out_temp}'.format(out_temp=out_temp))
        self.out_label_3.setText('{out_minmax_temp}'.format(out_minmax_temp=out_minmax_temp))
        self.in_humidity_label_1.setText('Humidité : {humid}'.format(humid=humid))
        self.out_pressure_label_1.setText('Pression : {pres}'.format(pres=pres))

    def plot_time_series(self):
        logging.debug('gui - mainwindow.py - MainWindow - plot_time_series')

        # wait_window = MyWait(self.page_2)
        # wait_window.setGeometry(448, 210, 128, 90)
        # wait_window.exec_()

        try:
            color_1, color_2, color_3 = (0.785, 0, 0), (0, 0, 0.785), (0.1, 0.1, 0.1)
            hours_list = mpl_hour_list()
            now = datetime.datetime.now()
            limit = now - datetime.timedelta(hours=24)
            self.cursor.execute("select int_tp_time, int_tp_data from int_temp where "
                                "int_tp_time>='{time}' ORDER BY id".format(time=limit.strftime('%Y-%m-%d %H:%M:%S')))
            temp_in_x, temp_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute("select ext_tp_time, ext_tp_data from ext_temp where "
                                "ext_tp_time>='{time}' ORDER BY id".format(time=limit.strftime('%Y-%m-%d %H:%M:%S')))
            temp_out_x, temp_out_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute("select int_hd_time, int_hd_data from int_hum where "
                                "int_hd_time>='{time}' ORDER BY id".format(time=limit.strftime('%Y-%m-%d %H:%M:%S')))
            hum_in_x, hum_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())
            self.cursor.execute("select int_ps_time, int_ps_data from int_pres where "
                                "int_ps_time>='{time}' ORDER BY id".format(time=limit.strftime('%Y-%m-%d %H:%M:%S')))
            pres_in_x, pres_in_y = db_data_to_mpl_vectors(self.cursor.fetchall())

            self.plot_in.clear()
            self.plot_in_2.clear()
            self.plot_out.clear()
            self.plot_out_2.clear()
            self.plot_in.set_ylabel('Température (°C)', color=color_1)
            self.plot_in.tick_params(axis='y', labelcolor=color_1)
            self.plot_in_2.set_ylabel('Humidité (%)', color=color_2)
            self.plot_in_2.tick_params(axis='y', labelcolor=color_2)
            self.plot_out.set_ylabel('Température (°C)', color=color_1)
            self.plot_out.tick_params(axis='y', labelcolor=color_1)
            self.plot_out_2.set_ylabel('Pression (hPa)', color=color_3)
            self.plot_out_2.tick_params(axis='y', labelcolor=color_3)
            self.plot_in.plot(temp_in_x, temp_in_y, color=color_1, linewidth=1.)

            if np.min(temp_in_y) < 10:
                y_min = np.min(temp_in_y) - 5
            else:
                y_min = 10
            if np.max(temp_in_y) > 30:
                y_max = np.max(temp_in_y) + 5
            else:
                y_max = 30

            self.plot_in.set_ylim(y_min, y_max)
            self.plot_in_2.plot(hum_in_x, hum_in_y, color=color_2, linewidth=1.)
            self.plot_in_2.set_ylim(0, 100)
            self.plot_in.set_xlim(limit, now)
            self.plot_in.set_xticks(hours_list)
            self.plot_in.set_xticklabels(['-24h', '-20h', '-16h', '-12h', '-8h', '-4h', 'Now'])
            self.plot_out.plot(temp_out_x, temp_out_y, color=color_1, linewidth=1.)

            if np.min(temp_out_y) < 0:
                y_min = np.min(temp_out_y) - 5
            else:
                y_min = 0
            if np.max(temp_out_y) > 30:
                y_max = np.max(temp_out_y) + 5
            else:
                y_max = 30

            self.plot_out.set_ylim(y_min, y_max)
            self.plot_out_2.plot(pres_in_x, pres_in_y, color=color_3, linewidth=1.)

            if np.min(pres_in_y) < 990:
                y_min = np.min(pres_in_y) - 10
            else:
                y_min = 990
            if np.max(pres_in_y) > 1030:
                y_max = np.max(pres_in_y) + 10
            else:
                y_max = 1030

            self.plot_out_2.set_ylim(y_min, y_max)
            self.plot_out.set_xlim(limit, now)
            self.plot_out.set_xticks(hours_list)
            self.plot_out.set_xticklabels(['-24h', '-20h', '-16h', '-12h', '-8h', '-4h', 'Now'])
            self.canvas_in.draw()
            self.canvas_out.draw()
        except Exception as e:
            self.log_thread_error(['time series', e])

    def parse_forecast_data(self, fc_data):
        logging.debug('gui - mainwindow.py - MainWindow - parse_forecast_data')
        if fc_data:
            self.mf_forecast_data = fc_data
            if fc_data['warning']:
                self.warning_button.setObjectName('warning_function')
                self.warning_button.setIcon(icon_creation_function('weather_warning_icon.svg', self.gui_path + '/'))

    def display_fc_1h(self):
        logging.debug('gui - mainwindow.py - MainWindow - display_fc_1h')
        if self.mf_forecast_data:
            clean_1h_forecast_widgets(self)
            lim = 0
            for t, forecast in self.mf_forecast_data['hourly'].items():
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
        if self.mf_forecast_data:
            clean_6h_forecast_widgets(self)

            logging.debug('gui - mainwindow.py - MainWindow - display_fc_6h - '
                          + str(len(list(self.mf_forecast_data['quaterly'].keys()))))

            for i in [0, 4, 8, 12, 16]:
                dt_list = list(self.mf_forecast_data['quaterly'].keys())[i: i + 4]
                dt = dt_list[2]
                weather = self.mf_forecast_data['quaterly'][dt]['weather']
                temp_list = [self.mf_forecast_data['quaterly'][t]['temp'] for t in dt_list]
                date = days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day)
                temp = str(round(min(temp_list))) + '°C / ' + str(round(max(temp_list))) + '°C'
                if i < 12:
                    horizontal_layout = self.prev6h_layout_1
                else:
                    horizontal_layout = self.prev6h_layout_2
                add_6h_forecast_widget(self, date, weather, temp, dt_list, horizontal_layout)

    def display_1h_forecast_details(self, full_dt):
        logging.debug('gui - mainwindow.py - MainWindow - display_1h_forecast_details')
        forecast = self.mf_forecast_data['hourly'][full_dt]
        details_window = My1hFCDetails(forecast, self.gui_path + '/', self)
        details_window.setGeometry(282, 110, 480, 380)
        details_window.exec_()

    def display_6h_forecast_details(self, dt_list):
        logging.debug('gui - mainwindow.py - MainWindow - display_6h_forecast_details')
        forecast = []
        for dt in dt_list:
            forecast.append([dt, self.mf_forecast_data['quaterly'][dt]])
        details_window = My6hFCDetails(forecast, self.gui_path + '/', self)
        details_window.setGeometry(52, 110, 920, 380)
        details_window.exec_()

    def warning_update_dispatch(self):
        logging.debug('gui - mainwindow.py - MainWindow - warning_update_dispatch')
        if self.warning_button.objectName() == 'update_function':
            update_window = MyWarningUpdate(self.gui_path + '/', self)
            update_window.setGeometry(182, 180, 660, 240)
            update_window.exec_()
            if not update_window.cancel:
                temp_folder = tempfile.gettempdir()
                download_window = MyDownload(self.update_url, temp_folder, self)
                download_window.setGeometry(237, 217, 550, 166)
                download_window.exec_()
                if download_window.success:
                    shutil.copy(self.gui_path + '/functions/unzip_update.py', temp_folder)
                    script_path = str(pathlib.Path(temp_folder).joinpath('unzip_update.py'))
                    update_path = str(pathlib.Path(temp_folder).joinpath(self.update_url['file']))
                    install_path = str(pathlib.Path(self.gui_path))
                    command = f'python3 {script_path} {update_path} {install_path}'
                    os.system('lxterminal -e ' + command)
                    time.sleep(1.5)
                    self.close()

        elif self.warning_button.objectName() == 'warning_function':
            warning_window = MyWarning(self.mf_forecast_data['warning'], self)
            warning_window.setGeometry(197, 175, 630, 350)
            warning_window.exec_()

    def open_options(self):
        logging.debug('gui - mainwindow.py - MainWindow - open_options')
        config_string = io.StringIO()
        self.config_dict.write(config_string)
        config_string.seek(0)
        config_dict_copy = configparser.ConfigParser()
        config_dict_copy.read_file(config_string)
        option_window = MyOptions(config_dict_copy, self.user_path, self.gui_path + '/', self)
        option_window.setGeometry(162, 125, 700, 364)
        option_window.exec_()
        if not option_window.cancel:
            self.config_dict = option_window.config_dict
            ini_file = open(str(pathlib.Path(self.user_path, 'weather_station.ini')), 'w')
            self.config_dict.write(ini_file)
            ini_file.close()
            if self.config_dict.getboolean('METEOFRANCE', 'user_place'):
                self.place_object = option_window.place_object
                f = open(self.user_path + '/place_object.dat', 'wb')
                pickle.dump(self.place_object, f)
                f.close()

    def about_weather_station(self):
        logging.debug('gui - mainwindow.py - MainWindow - about_weather_station')
        text = (f'<p align=\"justify\">La Station Météo v{gui_version} a été développée à partir de Python et de '
                f'PyQt.</p>')
        about_window = MyAbout(text, self.gui_path + '/', self)
        about_window.setGeometry(162, 75, 700, 450)
        about_window.exec_()

    def display_gui_update_button(self, url_dict):
        logging.debug('gui - mainwindow.py - MainWindow - display_gui_update_button')
        if url_dict:
            self.update_url = url_dict
            if self.warning_button.objectName() == 'no_function':
                self.warning_button.setObjectName('update_function')
                self.warning_button.setIcon(icon_creation_function('weather_station_update.svg', self.gui_path + '/'))

    @staticmethod
    def log_thread_error(e_list):
        logging.exception('gui - mainwindow.py - MainWindow - log_thread_error - '
                          'ERROR: {origin} | {error}'.format(origin=e_list[0], error=str(e_list[1])))

    def exit_menu(self):
        logging.debug('gui - mainwindow.py - MainWindow - exit_menu')
        if platform.system() == 'Windows':
            self.close()
        else:
            exit_window = MyExit(self)
            exit_window.setGeometry(369, 209, 286, 182)
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
        self.connector.close()
        event.accept()
        logging.info('**********************************')
        logging.info('WEATHER STATION ' + gui_version + ' is closing ...')
        logging.info('**********************************')
