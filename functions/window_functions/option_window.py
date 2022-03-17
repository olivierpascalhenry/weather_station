import platform

import copy
import pickle
import logging
import pathlib
from meteofrance_api import MeteoFranceClient
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from PyQt5 import QtCore, QtWidgets
from ui.Ui_optionwindow import Ui_optionWindow
from functions.utils import code_to_departement
from functions.window_functions.other_windows import MyInfo, MyNumpad, MyKeyboard, MyTown, MyAPI
from functions.window_functions.sensor_windows import MqttManager, W1SensorManager, BME280SensorManager


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
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
        self.af_vl.setAlignment(QtCore.Qt.AlignTop)
        self.ca_vl.setAlignment(QtCore.Qt.AlignTop)
        self.ap_vl.setAlignment(QtCore.Qt.AlignTop)
        self.sy_vl.setAlignment(QtCore.Qt.AlignTop)
        self.st_vl.setAlignment(QtCore.Qt.AlignTop)
        self.lo_gb_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_int_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.af_gb_ext_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_int_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_int_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_ext_cb_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ts_gb_ext_cb_2.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.section_list.currentRowChanged.connect(self.display_options)
        self.ok_button.clicked.connect(self.save_config_dict)
        self.cancel_button.clicked.connect(self.close_window)
        self.lo_gb_bt_1.clicked.connect(self.get_folder_path)
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
        self.create_sensor_list()
        self.parse_sensor_list_in_cb()
        self.read_config_dict()
        self.section_list.setCurrentRow(0)

    def display_options(self, idx):
        logging.debug(f'gui - option_window.py - MyOptions - display_options - idx: {idx}')
        self.stack_widget.setCurrentIndex(idx)

    def create_sensor_list(self):
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
        cb_list = [self.af_gb_int_cb_1, self.af_gb_ext_cb_1, self.ts_gb_int_cb_1, self.ts_gb_int_cb_2,
                   self.ts_gb_ext_cb_1, self.ts_gb_ext_cb_2]
        if self.sensor_list:
            for cb in cb_list:
                cb.clear()
                cb.addItem('Choisir un capteur')
                cb.addItems(sorted(self.sensor_list))
        else:
            for cb in cb_list:
                cb.clear()
                cb.addItem('Pas de capteur')

    def update_cb_with_sensor_list(self):
        self.create_sensor_list()
        cb_list = [self.af_gb_int_cb_1, self.af_gb_ext_cb_1, self.ts_gb_int_cb_1, self.ts_gb_int_cb_2,
                   self.ts_gb_ext_cb_1, self.ts_gb_ext_cb_2]
        if self.sensor_list:
            for cb in cb_list:
                device = cb.currentText()
                cb.clear()
                cb.addItem('Choisir un capteur')
                cb.addItems(sorted(self.sensor_list))
                if device in self.sensor_list:
                    cb.setCurrentIndex(cb.findText(device))
        else:
            for cb in cb_list:
                cb.clear()
                cb.addItem('Pas de capteur')

    def read_config_dict(self):
        logging.debug('gui - option_window.py - MyOptions - read_config_dict')
        api = None
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
        self.ts_gb_ext_ck_1.setChecked(self.config_dict.getboolean('TIMESERIES', 'msl_pressure'))
        if self.config_dict.get('DISPLAY', 'in_sensor') in self.sensor_list:
            self.af_gb_int_cb_1.setCurrentIndex(self.af_gb_int_cb_1.findText(self.config_dict.get('DISPLAY',
                                                                                                  'in_sensor')))
        if self.config_dict.get('DISPLAY', 'out_sensor') in self.sensor_list:
            self.af_gb_ext_cb_1.setCurrentIndex(self.af_gb_ext_cb_1.findText(self.config_dict.get('DISPLAY',
                                                                                                  'out_sensor')))
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
            api = 'meteofrance'
            self.ap_gb_rb_1.click()
        elif self.config_dict.get('API', 'api_used') == 'openweather':
            api = 'openweather'
            self.ap_gb_rb_2.click()
            self.api_key = self.config_dict.get('API', 'api_key')
            self.ap_gb_lb_1.setText(self.config_dict.get('API', 'api_key'))
        if self.config_dict.getboolean('API', 'user_place'):
            f = open(self.user_path + '/place_object.dat', 'rb')
            self.place_object = pickle.load(f)
            f.close()
            self.ap_gb_2_ln_1.setText(self.place_object.name)
            if api == 'meteofrance':
                self.ap_gb_2_lb_4.setText(str(self.place_object.postal_code))
                self.ap_gb_2_lb_5.setText(code_to_departement()[self.place_object.admin2])
            elif api == 'openweather':
                self.ap_gb_2_lb_4.setText(str(self.place_object.id))
                lon = str(self.place_object.lon)
                lat = str(self.place_object.lat)
                if lon == '-':
                    lon = lon + '°W'
                else:
                    lon += '°E'
                if lat == '-':
                    lat = lat + '°S'
                else:
                    lat += '°N'
                self.ap_gb_2_lb_5.setText(f'Lon : {lon} ; Lat : {lat}')

    def save_config_dict(self):
        logging.debug('gui - option_window.py - MyOptions - save_config_dict')
        if not pathlib.Path(str(self.lo_gb_ln_1.text())).exists():
            text = ('After checking, it appears that the path for the log file is not valid. Thus it is not possible '
                    'to save the new configuration. Please correct it and try again.')
            info_window = MyInfo(text)
            info_window.exec_()
        else:
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
                self.config_dict.set('DISPLAY', 'out_sensor', str(self.af_gb_ext_cb_1.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'out_sensor', '')
            if self.af_gb_int_cb_1.currentText() not in ['Choisir un capteur', 'Pas de capteur']:
                self.config_dict.set('DISPLAY', 'in_sensor', str(self.af_gb_int_cb_1.currentText()))
            else:
                self.config_dict.set('DISPLAY', 'in_sensor', '')
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
        mqtt_manager = MqttManager(copy.deepcopy(self.sensor_dict['MQTT']), self.mainparent)
        mqtt_manager.exec_()
        if not mqtt_manager.cancel:
            self.sensor_dict['MQTT'] = mqtt_manager.mqtt_dict
            self.update_cb_with_sensor_list()

    def show_1w_manager(self):
        manager_window = W1SensorManager(copy.deepcopy(self.sensor_dict['DS18B20']), self.mainparent)
        manager_window.exec_()
        if not manager_window.cancel:
            self.sensor_dict['DS18B20'] = manager_window.sensor_dict
            self.update_cb_with_sensor_list()

    def show_bme280_manager(self):
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
        if self.ap_gb_rb_2.isChecked():
            self.ap_gb_2_lb_2.setText('ID :')
            self.ap_gb_2_lb_3.setText('Coordonnées :')
            self.ap_gb_2_ln_1.setText('')
            self.ap_gb_2_lb_4.setText('')
            self.ap_gb_2_lb_5.setText('')
            if self.place_object is not None and self.place_object.api == 'openweather':
                self.ap_gb_2_ln_1.setText(self.place_object.name)
                self.ap_gb_2_lb_4.setText(str(self.place_object.id))
                lon = str(self.place_object.lon)
                lat = str(self.place_object.lat)
                if lon == '-':
                    lon = lon + '°W'
                else:
                    lon += '°E'
                if lat == '-':
                    lat = lat + '°S'
                else:
                    lat += '°N'
                self.ap_gb_2_lb_5.setText(f'Lon : {lon} ; Lat : {lat}')
        elif self.ap_gb_rb_1.isChecked():
            self.ap_gb_2_lb_2.setText('Code postal :')
            self.ap_gb_2_lb_3.setText('Département :')
            self.ap_gb_2_ln_1.setText('')
            self.ap_gb_2_lb_4.setText('')
            self.ap_gb_2_lb_5.setText('')
            if self.place_object is not None and self.place_object.api == 'meteofrance':
                self.ap_gb_2_ln_1.setText(self.place_object.name)
                self.ap_gb_2_lb_4.setText(str(self.place_object.postal_code))
                self.ap_gb_2_lb_5.setText(code_to_departement()[self.place_object.admin2])

    def activate_search_button(self):
        logging.debug('gui - option_window.py - MyOptions - activate_search_button')
        if self.ap_gb_2_ln_1.text():
            self.ap_gb_2_bt_2.setEnabled(True)
        else:
            self.ap_gb_2_bt_2.setEnabled(False)

    def search_place(self):
        logging.debug('gui - option_window.py - MyOptions - search_place')
        place, ville, cp_id, dp_gps = None, None, None, None
        list_places = None
        api = None
        if self.ap_gb_rb_1.isChecked():
            list_places = MeteoFranceClient().search_places(self.ap_gb_2_ln_1.text())
            api = 'meteofrance'
        elif self.ap_gb_rb_2.isChecked():
            api = 'openweather'
            config_dict = get_default_config()
            config_dict['language'] = 'fr'
            owm = OWM(self.api_key, config_dict)
            reg = owm.city_id_registry()
            list_places = reg.locations_for(self.ap_gb_2_ln_1.text())

        if len(list_places) > 1:
            place_search = MyTown(list_places, api, self)
            place_search.exec_()
            if not place_search.cancel:
                place = place_search.place
                ville = place_search.ville
                cp_id = place_search.cp_id
                dp_gps = place_search.dp_gps
        else:
            if api == 'meteofrance':
                list_places[0].api = 'meteofrance'
                place = list_places[0]
                ville = list_places[0].name
                cp_id = list_places[0].postal_code
                dp_gps = code_to_departement()[list_places[0].admin2]
            elif api == 'openweather':
                list_places[0].api = 'openweather'
                ville = list_places[0].name
                cp_id = list_places[0].id
                dp_gps = {'lon': list_places[0].lon, 'lat': list_places[0].lat}
                place = list_places[0]

        if place is not None:
            self.place_object = place
            self.ap_gb_2_ln_1.setText(ville)
            self.ap_gb_2_lb_4.setText(str(cp_id))
            if api == 'meteofrance':
                self.ap_gb_2_lb_5.setText(dp_gps)
            elif api == 'openweather':
                lon = str(dp_gps['lon'])
                lat = str(dp_gps['lat'])
                if lon == '-':
                    lon = lon + '°W'
                else:
                    lon += '°E'
                if lat == '-':
                    lat = lat + '°S'
                else:
                    lat += '°N'
                self.ap_gb_2_lb_5.setText(f'Lon : {lon} ; Lat : {lat}')

    def set_openweather_key(self):
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
                self.ap_gb_3_ln_1.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'sy_gb_bt_1':
                self.sy_gb_ln_1.setText(numpad_window.num_line.text())

    def display_keyboard(self):
        logging.debug('gui - option_window.py - MyOptions - display_keyboard')
        keyboard_window = MyKeyboard(self.mainparent)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            self.ap_gb_2_ln_1.setText(keyboard_window.num_line.text())

    def close_window(self):
        logging.debug('gui - option_window.py - MyOptions - close_window')
        self.close()
