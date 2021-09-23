#!/usr/bin/env python3

import psutil
import tarfile
import sys
import time
import os
import signal
import shutil
import tempfile
import logging
import pathlib
import distutils.dir_util


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


logging.getLogger('').handlers = []
logging.basicConfig(filename='weather_station_updater_log.out',
                    level=getattr(logging, 'INFO'),
                    filemode='w',
                    format='%(asctime)s : %(levelname)s : %(message)s')


logging.info('********************************************')
logging.info('WEATHER STATION update is starting ...')
logging.info('********************************************')

zip_file = sys.argv[1]
dest_folder = pathlib.Path(sys.argv[2])
tmp_folder = pathlib.Path(tempfile.gettempdir()).joinpath('weather_station')
success = True
logging.info('zip file: ' + zip_file)
logging.info('destination folder: ' + str(dest_folder))
logging.info('temporary folder: ' + str(tmp_folder))

print('')
print('--------------------------------------------------------------------')
print('---- An update is going to be installed for the weather station ----')
print('------ Do not close the terminal until the end of the process ------')
print('--------------------------------------------------------------------')
print('')
print('File to unzip:\t\t' + zip_file)
print('Destination folder:\t' + str(dest_folder))
print('')
print('WEATHER STATION is closing, waiting...')


while True:
    running = False
    retry = 0
    error = False
    for proc in psutil.process_iter():
        if proc.name().lower() == 'weather_station':
            running = True
            logging.info('weather_station still running...')

    if running:
        time.sleep(0.25)
        retry += 1
        if retry > 20:
            error = True
            break
    else:
        break

if error:
    logging.info('weather_station still running, time out, an error occurred')
    print('')
    print('An error occured and WEATHER STATION couldn\'t be closed. Please check if WEATHER STATION is still '
          'running and start the update procedure again. If the update process fails again, contact the developer.')
    time.sleep(15)
else:
    logging.info('weather_station has been closed')
    print('WEATHER STATION closed')
    print('')
    print('Uncompressing update...')
    logging.info('uncompressing starting...')

    try:
        tar = tarfile.open(zip_file, "r:gz")
        tar.extractall(path=tempfile.gettempdir())
        tar.close()
        logging.info('uncompressing finished...')
    except Exception:
        success = False
        logging.exception('an exception occured during uncompressing')

    print('')
    print('Installing update...')
    logging.info('installing update...')

    try:
        for f in tmp_folder.iterdir():
            logging.info('---> ' + str(f))
            if f.is_dir():
                distutils.dir_util.copy_tree(str(f), str(dest_folder.joinpath(f.name)))
            else:
                shutil.move(f, dest_folder.joinpath(f.name))
        logging.info('installation finished...')
    except Exception:
        success = False
        logging.exception('an exception occured during installation')

    print('')
    print('Cleaning...')
    logging.info('cleaning...')

    try:
        shutil.rmtree(tmp_folder)
        logging.info('cleaning finished...')
    except Exception:
        success = False
        logging.exception('an exception occurred during cleaning')

    print('')
    print('End of the process...')
    print('')
    if not success:
        print('Something went wrong during the installation of the update. Please check the log file.')
    logging.info('end of the process...')
    print('Raspberry will reboot in 5 seconds')
    time.sleep(5)
    logging.info('raspberry rebooting...')

    os.system('sudo shutdown -r now')
