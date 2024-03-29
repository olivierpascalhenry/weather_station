import collections
import json
import shutil
import logging
import pathlib
import datetime
import platform
import configparser
from dirsync import sync
from logging.handlers import RotatingFileHandler
from PyQt5 import QtGui, QtWidgets


def create_option_file(user_path):
    config_dict = configparser.ConfigParser()
    config_dict['LOG'] = {'level': 'DEBUG', 'path': str(user_path)}
    config_dict['SYSTEM'] = {'place_altitude': '', 'check_update': 'False', 'auto_check_connexion': 'False',
                             'auto_connexion_unit': 'minutes', 'auto_connexion_value': ''}
    config_dict['API'] = {'api_used': 'meteofrance', 'api_key': '', 'user_place': 'False', 'request_rate': '30'}
    config_dict['DISPLAY'] = {'in_display_rate': '30', 'in_temperature': '', 'in_humidity': '', 'in_pressure': '',
                              'in_msl_pressure': 'False', 'out_display_rate': '30', 'out_temperature': '',
                              'out_humidity': '', 'out_pressure': '', 'out_msl_pressure': 'False', 'in_bat_signal': '',
                              'out_bat_signal': ''}
    config_dict['SENSOR'] = {'sensors_rate': '30'}
    config_dict['TIMESERIES'] = {'in_temperature': '', 'in_humidity': '', 'out_temperature': '', 'out_pressure': '',
                                 'msl_pressure': 'False'}
    config_dict['DATABASE'] = {'port': '', 'username': '', 'password': '', 'database': '', 'host': ''}
    ini_file = open(pathlib.Path(user_path).joinpath('weather_station.ini'), 'w')
    config_dict.write(ini_file)
    ini_file.close()


def update_config_file(user_path):
    ini_path = pathlib.Path(user_path).joinpath('weather_station.ini')
    option_missing, remove_option = False, False
    config_dict = configparser.ConfigParser()
    config_dict.read(ini_path)
    new_option_list = {'SYSTEM': {'auto_check_connexion': 'False',
                                  'auto_connexion_unit': 'minutes',
                                  'auto_connexion_value': ''},
                       'DISPLAY': {'in_temperature': '', 'in_humidity': '', 'in_pressure': '', 'in_bat_signal': '',
                                   'out_temperature': '', 'out_humidity': '', 'out_pressure': '', 'out_bat_signal': ''}}
    old_options_list = {'DISPLAY': ['in_sensor', 'out_sensor']}
    for section, options in new_option_list.items():
        if section not in list(config_dict.keys()):
            option_missing = True
            config_dict[section] = {}
        for option, value in options.items():
            if option not in list(config_dict[section].keys()):
                config_dict[section][option] = value
    for section, options in old_options_list.items():
        for option in options:
            config_dict.remove_option(section, option)
            remove_option = True
            if not config_dict.items(section):
                config_dict.remove_section(section)
    if option_missing or remove_option:
        ini_file = open(ini_path, 'w')
        config_dict.write(ini_file)
        ini_file.close()


def create_sensor_file(user_path):
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    json_dict = {'creation_date': date, 'modification_date': date, 'DS18B20': {}, 'BME280': {},
                 'MQTT': {'username': '', 'password': '', 'address': '', 'port': '', 'main_topics': [], 'devices': {}}}
    f = open(pathlib.Path(user_path).joinpath('sensor_file.json'), 'w')
    json.dump(json_dict, f, indent=4)
    f.close()


def update_sensor_file(user_path):
    f = open(pathlib.Path(user_path).joinpath('sensor_file.json'), 'r')
    json_dict = json.load(f)
    f.close()
    option_missing = False

    if 'port' not in list(json_dict['MQTT'].keys()):
        json_dict['MQTT']['port'] = '1883'
        option_missing = True

    if 'main_topics' not in list(json_dict['MQTT'].keys()):
        json_dict['MQTT']['main_topics'] = ['']
        option_missing = True

    if option_missing:
        f = open(pathlib.Path(user_path).joinpath('sensor_file.json'), 'w')
        json.dump(json_dict, f, indent=4)
        f.close()


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


def sync_graphic_folders(gui_path):
    logging.debug(f'gui - utils.py - sync_graphic_folders - gui_path: {gui_path}')
    if platform.system() == 'Linux':
        path = pathlib.Path().home()
        gui_path = pathlib.Path(gui_path)
        if path.joinpath('icons').exists():
            logging.debug('gui - utils.py - sync_graphic_folders - synchronizing graphic folders')
            sync(str(gui_path.joinpath('icons')), path.joinpath('icons'), 'sync')
            sync(str(gui_path.joinpath('graphic_materials')), path.joinpath('graphic_materials'), 'sync')
        else:
            logging.debug('gui - utils.py - sync_graphic_folders - coping graphic folders')
            shutil.copytree(str(gui_path.joinpath('icons')), path.joinpath('icons'))
            shutil.copytree(str(gui_path.joinpath('graphic_materials')), path.joinpath('graphic_materials'))


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
    logging.debug(f'gui - utils.py - icon_creation_function - icon_filename: {icon_filename}')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(f'icons/{icon_filename}'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap(f'icons/{icon_filename}'), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
    icon.addPixmap(QtGui.QPixmap(f'icons/{icon_filename}'), QtGui.QIcon.Disabled, QtGui.QIcon.On)
    return icon


def pictogramme_creation_function(icon_filename):
    logging.debug(f'gui - utils.py - icon_creation_function - icon_filename: {icon_filename}')
    path = f'graphic_materials/pictogrammes/{icon_filename}'
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon


def font_creation_function(font_style):
    logging.debug(f'gui - utils.py - font_creation_function - font_style: {font_style}')
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
    logging.debug(f'gui - utils.py - stylesheet_creation_function - stylesheet: {stylesheet}')
    f = open(f'graphic_materials/style_sheets/{stylesheet}_stylesheet.dat', 'r')
    stylesheet_str = ''.join(f.readlines())
    f.close()
    return stylesheet_str


def shadow_creation_function(offset, blur):
    logging.debug(f'gui - utils.py - shadow_creation_function - offset: {offset} ; blur: {blur}')
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


def weather_to_pictogrammes(weather, dt=None, sunrise=None, sunset=None):
    logging.debug(f'gui - utils.py - weather_to_pictogrammes - weather: {weather} ; sunrise: {sunrise} ; sunset: '
                  f'{sunset}')
    available_weather = {'Eclaircies': 'eclaircies.svg',
                         'Très nuageux': 'couvert.svg',
                         'Ensoleillé': 'ensoleille.svg',
                         'Risque d\'orages': 'risque_orages.svg',
                         'Nuit claire': 'nuit_claire.svg',
                         'Couvert': 'couvert.svg',
                         'Rares averses': 'rares_averses.svg',
                         'Pluies éparses': 'pluies_eparses.svg',
                         'Risque de grêle': 'risque_grele.svg',
                         'Averses orageuses': 'averses_orageuses.svg',
                         'Brume': 'brume.svg',
                         'Averses': 'pluie.svg',
                         'Pluie': 'pluie.svg',
                         'Pluies orageuses': 'averses_orageuses.svg',
                         'Orages': 'orages.svg',
                         'Ciel voilé': 'ciel_voile.svg',
                         'Bancs de Brouillard': 'brume.svg',
                         'Brouillard': 'brouillard.svg',
                         'Brouillard givrant': 'brouillard_givrant.svg',
                         'Neige': 'neige.svg',
                         'Averses de neige': 'neige.svg',
                         'Pluie et neige': 'pluie_et_neige.svg',
                         'Quelques flocons': 'quelques_flocons.svg'}
    try:
        pictogramme = available_weather[weather]
    except KeyError:
        logging.warning('gui - utils.py - weather_to_pictogrammes - pictogramme is missing : ' + weather)
        pictogramme = ''

    if sunrise is None or sunset is None or dt is None:
        period = 'jour'
    else:
        if isinstance(sunset, list):
            if sunset[0] <= dt <= sunrise[1]:
                period = 'nuit'
            else:
                period = 'jour'
        else:
            if sunrise <= dt <= sunset:
                period = 'jour'
            else:
                period = 'nuit'
    if pictogramme:
        link = f'graphic_materials/pictogrammes/{period}/{pictogramme}'
    else:
        link = 'icons/none_icon.png'
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(link), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    return icon


def openweather_to_mf_desc(item):
    logging.debug(f'gui - utils.py - openweather_to_mf_desc - item : {item}')
    conversion = {'800n': 'Nuit claire', '800d': 'Ensoleillé', '801d': 'Eclaircies', '801n': 'Eclaircies',
                  '802d': 'Très nuageux', '802n': 'Très nuageux', '803d': 'Très nuageux',
                  '803n': 'Très nuageux', '804d': 'Couvert', '804n': 'Couvert', '500d': 'Pluies éparses',
                  '500n': 'Pluies éparses', '501d': 'Pluie', '501n': 'Pluie', '502d': 'Pluie', '502n': 'Pluie',
                  '503d': 'Pluie', '503n': 'Pluie', '504d': 'Pluie', '504n': 'Pluie',
                  '511d': 'Pluies verglaçantes', '511n': 'Pluies verglaçantes',
                  '520d': 'Rares averses', '520n': 'Rares averses', '521d': 'Averses', '521n': 'Averses',
                  '522d': 'Averses', '522n': 'Averses', '531d': 'Averses', '531n': 'Averses',
                  '701d': 'Brume', '701n': 'Brume', '711d': 'Brouillard', '711n': 'Brouillard',
                  '721d': 'Brouillard', '721n': 'Brouillard', '731d': 'Brouillard', '731n': 'Brouillard',
                  '741d': 'Brouillard', '741n': 'Brouillard', '751d': 'Brouillard', '751n': 'Brouillard',
                  '761d': 'Brouillard', '761n': 'Brouillard', '762d': 'Brouillard', '762n': 'Brouillard',
                  '771d': 'Brouillard', '771n': 'Brouillard', '781d': 'Brouillard', '781n': 'Brouillard',
                  '200d': 'Pluies orageuses', '200n': 'Pluies orageuses', '201d': 'Averses orageuses',
                  '201n': 'Averses orageuses', '202d': 'Averses orageuses', '202n': 'Averses orageuses',
                  '210d': 'Risque d\'orages', '210n': 'Risque d\'orages', '211d': 'Orages', '211n': 'Orages',
                  '212d': 'Orages', '212n': 'Orages', '221d': 'Orages', '221n': 'Orages',
                  '230d': 'Risque de grèle', '230n': 'Risque de grèle', '231d': 'Risque de grèle',
                  '231n': 'Risque de grèle', '232d': 'Risque de grèle', '232n': 'Risque de grèle',
                  '300d': 'Averses', '300n': 'Averses', '301d': 'Averses', '301n': 'Averses',
                  '302d': 'Averses', '302n': 'Averses', '310d': 'Averses', '310n': 'Averses',
                  '311d': 'Averses', '311n': 'Averses', '312d': 'Averses', '312n': 'Averses',
                  '313d': 'Averses', '313n': 'Averses', '314d': 'Averses', '314n': 'Averses',
                  '321d': 'Averses', '321n': 'Averses', '600d': 'Neige', '601d': 'Neige', '602d': 'Neige',
                  '611d': 'Pluie et neige', '612d': 'Pluie et neige', '613d': 'Pluie et neige',
                  '615d': 'Pluie et neige', '616d': 'Pluie et neige', '621d': 'Neige', '622d': 'Neige',
                  '623d': 'Neige', '600n': 'Neige', '601n': 'Neige', '602n': 'Neige', '611n': 'Pluie et neige',
                  '612n': 'Pluie et neige',  '613n': 'Pluie et neige', '615n': 'Pluie et neige',
                  '616n': 'Pluie et neige', '621n': 'Neige', '622n': 'Neige', '623n': 'Neige'}

    try:
        weather = conversion[item]
    except KeyError:
        weather = 'none'
    return weather


def wind_dir_to_pictogramme(dir_idx):
    logging.debug(f'gui - utils.py - wind_dir_to_pictogramme - dir_idx: {dir_idx}')
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


def define_time_ticks(now):
    tick_list, label_list = [], []
    i = 0
    for hour in reversed(list(range(1, 25, 1))):
        tick_list.append(now - datetime.timedelta(hours=hour))
        if i == 0:
            label_list.append(f'-{hour}h')
        else:
            label_list.append('')
        i += 1
        if i == 4:
            i = 0
    tick_list.append(now)
    label_list.append('Now')
    return tick_list, label_list


def set_size(bytes_size):
    logging.debug('gui - utils.py - set_size')
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while bytes_size >= 1024 and i < len(suffixes) - 1:
        bytes_size /= 1024.
        i += 1
    f = ('%.2f' % bytes_size).rstrip('0').rstrip('.')
    idx = f.find('.')
    if idx >= 0:
        if len(f[idx:]) == 2:
            f += '0'
        elif len(f[idx:]) == 1:
            f += '00'
    else:
        f += '.00'
    return f'{f} {suffixes[i]}'


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


def angle_moon_phase():
    logging.debug('gui - utils.py - angle_moon_phase')
    angle_dict = collections.OrderedDict()
    angle_dict[0.] = 'wi-moon-alt-new.svg'
    angle_dict[6.428571] = 'wi-moon-alt-waning-crescent-6.svg'
    angle_dict[19.285713] = 'wi-moon-alt-waning-crescent-5.svg'
    angle_dict[32.142855] = 'wi-moon-alt-waning-crescent-4.svg'
    angle_dict[44.999997] = 'wi-moon-alt-waning-crescent-3.svg'
    angle_dict[57.857138] = 'wi-moon-alt-waning-crescent-2.svg'
    angle_dict[70.714281] = 'wi-moon-alt-waning-crescent-1.svg'
    angle_dict[83.571423] = 'wi-moon-alt-third-quarter.svg'
    angle_dict[96.428565] = 'wi-moon-alt-waning-gibbous-6.svg'
    angle_dict[109.285707] = 'wi-moon-alt-waning-gibbous-5.svg'
    angle_dict[122.142849] = 'wi-moon-alt-waning-gibbous-4.svg'
    angle_dict[134.999991] = 'wi-moon-alt-waning-gibbous-3.svg'
    angle_dict[147.857133] = 'wi-moon-alt-waning-gibbous-2.svg'
    angle_dict[160.714275] = 'wi-moon-alt-waning-gibbous-1.svg'
    angle_dict[173.571417] = 'wi-moon-alt-full.svg'
    angle_dict[186.428559] = 'wi-moon-alt-waxing-gibbous-6.svg'
    angle_dict[199.285701] = 'wi-moon-alt-waxing-gibbous-5.svg'
    angle_dict[212.142843] = 'wi-moon-alt-waxing-gibbous-4.svg'
    angle_dict[224.999985] = 'wi-moon-alt-waxing-gibbous-3.svg'
    angle_dict[237.857127] = 'wi-moon-alt-waxing-gibbous-2.svg'
    angle_dict[250.714269] = 'wi-moon-alt-waxing-gibbous-1.svg'
    angle_dict[263.571411] = 'wi-moon-alt-first-quarter.svg'
    angle_dict[276.428553] = 'wi-moon-alt-waxing-crescent-6.svg'
    angle_dict[289.285695] = 'wi-moon-alt-waxing-crescent-5.svg'
    angle_dict[302.142837] = 'wi-moon-alt-waxing-crescent-4.svg'
    angle_dict[314.999979] = 'wi-moon-alt-waxing-crescent-3.svg'
    angle_dict[327.857121] = 'wi-moon-alt-waxing-crescent-2.svg'
    angle_dict[340.714263] = 'wi-moon-alt-waxing-crescent-1.svg'
    angle_dict[353.571405] = 'wi-moon-alt-new.svg'
    angle_dict[360.] = None
    return angle_dict


def get_season(dt):
    logging.debug(f'gui - utils.py - get_season - dt: {dt}')
    if isinstance(dt, datetime.datetime):
        dt = dt.date()
    y = dt.year
    seasons = [('Hiver', (datetime.date(y, 1, 1), datetime.date(y, 3, 20))),
               ('Printemps', (datetime.date(y, 3, 21), datetime.date(y, 6, 20))),
               ('Eté', (datetime.date(y, 6, 21), datetime.date(y, 9, 22))),
               ('Automne', (datetime.date(y, 9, 23), datetime.date(y, 12, 20))),
               ('Hiver', (datetime.date(y, 12, 21), datetime.date(y, 12, 31)))]
    return next(season for season, (start, end) in seasons if start <= dt <= end)


def str2bool(string):
    logging.debug(f'gui - utils.py - str2bool - string: {string}')
    if string == 'True':
        return True
    elif string == 'False':
        return False
    else:
        raise ValueError
