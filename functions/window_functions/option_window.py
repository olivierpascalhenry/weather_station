import pickle
import logging
import pathlib
from meteofrance_api import MeteoFranceClient
from PyQt5 import QtCore, QtWidgets
from ui.Ui_optionwindow import Ui_optionWindow
from functions.utils import code_to_departement
from functions.window_functions.other_windows import MyInfo, MyNumpad, MyKeyboard, MyTown


class MyOptions(QtWidgets.QDialog, Ui_optionWindow):
    def __init__(self, config_dict, user_path, parent=None):
        logging.debug('gui - other_windows.py - MyOptions - __init__ ')
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setOffset(5)
        shadow.setBlurRadius(25)
        self.setGraphicsEffect(shadow)
        self.mainparent = parent
        self.move(int((self.parent().width() - self.width()) / 2), int((self.parent().height() - self.height()) / 2))
        self.config_dict = config_dict
        self.ow_splitter.setSizes([180, 520])
        self.user_path = user_path
        self.cancel = True
        self.place_object = None
        self.ow_vertical_layout.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_2.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_3.setAlignment(QtCore.Qt.AlignTop)
        self.ow_vertical_layout_4.setAlignment(QtCore.Qt.AlignTop)
        self.ow_combobox_1.setItemDelegate(QtWidgets.QStyledItemDelegate())
        self.ow_section_list.currentRowChanged.connect(self.display_options)
        self.ow_ok_button.clicked.connect(self.save_config_dict)
        self.ow_cancel_button.clicked.connect(self.close_window)
        self.ow_openButton.clicked.connect(self.get_folder_path)
        self.ow_edit_bt_1.clicked.connect(self.display_numpad)
        self.ow_edit_bt_2.clicked.connect(self.display_numpad)
        self.ow_edit_bt_3.clicked.connect(self.display_keyboard)
        self.ow_edit_bt_4.clicked.connect(self.display_numpad)
        self.ow_edit_bt_5.clicked.connect(self.display_numpad)
        self.ow_edit_bt_6.clicked.connect(self.display_numpad)
        self.ow_edit_bt_7.clicked.connect(self.display_numpad)
        self.ow_line_4.textChanged.connect(self.activate_search_button)
        self.ow_search_button.clicked.connect(self.search_place)
        scroll_1 = QtWidgets.QScroller.scroller(self.ow_scroll_area_2.viewport())
        scroll_1.grabGesture(self.ow_scroll_area_2.viewport(), QtWidgets.QScroller.LeftMouseButtonGesture)
        properties_1 = scroll_1.scrollerProperties()
        properties_1.setScrollMetric(QtWidgets.QScrollerProperties.VerticalOvershootPolicy,
                                     QtWidgets.QScrollerProperties.OvershootAlwaysOff)
        scroll_1.setScrollerProperties(properties_1)
        self.read_config_dict()
        self.ow_section_list.setCurrentRow(0)

    def display_options(self, idx):
        self.ow_stacked_widget.setCurrentIndex(idx)

    def read_config_dict(self):
        logging.debug('gui - option_window_functions.py - MyOptions - read_config_dict')
        self.ow_combobox_1.setCurrentIndex(self.ow_combobox_1.findText(self.config_dict.get('LOG', 'level')))
        self.ow_line_1.setText(self.config_dict.get('LOG', 'path'))
        self.ow_line_1.setCursorPosition(0)
        self.ow_line_2.setText(self.config_dict.get('SENSOR', 'sensors_rate'))
        self.ow_line_3.setText(self.config_dict.get('DISPLAY', 'in_display_rate'))
        self.ow_line_8.setText(self.config_dict.get('DISPLAY', 'out_display_rate'))
        self.ow_line_7.setText(self.config_dict.get('SYSTEM', 'place_altitude'))
        self.ow_line_5.setText(self.config_dict.get('API', 'request_rate'))
        if self.config_dict.getboolean('API', 'user_place'):
            f = open(self.user_path + '/place_object.dat', 'rb')
            self.place_object = pickle.load(f)
            f.close()
            self.ow_line_4.setText(self.place_object.name)
            self.ow_label_13.setText(self.place_object.postal_code)
            self.ow_label_14.setText(code_to_departement()[self.place_object.admin2])

    def save_config_dict(self):
        logging.debug('gui - option_window_functions.py - MyOptions - save_config_dict')
        if not pathlib.Path(str(self.ow_line_1.text())).exists():
            text = ('After checking, it appears that the path for the log file is not valid. Thus it is not possible '
                    'to save the new configuration. Please correct it and try again.')
            info_window = MyInfo(text)
            info_window.exec_()
        else:

            self.config_dict.set('LOG', 'level', str(self.ow_combobox_1.currentText()))
            self.config_dict.set('LOG', 'path', str(self.ow_line_1.text()))
            self.config_dict.set('SENSOR', 'sensors_rate', str(self.ow_line_2.text()))
            self.config_dict.set('DISPLAY', 'in_display_rate', str(self.ow_line_3.text()))
            self.config_dict.set('DISPLAY', 'out_display_rate', str(self.ow_line_8.text()))
            self.config_dict.set('API', 'request_rate', str(self.ow_line_5.text()))
            self.config_dict.set('SYSTEM', 'place_altitude', str(self.ow_line_7.text()))
            if self.place_object is not None:
                self.config_dict.set('API', 'user_place', 'True')
            else:
                self.config_dict.set('API', 'user_place', 'False')
            self.cancel = False
            self.close_window()

    def get_folder_path(self):
        logging.debug('gui - other_windows.py - MyOptions - get_folder_path')
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Sélectionner un répertoire')
        if folder_path:
            self.ow_line_1.setText(str(pathlib.Path(folder_path)))
            self.ow_line_1.setCursorPosition(0)

    def activate_search_button(self):
        if self.ow_line_4.text():
            self.ow_search_button.setEnabled(True)
        else:
            self.ow_search_button.setEnabled(False)

    def search_place(self):
        place, ville, code_postal, departement = None, None, None, None
        list_places = MeteoFranceClient().search_places(str(self.ow_line_4.text()))
        if len(list_places) > 1:
            place_search = MyTown(list_places, self.mainparent)
            place_search.exec_()
            if not place_search.cancel:
                place = place_search.place
                ville = place_search.ville
                code_postal = place_search.code_postal
                departement = place_search.departement
        else:
            place = list_places[0]
            ville = list_places[0].name
            code_postal = list_places[0].postal_code
            departement = code_to_departement()[list_places[0].admin2]

        if place is not None:
            self.place_object = place
            self.ow_line_4.setText(ville)
            self.ow_label_13.setText(code_postal)
            self.ow_label_14.setText(departement)

    def display_numpad(self):
        numpad_window = MyNumpad(self.mainparent)
        numpad_window.exec_()
        if not numpad_window.cancel:
            if self.sender().objectName() == 'ow_edit_bt_1':
                self.ow_line_2.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_2':
                self.ow_line_3.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_4':
                self.ow_line_5.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_5':
                self.ow_line_7.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_6':
                self.ow_line_6.setText(numpad_window.num_line.text())
            elif self.sender().objectName() == 'ow_edit_bt_7':
                self.ow_line_8.setText(numpad_window.num_line.text())

    def display_keyboard(self):
        keyboard_window = MyKeyboard(self.mainparent)
        keyboard_window.exec_()
        if not keyboard_window.cancel:
            self.ow_line_4.setText(keyboard_window.num_line.text())

    def close_window(self):
        logging.debug('gui - other_windows.py - MyAbout - close_window')
        self.close()
