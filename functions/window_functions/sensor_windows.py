import logging
import platform
import pathlib

from PyQt5 import QtCore, QtWidgets, QtGui
from ui.Ui_mqttmanagerwindow import Ui_mqttmanagerWindow
from ui.Ui_1wiremanagerwindow import Ui_sensormanagerWindow
from ui.Ui_townsearchwindow import Ui_townsearchWindow
from functions.window_functions.other_windows import MyKeyboard, MyNumpad
from functions.utils import code_to_departement, stylesheet_creation_function, font_creation_function
if platform.system() == 'Linux':
    import pigpio


class MqttManager(QtWidgets.QDialog, Ui_mqttmanagerWindow):
    def __init__(self, mqtt_dict, parent=None):
        logging.info('gui - other_windows.py - MqttManager - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((parent.width() - self.width()) / 2), int((parent.height() - self.height()) / 2))
        self.cancel = True
        self.mqtt_dict = mqtt_dict
        self.cancel_button.clicked.connect(self.close_window)
        self.ok_button.clicked.connect(self.confirm_device_dict)
        self.sensor_list.itemClicked.connect(self.show_device_information)
        self.add_sensor.clicked.connect(self.add_device)
        self.del_sensor.clicked.connect(self.del_device)
        self.username_ln.textChanged.connect(self.add_text_to_dict)
        self.password_ln.textChanged.connect(self.add_text_to_dict)
        self.address_ln.textChanged.connect(self.add_text_to_dict)
        self.main_topic_ln.textChanged.connect(self.add_text_to_dict)
        self.temperature_ln.textChanged.connect(self.add_text_to_dict)
        self.humidity_ln.textChanged.connect(self.add_text_to_dict)
        self.pressure_ln.textChanged.connect(self.add_text_to_dict)
        self.battery_ln.textChanged.connect(self.add_text_to_dict)
        self.signal_ln.textChanged.connect(self.add_text_to_dict)
        for button in self.findChildren(QtWidgets.QToolButton):
            if button.objectName()[: 3] not in ['del', 'add', 'ok_', 'can']:
                button.clicked.connect(self.display_keyboard)
        self.parse_mqtt_dict()

    def parse_mqtt_dict(self):
        logging.debug('gui - other_windows.py - MqttManager - parse_mqtt_dict')
        self.username_ln.setText(self.mqtt_dict['username'])
        self.password_ln.setText(self.mqtt_dict['password'])
        self.address_ln.setText(self.mqtt_dict['address'])
        self.main_topic_ln.setText(self.mqtt_dict['main_topic'])
        for device, ddict in self.mqtt_dict['devices'].items():
            self.sensor_list.addItem(device)

    def show_device_information(self, item):
        logging.debug('gui - other_windows.py - MqttManager - show_device_information')
        self.del_sensor.setEnabled(True)
        self.temperature_ln.setEnabled(True)
        self.pressure_ln.setEnabled(True)
        self.humidity_ln.setEnabled(True)
        self.battery_ln.setEnabled(True)
        self.signal_ln.setEnabled(True)
        self.temperature_ln.setText(self.mqtt_dict['devices'][item.text()]['temperature'])
        self.pressure_ln.setText(self.mqtt_dict['devices'][item.text()]['pressure'])
        self.humidity_ln.setText(self.mqtt_dict['devices'][item.text()]['humidity'])
        self.battery_ln.setText(self.mqtt_dict['devices'][item.text()]['battery'])
        self.signal_ln.setText(self.mqtt_dict['devices'][item.text()]['signal'])
        self.temperature_bt.setEnabled(True)
        self.pressure_bt.setEnabled(True)
        self.humidity_bt.setEnabled(True)
        self.battery_bt.setEnabled(True)
        self.signal_bt.setEnabled(True)

    def add_device(self):
        logging.debug('gui - other_windows.py - MqttManager - add_device')
        keyboard_window = MyKeyboard(self)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            name = str(keyboard_window.num_line.text())
            if not self.sensor_list.findItems(name, QtCore.Qt.MatchFixedString):
                self.sensor_list.addItem(name)
                tmp_dict = {'temperature': '', 'humidity': '', 'pressure': '', 'battery': '', 'signal': ''}
                self.mqtt_dict['devices'][name] = tmp_dict

    def del_device(self):
        logging.debug('gui - other_windows.py - MqttManager - del_device')
        item = self.sensor_list.takeItem(self.sensor_list.currentRow())
        del self.mqtt_dict['devices'][item.text()]
        if not self.sensor_list.selectedItems():
            self.del_sensor.setEnabled(False)
            self.temperature_ln.setEnabled(False)
            self.pressure_ln.setEnabled(False)
            self.humidity_ln.setEnabled(False)
            self.battery_ln.setEnabled(False)
            self.signal_ln.setEnabled(False)
            self.temperature_bt.setEnabled(False)
            self.pressure_bt.setEnabled(False)
            self.humidity_bt.setEnabled(False)
            self.battery_bt.setEnabled(False)
            self.signal_bt.setEnabled(False)
            self.temperature_ln.setText('')
            self.pressure_ln.setText('')
            self.humidity_ln.setText('')
            self.battery_ln.setText('')
            self.signal_ln.setText('')
        else:
            self.show_device_information(self.sensor_list.currentItem())

    def add_text_to_dict(self):
        logging.debug('gui - other_windows.py - MqttManager - add_text_to_dict')
        try:
            if self.sender().objectName()[: -3] in ['temperature', 'humidity', 'pressure', 'battery', 'signal']:
                device = str(self.sensor_list.currentItem().text())
                self.mqtt_dict['devices'][device][self.sender().objectName()[: -3]] = str(self.sender().text())
            else:
                self.mqtt_dict[self.sender().objectName()[: -3]] = str(self.sender().text())
        except AttributeError:
            pass

    def display_keyboard(self):
        logging.debug('gui - other_windows.py - MqttManager - display_keyboard')
        lineedit = self.findChild(QtWidgets.QLineEdit, self.sender().objectName()[: -2] + 'ln')
        keyboard_window = MyKeyboard(self)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            lineedit.setText(keyboard_window.num_line.text())

    def confirm_device_dict(self):
        logging.debug('gui - other_windows.py - MqttManager - confirm_device_dict')
        self.cancel = False
        self.close_window()

    def close_window(self):
        logging.debug('gui - other_windows.py - MqttManager - close_window')
        self.close()


class W1SensorManager(QtWidgets.QDialog, Ui_sensormanagerWindow):
    def __init__(self, sensor_dict, parent=None):
        logging.debug('gui - sensor_window.py - W1SensorManager - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mainparent = parent
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.splitter.setSizes([270, 508])  # 778
        self.cancel = True
        self.sensor_dict = sensor_dict
        self.section_list.itemClicked.connect(self.display_information)
        self.section_list.itemClicked.connect(self.activate_delete_button)
        self.cancel_button.clicked.connect(self.close_window)
        self.ok_button.clicked.connect(self.save_sensor_dict)
        self.name_bt.clicked.connect(self.display_keyboard)
        self.table_bt.clicked.connect(self.display_keyboard)
        self.refresh_bt.clicked.connect(self.display_numpad)
        self.store_bt.clicked.connect(self.display_numpad)
        self.add_sensor.clicked.connect(self.display_available_sensors)
        self.del_sensor.clicked.connect(self.delete_sensor)
        self.name_ln.textChanged.connect(self.set_sensor_dict_info)
        self.refresh_ln.textChanged.connect(self.set_sensor_dict_info)
        self.table_ln.textChanged.connect(self.set_sensor_dict_info)
        self.store_ln.textChanged.connect(self.set_sensor_dict_info)
        self.parse_sensor_dict()

    def parse_sensor_dict(self):
        for sensor, _ in self.sensor_dict.items():
            widget = QtWidgets.QListWidgetItem()
            widget.setText(sensor)
            self.section_list.addItem(widget)

    def display_available_sensors(self):
        if platform.system() == 'Linux':
            path = pathlib.Path('/sys/bus/w1/devices')
        else:
            path = pathlib.Path('D:\\Travail\\Developement\\files\\sys_bus_w1_devices')
        sensor_list = [item.name for item in path.glob('*') if item.name != 'w1_bus_master1']
        registered_list = [self.section_list.item(idx).text() for idx in range(self.section_list.count())]
        sensor_window = AvailableSensorsWindow(sensor_list, self.mainparent)
        sensor_window.exec_()
        if not sensor_window.cancel:
            if sensor_window.sensor not in registered_list:
                widget = QtWidgets.QListWidgetItem()
                widget.setText(sensor_window.sensor)
                self.section_list.addItem(widget)
                self.sensor_dict[sensor_window.sensor] = {'name': '', 'table': '', 'refresh': 30, 'store': 24,
                                                          'id': sensor_window.sensor}

    def delete_sensor(self):
        item = self.section_list.selectedItems()[0]
        self.section_list.takeItem(self.section_list.row(item))
        self.display_information()

    def display_information(self):
        items = self.section_list.selectedItems()
        if items:
            sensor = items[0].text()
            self.name_ln.setEnabled(True)
            self.refresh_ln.setEnabled(True)
            self.table_ln.setEnabled(True)
            self.store_ln.setEnabled(True)
            self.name_bt.setEnabled(True)
            self.refresh_bt.setEnabled(True)
            self.table_bt.setEnabled(True)
            self.store_bt.setEnabled(True)
            self.id_ln.setText(self.sensor_dict[sensor]['id'])
            try:
                self.name_ln.setText(self.sensor_dict[sensor]['name'])
            except KeyError:
                pass
            try:
                self.refresh_ln.setText(str(self.sensor_dict[sensor]['refresh']))
            except KeyError:
                pass
            try:
                self.table_ln.setText(self.sensor_dict[sensor]['table'])
            except KeyError:
                pass
            try:
                self.store_ln.setText(str(self.sensor_dict[sensor]['store']))
            except KeyError:
                pass
        else:
            self.name_ln.setEnabled(False)
            self.refresh_ln.setEnabled(False)
            self.table_ln.setEnabled(False)
            self.store_ln.setEnabled(False)
            self.name_bt.setEnabled(False)
            self.refresh_bt.setEnabled(False)
            self.table_bt.setEnabled(False)
            self.store_bt.setEnabled(False)
            self.name_ln.clear()
            self.refresh_ln.clear()
            self.table_ln.clear()
            self.store_ln.clear()
            self.id_ln.clear()

    def set_sensor_dict_info(self):
        if self.section_list.selectedItems():
            sensor = self.section_list.selectedItems()[0].text()
            item = self.sender().objectName()[: -3]
            self.sensor_dict[sensor][item] = str(self.sender().text())

    def display_keyboard(self):
        keyboard_window = MyKeyboard(self.mainparent)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            if self.sender().objectName() == 'name_bt':
                self.name_ln.setText(keyboard_window.num_line.text())
            elif self.sender().objectName() == 'table_bt':
                self.table_ln.setText(keyboard_window.num_line.text())

    def display_numpad(self):
        numpad_window = MyNumpad(self.mainparent)
        numpad_window.exec_()
        if not numpad_window.cancel:
            if self.sender().objectName() == 'refresh_bt':
                self.refresh_ln.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'store_bt':
                self.store_ln.setText(numpad_window.num_line.text())

    def activate_delete_button(self):
        if self.section_list.selectedItems():
            self.del_sensor.setEnabled(True)
        else:
            self.del_sensor.setEnabled(False)

    def save_sensor_dict(self):
        self.cancel = False
        self.close_window()

    def close_window(self):
        logging.debug('gui - sensor_window.py - W1SensorManager - close_window')
        self.close()


class BME280SensorManager(QtWidgets.QDialog, Ui_sensormanagerWindow):
    def __init__(self, sensor_dict, parent=None):
        logging.debug('gui - sensor_window.py - W1SensorManager - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mainparent = parent
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.splitter.setSizes([270, 508])
        self.cancel = True
        self.sensor_dict = sensor_dict
        self.section_list.itemClicked.connect(self.display_information)
        self.section_list.itemClicked.connect(self.activate_delete_button)
        self.cancel_button.clicked.connect(self.close_window)
        self.ok_button.clicked.connect(self.save_sensor_dict)
        self.name_bt.clicked.connect(self.display_keyboard)
        self.table_bt.clicked.connect(self.display_keyboard)
        self.refresh_bt.clicked.connect(self.display_numpad)
        self.store_bt.clicked.connect(self.display_numpad)
        self.add_sensor.clicked.connect(self.display_available_sensors)
        self.del_sensor.clicked.connect(self.delete_sensor)
        self.name_ln.textChanged.connect(self.set_sensor_dict_info)
        self.refresh_ln.textChanged.connect(self.set_sensor_dict_info)
        self.table_ln.textChanged.connect(self.set_sensor_dict_info)
        self.store_ln.textChanged.connect(self.set_sensor_dict_info)
        self.parse_sensor_dict()

    def parse_sensor_dict(self):
        for sensor, _ in self.sensor_dict.items():
            widget = QtWidgets.QListWidgetItem()
            widget.setText(sensor)
            self.section_list.addItem(widget)

    def display_available_sensors(self):
        sensor_list = []
        if platform.system() == 'Linux':
            pi = pigpio.pi()
            for device in range(128):
                h = pi.i2c_open(1, device)
                try:
                    pi.i2c_read_byte(h)
                    sensor_id = f'id-1-{hex(device)}'
                    sensor_list.append(sensor_id)
                except:
                    pass
                pi.i2c_close(h)

            pi.stop
        else:
            sensor_list.append('id-1-0x77')

        # sensor_list = [item.name for item in path.glob('*') if item.name != 'w1_bus_master1']
        registered_list = [self.section_list.item(idx).text() for idx in range(self.section_list.count())]
        sensor_window = AvailableSensorsWindow(sensor_list, self.mainparent)
        sensor_window.exec_()
        if not sensor_window.cancel:
            if sensor_window.sensor not in registered_list:
                widget = QtWidgets.QListWidgetItem()
                widget.setText(sensor_window.sensor)
                self.section_list.addItem(widget)
                self.sensor_dict[sensor_window.sensor] = {'name': '', 'table': '', 'refresh': 30, 'store': 24,
                                                          'id': sensor_window.sensor, 'bus': 1}

    def delete_sensor(self):
        item = self.section_list.selectedItems()[0]
        self.section_list.takeItem(self.section_list.row(item))
        self.display_information()

    def display_information(self):
        items = self.section_list.selectedItems()
        if items:
            sensor = items[0].text()
            self.name_ln.setEnabled(True)
            self.refresh_ln.setEnabled(True)
            self.table_ln.setEnabled(True)
            self.store_ln.setEnabled(True)
            self.name_bt.setEnabled(True)
            self.refresh_bt.setEnabled(True)
            self.table_bt.setEnabled(True)
            self.store_bt.setEnabled(True)
            self.id_ln.setText(self.sensor_dict[sensor]['id'])
            try:
                self.name_ln.setText(self.sensor_dict[sensor]['name'])
            except KeyError:
                pass
            try:
                self.refresh_ln.setText(str(self.sensor_dict[sensor]['refresh']))
            except KeyError:
                pass
            try:
                self.table_ln.setText(self.sensor_dict[sensor]['table'])
            except KeyError:
                pass
            try:
                self.store_ln.setText(str(self.sensor_dict[sensor]['store']))
            except KeyError:
                pass
        else:
            self.name_ln.setEnabled(False)
            self.refresh_ln.setEnabled(False)
            self.table_ln.setEnabled(False)
            self.store_ln.setEnabled(False)
            self.name_bt.setEnabled(False)
            self.refresh_bt.setEnabled(False)
            self.table_bt.setEnabled(False)
            self.store_bt.setEnabled(False)
            self.name_ln.clear()
            self.refresh_ln.clear()
            self.table_ln.clear()
            self.store_ln.clear()
            self.id_ln.clear()

    def set_sensor_dict_info(self):
        if self.section_list.selectedItems():
            sensor = self.section_list.selectedItems()[0].text()
            item = self.sender().objectName()[: -3]
            self.sensor_dict[sensor][item] = str(self.sender().text())

    def display_keyboard(self):
        keyboard_window = MyKeyboard(self.mainparent)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            if self.sender().objectName() == 'name_bt':
                self.name_ln.setText(keyboard_window.num_line.text())
            elif self.sender().objectName() == 'table_bt':
                self.table_ln.setText(keyboard_window.num_line.text())

    def display_numpad(self):
        numpad_window = MyNumpad(self.mainparent)
        numpad_window.exec_()
        if not numpad_window.cancel:
            if self.sender().objectName() == 'refresh_bt':
                self.refresh_ln.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'store_bt':
                self.store_ln.setText(numpad_window.num_line.text())

    def activate_delete_button(self):
        if self.section_list.selectedItems():
            self.del_sensor.setEnabled(True)
        else:
            self.del_sensor.setEnabled(False)

    def save_sensor_dict(self):
        self.cancel = False
        self.close_window()

    def close_window(self):
        logging.debug('gui - sensor_window.py - W1SensorManager - close_window')
        self.close()



class AvailableSensorsWindow(QtWidgets.QDialog, Ui_townsearchWindow):
    def __init__(self, sensor_list, parent=None):
        logging.debug('gui - sensor_window.py - AvailableSensorsWindow - __init__')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.cancel = True
        self.sensor_list = sensor_list
        self.radio_bt_list = []
        self.sensor = None
        self.ok_button.clicked.connect(self.confirm_sensor)
        self.cancel_button.clicked.connect(self.close_window)
        self.ok_button.setEnabled(False)
        self.display_sensors()

    def display_sensors(self):
        logging.debug('gui - sensor_window.py - AvailableSensorsWindow - display_sensors')
        idx = 0
        for sensor in self.sensor_list:
            self.radio_bt_list.append(QtWidgets.QRadioButton())
            self.radio_bt_list[idx].setMinimumSize(QtCore.QSize(0, 40))
            self.radio_bt_list[idx].setMaximumSize(QtCore.QSize(16777215, 40))
            self.radio_bt_list[idx].setFont(font_creation_function('medium_big'))
            self.radio_bt_list[idx].setStyleSheet(stylesheet_creation_function('qradiobutton'))
            self.radio_bt_list[idx].setObjectName('sensor_' + str(idx))
            self.radio_bt_list[idx].setText(sensor)
            self.verticalLayout.addWidget(self.radio_bt_list[idx])
            self.radio_bt_list[idx].clicked.connect(self.set_sensor)
            self.radio_bt_list[idx].clicked.connect(self.activate_ok)
            idx += 1
        self.verticalLayout.setAlignment(QtCore.Qt.AlignTop)

    def set_sensor(self):
        logging.debug('gui - sensor_window.py - AvailableSensorsWindow - set_sensor')
        idx = int(self.sender().objectName()[7:])
        self.sensor = self.sensor_list[idx]

    def activate_ok(self):
        logging.debug('gui - sensor_window.py - AvailableSensorsWindow - activate_ok')
        self.ok_button.setEnabled(True)

    def confirm_sensor(self):
        logging.debug('gui - sensor_window.py - AvailableSensorsWindow - confirm_sensor')
        if self.sensor is not None:
            self.cancel = False
            self.close_window()

    def close_window(self):
        logging.debug('gui - sensor_window.py - AvailableSensorsWindow - close_window')
        self.close()
