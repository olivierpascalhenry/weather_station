import time
import logging
import collections
import datetime
import meteofrance_api
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from functions.utils import days_months_dictionary, openweather_to_mf_desc


from PyQt5 import QtCore


class MFForecastRequest(QtCore.QThread):
    fc_data = QtCore.pyqtSignal(dict)

    def __init__(self, user_place, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - forecast_resquest.py - MFForecastRequest - __init__')
        self.user_place = user_place
        self.request_rate = int(config_dict.get('API', 'request_rate')) * 60
        self.forecast = {'api': 'meteofrance'}

    def run(self):
        logging.debug('gui - forecast_resquest.py - MFForecastRequest - run')
        while True:
            try:
                mf_client = meteofrance_api.MeteoFranceClient()
                place_forecast = mf_client.get_forecast_for_place(self.user_place['object'])
                place_warning = mf_client.get_warning_current_phenomenoms(self.user_place['object'].admin2)
                fc_1h = collections.OrderedDict()
                now = datetime.datetime.now().replace(minute=0, second=0)
                limite = now + datetime.timedelta(hours=24)
                for i, forecast in enumerate(place_forecast.forecast):
                    dt = datetime.datetime.utcfromtimestamp(forecast['dt'])
                    if now <= dt <= limite:
                        fc_1h[dt] = {'datetime': dt,
                                     'temp': forecast['T']['value'],
                                     'hum': forecast['humidity'],
                                     'pres': forecast['sea_level'],
                                     'w_spd': forecast['wind']['speed'],
                                     'w_dir': forecast['wind']['direction'],
                                     'w_gst': forecast['wind']['gust'],
                                     'rain': forecast['rain']['1h'],
                                     'snow': forecast['snow']['1h'],
                                     'weather': forecast['weather']['desc'],
                                     'cover': forecast['clouds']}
                    if dt > limite:
                        break
                self.forecast['hourly'] = fc_1h

                fc_6h = collections.OrderedDict()
                dt = (datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                      + datetime.timedelta(days=1))
                day_time_list = [dt]
                for i in range(19):
                    dt += datetime.timedelta(hours=6)
                    day_time_list.append(dt)

                forecast_next = place_forecast.forecast
                forecast_dt = [datetime.datetime.utcfromtimestamp(forecast['dt']) for forecast in forecast_next]
                occurences = [i for i, item in enumerate(forecast_dt) if item in set(day_time_list)]
                for idx in occurences:
                    forecast = forecast_next[idx]
                    dt = datetime.datetime.utcfromtimestamp(forecast['dt'])
                    fc_6h[dt] = {'datetime': dt,
                                 'temp': forecast['T']['value'],
                                 'hum': forecast['humidity'],
                                 'pres': forecast['sea_level'],
                                 'w_spd': forecast['wind']['speed'],
                                 'w_dir': forecast['wind']['direction'],
                                 'w_gst': forecast['wind']['gust'],
                                 'weather': forecast['weather']['desc'],
                                 'cover': forecast['clouds']}

                self.forecast['quaterly'] = fc_6h

                warn_str = ''
                warn_bool = False
                for warn in place_warning.phenomenons_max_colors:
                    color_id, phenomenon_id = warn['phenomenon_max_color_id'], warn['phenomenon_id']
                    if color_id >= 3:
                        warn_bool = True
                        color = meteofrance_api.helpers.get_warning_text_status_from_indice_color(color_id)
                        phenomenon = meteofrance_api.helpers.get_phenomenon_name_from_indice(phenomenon_id)
                        warn_str += f'Alerte {color} pour {phenomenon}\n\n'

                if warn_bool:
                    dt = datetime.datetime.utcfromtimestamp(place_warning.end_validity_time)
                    date = (days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day) + ' '
                            + days_months_dictionary()['month'][dt.month] + ' ' + str(dt.year))
                    hour = dt.strftime('%Hh%M')
                    warn_str += f'Fin de l\'alerte : à {hour}, le {date}'
                    self.forecast['warning'] = warn_str
                else:
                    self.forecast['warning'] = ''

                self.fc_data.emit(self.forecast)
            except Exception:
                logging.exception('gui - forecast_resquest.py - MFForecastRequest - run - an issue occured during'
                                  'the request of MF forecasts')
            time.sleep(self.request_rate)

    def stop(self):
        logging.debug('gui - forecast_resquest.py - MFForecastRequest - stop')
        self.terminate()
        logging.debug('gui - forecast_resquest.py - MFForecastRequest - stop - terminate')


class OWForecastRequest(QtCore.QThread):
    fc_data = QtCore.pyqtSignal(dict)

    def __init__(self, user_place, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - forecast_resquest.py - OWForecastRequest - __init__')
        self.user_place = user_place
        self.request_rate = int(config_dict.get('API', 'request_rate')) * 60
        self.api_key = config_dict.get('API', 'api_key')
        self.forecast = {'api': 'openweather', 'warning': ''}

    def run(self):
        logging.debug('gui - forecast_resquest.py - OWForecastRequest - run')
        while True:
            try:
                config_dict = get_default_config()
                config_dict['language'] = 'fr'
                owm = OWM(self.api_key)
                mgr = owm.weather_manager()
                one_call = mgr.one_call(lon=self.user_place['longitude'], lat=self.user_place['latitude'],
                                        exclude='minutely', units='metric')
                fc_1h = collections.OrderedDict()
                now = datetime.datetime.now().replace(minute=0, second=0)
                limite = now + datetime.timedelta(hours=24)
                for i, fc in enumerate(one_call.forecast_hourly):
                    dt = datetime.datetime.utcfromtimestamp(fc.reference_time())
                    if now <= dt <= limite:
                        if fc.rain:
                            try:
                                rain = fc.rain['1h']
                            except Exception:
                                rain = 0
                        else:
                            rain = 0
                        weather = openweather_to_mf_desc(str(fc.weather_code) + fc.weather_icon_name[-1:])
                        fc_1h[dt] = {'datetime': dt,
                                     'temp': fc.temperature()['temp'],
                                     'hum': fc.humidity,
                                     'pres': fc.pressure['press'],
                                     'w_spd': fc.wnd['speed'],
                                     'w_dir': fc.wnd['deg'],
                                     'w_gst': fc.wnd['gust'],
                                     'rain': rain,
                                     'snow': fc.snow,
                                     'weather': weather,
                                     'cover': fc.clouds}
                    if dt > limite:
                        break
                self.forecast['hourly'] = fc_1h

                fc_6h = collections.OrderedDict()
                for i, fc in enumerate(one_call.forecast_daily):
                    dt = datetime.datetime.utcfromtimestamp(fc.reference_time())
                    if now.replace(hour=0) < dt.replace(hour=0) <= now.replace(hour=0) + datetime.timedelta(days=5):
                        weather = openweather_to_mf_desc(str(fc.weather_code) + fc.weather_icon_name[-1:])
                        if fc.rain:
                            try:
                                rain = fc.rain['all']
                            except Exception:
                                rain = 0
                        else:
                            rain = 0
                        fc_6h[dt] = {'datetime': dt,
                                     'temp': {'min': fc.temperature()['min'], 'max': fc.temperature()['max']},
                                     'hum': fc.humidity,
                                     'pres': fc.pressure['press'],
                                     'w_spd': fc.wnd['speed'],
                                     'w_dir': fc.wnd['deg'],
                                     'w_gst': fc.wnd['gust'],
                                     'weather': weather,
                                     'cover': fc.clouds,
                                     'rain': rain}

                self.forecast['quaterly'] = fc_6h
                self.fc_data.emit(self.forecast)
            except Exception:
                logging.exception('gui - forecast_resquest.py - OWForecastRequest - run - an issue occured during'
                                  'the request of OWM forecasts')
            time.sleep(self.request_rate)

    def stop(self):
        logging.debug('gui - forecast_resquest.py - OWForecastRequest - stop')
        self.terminate()
        logging.debug('gui - forecast_resquest.py - OWForecastRequest - stop - terminate')
