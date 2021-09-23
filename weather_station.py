import os
import sys
import logging
import pathlib
import platform
import configparser
from PyQt5 import QtWidgets, QtGui, QtCore
from ui.mainwindow import MainWindow
from ui.version import gui_version
from functions.utils import create_option_file, create_logging_handlers
from matplotlib import __version__ as mpl_version
from markdown import __version__ as mk_version
from psycopg2 import __version__ as pg_version
from requests import __version__ as rq_version
if platform.system() == 'Linux':
    from smbus2 import __version__ as bu_version
    from bme280 import __version__ as bm_version


def launch_station(gui_path, user_path):
    app = QtWidgets.QApplication(sys.argv)
    # splash_pix = QtGui.QPixmap('icons/egads_gui_splashscreen.png')
    # splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # splash.show()
    app.processEvents()
    if not pathlib.Path(pathlib.Path(user_path).joinpath('weather_station.ini')).is_file():
        if not pathlib.Path(user_path).is_dir():
            pathlib.Path(user_path).mkdir()
        create_option_file(user_path)
    config_dict = configparser.ConfigParser()
    config_dict.read(str(pathlib.Path(user_path).joinpath('weather_station.ini')))
    create_logging_handlers(config_dict, 'weather_station.log', user_path)
    logging.info('**********************************')
    logging.info('WEATHER STATION ' + gui_version + ' is starting ...')
    logging.info('**********************************')
    system, release, version = platform.system_alias(platform.system(), platform.release(), platform.version())
    logging.info('gui - operating system: ' + system + ' ' + release + ' (' + version + ')')
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.info('gui - python version: ' + python_version)
    logging.info('gui - pyqt5 version: ' + QtCore.QT_VERSION_STR)
    logging.info('gui - matplotlib version: ' + mpl_version)
    logging.info('gui - markdown version: ' + mk_version)
    logging.info('gui - psycopg2 version: ' + pg_version)
    logging.info('gui - requests version: ' + rq_version)
    if platform.system() == 'Linux':
        logging.info('gui - smbus2 version: ' + bu_version)
        logging.info('gui - bme280 version: ' + bm_version)
    ui = MainWindow(gui_path, user_path, config_dict)
    ui.show()
    # splash.finish(ui)
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    user_path = str(pathlib.Path.home().joinpath('.weather_station'))
    main_path = os.path.abspath(os.path.dirname(__file__))
    launch_station(main_path, user_path)
