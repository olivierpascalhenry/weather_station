import logging
import pathlib
import datetime
import platform
import psycopg2
import subprocess
import configparser
from logging.handlers import RotatingFileHandler
from PyQt5 import QtGui, QtWidgets
from numpy import nan


def create_option_file(user_path):
    ini_file = open(str(pathlib.Path(user_path).joinpath('weather_station.ini')), 'w')
    config_dict = configparser.ConfigParser()
    config_dict.add_section('LOG')
    config_dict.add_section('SYSTEM')
    config_dict.add_section('API')
    config_dict.add_section('DISPLAY')
    config_dict.add_section('SENSOR')
    config_dict.set('LOG', 'level', 'DEBUG')
    config_dict.set('LOG', 'path', str(user_path))
    config_dict.set('SENSOR', 'sensors_rate', '30')
    config_dict.set('SENSOR', 'bme280', 'False')
    config_dict.set('SENSOR', 'ds18b20', 'False')
    config_dict.set('SENSOR', 'mqtt', 'False')
    config_dict.set('DISPLAY', 'in_display_rate', '30')
    config_dict.set('DISPLAY', 'in_sensor', '')
    config_dict.set('DISPLAY', 'out_display_rate', '30')
    config_dict.set('DISPLAY', 'out_sensor', '')
    config_dict.set('SYSTEM', 'place_altitude', '')
    config_dict.set('API', 'api_used', 'meteofrance')
    config_dict.set('API', 'api_key', '')
    config_dict.set('API', 'user_place', 'False')
    config_dict.set('API', 'request_rate', '30')
    config_dict.write(ini_file)
    ini_file.close()


def create_logging_handlers(config_dict, filename, default_path):
    using_default_path = False
    if pathlib.Path(config_dict.get('LOG', 'path')).exists():
        log_filename = str(pathlib.Path(config_dict.get('LOG', 'path')).joinpath(filename))
    else:
        using_default_path = True
        log_filename = str(pathlib.Path(default_path).joinpath(filename))
    logging.getLogger('').handlers = []
    logging.basicConfig(handlers=[RotatingFileHandler(log_filename, maxBytes=2000000, backupCount=5)],
                        level=getattr(logging, config_dict.get('LOG', 'level')),
                        format='%(asctime)s : %(levelname)s : %(message)s')
    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    formatter = logging.Formatter('%(levelname)s : %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    if using_default_path:
        logging.error('gui - logging system - path from ini file not found, using default path')


def check_postgresql_server():
    logging.debug('gui - utils.py - check_postgresql_server')
    installed, database, tables = False, False, False
    if platform.system() == 'Linux':
        res = subprocess.run(['which', '-s', 'psql'])
        if res.returncode == 0:
            installed = True
        else:
            logging.error('gui - utils.py - check_postgresql_server - which -s psql returned 1, postgresql is not '
                          'installed')
    else:
        installed = True
    if installed:
        try:
            connector = psycopg2.connect(user='weather_station', password='31weather64', host='127.0.0.1',
                                         database='weather_station_db', connect_timeout=1)
            database = True
            cursor = connector.cursor()
            cursor.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
            if cursor.fetchall():
                tables = True
            cursor.close()
            connector.close()
        except psycopg2.OperationalError:
            pass
    return installed, database, tables


def clear_layout(layout):
    logging.debug('gui - utils.py - clear_layout')
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        if isinstance(item, QtWidgets.QWidgetItem):
            item.widget().deleteLater()
        elif isinstance(item, QtWidgets.QLayout):
            clear_layout(item.layout())
        layout.removeItem(item)


def icon_creation_function(icon_filename):
    logging.debug('gui - utils.py - icon_creation_function')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(f'icons/{icon_filename}'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap(f'icons/{icon_filename}'), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap(f'icons/{icon_filename}'), QtGui.QIcon.Disabled, QtGui.QIcon.On)
    return icon


def pictogramme_creation_function(icon_filename):
    logging.debug('gui - utils.py - icon_creation_function')
    path = f'graphic_materials/pictogrammes/{icon_filename}'
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon


def font_creation_function(font_style):
    logging.debug('gui - utils.py - font_creation_function')
    font = QtGui.QFont()
    font.setKerning(True)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    font.setFamily("Source Sans Pro")
    if font_style == 'normal':
        font.setPointSize(11)
    elif font_style == 'big':
        font.setFamily("Source Sans Pro Semibold")
        font.setPointSize(11)
    elif font_style == 'small':
        font.setPointSize(10)
    elif font_style == 'small-italic':
        font.setPointSize(10)
        font.setItalic(True)
    elif font_style == 'very_big':
        font.setPointSize(18)
    elif font_style == 'medium_big':
        font.setPointSize(14)
    return font


def stylesheet_creation_function(stylesheet):
    logging.debug('gui - utils.py - stylesheet_creation_function')
    f = open(f'graphic_materials/style_sheets/{stylesheet}_stylesheet.dat', 'r')
    stylesheet_str = ''.join(f.readlines())
    f.close()
    return stylesheet_str


def shadow_creation_function(offset, blur):
    logging.debug('gui - utils.py - shadow_creation_function')
    shadow = QtWidgets.QGraphicsDropShadowEffect()
    shadow.setOffset(offset)
    shadow.setBlurRadius(blur)
    return shadow


def days_months_dictionary():
    logging.debug('gui - utils.py - days_months_dictionary')
    date_dict = {'day': {1: 'Lundi', 2: 'Mardi', 3: 'Mercredi', 4: 'Jeudi', 5: 'Vendredi', 6: 'Samedi', 7: 'Dimanche'},
                 'month': {1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril', 5: 'Mai', 6: 'Juin', 7: 'Juillet',
                           8: 'Août', 9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'}}
    return date_dict


def weather_to_pictogrammes(weather):
    logging.debug('gui - utils.py - weather_to_pictogrammes')
    available_weather = {'Eclaircies': 'eclaircies.svg', 'Très nuageux': 'tres_nuageux.svg',
                         'Ensoleillé': 'ensoleille.svg', 'Risque d\'orages': 'risque_orages.svg',
                         'Nuit claire': 'nuit_claire.svg', 'Couvert': 'couvert.svg',
                         'Rares averses': 'rares_averses.svg', 'Pluies éparses': 'pluies_eparses.svg',
                         'Risque de grèle': 'risque_grele.svg', 'Averses orageuses': 'averses_orageuses.svg',
                         'Brume': 'brume.svg', 'Averses': 'averses.svg', 'Pluie': 'pluie.svg',
                         'Pluies orageuses': 'pluies_orageuses.svg', 'Orages': 'orages.svg',
                         'Ciel voilé': 'ciel_voile.svg', 'Bancs de Brouillard': 'bancs_brouillard.svg',
                         'Brouillard': 'brouillard.svg', 'Brouillard givrant': 'brouillard_givrant.svg'}
    try:
        pictogramme = available_weather[weather]
    except KeyError:
        logging.warning('gui - utils.py - weather_to_pictogrammes - pictogramme is missing : ' + weather)
        pictogramme = ''
    if pictogramme:
        link = f'graphic_materials/pictogrammes/{pictogramme}'
    else:
        link = 'icons/none_icon.png'
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(link), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon


def wind_dir_to_pictogramme(dir_idx):
    logging.debug('gui - utils.py - wind_dir_to_pictogramme')
    path = f'graphic_materials/pictogrammes/wind_dir_images/wind_dir_arrow_{dir_idx}.svg'
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon


def code_to_departement():
    logging.debug('gui - utils.py - code_to_departement')
    code_dict = {
        '01': 'Ain',
        '02': 'Aisne',
        '03': 'Allier',
        '04': 'Alpes-de-Haute-Provence',
        '05': 'Hautes-Alpes',
        '06': 'Alpes-Maritimes',
        '07': 'Ardèche',
        '08': 'Ardennes',
        '09': 'Ariège',
        '10': 'Aube',
        '11': 'Aude',
        '12': 'Aveyron',
        '13': 'Bouches-du-Rhône',
        '14': 'Calvados',
        '15': 'Cantal',
        '16': 'Charente',
        '17': 'Charente-Maritime',
        '18': 'Cher',
        '19': 'Corrèze',
        '2A': 'Corse-du-Sud',
        '2B': 'Haute-Corse',
        '21': 'Côte-d\'Or',
        '22': 'Côtes-d\'Armor',
        '23': 'Creuse',
        '24': 'Dordogne',
        '25': 'Doubs',
        '26': 'Drôme',
        '27': 'Eure',
        '28': 'Eure-et-Loir',
        '29': 'Finistère',
        '30': 'Gard',
        '31': 'Haute-Garonne',
        '32': 'Gers',
        '33': 'Gironde',
        '34': 'Hérault',
        '35': 'Ille-et-Vilaine',
        '36': 'Indre',
        '37': 'Indre-et-Loire',
        '38': 'Isère',
        '39': 'Jura',
        '40': 'Landes',
        '41': 'Loir-et-Cher',
        '42': 'Loire',
        '43': 'Haute-Loire',
        '44': 'Loire-Atlantique',
        '45': 'Loiret',
        '46': 'Lot',
        '47': 'Lot-et-Garonne',
        '48': 'Lozère',
        '49': 'Maine-et-Loire',
        '50': 'Manche',
        '51': 'Marne',
        '52': 'Haute-Marne',
        '53': 'Mayenne',
        '54': 'Meurthe-et-Moselle',
        '55': 'Meuse',
        '56': 'Morbihan',
        '57': 'Moselle',
        '58': 'Nièvre',
        '59': 'Nord',
        '60': 'Oise',
        '61': 'Orne',
        '62': 'Pas-de-Calais',
        '63': 'Puy-de-Dôme',
        '64': 'Pyrénées-Atlantiques',
        '65': 'Hautes-Pyrénées',
        '66': 'Pyrénées-Orientales',
        '67': 'Bas-Rhin',
        '68': 'Haut-Rhin',
        '69': 'Rhône',
        '70': 'Haute-Saône',
        '71': 'Saône-et-Loire',
        '72': 'Sarthe',
        '73': 'Savoie',
        '74': 'Haute-Savoie',
        '75': 'Paris',
        '76': 'Seine-Maritime',
        '77': 'Seine-et-Marne',
        '78': 'Yvelines',
        '79': 'Deux-Sèvres',
        '80': 'Somme',
        '81': 'Tarn',
        '82': 'Tarn-et-Garonne',
        '83': 'Var',
        '84': 'Vaucluse',
        '85': 'Vendée',
        '86': 'Vienne',
        '87': 'Haute-Vienne',
        '88': 'Vosges',
        '89': 'Yonne',
        '90': 'Territoire de Belfort',
        '91': 'Essonne',
        '92': 'Hauts-de-Seine',
        '93': 'Seine-Saint-Denis',
        '94': 'Val-de-Marne',
        '95': 'Val-d\'Oise',
        '971': 'Guadeloupe',
        '972': 'Martinique',
        '973': 'Guyane',
        '974': 'La Réunion',
        '976': 'Mayotte'}
    return code_dict


def mpl_hour_list():
    logging.debug('gui - utils.py - mpl_hour_list')
    now = datetime.datetime.now()
    hours_list = [now]
    for h in range(1, 25, 1):
        new_hour = now - datetime.timedelta(hours=h)
        hours_list.append(new_hour)
    return list(reversed(hours_list))


def db_data_to_mpl_vectors(data):
    logging.debug('gui - utils.py - db_data_to_mpl_vectors')
    t, x = [], []
    for tx in data:
        t.append(tx[0])
        if tx[1] is None:
            x.append(nan)
        else:
            x.append(tx[1])
    return t, x


def set_size(bytes_size):
    logging.debug('gui - utils.py - set_size')
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while bytes_size >= 1024 and i < len(suffixes)-1:
        bytes_size /= 1024.
        i += 1
    f = ('%.2f' % bytes_size).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def battery_value_icon_dict():
    logging.debug('gui - utils.py - battery_value_icon_dict')
    data_dict = {0: 'batterie_0-5_icon.svg', 10: 'batterie_1-5_icon.svg', 30: 'batterie_2-5_icon.svg',
                 50: 'batterie_3-5_icon.svg', 70: 'batterie_4-5_icon.svg', 90: 'batterie_full_icon.svg',
                 101: 'batterie_full_icon.svg'}
    return data_dict


def link_value_icon_dict():
    logging.debug('gui - utils.py - link_value_icon_dict')
    data_dict = {0: 'signal_0-5_icon.svg', 40: 'signal_1-5_icon.svg', 80: 'signal_2-5_icon.svg',
                 120: 'signal_3-5_icon.svg', 160: 'signal_4-5_icon.svg', 200: 'signal_full_icon.svg',
                 256: 'signal_full_icon.svg'}
    return data_dict
