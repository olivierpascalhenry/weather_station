import time
import logging
import markdown
import pathlib
from PyQt5 import QtCore, QtWidgets
from ui.Ui_aboutlogwindow import Ui_aboutlogWindow
from ui.Ui_infowindow import Ui_infoWindow
from ui.Ui_closewindow import Ui_closeWindow
from ui.Ui_numpadwindow import Ui_numpadWindow
from ui.Ui_keyboardwindow import Ui_keyboardWindow
from ui.Ui_townsearchwindow import Ui_townsearchWindow
from ui.Ui_warningwindow import Ui_warningWindow
from ui.Ui_updatewindow import Ui_updateWindow
from ui.Ui_downloadwindow import Ui_downloadWindow
from ui.Ui_connexionwindow import Ui_connexionWindow
from ui.Ui_batlinkwindow import Ui_batlinkWindow
from ui.Ui_pressurewindow import Ui_pressureWindow
from ui.Ui_temphumwindow import Ui_temphumWindow
from functions.utils import code_to_departement, stylesheet_creation_function, font_creation_function
from functions.thread_functions.other_threads import DownloadFile


class MyAbout(QtWidgets.QDialog, Ui_aboutlogWindow):
    def __init__(self, text, gui_path, parent=None):
        logging.debug('gui - other_windows.py - MyAbout - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.gui_path = gui_path
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
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
        logging.info('gui - other_windows.py - MyAbout - ready')

    def read_markdown_file(self):
        changelog = open(pathlib.Path(self.gui_path).joinpath('documentation').joinpath('changelog.txt')).read()
        self.browser_2.setHtml(markdown.markdown(changelog))

    def close_window(self):
        logging.debug('gui - other_windows.py - MyAbout - close_window')
        self.close()


class MyInfo(QtWidgets.QDialog, Ui_infoWindow):
    def __init__(self, info_text, parent=None):
        logging.debug('gui - other_windows.py - MyInfo - __init__ : infoText ' + str(info_text))
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.iw_label_1.setText(info_text)
        self.iw_okButton.clicked.connect(self.close_window)
        logging.info('gui - other_windows.py - MyInfo - ready')

    def close_window(self):
        logging.debug('gui - other_windows.py - MyInfo - closeWindow')
        self.close()


class MyExit(QtWidgets.QDialog, Ui_closeWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows.py - MyExit - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.cancel = True
        self.exit = False
        self.shutdown = False
        self.reboot = False
        self.exit_button.clicked.connect(self.exit_station)
        self.reboot_button.clicked.connect(self.reboot_system)
        self.shutdown_button.clicked.connect(self.shutdown_system)
        logging.info('gui - other_windows.py - MyExit - ready')

    def exit_station(self):
        logging.debug('gui - other_windows.py - MyExit - exit_station')
        self.cancel = False
        self.exit = True
        self.close_window()

    def reboot_system(self):
        logging.debug('gui - other_windows.py - MyExit - reboot_system')
        self.cancel = False
        self.reboot = True
        self.close_window()

    def shutdown_system(self):
        logging.debug('gui - other_windows.py - MyExit - shutdown_system')
        self.cancel = False
        self.shutdown = True
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows.py - MyExit - close_window')
        self.close()


class MyNumpad(QtWidgets.QDialog, Ui_numpadWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows.py - MyNumpad - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((parent.width() - self.width()) / 2), int((parent.height() - self.height()) / 2))
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
        logging.debug('gui - other_windows.py - MyNumpad - close_window')
        self.close()


class MyKeyboard(QtWidgets.QDialog, Ui_keyboardWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows.py - MyKeyboard - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((parent.width() - self.width()) / 2), int((parent.height() - self.height()) / 2))
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
        logging.debug('gui - other_windows.py - MyKeyboard - close_window')
        self.close()


class MyTown(QtWidgets.QDialog, Ui_townsearchWindow):
    def __init__(self, place_list, parent=None):
        logging.debug('gui - other_windows.py - MyTown - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((parent.width() - self.width()) / 2), int((parent.height() - self.height()) / 2))
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
                self.radio_bt_list[idx].setStyleSheet(stylesheet_creation_function('qradiobutton'))
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
        logging.debug('gui - other_windows.py - MyKeyboard - close_window')
        self.close()


class MyWarning(QtWidgets.QDialog, Ui_warningWindow):
    def __init__(self, warning_object, parent=None):
        logging.debug('gui - other_windows.py - MyWarning - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.ok_button.clicked.connect(self.close_window)
        self.text_edit.setText(warning_object)

    def close_window(self):
        logging.debug('gui - other_windows.py - MyWarning - close_window')
        self.close()


class MyWarningUpdate(QtWidgets.QDialog, Ui_updateWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows.py - MyWarningUpdate - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.ok_button.clicked.connect(self.agree_update)
        self.cancel_button.clicked.connect(self.close_window)
        self.cancel = True
        logging.info('gui - other_windows.py - MyWarningUpdate - ready')

    def agree_update(self):
        logging.debug('gui - other_windows.py - MyWarningUpdate - agree_update')
        self.cancel = False
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows.py - MyWarningUpdate - close_window')
        self.close()


class MyDownload(QtWidgets.QDialog, Ui_downloadWindow):
    def __init__(self, url_dict, folder, parent=None):
        logging.debug('gui - other_windows.py - MyDownload - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.temp_folder = folder
        self.url = url_dict['url']
        self.update_file = pathlib.Path(folder).joinpath(url_dict['file'])
        self.dw_button.clicked.connect(self.cancel_download)
        self.cancel = False
        self.thread = None
        self.success = False
        self.download_update()
        logging.info('gui - other_windows.py - MyDownload - ready')

    def update_progress_bar(self, val):
        if isinstance(val, list):
            self.dw_progress_bar.setValue(val[0])
            self.dw_label.setText(val[1])
        else:
            self.dw_progress_bar.setValue(val)

    def download_update(self):
        logging.debug('gui - other_windows.py - MyDownload - download_update')
        self.thread = DownloadFile(self.url, self.update_file)
        self.thread.download_update.connect(self.update_progress_bar)
        self.thread.download_done.connect(self.donwload_done)
        self.thread.download_failed.connect(self.download_failed)
        self.thread.start()

    def donwload_done(self):
        logging.debug('gui - other_windows.py - MyDownload - donwload_done')
        self.success = True
        self.close_window()

    def cancel_download(self):
        logging.debug('gui - other_windows.py - MyDownload - cancel_download')
        if self.thread is not None:
            self.thread.cancel_download()
        self.cancel = True
        time.sleep(0.25)
        self.close_window()

    def download_failed(self):
        logging.debug('gui - other_windows.py - MyDownload - download_failed')
        self.update_progress_bar(0)
        self.dw_label.setText('Download failed')
        self.cancel_download()

    def close_window(self):
        logging.info('gui - other_windows.py - MyDownload - close_window')
        self.close()


class MyConnexion(QtWidgets.QDialog, Ui_connexionWindow):
    def __init__(self, parent=None):
        logging.debug('gui - other_windows.py - MyConnexion - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.retry = False
        self.ok_button.clicked.connect(self.retry_connexion)
        self.cancel_button.clicked.connect(self.close_window)

    def retry_connexion(self):
        self.retry = True
        self.close_window()

    def close_window(self):
        logging.info('gui - other_windows.py - MyConnexion - close_window')
        self.close()


class MyBatLink(QtWidgets.QDialog, Ui_batlinkWindow):
    def __init__(self, bat, link, parent=None):
        logging.debug('gui - other_windows.py - MyBatLink - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.bat = bat
        self.link = link
        self.ok_button.clicked.connect(self.close_window)
        self.set_details()

    def set_details(self):
        logging.debug('gui - other_windows.py - MyBatLink - set_details')
        self.batterie_lb_2.setText(f'{int(self.bat)} %')
        self.signal_lb_3.setText(f'{int(round((self.link / 255) * 100, 0))} %')

    def close_window(self):
        logging.debug('gui - other_windows.py - MyBatLink - close_window')
        self.close()


class MyPressure(QtWidgets.QDialog, Ui_pressureWindow):
    def __init__(self, pres, pres_msl, alt, parent=None):
        logging.debug('gui - other_windows.py - MyPressure - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.pres = pres
        self.pres_msl = pres_msl
        self.alt = alt
        self.ok_button.clicked.connect(self.close_window)
        self.set_details()

    def set_details(self):
        logging.debug('gui - other_windows.py - MyPressure - set_details')
        self.pressure_lb_4.setText(f'{self.pres} hPa')
        self.pressure_lb_5.setText(f'{self.pres_msl} hPa')
        self.pressure_lb_6.setText(f'{self.alt} m')

    def close_window(self):
        logging.debug('gui - other_windows.py - MyPressure - close_window')
        self.close()


class MyTempHum(QtWidgets.QDialog, Ui_temphumWindow):
    def __init__(self, hum, temp, dew, parent=None):
        logging.debug('gui - other_windows.py - MyPressure - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.hum = hum
        self.temp = temp
        self.dew = dew
        self.ok_button.clicked.connect(self.close_window)
        self.set_details()

    def set_details(self):
        logging.debug('gui - other_windows.py - MyPressure - set_details')
        self.hum_lb.setText(f'{self.hum} %')
        self.temp_lb.setText(f'{self.temp} °C')
        self.dew_lb.setText(f'{self.dew} °C')

    def close_window(self):
        logging.debug('gui - other_windows.py - MyPressure - close_window')
        self.close()