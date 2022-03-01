import bisect
import logging
from numpy import arange
from PyQt5 import QtCore, QtWidgets
from ui.Ui_forecast1hwindow import Ui_forecast1hWindow
from ui.Ui_forecast6hwindow import Ui_forecast6hWindow
from functions.utils import weather_to_pictogrammes, days_months_dictionary, wind_dir_to_pictogramme


class My1hFCDetails(QtWidgets.QDialog, Ui_forecast1hWindow):
    def __init__(self, forecast, parent=None):
        logging.info('gui - weather_windows.py - My1hFCDetails - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.forecast = forecast
        self.ok_button.clicked.connect(self.close_window)
        self.parse_forecast()

    def parse_forecast(self):
        logging.debug('gui - weather_windows.py - My1hFCDetails - parse_forecast')
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
            icon = wind_dir_to_pictogramme(idx)
        else:
            icon = wind_dir_to_pictogramme(0)
        self.dir_ln.setIcon(icon)
        self.date_label.setText(date)
        self.hour_label.setText(str(dt.hour) + 'h')
        self.temp_ln.setText(str(self.forecast['temp']) + '°C')
        self.pres_ln.setText(str(self.forecast['pres']) + ' hPa')
        self.speed_ln.setText(str(wspeed) + ' km/h')
        self.cover_ln.setText(str(self.forecast['cover']) + ' %')
        self.rain_ln.setText(str(self.forecast['rain']) + ' mm')
        self.weather_lb.setIcon(weather_to_pictogrammes(self.forecast['weather']))

    def close_window(self):
        logging.debug('gui - weather_windows.py - My1hFCDetails - close_window')
        self.close()


class My6hFCDetails(QtWidgets.QDialog, Ui_forecast6hWindow):
    def __init__(self, forecast, parent=None):
        logging.info('gui - weather_windows.py - My6hFCDetails - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.forecast = forecast
        self.ok_button.clicked.connect(self.close)
        self.parse_forecast()

    def parse_forecast(self):
        logging.debug('gui - weather_windows.py - My6hFCDetails - parse_forecast')
        for i, fc in enumerate(self.forecast):
            wspeed = round(fc[1]['w_spd'] * 3600 / 1000)
            wdir = fc[1]['w_dir']
            if wspeed > 5:
                if wdir > 180:
                    wdir -= 180
                else:
                    wdir += 180
                idx = bisect.bisect_right(list(arange(0, 360, 7.5)) + [360], wdir)
                icon = wind_dir_to_pictogramme(idx)
            else:
                icon = wind_dir_to_pictogramme(0)
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
                           + str(i + 1)).setIcon(weather_to_pictogrammes(fc[1]['weather']))

    def close_window(self):
        logging.debug('gui - weather_windows.py - My6hFCDetails - close_window')
        self.close()
