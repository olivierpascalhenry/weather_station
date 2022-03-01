import time
import logging
import collections
import datetime
import meteofrance_api
from functions.utils import days_months_dictionary


from PyQt5 import QtCore


class MFForecastRequest(QtCore.QThread):
    fc_data = QtCore.pyqtSignal(dict)
    error = QtCore.pyqtSignal(list)

    def __init__(self, user_place, config_dict):
        QtCore.QThread.__init__(self)
        logging.info('gui - forecast_resquest.py - MFForecastRequest - __init__')
        self.user_place = user_place
        self.request_rate = int(config_dict.get('API', 'request_rate')) * 60
        self.forecast = {}

    def run(self):
        logging.debug('gui - forecast_resquest.py - MFForecastRequest - run')
        # {'dt': 1629644400, 'T': {'value': 26.3, 'windchill': 29.9}, 'humidity': 50, 'sea_level': 1022.3,
        # 'wind': {'speed': 4, 'gust': 0, 'direction': 315, 'icon': 'NO'}, 'rain': {'1h': 0}, 'snow': {'1h': 0},
        # 'iso0': 4350, 'rain snow limit': 'Non pertinent', 'clouds': 70, 'weather': {'icon': 'p2j',
        # 'desc': 'Eclaircies'}}
        while True:
            try:
                mf_client = meteofrance_api.MeteoFranceClient()
                place_forecast = mf_client.get_forecast_for_place(self.user_place)
                place_warning = mf_client.get_warning_current_phenomenoms(self.user_place.admin2)
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
                                     'rain_test': float(forecast['rain']['1h']) * 100,
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
                        warn_str += 'Alerte {color} pour {phenomenon}\n\n'.format(color=color, phenomenon=phenomenon)

                if warn_bool:
                    dt = datetime.datetime.utcfromtimestamp(place_warning.end_validity_time)
                    date = (days_months_dictionary()['day'][dt.weekday() + 1] + ' ' + str(dt.day) + ' '
                            + days_months_dictionary()['month'][dt.month] + ' ' + str(dt.year))
                    hour = dt.strftime('%Hh%M')
                    warn_str += 'Fin de l\'alerte : à {hour}, le {date}'.format(hour=hour, date=date)
                    self.forecast['warning'] = warn_str
                else:
                    self.forecast['warning'] = ''

                self.fc_data.emit(self.forecast)
            except Exception as e:
                self.error.emit(['forecast request', e])
            time.sleep(self.request_rate)

    def stop(self):
        logging.debug('gui - forecast_resquest.py - MFForecastRequest - stop')
        self.terminate()
