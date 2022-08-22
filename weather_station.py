import os
import sys
import json
import logging
import pathlib
import platform
import configparser
from PyQt5 import QtWidgets, QtCore
from ui.mainwindow import MainWindow
from ui.version import gui_version
from functions.utils import (create_option_file, create_logging_handlers, sync_graphic_folders, create_sensor_file,
                             update_config_file)
from matplotlib import __version__ as mpl_version
from markdown import __version__ as mk_version
from psycopg2 import __version__ as pg_version
from requests import __version__ as rq_version
from pyowm import __version__ as ow_version
from ephem import __version__ as ep_version
if platform.system() == 'Linux':
    from smbus2 import __version__ as bu_version
    from bme280 import __version__ as bm_version
    from paho.mqtt import __version__ as mq_version


def launch_station(gui_path, user_path):
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    if not pathlib.Path(pathlib.Path(user_path).joinpath('weather_station.ini')).is_file():
        if not pathlib.Path(user_path).is_dir():
            pathlib.Path(user_path).mkdir()
        create_option_file(user_path)
    update_config_file(user_path)
    config_dict = configparser.ConfigParser()
    config_dict.read(str(pathlib.Path(user_path).joinpath('weather_station.ini')))
    if not pathlib.Path(pathlib.Path(user_path).joinpath('sensor_file.json')).is_file():
        create_sensor_file(user_path)
    f = open(pathlib.Path(user_path).joinpath('sensor_file.json'), 'r')
    sensor_dict = json.load(f)
    f.close()
    create_logging_handlers(config_dict, 'weather_station.log', user_path)
    if getattr(sys, 'frozen', False):
        frozen = True
    else:
        frozen = False
    logging.info('**********************************')
    logging.info(f'WEATHER STATION {gui_version} is starting ...')
    logging.info('**********************************')
    system, release, version = platform.system_alias(platform.system(), platform.release(), platform.version())
    logging.info(f'gui - operating system: {system} {release} ({version})')
    python_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
    logging.info(f'gui - python version: {python_version}')
    logging.info(f'gui - pyqt5 version: {QtCore.QT_VERSION_STR}')
    logging.info(f'gui - matplotlib version: {mpl_version}')
    logging.info(f'gui - markdown version: {mk_version}')
    logging.info(f'gui - psycopg2 version: {pg_version}')
    logging.info(f'gui - requests version: {rq_version}')
    logging.info(f'gui - pyephem version: {ep_version}')
    logging.info('gui - meteofrance_api version: 1.0.2')
    ow_maj, ow_moy, ow_min = ow_version.constants.PYOWM_VERSION
    logging.info(f'gui - pyowm version: {ow_maj}.{ow_moy}.{ow_min}')
    if platform.system() == 'Linux':
        logging.info(f'gui - smbus2 version: {bu_version}')
        logging.info(f'gui - bme280 version: {bm_version}')
        logging.info(f'gui - paho.mqtt version: {mq_version}')
    logging.info(f'gui - gui frozen ? {frozen}')
    logging.info(f'gui - main path: {gui_path}')
    sync_graphic_folders(gui_path)
    ui = MainWindow(gui_path, user_path, config_dict, sensor_dict)
    ui.show()
    sys.exit(app.exec_())


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical('Uncaught exception', exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


if __name__ == '__main__':
    launch_station(os.path.abspath(os.path.dirname(__file__)), str(pathlib.Path.home().joinpath('.weather_station')))
