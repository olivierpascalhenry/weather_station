Project Overview:
-----------------

This project comes from the idea to propose an "out-of-the-box" system, as complete as possible, in both the management of different sensors and the implementation of different weather APIs. In this way, an ensemble of meteorological and local variables are centralised in a Raspberry PI (preferably a 4b with 4GB or more RAM), as well as different forecasts produced by public (ex: Météo-France) or private (ex: OpenWeather) entities.


More Information:
-----------------

The weather station is coded with Python 3.9 and relies on few technologies such as PostgreSQL, MQTT and Zigbee2MQTT.
It has been tested on a Raspberry PI 4b with Buster and Bullseye Raspberry PI OS.
Few APIs have been included : Météo-France and OpenWeatherMap. More will come in the future.
Few sensors are handled by the weather station : DS18B20 (one or more) and BME280 (one or more), through 1-wire and I2C buses. More will come in the future, once I can get my hand on them.
The main language of the software is French. English will be added once the full code is stable.


Features:
---------

* ephemeris of the day
* management of 1-Wire sensors (for now : DS18B20)
* management of I2C sensors (for now : BME280)
* management of MQTT-based sensors (temperature, humidity, pressure, battery and signal quality)
* management of weather APIs (for now : Météo-France, OpenWeatherMap)
* two different forecasts are handled : 1h forecasts and 6h/1day forecasts.
* forecasts are based on localisation (must be entered by the user)
* data are displayed as real time measurements and as times series on 24h.


Developments:
-------------

Develoments are made on my free time. As said above, the weather station software has been coded with Python 3.7, and thus it is pure Python. The GUI is handled by PyQt 5.15 and designed with QtCreator 5.0. The latest version of PyCharm is used to develop the software.


Installation:
-------------

The weather station system is a pure python script. Thus it can be used from a terminal, with the simple command : python3 weather_station.py.
At the present time, it is launched by *pi* user, but it can be used by any user as long as all rights have been set.

For developments or to run it as a script, it needs few dependancies.

Operating systems :

* Raspberry PI OS Buster

  or

* Raspberry PI OS Bullseye

Python modules :

* Python (3.7+)
* PyQt5 (5.15.0+)
* numpy (1.19.5+)
* matplotlib (3.3.0+)
* markdown (3.3.0+)
* requests (2.25.0+)
* psycopg2 (2.8.6+)
* pyowm (3.2.0+)
* meteofrance-api (1.0.2+)
* smbus2 (0.4.1+)
* RPi.bme280 (0.2.4+)
* paho.mqtt (1.6.1+)
* pigpio (1.78+) -> pigpiod service must me enabled
* pyephem (4.1.3+)
* pyqtspinner (0.1.1+)
* dirsync (2.2.5 +)

Other software :

* PostgreSQL (13.5+)
* Mosquitto (2.0.11+)
* Zigbee2Mqtt (1.24.0)

Fonts :

The weather station uses Source Sans Pro as a font. It needs to be installed to give better results.

Stand-alone package:
--------------------

A stand-alone package is compiled using PyInstaller. Thus, a Python installation is not necessary. In that case, only PostgreSQL, Mosquitto and Zigbee2Mqtt are mandatory.

The weather station uses Source Sans Pro as a font. It needs to be installed to give better results.

Specific configuration for PostgreSQL, Mosquitto and Zigbee2Mqtt
----------------------------------------------------------------

For PosgreSQL, the following configuration must be used :

* a specific database must be created for the weather station with a dedicated user.
* read/write privileges on the database must be granted to the user.
* user, password, database and address must be entered in the Weather Station options.
* tables will be handled by the Weather Station.

For Mosquitto and Zigbee2Mqtt :

* the installation of Mosquitto and Zigbee2Mqtt have to be handled by the user. 
* the Weather Station uses a username, password, address and a maintopic (ex: zigbee2mqtt) to connect to mosquitto and subscribe to Zigbee2Mqtt topics. Thus the user must configure Mosquitto and Zigbee2Mqtt accordingly. The port in use is the default one.
* variables retrieve from Mosquitto through Zigbee2Mqtt must be set this way :
  * for each variable : MQTT/[maintopic]/[device]/[variable]
  * for exemple, temperature : MQTT/zigbee2mqtt/[device]/temperature
  * the [device] can be its serial number or its friendly name as set in Zigbee2Mqtt configuration file
* read the Zigbee2Mqtt documentation for a better explanation ;o) !


Sensors
-------

Currently, only BME280 and DS18B20 are officialy supported and tested. More will be supported once I can put my hand on them.
Sensors relying on MQTT to send and store data are supported if each variable has its own topic. At this time, only temperature, humidity, pressure, battery and signal quality are used by the weather station.


Limitations
-----------

The GUI has been developed on a raspberry pi 4 connected to a Waveshare 7" monitor (https://www.waveshare.com/product/raspberry-pi/displays/7inch-hdmi-lcd-c.htm?___SID=U) and is not responsive (lack of knowledge from the 
developer). Thus it can't adapt automatically to different screen size. It will be adapted in the next major version.

As the GUI is intended to be used with a touch screen, the mouse cursor is hidden on a linux system for all windows.

I found an issue between PyQt5, stylesheet and raspberry pi. Stylesheet and icons are not applied until those files are stored in the home directory of the user. That's why a sync function has been introduced to copy all icons and stylesheets in the home directory and keep those folders in sync. Once a proper solution is found, that limitation will be removed.


Documentation:
--------------

At this time, there is no documentation yet.


Screenshots:
------------

![Sensor parameters](screenshots/screenshot_1.png?raw=true "Parameters from different sensors") 

![Sensor time series](screenshots/screenshot_4.png?raw=true "Parameters can be displayed as time series")

![1h forecast](screenshots/screenshot_2.png?raw=true "Forecast every 1h on a 24h period")

![1d forecast](screenshots/screenshot_3.png?raw=true "Forecast every day on a 5d period")

(displayed parameters are randomly generated for development purpose)
