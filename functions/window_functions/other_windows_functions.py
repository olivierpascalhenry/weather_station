import pickle
import logging
import pathlib
import platform
import markdown
from numpy import arange
import bisect
import time
from meteofrance_api import MeteoFranceClient
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_optionwindow import Ui_optionWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_closewindow import Ui_closeWindow
from ui.Ui_forecast1hwindow import Ui_forecast1hWindow
from ui.Ui_forecast6hwindow import Ui_forecast6hWindow
from ui.Ui_numpadwindow import Ui_numpadWindow
from ui.Ui_keyboardwindow import Ui_keyboardWindow
from ui.Ui_townsearchwindow import Ui_townsearchWindow
from ui.Ui_warningwindow import Ui_warningWindow
from ui.Ui_updatewindow import Ui_updateWindow
from ui.Ui_downloadwindow import Ui_downloadWindow
from ui.Ui_connexionwindow import Ui_connexionWindow
from ui.Ui_waitwindow import Ui_waitWindow
from functions.utils import (weather_to_pictogrammes, days_months_dictionary, wind_dir_to_pictogramme,
                             code_to_departement, stylesheet_creation_function, font_creation_function)
from functions.thread_functions.other_threads import DownloadFile
from functions.gui_widgets import QtWaitingSpinner


class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, text, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
            self.browser_1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
            self.browser_2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.gui_path = gui_path
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.browser_1.setHtml(text)
        scroll_1 = QtWidgets.QScroller.scroller(self.browser_1.viewport())
        scroll_1.grabGesture(self.browser_1.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties_1 = scroll_1.scrollerProperties()
        properties_1.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                     QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll_1.setScrollerProperties(properties_1)
        scroll_2 = QtWidgets.QScroller.scroller(self.browser_2.viewport())
        scroll_2.grabGesture(self.browser_2.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties_2 = scroll_2.scrollerProperties()
        properties_2.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                     QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll_2.setScrollerProperties(properties_2)
        self.button.clicked.connect(self.close_window)
        self.splitter.setSizes([100, 200])
        self.read_markdown_file()
        logging.info('gui - other_windows_functions.py - MyAbout - ready')

    def read_markdown_file(self):
        changelog = open(pathlib.Path(self.gui_path).joinpath('documentation').joinpath('changelog.txt')).read()
        self.browser_2.setHtml(markdown.markdown(changelog))

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyAbout - close_window')
        self.close()


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict, user_path, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyOptions - __init__ ')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.gui_path = gui_path
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.config_dict = config_dict
        self.ow_splitter.setSizes([180, 520])
        self.user_path = user_path
        self.cancel = True
        self.place_object = None
        self.ow_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_2.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_3.setAlignment(QtCore.Qt.AlignTop)
        self.ow_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_section_list.currentRowChanged.connect(self.display_options)
        self.ow_ok_button.clicked.connect(self.save_config_dict)
        self.ow_cancel_button.clicked.connect(self.close_window)
        self.ow_openButton.clicked.connect(self.get_folder_path)
        self.ow_edit_bt_1.clicked.connect(self.display_numpad)
        self.ow_edit_bt_2.clicked.connect(self.display_numpad)
        self.ow_edit_bt_3.clicked.connect(self.display_keyboard)
        self.ow_edit_bt_4.clicked.connect(self.display_numpad)
        self.ow_edit_bt_5.clicked.connect(self.display_numpad)
        self.ow_line_4.textChanged.connect(self.activate_search_button)
        self.ow_search_button.clicked.connect(self.search_place)
        self.read_config_dict()
        self.ow_section_list.setCurrentRow(0)

    def display_options(self, idx):
        self.ow_stacked_widget.setCurrentIndex(idx)

    def read_config_dict(self):
        logging.debug('gui - option_window_functions.py - MyOptions - read_config_dict')
        self.ow_combobox_1.setCurrentIndex(self.ow_combobox_1.findText(self.config_dict.get('LOG', 'level')))
        self.ow_line_1.setText(self.config_dict.get('LOG', 'path'))
        self.ow_line_1.setCursorPosition(0)
        self.ow_line_2.setText(self.config_dict.get('SYSTEM', 'sensors_rate'))
        self.ow_line_3.setText(self.config_dict.get('SYSTEM', 'display_rate'))
        self.ow_line_7.setText(self.config_dict.get('SYSTEM', 'place_altitude'))
        self.ow_line_5.setText(self.config_dict.get('METEOFRANCE', 'request_rate'))
        if self.config_dict.getboolean('METEOFRANCE', 'user_place'):
            f = open(self.user_path + '/place_object.dat', 'rb')
            self.place_object = pickle.load(f)
            f.close()
            self.ow_line_4.setText(self.place_object.name)
            self.ow_label_13.setText(self.place_object.postal_code)
            self.ow_label_14.setText(code_to_departement()[self.place_object.admin2])

    def save_config_dict(self):
        logging.debug('gui - option_window_functions.py - MyOptions - save_config_dict')
        if not pathlib.Path(str(self.ow_line_1.text())).exists():
            text = ('After checking, it appears that the path for the log file is not valid. Thus it is not possible '
                    'to save the new configuration. Please correct it and try again.')
            info_window = MyInfo(text)
            info_window.exec_()
        else:
            self.config_dict.set('LOG', 'level', str(self.ow_combobox_1.currentText()))
            self.config_dict.set('LOG', 'path', str(self.ow_line_1.text()))
            self.config_dict.set('SYSTEM', 'sensors_rate', str(self.ow_line_2.text()))
            self.config_dict.set('SYSTEM', 'display_rate', str(self.ow_line_3.text()))
            self.config_dict.set('METEOFRANCE', 'request_rate', str(self.ow_line_5.text()))
            self.config_dict.set('SYSTEM', 'place_altitude', str(self.ow_line_7.text()))
            if self.place_object is not None:
                self.config_dict.set('METEOFRANCE', 'user_place', 'True')
            else:
                self.config_dict.set('METEOFRANCE', 'user_place', 'False')
            self.cancel = False
            self.close_window()

    def get_folder_path(self):
        logging.debug('gui - other_windows_functions.py - MyOptions - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Sélectionner un répertoire')
        if folder_path:
            self.ow_line_1.setText(str(pathlib.Path(folder_path)))
            self.ow_line_1.setCursorPosition(0)

    def activate_search_button(self):
        if self.ow_line_4.text():
            self.ow_search_button.setEnabled(True)
        else:
            self.ow_search_button.setEnabled(False)

    def search_place(self):
        place, ville, code_postal, departement = None, None, None, None
        list_places = MeteoFranceClient().search_places(str(self.ow_line_4.text()))
        if len(list_places) > 1:
            place_search = MyTown(list_places, self.gui_path, None)
            place_search.setGeometry(260, 157, 504, 286)
            place_search.exec_()
            if not place_search.cancel:
                place = place_search.place
                ville = place_search.ville
                code_postal = place_search.code_postal
                departement = place_search.departement
        else:
            place = list_places[0]
            ville = list_places[0].name
            code_postal = list_places[0].postal_code
            departement = code_to_departement()[list_places[0].admin2]

        if place is not None:
            self.place_object = place
            self.ow_line_4.setText(ville)
            self.ow_label_13.setText(code_postal)
            self.ow_label_14.setText(departement)

    # def button_info(self):
    #     logging.debug('gui - other_windows_functions.py - MyOptions - button_info')
    #     text = self.information_text[self.sender().objectName()]
    #     text = 'no information yet'
    #     info_window = MyInfo(text)
    #     info_window.exec_()

    def display_numpad(self):
        numpad_window = MyNumpad(self.gui_path, self)
        numpad_window.setGeometry(227, 26, 246, 298)
        numpad_window.exec_()
        if not numpad_window.cancel:
            if self.sender().objectName() == 'ow_edit_bt_1':
                self.ow_line_2.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_2':
                self.ow_line_3.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_4':
                self.ow_line_5.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_5':
                self.ow_line_7.setText(numpad_window.num_line.text())

    def display_keyboard(self):
        keyboard_window = MyKeyboard(self.gui_path, self)
        keyboard_window.setGeometry(56, 11, 588, 328)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            self.ow_line_4.setText(keyboard_window.num_line.text())

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyAbout - close_window')
        self.close()


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, info_text):
        logging.debug('gui - other_windows_functions.py - MyInfo - __init__ : infoText ' + str(info_text))
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.iw_label_1.setText(info_text)
        self.iw_okButton.clicked.connect(self.close_window)
        logging.info('gui - other_windows_functions.py - MyInfo - ready')

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyInfo - closeWindow')
        self.close()


class MyExit(QtWidgets.QDialog, Ui_closeWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows_functions.py - MyExit - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.cancel = True
        self.exit = False
        self.shutdown = False
        self.reboot = False
        self.exit_button.clicked.connect(self.exit_station)
        self.reboot_button.clicked.connect(self.reboot_system)
        self.shutdown_button.clicked.connect(self.shutdown_system)
        logging.info('gui - other_windows_functions.py - MyExit - ready')

    def exit_station(self):
        logging.debug('gui - other_windows_functions.py - MyExit - exit_station')
        self.cancel = False
        self.exit = True
        self.close_window()

    def reboot_system(self):
        logging.debug('gui - other_windows_functions.py - MyExit - reboot_system')
        self.cancel = False
        self.reboot = True
        self.close_window()

    def shutdown_system(self):
        logging.debug('gui - other_windows_functions.py - MyExit - shutdown_system')
        self.cancel = False
        self.shutdown = True
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyExit - close_window')
        self.close()


class My1hFCDetails(QtWidgets.QDialog, Ui_forecast1hWindow):
    def __init__(self, forecast, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - My1hFCDetails - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.gui_path = gui_path
        self.forecast = forecast
        self.ok_button.clicked.connect(self.close_window)
        self.parse_forecast()

    def parse_forecast(self):
        wspeed = round(self.forecast['w_spd'] * 3600 / 1000)
        wdir = self.forecast['w_dir']
        dt = self.forecast['datetime']
        date = (days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day) + ' '
                + days_months_dictionary()['month'][dt.month])
        if wspeed > 5:
            if wdir > 180:
                wdir -= 180
            else:
                wdir += 180
            idx = bisect.bisect_right(list(arange(0, 360, 7.5)) + [360], wdir)
            icon = wind_dir_to_pictogramme(idx, self.gui_path + '/')
        else:
            icon = wind_dir_to_pictogramme(0, self.gui_path + '/')
        self.dir_ln.setIcon(icon)
        self.date_label.setText(date)
        self.hour_label.setText(str(dt.hour) + 'h')
        self.temp_ln.setText(str(self.forecast['temp']) + '°C')
        self.pres_ln.setText(str(self.forecast['pres']) + ' hPa')
        self.speed_ln.setText(str(wspeed) + ' km/h')
        self.cover_ln.setText(str(self.forecast['cover']) + ' %')
        self.rain_ln.setText(str(self.forecast['rain']) + ' mm')
        self.weather_lb.setIcon(weather_to_pictogrammes(self.forecast['weather'], self.gui_path + '/'))

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - My1hFCDetails - close_window')
        self.close()


class My6hFCDetails(QtWidgets.QDialog, Ui_forecast6hWindow):
    def __init__(self, forecast, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - My6hFCDetails - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.gui_path = gui_path
        self.forecast = forecast
        self.ok_button.clicked.connect(self.close)
        self.parse_forecast()

    def parse_forecast(self):
        for i, fc in enumerate(self.forecast):
            wspeed = round(fc[1]['w_spd'] * 3600 / 1000)
            wdir = fc[1]['w_dir']

            if wspeed > 5:
                if wdir > 180:
                    wdir -= 180
                else:
                    wdir += 180
                idx = bisect.bisect_right(list(arange(0, 360, 7.5)) + [360], wdir)
                icon = wind_dir_to_pictogramme(idx, self.gui_path + '/')
            else:
                icon = wind_dir_to_pictogramme(0, self.gui_path + '/')
            if i == 0:
                dt = fc[0]
                date = (days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day) + ' '
                        + days_months_dictionary()['month'][dt.month])
                self.date_label.setText(date)

            self.findChild(QtWidgets.QLabel, 'temp_ln_' + str(i + 1)).setText(str(fc[1]['temp']) + '°C')
            self.findChild(QtWidgets.QLabel, 'pres_ln_' + str(i + 1)).setText(str(round(fc[1]['pres'])) + ' hPa')
            self.findChild(QtWidgets.QLabel, 'speed_ln_' + str(i + 1)).setText(str(wspeed) + ' km/h')
            self.findChild(QtWidgets.QToolButton, 'dir_ln_' + str(i + 1)).setIcon(icon)
            self.findChild(QtWidgets.QToolButton, 'weather_lb_'
                           + str(i + 1)).setIcon(weather_to_pictogrammes(fc[1]['weather'], self.gui_path + '/'))

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - My6hFCDetails - close_window')
        self.close()


class MyNumpad(QtWidgets.QDialog, Ui_numpadWindow):
    def __init__(self, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyNumpad - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.cancel = True
        for button in self.findChildren(QtWidgets.QToolButton):
            if 'ok' in button.objectName():
                button.clicked.connect(self.confirm_num)
            elif 'cancel' in button.objectName():
                button.clicked.connect(self.close_window)
            elif 'ret' in button.objectName():
                button.clicked.connect(self.del_number)
            else:
                button.clicked.connect(self.add_number)

    def add_number(self):
        self.num_line.setText(self.num_line.text() + self.sender().objectName()[-1:])

    def del_number(self):
        self.num_line.setText(self.num_line.text()[:-1])

    def confirm_num(self):
        if self.num_line.text():
            self.cancel = False
            self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyNumpad - close_window')
        self.close()


class MyKeyboard(QtWidgets.QDialog, Ui_keyboardWindow):
    def __init__(self, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyKeyboard - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.cancel = True
        for button in self.findChildren(QtWidgets.QToolButton):
            if 'ok' in button.objectName():
                button.clicked.connect(self.confirm_word)
            elif 'cancel' in button.objectName():
                button.clicked.connect(self.close_window)
            elif 'ret' in button.objectName():
                button.clicked.connect(self.del_letter)
            elif 'esc' in button.objectName():
                button.clicked.connect(self.add_space)
            elif 'min' in button.objectName():
                button.clicked.connect(self.add_minus)
            else:
                button.clicked.connect(self.add_letter)

    def add_letter(self):
        self.num_line.setText(self.num_line.text() + self.sender().objectName()[-1:])

    def add_space(self):
        self.num_line.setText(self.num_line.text() + ' ')

    def add_minus(self):
        self.num_line.setText(self.num_line.text() + '-')

    def del_letter(self):
        self.num_line.setText(self.num_line.text()[:-1])

    def confirm_word(self):
        if self.num_line.text():
            self.cancel = False
            self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyKeyboard - close_window')
        self.close()


class MyTown(QtWidgets.QDialog, Ui_townsearchWindow):
    def __init__(self, place_list, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyTown - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.gui_path = gui_path
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.cancel = True
        self.place_list = place_list
        self.radio_bt_list = []
        self.ville = None
        self.code_postal = None
        self.departement = None
        self.place = None
        self.ok_button.clicked.connect(self.confirm_place)
        self.cancel_button.clicked.connect(self.close_window)
        self.ok_button.setEnabled(False)
        self.display_place_list()

    def display_place_list(self):
        idx = 0
        for place in self.place_list:
            if place.country == 'FR':
                self.radio_bt_list.append(QtWidgets.QRadioButton())
                self.radio_bt_list[idx].setMinimumSize(QtCore.QSize(0, 40))
                self.radio_bt_list[idx].setMaximumSize(QtCore.QSize(16777215, 40))
                self.radio_bt_list[idx].setFont(font_creation_function('medium_big'))
                stylesheet = stylesheet_creation_function('qradiobutton',
                                                          self.gui_path + '/').replace('icons', self.gui_path + 'icons')
                self.radio_bt_list[idx].setStyleSheet(stylesheet)
                self.radio_bt_list[idx].setObjectName('place_' + str(idx))
                self.radio_bt_list[idx].setText(place.name + ', ' + place.postal_code + ', '
                                                + code_to_departement()[place.admin2])
                self.verticalLayout.addWidget(self.radio_bt_list[idx])
                self.radio_bt_list[idx].clicked.connect(self.set_place)
                self.radio_bt_list[idx].clicked.connect(self.activate_ok)
                idx += 1
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)

    def set_place(self):
        idx = int(self.sender().objectName()[6:])
        self.ville = self.place_list[idx].name
        self.code_postal = self.place_list[idx].postal_code
        self.departement = code_to_departement()[self.place_list[idx].admin2]
        self.place = self.place_list[idx]

    def activate_ok(self):
        self.ok_button.setEnabled(True)

    def confirm_place(self):
        if self.ville is not None:
            self.cancel = False
            self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyKeyboard - close_window')
        self.close()


class MyWarning(QtWidgets.QDialog, Ui_warningWindow):
    def __init__(self, warning_object, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyWarning - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.ok_button.clicked.connect(self.close_window)
        self.text_edit.setText(warning_object)

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyWarning - close_window')
        self.close()


class MyWarningUpdate(QtWidgets.QDialog, Ui_updateWindow):
    def __init__(self, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyWarningUpdate - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.ok_button.clicked.connect(self.agree_update)
        self.cancel_button.clicked.connect(self.close_window)
        self.cancel = True
        logging.info('gui - other_windows_functions.py - MyWarningUpdate - ready')

    def agree_update(self):
        logging.debug('gui - other_windows_functions.py - MyWarningUpdate - agree_update')
        self.cancel = False
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows_functions.py - MyWarningUpdate - close_window')
        self.close()


class MyDownload(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, url_dict, folder, parent=None):
        logging.debug('gui - other_windows_functions.py - MyDownload - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.temp_folder = folder
        self.url = url_dict['url']
        self.update_file = pathlib.Path(folder).joinpath(url_dict['file'])
        self.dw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.thread = None
        self.success = False
        self.download_update()
        logging.info('gui - other_windows_functions.py - MyDownload - ready')

    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.dw_progress_bar.setValue(val[0])
            self.dw_label.setText(val[1])
        else:
            self.dw_progress_bar.setValue(val)

    def download_update(self):
        logging.debug('gui - other_windows_functions.py - MyDownload - download_update')
        self.thread = DownloadFile(self.url, self.update_file)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.donwload_done)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()

    def donwload_done(self):
        logging.debug('gui - other_windows_functions.py - MyDownload - donwload_done')
        self.success = True
        self.close_window()

    def cancel_download(self):
        logging.debug('gui - other_windows_functions.py - MyDownload - cancel_download')
        if self.thread is not None:
            self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close_window()

    def download_failed(self):
        logging.debug('gui - other_windows_functions.py - MyDownload - download_failed')
        self.update_progress_bar(0)
        self.dw_label.setText('Download failed')
        self.cancel_download()

    def close_window(self):
        logging.info('gui - other_windows_functions.py - MyDownload - close_window')
        self.close()


class MyConnexion(QtWidgets.QDialog, Ui_connexionWindow):
    def __init__(self, gui_path, parent=None):
        logging.debug('gui - other_windows_functions.py - MyConnexion - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setupUi(self, gui_path)
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        else:
            self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.retry = False
        self.ok_button.clicked.connect(self.retry_connexion)
        self.cancel_button.clicked.connect(self.close_window)

    def retry_connexion(self):
        self.retry = True
        self.close_window()

    def close_window(self):
        logging.info('gui - other_windows_functions.py - MyConnexion - close_window')
        self.close()


class MyWait(QtWidgets.QDialog, Ui_waitWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows_functions.py - MyWait - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        if platform.system() == 'Linux' and platform.node() != 'raspberry':
            self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.spinner = None
        self.setup_spinner()
        logging.info('gui - other_windows_functions.py - MyWait - ready')

    def setup_spinner(self):
        logging.debug('gui - other_windows_functions.py - MyWait - setup_spinner')
        self.spinner = QtWaitingSpinner(self, centerOnParent=False)
        self.verticalLayout.addWidget(self.spinner)
        self.spinner.setRoundness(70.0)
        self.spinner.setMinimumTrailOpacity(15.0)
        self.spinner.setTrailFadePercentage(70.0)
        self.spinner.setNumberOfLines(12)
        self.spinner.setLineLength(10)
        self.spinner.setLineWidth(5)
        self.spinner.setInnerRadius(10)
        self.spinner.setRevolutionsPerSecond(1)
        self.spinner.setColor(QtGui.QColor(45, 45, 45))
        self.spinner.start()

    def closeWindow(self):
        logging.debug('gui - other_windows_functions.py - MyWait - closeWindow')
        self.close()
