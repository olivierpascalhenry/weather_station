import sys
import platform
import copy
import pickle
import logging
import pathlib
import datetime
import psycopg2
import requests
from meteofrance_api import MeteoFranceClient
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from PyQt5 import QtCore, QtWidgets
from ui.Ui_optionwindow import Ui_optionWindow
from functions.utils import code_to_departement
from ui.version import gui_version
from functions.window_functions.other_windows import MyInfo, MyNumpad, MyKeyboard, MyTown, MyAPI
from functions.window_functions.sensor_windows import MqttManager, W1SensorManager, BME280SensorManager
from functions.thread_functions.other_threads import CheckUpdate


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    available_update = QtCore.pyqtSignal(dict)

    def __init__(self, config_dict, sensor_dict, user_path, parent=None):
        logging.info('gui - option_window.py - MyOptions - __init__ ')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.mainparent = parent
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        scroll = QtWidgets.QScroller.scroller(self.scroll_area_3.viewport())
        scroll.grabGesture(self.scroll_area_3.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties = scroll.scrollerProperties()
        properties.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                   QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll.setScrollerProperties(properties)
        scroll = QtWidgets.QScroller.scroller(self.scroll_area_1.viewport())
        scroll.grabGesture(self.scroll_area_1.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties = scroll.scrollerProperties()
        properties.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                   QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll.setScrollerProperties(properties)
        scroll = QtWidgets.QScroller.scroller(self.scroll_area_2.viewport())
        scroll.grabGesture(self.scroll_area_2.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties = scroll.scrollerProperties()
        properties.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                   QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll.setScrollerProperties(properties)
        scroll = QtWidgets.QScroller.scroller(self.scroll_area_4.viewport())
        scroll.grabGesture(self.scroll_area_4.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties = scroll.scrollerProperties()
        properties.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                   QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll.setScrollerProperties(properties)
        scroll = QtWidgets.QScroller.scroller(self.scroll_area_5.viewport())
        scroll.grabGesture(self.scroll_area_5.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties = scroll.scrollerProperties()
        properties.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                   QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll.setScrollerProperties(properties)
        self.config_dict = config_dict
        self.sensor_dict = sensor_dict
        self.splitter.setSizes([230, 682])
        self.user_path = user_path
        self.cancel = True
        self.place_object = None
        self.api_key = None
        self.sensor_list = []
        self.check_update_thread = None
        self.cb_list = [self.af_gb_int_cb_1, self.af_gb_ext_cb_1, self.ts_gb_int_cb_1, self.ts_gb_int_cb_2,
                        self.ts_gb_ext_cb_1, self.ts_gb_ext_cb_2, self.db_gb_2_cb_1, self.af_gb_int_cb_2,
                        self.af_gb_ext_cb_2, self.af_gb_int_cb_3, self.af_gb_ext_cb_3, self.af_gb_int_cb_4,
                        self.af_gb_ext_cb_4]
        self.af_vl.setAlignment(QtCore.Qt.AlignTop)
        self.ca_vl.setAlignment(QtCore.Qt.AlignTop)
        self.ap_vl.setAlignment(QtCore.Qt.AlignTop)
        self.sy_vl.setAlignment(QtCore.Qt.AlignTop)
        self.st_vl.setAlignment(QtCore.Qt.AlignTop)
        self.db_vl.setAlignment(QtCore.Qt.AlignTop)
        self.db_gb_2_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.lo_gb_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.sy_gb_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_int_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_ext_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_int_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_ext_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_int_cb_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_ext_cb_3.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_int_cb_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_ext_cb_4.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_int_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_int_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_ext_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_ext_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.section_list.currentRowChanged.connect(self.display_options)
        self.ok_button.clicked.connect(self.save_config_dict)
        self.cancel_button.clicked.connect(self.close_window)
        self.lo_gb_bt_1.clicked.connect(self.get_folder_path)
        self.db_gb_bt_1.clicked.connect(self.display_keyboard)
        self.db_gb_bt_2.clicked.connect(self.display_keyboard)
        self.db_gb_bt_3.clicked.connect(self.display_keyboard)
        self.db_gb_bt_4.clicked.connect(self.display_keyboard)
        self.db_gb_bt_5.clicked.connect(self.display_numpad)
        self.af_gb_int_bt_1.clicked.connect(self.display_numpad)
        self.af_gb_ext_bt_1.clicked.connect(self.display_numpad)
        self.ca_bt_1.clicked.connect(self.display_numpad)
        self.ap_gb_3_bt_1.clicked.connect(self.display_numpad)
        self.sy_gb_bt_1.clicked.connect(self.display_numpad)
        self.ap_gb_2_bt_1.clicked.connect(self.display_keyboard)
        self.ca_gc_bt_3.clicked.connect(self.show_mqtt_manager)
        self.ca_gc_bt_1.clicked.connect(self.show_1w_manager)
        self.ca_gc_bt_2.clicked.connect(self.show_bme280_manager)
        self.ap_gb_2_ln_1.textChanged.connect(self.activate_search_button)
        self.ap_gb_rb_1.clicked.connect(self.activate_place_search)
        self.ap_gb_rb_2.clicked.connect(self.activate_place_search)
        self.ap_gb_2_bt_2.clicked.connect(self.search_place)
        self.ap_gb_rb_1.clicked.connect(self.activate_openweather_edit)
        self.ap_gb_rb_2.clicked.connect(self.activate_openweather_edit)
        self.ap_gb_rb_1.clicked.connect(self.change_place_info)
        self.ap_gb_rb_2.clicked.connect(self.change_place_info)
        self.ap_gb_bt_1.clicked.connect(self.set_openweather_key)
        self.sy_gb_2_bt_1.clicked.connect(self.check_update)
        self.sy_gb_2_bt_2.clicked.connect(self.export_to_csv)
        self.db_gb_2_cb_1.currentIndexChanged.connect(self.activate_export_button)
        self.sy_gb_cb_1.currentIndexChanged.connect(self.activate_elevation_widgets)
        self.sy_gb_bt_4.clicked.connect(self.elevation_request)
        self.sy_gb_4_ck_1.stateChanged.connect(self.activate_auto_connexion_period)
        if getattr(sys, 'frozen', False):
            self.sy_gb_2_bt_1.setEnabled(True)
        else:
            self.sy_gb_2_bt_1.setEnabled(False)
        self.create_sensor_list()
        self.parse_sensor_list_in_cb()
        self.read_config_dict()
        self.section_list.setCurrentRow(0)

    def display_options(self, idx):
        logging.debug(f'gui - option_window.py - MyOptions - display_options - idx: {idx}')
        self.stack_widget.setCurrentIndex(idx)

    def create_sensor_list(self):
        logging.debug('gui - option_window.py - MyOptions - create_sensor_list')
        self.sensor_list.clear()
        if platform.system() == 'Windows':
            self.sensor_list.append('DS18B20_TEST')
            self.sensor_list.append('BME280_TEST')
            self.sensor_list.append('AQARA_THP_TEST')
        for _, ddict in self.sensor_dict['DS18B20'].items():
            self.sensor_list.append(ddict['name'])
        for _, ddict in self.sensor_dict['BME280'].items():
            self.sensor_list.append(ddict['name'])
        for device, _ in self.sensor_dict['MQTT']['devices'].items():
            self.sensor_list.append(device)

    def parse_sensor_list_in_cb(self):
        logging.debug('gui - option_window.py - MyOptions - parse_sensor_list_in_cb')
        if self.sensor_list:
            for cb in self.cb_list:
                cb.clear()
                cb.addItem('Choisir un capteur')
                cb.addItems(sorted(self.sensor_list))
        else:
            for cb in self.cb_list:
                cb.clear()
                cb.addItem('Pas de capteur')
        self.activate_export_button()

    def update_cb_with_sensor_list(self):
        logging.debug('gui - option_window.py - MyOptions - update_cb_with_sensor_list')
        self.create_sensor_list()
        if self.sensor_list:
            for cb in self.cb_list:
                device = cb.currentText()
                cb.clear()
                cb.addItem('Choisir un capteur')
                cb.addItems(sorted(self.sensor_list))
                if device in self.sensor_list:
                    cb.setCurrentIndex(cb.findText(device))
        else:
            for cb in self.cb_list:
                cb.clear()
                cb.addItem('Pas de capteur')
        self.activate_export_button()

    def read_config_dict(self):
        logging.debug('gui - option_window.py - MyOptions - read_config_dict')
        self.db_gb_ln_1.setText(self.config_dict.get('DATABASE', 'username'))
        self.db_gb_ln_2.setText(self.config_dict.get('DATABASE', 'password'))
        self.db_gb_ln_3.setText(self.config_dict.get('DATABASE', 'database'))
        self.db_gb_ln_4.setText(self.config_dict.get('DATABASE', 'host'))
        self.db_gb_ln_5.setText(self.config_dict.get('DATABASE', 'port'))
        self.lo_gb_cb_1.setCurrentIndex(self.lo_gb_cb_1.findText(self.config_dict.get('LOG', 'level')))
        self.lo_gb_ln_1.setText(self.config_dict.get('LOG', 'path'))
        self.lo_gb_ln_1.setCursorPosition(0)
        self.af_gb_int_ln_1.setText(self.config_dict.get('DISPLAY', 'in_display_rate'))
        self.af_gb_ext_ln_1.setText(self.config_dict.get('DISPLAY', 'out_display_rate'))
        self.af_gb_int_ck_1.setChecked(self.config_dict.getboolean('DISPLAY', 'in_msl_pressure'))
        self.af_gb_ext_ck_1.setChecked(self.config_dict.getboolean('DISPLAY', 'out_msl_pressure'))
        self.ca_ln_1.setText(self.config_dict.get('SENSOR', 'sensors_rate'))
        self.ap_gb_5_ln_1.setText(self.config_dict.get('API', 'request_rate'))
        self.sy_gb_ln_1.setText(self.config_dict.get('SYSTEM', 'place_altitude'))
        self.sy_gb_2_ck_1.setChecked(self.config_dict.getboolean('SYSTEM', 'check_update'))
        self.sy_gb_4_ck_1.setChecked(self.config_dict.getboolean('SYSTEM', 'auto_check_connexion'))
        if self.sy_gb_4_ck_1.isChecked():
            self.sy_gb_4_ln_1.setText(self.config_dict.get('SYSTEM', 'auto_connexion_value'))
            self.sy_gb_4_cb_1.setCurrentText(self.config_dict.get('SYSTEM', 'auto_connexion_unit'))
        self.ts_gb_ext_ck_1.setChecked(self.config_dict.getboolean('TIMESERIES', 'msl_pressure'))
        if self.config_dict.get('DISPLAY', 'in_temperature') in self.sensor_list:
            self.af_gb_int_cb_1.setCurrentIndex(self.af_gb_int_cb_1.findText(self.config_dict.get('DISPLAY',
                                                                                                  'in_temperature')))
        if self.config_dict.get('DISPLAY', 'in_humidity') in self.sensor_list:
            self.af_gb_int_cb_2.setCurrentIndex(self.af_gb_int_cb_2.findText(self.config_dict.get('DISPLAY',
                                                                                                  'in_humidity')))
        if self.config_dict.get('DISPLAY', 'in_pressure') in self.sensor_list:
            self.af_gb_int_cb_3.setCurrentIndex(self.af_gb_int_cb_3.findText(self.config_dict.get('DISPLAY',
                                                                                                  'in_pressure')))
        if self.config_dict.get('DISPLAY', 'in_bat_signal') in self.sensor_list:
            self.af_gb_int_cb_4.setCurrentIndex(self.af_gb_int_cb_4.findText(self.config_dict.get('DISPLAY',
                                                                                                  'in_bat_signal')))
        if self.config_dict.get('DISPLAY', 'out_temperature') in self.sensor_list:
            self.af_gb_ext_cb_1.setCurrentIndex(self.af_gb_ext_cb_1.findText(self.config_dict.get('DISPLAY',
                                                                                                  'out_temperature')))
        if self.config_dict.get('DISPLAY', 'out_humidity') in self.sensor_list:
            self.af_gb_ext_cb_2.setCurrentIndex(self.af_gb_ext_cb_2.findText(self.config_dict.get('DISPLAY',
                                                                                                  'out_humidity')))
        if self.config_dict.get('DISPLAY', 'out_bat_signal') in self.sensor_list:
            self.af_gb_ext_cb_4.setCurrentIndex(self.af_gb_ext_cb_4.findText(self.config_dict.get('DISPLAY',
                                                                                                  'out_bat_signal')))
        if self.config_dict.get('DISPLAY', 'out_pressure') in self.sensor_list:
            self.af_gb_ext_cb_3.setCurrentIndex(self.af_gb_ext_cb_3.findText(self.config_dict.get('DISPLAY',
                                                                                                  'out_pressure')))
        if self.config_dict.get('TIMESERIES', 'in_temperature') in self.sensor_list:
            self.ts_gb_int_cb_1.setCurrentIndex(self.ts_gb_int_cb_1.findText(self.config_dict.get('TIMESERIES',
                                                                                                  'in_temperature')))
        if self.config_dict.get('TIMESERIES', 'in_humidity') in self.sensor_list:
            self.ts_gb_int_cb_2.setCurrentIndex(self.ts_gb_int_cb_2.findText(self.config_dict.get('TIMESERIES',
                                                                                                  'in_humidity')))
        if self.config_dict.get('TIMESERIES', 'out_temperature') in self.sensor_list:
            self.ts_gb_ext_cb_1.setCurrentIndex(self.ts_gb_ext_cb_1.findText(self.config_dict.get('TIMESERIES',
                                                                                                  'out_temperature')))
        if self.config_dict.get('TIMESERIES', 'out_pressure') in self.sensor_list:
            self.ts_gb_ext_cb_2.setCurrentIndex(self.ts_gb_ext_cb_2.findText(self.config_dict.get('TIMESERIES',
                                                                                                  'out_pressure')))
        if self.config_dict.get('API', 'api_used') == 'meteofrance':
            self.ap_gb_rb_1.click()
        elif self.config_dict.get('API', 'api_used') == 'openweather':
            self.ap_gb_rb_2.click()
            self.api_key = self.config_dict.get('API', 'api_key')
            self.ap_gb_lb_1.setText(self.config_dict.get('API', 'api_key'))
        place_file = pathlib.Path(self.user_path).joinpath('place_object.dat')
        if self.config_dict.getboolean('API', 'user_place') and place_file.exists():
            f = open(place_file, 'rb')
            self.place_object = pickle.load(f)
            f.close()
            self.ap_gb_2_ln_1.setText(self.place_object['ville'])
            self.ap_gb_2_lb_4.setText(self.place_object['cp_id'])
            self.ap_gb_2_lb_5.setText(self.place_object['dp_gps'])

    def save_config_dict(self):
        logging.debug('gui - option_window.py - MyOptions - save_config_dict')
        if not pathlib.Path(str(self.lo_gb_ln_1.text())).exists():
            text = ('Après vérification, il semblerait que le chemin du fichier de log ne soit pas correcte. Ainsi, il '
                    'n\'est pas possible de sauvegarder les options. Veuillez corriger le problème et réessayer.')
            info_window = MyInfo(text, self.mainparent)
            info_window.exec_()
        else:
            self.config_dict.set('DATABASE', 'username', str(self.db_gb_ln_1.text()))
            self.config_dict.set('DATABASE', 'password', str(self.db_gb_ln_2.text()))
            self.config_dict.set('DATABASE', 'database', str(self.db_gb_ln_3.text()))
            self.config_dict.set('DATABASE', 'host', str(self.db_gb_ln_4.text()))
            self.config_dict.set('DATABASE', 'port', str(self.db_gb_ln_5.text()))
            self.config_dict.set('LOG', 'level', str(self.lo_gb_cb_1.currentText()))
            self.config_dict.set('LOG', 'path', str(self.lo_gb_ln_1.text()))
            self.config_dict.set('DISPLAY', 'in_display_rate', self.af_gb_int_ln_1.text())
            self.config_dict.set('DISPLAY', 'out_display_rate', self.af_gb_ext_ln_1.text())
            self.config_dict.set('DISPLAY', 'in_msl_pressure', str(self.af_gb_int_ck_1.isChecked()))
            self.config_dict.set('DISPLAY', 'out_msl_pressure', str(self.af_gb_ext_ck_1.isChecked()))
            self.config_dict.set('TIMESERIES', 'msl_pressure', str(self.ts_gb_ext_ck_1.isChecked()))
            self.config_dict.set('SENSOR', 'sensors_rate', self.ca_ln_1.text())
            self.config_dict.set('API', 'request_rate', self.ap_gb_5_ln_1.text())
            self.config_dict.set('SYSTEM', 'place_altitude', self.sy_gb_ln_1.text())
            self.config_dict.set('SYSTEM', 'check_update', str(self.sy_gb_2_ck_1.isChecked()))
            self.config_dict.set('SYSTEM', 'auto_check_connexion', str(self.sy_gb_4_ck_1.isChecked()))
            if self.sy_gb_4_ck_1.isChecked():
                self.config_dict.set('SYSTEM', 'auto_connexion_value', str(self.sy_gb_4_ln_1.text()))
                self.config_dict.set('SYSTEM', 'auto_connexion_unit', str(self.sy_gb_4_cb_1.currentText()))
            else:
                self.config_dict.set('SYSTEM', 'auto_connexion_value', '')
                self.config_dict.set('SYSTEM', 'auto_connexion_unit', 'minutes')
            if self.ts_gb_int_cb_1.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('TIMESERIES', 'in_temperature', str(self.ts_gb_int_cb_1.currentText()))
            else:
                self.config_dict.set('TIMESERIES', 'in_temperature', '')
            if self.ts_gb_int_cb_2.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('TIMESERIES', 'in_humidity', str(self.ts_gb_int_cb_2.currentText()))
            else:
                self.config_dict.set('TIMESERIES', 'in_humidity', '')
            if self.ts_gb_ext_cb_1.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('TIMESERIES', 'out_temperature', str(self.ts_gb_ext_cb_1.currentText()))
            else:
                self.config_dict.set('TIMESERIES', 'out_temperature', '')
            if self.ts_gb_ext_cb_2.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('TIMESERIES', 'out_pressure', str(self.ts_gb_ext_cb_2.currentText()))
            else:
                self.config_dict.set('TIMESERIES', 'out_pressure', '')
            if self.af_gb_ext_cb_1.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'out_temperature', str(self.af_gb_ext_cb_1.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'out_temperature', '')
            if self.af_gb_int_cb_1.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'in_temperature', str(self.af_gb_int_cb_1.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'in_temperature', '')
            if self.af_gb_ext_cb_2.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'out_humidity', str(self.af_gb_ext_cb_2.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'out_humidity', '')
            if self.af_gb_int_cb_2.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'in_humidity', str(self.af_gb_int_cb_2.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'in_humidity', '')
            if self.af_gb_ext_cb_3.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'out_pressure', str(self.af_gb_ext_cb_3.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'out_pressure', '')
            if self.af_gb_int_cb_3.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'in_pressure', str(self.af_gb_int_cb_3.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'in_pressure', '')

            if self.af_gb_ext_cb_4.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'out_bat_signal', str(self.af_gb_ext_cb_4.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'out_bat_signal', '')
            if self.af_gb_int_cb_4.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'in_bat_signal', str(self.af_gb_int_cb_4.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'in_bat_signal', '')

            if self.ap_gb_rb_1.isChecked():
                self.config_dict.set('API', 'api_used', 'meteofrance')
                self.config_dict.set('API', 'api_key', '')
            elif self.ap_gb_rb_2.isChecked():
                self.config_dict.set('API', 'api_used', 'openweather')
                self.config_dict.set('API', 'api_key', self.api_key)
            else:
                self.config_dict.set('API', 'api_used', '')
                self.config_dict.set('API', 'api_key', '')
            if self.place_object is not None:
                self.config_dict.set('API', 'user_place', 'True')
            else:
                self.config_dict.set('API', 'user_place', 'False')
            self.cancel = False
            self.close_window()

    def show_mqtt_manager(self):
        logging.debug('gui - option_window.py - MyOptions - show_mqtt_manager')
        mqtt_manager = MqttManager(copy.deepcopy(self.sensor_dict['MQTT']), self.mainparent)
        mqtt_manager.exec_()
        if not mqtt_manager.cancel:
            self.sensor_dict['MQTT'] = mqtt_manager.mqtt_dict
            self.update_cb_with_sensor_list()

    def show_1w_manager(self):
        logging.debug('gui - option_window.py - MyOptions - show_1w_manager')
        manager_window = W1SensorManager(copy.deepcopy(self.sensor_dict['DS18B20']), self.mainparent)
        manager_window.exec_()
        if not manager_window.cancel:
            self.sensor_dict['DS18B20'] = manager_window.sensor_dict
            self.update_cb_with_sensor_list()

    def show_bme280_manager(self):
        logging.debug('gui - option_window.py - MyOptions - show_bme280_manager')
        manager_window = BME280SensorManager(copy.deepcopy(self.sensor_dict['BME280']), self.mainparent)
        manager_window.exec_()
        if not manager_window.cancel:
            self.sensor_dict['BME280'] = manager_window.sensor_dict
            self.update_cb_with_sensor_list()

    def get_folder_path(self):
        logging.debug('gui - option_window.py - MyOptions - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Sélectionner un répertoire')
        if folder_path:
            self.lo_gb_ln_1.setText(str(pathlib.Path(folder_path)))
            self.lo_gb_ln_1.setCursorPosition(0)

    def activate_place_search(self):
        logging.debug('gui - option_window.py - MyOptions - activate_place_search')
        if self.ap_gb_rb_1.isChecked() or self.ap_gb_rb_2.isChecked():
            self.ap_gb_2_ln_1.setEnabled(True)
            self.ap_gb_2_bt_1.setEnabled(True)
        else:
            self.ap_gb_2_ln_1.setEnabled(False)
            self.ap_gb_2_bt_1.setEnabled(False)
            self.ap_gb_2_ln_1.clear()

    def activate_openweather_edit(self):
        logging.debug('gui - option_window.py - MyOptions - activate_openweather_edit')
        if self.ap_gb_rb_2.isChecked():
            self.ap_gb_bt_1.setEnabled(True)
            self.ap_gb_lb_1.setText(self.api_key)
        else:
            self.ap_gb_bt_1.setEnabled(False)
            self.ap_gb_lb_1.clear()

    def change_place_info(self):
        logging.debug('gui - option_window.py - MyOptions - change_place_info')
        self.ap_gb_2_ln_1.setText('')
        self.ap_gb_2_lb_4.setText('')
        self.ap_gb_2_lb_5.setText('')
        if self.ap_gb_rb_2.isChecked():
            self.ap_gb_2_lb_2.setText('ID :')
            self.ap_gb_2_lb_3.setText('Coordonnées :')
            if self.place_object is not None and self.place_object['api'] == 'openweather':
                self.ap_gb_2_ln_1.setText(self.place_object['ville'])
                self.ap_gb_2_lb_4.setText(self.place_object['cp_id'])
                self.ap_gb_2_lb_4.setText(self.place_object['dp_gps'])
        elif self.ap_gb_rb_1.isChecked():
            self.ap_gb_2_lb_2.setText('Code postal :')
            self.ap_gb_2_lb_3.setText('Département :')
            if self.place_object is not None and self.place_object['api'] == 'meteofrance':
                self.ap_gb_2_ln_1.setText(self.place_object['ville'])
                self.ap_gb_2_lb_4.setText(self.place_object['cp_id'])
                self.ap_gb_2_lb_5.setText(self.place_object['dp_gps'])

    def activate_search_button(self):
        logging.debug('gui - option_window.py - MyOptions - activate_search_button')
        if self.ap_gb_2_ln_1.text():
            self.ap_gb_2_bt_2.setEnabled(True)
        else:
            self.ap_gb_2_bt_2.setEnabled(False)

    def search_place(self):
        logging.debug('gui - option_window.py - MyOptions - search_place')
        place_dict = {'object': None, 'ville': None, 'cp_id': None, 'altitude': None, 'longitude': None,
                      'latitude': None, 'api': None, 'dp_gps': None}
        list_places = None
        if self.ap_gb_rb_1.isChecked():
            list_places = MeteoFranceClient().search_places(self.ap_gb_2_ln_1.text())
            place_dict['api'] = 'meteofrance'
        elif self.ap_gb_rb_2.isChecked():
            place_dict['api'] = 'openweather'
            config_dict = get_default_config()
            config_dict['language'] = 'fr'
            owm = OWM(self.api_key, config_dict)
            reg = owm.city_id_registry()
            list_places = reg.locations_for(self.ap_gb_2_ln_1.text())
        if len(list_places) > 1:
            place_search = MyTown(list_places, place_dict['api'], self)
            place_search.exec_()
            if not place_search.cancel:
                place_dict['object'] = place_search.place
                place_dict['ville'] = place_search.ville
                place_dict['cp_id'] = place_search.cp_id
                place_dict['dp_gps'] = place_search.dp_gps
                place_dict['longitude'] = place_search.lon
                place_dict['latitude'] = place_search.lat
        else:
            if place_dict['api'] == 'meteofrance':
                place_dict['object'] = list_places[0]
                place_dict['ville'] = list_places[0].name
                place_dict['cp_id'] = list_places[0].postal_code
                place_dict['dp_gps'] = code_to_departement()[list_places[0].admin2]
                place_dict['longitude'] = list_places[0].longitude
                place_dict['latitude'] = list_places[0].latitude
            elif place_dict['api'] == 'openweather':
                lon = str(list_places[0].lon)
                lat = str(list_places[0].lat)
                if '-' in lon:
                    lon = lon[1:] + '°W'
                else:
                    lon += '°E'
                if '-' in lat:
                    lat = lat[1:] + '°S'
                else:
                    lat += '°N'
                place_dict['dp_gps'] = f'Lon : {lon} ; Lat : {lat}'
                place_dict['object'] = list_places[0]
                place_dict['ville'] = list_places[0].name
                place_dict['cp_id'] = str(list_places[0].id)
                place_dict['longitude'] = list_places[0].lon
                place_dict['latitude'] = list_places[0].lat

        if place_dict['object'] is not None:
            self.place_object = place_dict
            self.ap_gb_2_ln_1.setText(place_dict['ville'])
            self.ap_gb_2_lb_4.setText(place_dict['cp_id'])
            self.ap_gb_2_lb_5.setText(place_dict['dp_gps'])

    def set_openweather_key(self):
        logging.debug('gui - option_window.py - MyOptions - set_openweather_key')
        api_window = MyAPI(self.api_key, self.mainparent)
        api_window.exec_()
        if not api_window.cancel:
            self.api_key = api_window.key
            self.ap_gb_lb_1.setText(self.api_key)

    def display_numpad(self):
        logging.debug('gui - option_window.py - MyOptions - display_numpad')
        numpad_window = MyNumpad(self.mainparent)
        numpad_window.exec_()
        if not numpad_window.cancel:
            if self.sender().objectName() == 'af_gb_int_bt_1':
                self.af_gb_int_ln_1.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'af_gb_ext_bt_1':
                self.af_gb_ext_ln_1.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ca_bt_1':
                self.ca_ln_1.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ap_gb_3_bt_1':
                self.ap_gb_5_ln_1.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'sy_gb_bt_1':
                self.sy_gb_ln_1.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'db_gb_bt_5':
                self.db_gb_ln_5.setText(numpad_window.num_line.text())

    def display_keyboard(self):
        logging.debug('gui - option_window.py - MyOptions - display_keyboard')
        keyboard_window = MyKeyboard(self.mainparent)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            if self.sender().objectName() == 'ap_gb_2_bt_1':
                self.ap_gb_2_ln_1.setText(keyboard_window.num_line.text())
            elif self.sender().objectName() == 'db_gb_bt_1':
                self.db_gb_ln_1.setText(keyboard_window.num_line.text())
            elif self.sender().objectName() == 'db_gb_bt_2':
                self.db_gb_ln_2.setText(keyboard_window.num_line.text())
            elif self.sender().objectName() == 'db_gb_bt_3':
                self.db_gb_ln_3.setText(keyboard_window.num_line.text())
            elif self.sender().objectName() == 'db_gb_bt_4':
                self.db_gb_ln_4.setText(keyboard_window.num_line.text())

    def check_update(self):
        logging.debug('gui - option_window.py - MyOptions - check_update')
        self.check_update_thread = CheckUpdate(gui_version)
        self.check_update_thread.finished.connect(self.parse_update_check)
        self.check_update_thread.start()

    def parse_update_check(self, url_dict):
        logging.debug(f'gui - option_window.py - MyOptions - parse_update_check - url_dict: {url_dict}')
        if url_dict:
            logging.debug('gui - mainwindow.py - MainWindow - parse_update_check - update available')
            self.available_update.emit(url_dict)
            text = ('Une nouvelle mise à jour est disponible. Pour l\'installer, veuillez quitter la fenêtre des '
                    'options et cliquer sur l\'icône de mise à jour dans la fenêtre principale.')
            info_window = MyInfo(text, self.mainparent)
            info_window.exec_()
        else:
            logging.debug('gui - option_window.py - MyOptions - parse_update_check - no update available')

    def export_to_csv(self):
        logging.debug(f'gui - option_window.py - MyOptions - export_to_csv')
        self.db_gb_2_lb_2.clear()
        sensor = self.db_gb_2_cb_1.currentText()
        table = None
        for _, ddict in self.sensor_dict['DS18B20'].items():
            if sensor == ddict['name']:
                table = ddict['table']
        for _, ddict in self.sensor_dict['BME280'].items():
            if sensor == ddict['name']:
                table = ddict['table']
        for device, _ in self.sensor_dict['MQTT']['devices'].items():
            if sensor == device:
                table = device

        if table is not None:
            file_dialog = QtWidgets.QFileDialog()
            filter_types = 'CSV Files (*.csv)'
            file_name = f'{table}_data_export_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}'
            file_name, _ = file_dialog.getSaveFileName(self, 'Sauvegarder un fichier', file_name, filter_types)
            if file_name:
                logging.debug(f'gui - option_window.py - MyOptions - export_to_csv - file_name: {file_name} ; table: '
                              f'{table}')
                try:
                    data_str = (f'data exported from the Weather Station\nsensor: {sensor}\ntable: {table}\nfields on '
                                f'the next line\n')
                    conn = psycopg2.connect(user=self.config_dict.get('DATABASE', 'username'),
                                            password=self.config_dict.get('DATABASE', 'password'),
                                            host=self.config_dict.get('DATABASE', 'host'),
                                            database=self.config_dict.get('DATABASE', 'database'),
                                            port=self.config_dict.get('DATABASE', 'port'))
                    curs = conn.cursor()
                    curs.execute(f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' "
                                 f"ORDER BY ordinal_position;")
                    data_str += ','.join([item[0] for item in curs.fetchall()]) + '\n'

                    curs.execute(f'SELECT * FROM "{table}" ORDER BY date_time DESC;')
                    data = curs.fetchall()

                    if data and data is not None:
                        for tmp in data:
                            dt, t, h, p, b, s, pm = tmp
                            data_str += f'{dt.strftime("%Y-%m-%d %H:%M:%S.%f")},{t},{h},{p},{b},{s},{pm}\n'

                        f = open(file_name, 'w')
                        f.write(data_str)
                        f.close()
                        self.db_gb_2_lb_2.setText('Les données ont été exportées !')
                    else:
                        self.db_gb_2_lb_2.setText('Pas de données pour cette table !')
                except:
                    logging.exception('gui - option_window.py - MyOptions - export_to_csv - an exception occured when '
                                      'trying to export data')
                    self.db_gb_2_lb_2.setText('Pas de données pour cette table !')

        else:
            self.db_gb_2_lb_2.setText('Cette table n\'existe plus !')

    def activate_export_button(self):
        logging.debug(f'gui - option_window.py - MyOptions - activate_export_button')
        if self.db_gb_2_cb_1.currentText() in ['Choisir un capteur', 'Pas de capteur']:
            self.sy_gb_2_bt_2.setEnabled(False)
        else:
            self.sy_gb_2_bt_2.setEnabled(True)

    def activate_elevation_widgets(self):
        logging.debug(f'gui - option_window.py - MyOptions - activate_elevation_widgets - current index: '
                      f'{self.sy_gb_cb_1.currentIndex()}')
        if self.sy_gb_cb_1.currentIndex() == 0:
            self.sy_gb_ln_1.setEnabled(True)
            self.sy_gb_ln_2.setEnabled(False)
            self.sy_gb_ln_3.setEnabled(False)
            self.sy_gb_bt_1.setEnabled(True)
            self.sy_gb_bt_2.setEnabled(False)
            self.sy_gb_bt_3.setEnabled(False)
            self.sy_gb_bt_4.setEnabled(False)
        elif self.sy_gb_cb_1.currentIndex() == 1:
            self.sy_gb_ln_1.setEnabled(False)
            self.sy_gb_ln_2.setEnabled(False)
            self.sy_gb_ln_3.setEnabled(False)
            self.sy_gb_bt_1.setEnabled(False)
            self.sy_gb_bt_2.setEnabled(False)
            self.sy_gb_bt_3.setEnabled(False)
            self.sy_gb_bt_4.setEnabled(True)
        else:
            self.sy_gb_ln_1.setEnabled(False)
            self.sy_gb_bt_1.setEnabled(False)
            self.sy_gb_ln_2.setEnabled(True)
            self.sy_gb_ln_3.setEnabled(True)
            self.sy_gb_bt_2.setEnabled(True)
            self.sy_gb_bt_3.setEnabled(True)
            self.sy_gb_bt_4.setEnabled(True)

    def elevation_request(self):
        logging.debug(f'gui - option_window.py - MyOptions - elevation_request')
        lon, lat = None, None
        error = False
        msg = ''
        elev = None
        if self.sy_gb_cb_1.currentIndex() == 1:
            if self.place_object is not None:
                lon, lat = self.place_object['longitude'], self.place_object['latitude']
        else:
            if self.sy_gb_ln_2.text() and self.sy_gb_ln_3.text():
                lon = float(self.sy_gb_ln_2.text())
                lat = float(self.sy_gb_ln_3.text())
        try:
            logging.debug(f'gui - option_window.py - MyOptions - elevation_request - lon: {lon} | lat: {lat}')
            query = f'https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}'
            ans = requests.get(query)

            if ans.status_code == 200:
                try:
                    elev = int(ans.json()['results'][0]['elevation'])
                except ValueError:
                    logging.exception('an exception occurred when sending a request for elevation data.')
                    error = True
                    msg = ('Le serveur OpenElevation n\'a pas retourné une réponse exploitable. En conséquence, '
                           'l\'élévation n\'a pas pu être récupérée.')
            else:
                logging.error('an exception occurred when sending a request for elevation data.')
                error = True
                msg = ('Le serveur OpenElevation a retourné un code d\'erreur. Veuillez vérifier les valeurs de '
                       'longitude et de latitude pour la requête.')
        except requests.exceptions.ConnectionError:
            logging.exception('an exception occurred when sending a request for elevation data.')
            error = True
            msg = ('Erreur de connexion. Soit la station météo n\'est pas connectée à Internet, soit le serveur '
                   'OpenElevation n\'est pas accessible.')
        if error:
            info_window = MyInfo(msg, self.mainparent)
            info_window.exec_()
        else:
            self.sy_gb_ln_1.setText(str(elev))

    def activate_auto_connexion_period(self):
        logging.debug('gui - option_window.py - MyOptions - activate_auto_connexion_period')
        self.sy_gb_4_ln_1.setEnabled(self.sy_gb_4_ck_1.isChecked())
        self.sy_gb_4_cb_1.setEnabled(self.sy_gb_4_ck_1.isChecked())
        self.sy_gb_4_bt_1.setEnabled(self.sy_gb_4_ck_1.isChecked())

    def close_window(self):
        logging.debug('gui - option_window.py - MyOptions - close_window')
        self.close()
