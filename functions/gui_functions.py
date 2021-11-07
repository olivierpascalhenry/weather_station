from PyQt5 import QtGui, QtWidgets, QtCore
from functions.utils import (stylesheet_creation_function, weather_to_pictogrammes, font_creation_function,
                             clear_layout, icon_creation_function)


def set_mainwindow_icons(self):
    self.exit_button.setIcon(icon_creation_function('exit_icon.svg', self.gui_path))
    self.separator.setIcon(icon_creation_function('separator_icon_2.png', self.gui_path))
    self.option_button.setIcon(icon_creation_function('option_icon.svg', self.gui_path))
    self.about_button.setIcon(icon_creation_function('about_popup_icon.svg', self.gui_path))
    self.in_out_bt.setIcon(icon_creation_function('int_ext_icon.svg', self.gui_path))
    self.time_series_bt.setIcon(icon_creation_function('time_series_icon.svg', self.gui_path))
    self.h1_prev_bt.setIcon(icon_creation_function('prev_1h_icon.svg', self.gui_path))
    self.h6_prev_bt.setIcon(icon_creation_function('prev_6h_icon.svg', self.gui_path))
    self.left_ts_button.setIcon(icon_creation_function('left_icon.svg', self.gui_path))
    self.ts_page_marker_1.setIcon(icon_creation_function('filled_circle_icon.svg', self.gui_path))
    self.ts_page_marker_2.setIcon(icon_creation_function('empty_circle_icon.svg', self.gui_path))
    self.right_ts_button.setIcon(icon_creation_function('right_icon.svg', self.gui_path))
    self.left_fc_button.setIcon(icon_creation_function('left_icon.svg', self.gui_path))
    self.fc_page_marker_1.setIcon(icon_creation_function('filled_circle_icon.svg', self.gui_path))
    self.fc_page_marker_2.setIcon(icon_creation_function('empty_circle_icon.svg', self.gui_path))
    self.right_fc_button.setIcon(icon_creation_function('right_icon.svg', self.gui_path))


def add_1h_forecast_widget(self, hour, weather, temp, full_dt, horizontal_layout=None):
    self.fc_1h_fr_1.append(QtWidgets.QFrame())
    if self.fc_1h_nbr1 not in [0, 6, 12, 18]:
        self.fc_1h_fr_1[self.fc_1h_nbr1].setStyleSheet("QFrame {\n"
                                                       "   background: rgb(190,190,190);\n"
                                                       "   width: 5px;\n"
                                                       "   border: 0px solid black;\n"
                                                       "   margin-top: 10px;\n"
                                                       "   margin-bottom: 10px;\n"
                                                       "}")
    else:
        self.fc_1h_fr_1[self.fc_1h_nbr1].setStyleSheet("QFrame {\n"
                                                       "   background: transparent;\n"
                                                       "   width: 5px;\n"
                                                       "   border: 0px solid black;\n"
                                                       "   margin-top: 10px;\n"
                                                       "   margin-bottom: 10px;\n"
                                                       "}")
    self.fc_1h_fr_1[self.fc_1h_nbr1].setFrameShape(QtWidgets.QFrame.VLine)
    self.fc_1h_fr_1[self.fc_1h_nbr1].setFrameShadow(QtWidgets.QFrame.Sunken)
    self.fc_1h_fr_1[self.fc_1h_nbr1].setObjectName('fc_1h_fr_1_' + str(self.fc_1h_nbr1))
    horizontal_layout.addWidget(self.fc_1h_fr_1[self.fc_1h_nbr1])
    self.fc_1h_vert_lay_1.append(QtWidgets.QVBoxLayout())
    self.fc_1h_vert_lay_1[self.fc_1h_nbr1].setObjectName('fc_1h_vert_lay_1_' + str(self.fc_1h_nbr1))
    self.fc_1h_lb_1.append(QtWidgets.QLabel())
    self.fc_1h_lb_1[self.fc_1h_nbr1].setMinimumSize(QtCore.QSize(0, 0))
    self.fc_1h_lb_1[self.fc_1h_nbr1].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.fc_1h_lb_1[self.fc_1h_nbr1].setFont(font_creation_function('very_big'))
    self.fc_1h_lb_1[self.fc_1h_nbr1].setStyleSheet(stylesheet_creation_function('qlabel', self.gui_path + '/'))
    self.fc_1h_lb_1[self.fc_1h_nbr1].setAlignment(QtCore.Qt.AlignCenter)
    self.fc_1h_lb_1[self.fc_1h_nbr1].setObjectName('fc_1h_lb_1_' + str(self.fc_1h_nbr1))
    self.fc_1h_lb_1[self.fc_1h_nbr1].setText(hour + 'h')
    self.fc_1h_vert_lay_1[self.fc_1h_nbr1].addWidget(self.fc_1h_lb_1[self.fc_1h_nbr1])
    self.fc_1h_bt_1.append(QtWidgets.QToolButton())
    self.fc_1h_bt_1[self.fc_1h_nbr1].setMinimumSize(QtCore.QSize(80, 80))
    self.fc_1h_bt_1[self.fc_1h_nbr1].setMaximumSize(QtCore.QSize(16777215, 80))
    self.fc_1h_bt_1[self.fc_1h_nbr1].setStyleSheet(stylesheet_creation_function('qtoolbutton_1hfc',
                                                                                self.gui_path + '/'))
    self.fc_1h_bt_1[self.fc_1h_nbr1].setIcon(weather_to_pictogrammes(weather, self.gui_path + '/'))
    self.fc_1h_bt_1[self.fc_1h_nbr1].setIconSize(QtCore.QSize(80, 80))
    self.fc_1h_bt_1[self.fc_1h_nbr1].setObjectName('fc_1h_bt_1_' + str(self.fc_1h_nbr1))
    self.fc_1h_vert_lay_1[self.fc_1h_nbr1].addWidget(self.fc_1h_bt_1[self.fc_1h_nbr1])
    self.fc_1h_lb_2.append(QtWidgets.QLabel())
    self.fc_1h_lb_2[self.fc_1h_nbr1].setMinimumSize(QtCore.QSize(0, 0))
    self.fc_1h_lb_2[self.fc_1h_nbr1].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.fc_1h_lb_2[self.fc_1h_nbr1].setFont(font_creation_function('very_big'))
    self.fc_1h_lb_2[self.fc_1h_nbr1].setStyleSheet(stylesheet_creation_function('qlabel', self.gui_path + '/'))
    self.fc_1h_lb_2[self.fc_1h_nbr1].setAlignment(QtCore.Qt.AlignCenter)
    self.fc_1h_lb_2[self.fc_1h_nbr1].setObjectName('fc_1h_lb_2_' + str(self.fc_1h_nbr1))
    self.fc_1h_lb_2[self.fc_1h_nbr1].setText(temp + '°C')
    self.fc_1h_vert_lay_1[self.fc_1h_nbr1].addWidget(self.fc_1h_lb_2[self.fc_1h_nbr1])
    horizontal_layout.addLayout(self.fc_1h_vert_lay_1[self.fc_1h_nbr1])
    self.fc_1h_bt_1[self.fc_1h_nbr1].clicked.connect(lambda: self.display_1h_forecast_details(full_dt))
    self.fc_1h_nbr1 += 1


def add_6h_forecast_widget(self, date, weather, temp, dt_list, horizontal_layout):
    self.fc_6h_fr_1.append(QtWidgets.QFrame())
    if self.fc_6h_nbr1 not in [0, 3]:
        self.fc_6h_fr_1[self.fc_6h_nbr1].setStyleSheet("QFrame {\n"
                                                       "   background: rgb(190,190,190);\n"
                                                       "   width: 5px;\n"
                                                       "   border: 0px solid black;\n"
                                                       "   margin-top: 10px;\n"
                                                       "   margin-bottom: 10px;\n"
                                                       "}")
    else:
        self.fc_6h_fr_1[self.fc_6h_nbr1].setStyleSheet("QFrame {\n"
                                                       "   background: transparent;\n"
                                                       "   width: 5px;\n"
                                                       "   border: 0px solid black;\n"
                                                       "   margin-top: 10px;\n"
                                                       "   margin-bottom: 10px;\n"
                                                       "}")
    self.fc_6h_fr_1[self.fc_6h_nbr1].setFrameShape(QtWidgets.QFrame.VLine)
    self.fc_6h_fr_1[self.fc_6h_nbr1].setFrameShadow(QtWidgets.QFrame.Sunken)
    self.fc_6h_fr_1[self.fc_6h_nbr1].setObjectName('fc_6h_fr_1_' + str(self.fc_6h_nbr1))
    horizontal_layout.addWidget(self.fc_6h_fr_1[self.fc_6h_nbr1])
    self.fc_6h_vert_lay_1.append(QtWidgets.QVBoxLayout())
    self.fc_6h_vert_lay_1[self.fc_6h_nbr1].setObjectName('fc_1h_vert_lay_1_' + str(self.fc_6h_nbr1))
    self.fc_6h_lb_1.append(QtWidgets.QLabel())
    self.fc_6h_lb_1[self.fc_6h_nbr1].setMinimumSize(QtCore.QSize(0, 0))
    self.fc_6h_lb_1[self.fc_6h_nbr1].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.fc_6h_lb_1[self.fc_6h_nbr1].setFont(font_creation_function('very_big'))
    self.fc_6h_lb_1[self.fc_6h_nbr1].setStyleSheet(stylesheet_creation_function('qlabel', self.gui_path + '/'))
    self.fc_6h_lb_1[self.fc_6h_nbr1].setAlignment(QtCore.Qt.AlignCenter)
    self.fc_6h_lb_1[self.fc_6h_nbr1].setObjectName('fc_6h_lb_1_' + str(self.fc_6h_nbr1))
    self.fc_6h_lb_1[self.fc_6h_nbr1].setText(date)
    self.fc_6h_vert_lay_1[self.fc_6h_nbr1].addWidget(self.fc_6h_lb_1[self.fc_6h_nbr1])
    self.fc_6h_bt_1.append(QtWidgets.QToolButton())
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    size_policy.setHorizontalStretch(0)
    size_policy.setVerticalStretch(0)
    size_policy.setHeightForWidth(self.fc_6h_bt_1[self.fc_6h_nbr1].sizePolicy().hasHeightForWidth())
    self.fc_6h_bt_1[self.fc_6h_nbr1].setSizePolicy(size_policy)
    self.fc_6h_bt_1[self.fc_6h_nbr1].setMinimumSize(QtCore.QSize(80, 80))
    self.fc_6h_bt_1[self.fc_6h_nbr1].setMaximumSize(QtCore.QSize(16777215, 80))
    self.fc_6h_bt_1[self.fc_6h_nbr1].setStyleSheet(stylesheet_creation_function('qtoolbutton_1hfc',
                                                                                self.gui_path + '/'))
    self.fc_6h_bt_1[self.fc_6h_nbr1].setIcon(weather_to_pictogrammes(weather, self.gui_path + '/'))
    self.fc_6h_bt_1[self.fc_6h_nbr1].setIconSize(QtCore.QSize(80, 80))
    self.fc_6h_bt_1[self.fc_6h_nbr1].setObjectName('fc_6h_bt_1_' + str(self.fc_6h_nbr1))
    self.fc_6h_vert_lay_1[self.fc_6h_nbr1].addWidget(self.fc_6h_bt_1[self.fc_6h_nbr1])
    self.fc_6h_lb_2.append(QtWidgets.QLabel())
    self.fc_6h_lb_2[self.fc_6h_nbr1].setMinimumSize(QtCore.QSize(0, 0))
    self.fc_6h_lb_2[self.fc_6h_nbr1].setMaximumSize(QtCore.QSize(16777215, 16777215))
    self.fc_6h_lb_2[self.fc_6h_nbr1].setFont(font_creation_function('very_big'))
    self.fc_6h_lb_2[self.fc_6h_nbr1].setStyleSheet(stylesheet_creation_function('qlabel', self.gui_path + '/'))
    self.fc_6h_lb_2[self.fc_6h_nbr1].setAlignment(QtCore.Qt.AlignCenter)
    self.fc_6h_lb_2[self.fc_6h_nbr1].setObjectName('fc_6h_lb_2_' + str(self.fc_6h_nbr1))
    self.fc_6h_lb_2[self.fc_6h_nbr1].setText(temp)
    self.fc_6h_vert_lay_1[self.fc_6h_nbr1].addWidget(self.fc_6h_lb_2[self.fc_6h_nbr1])
    horizontal_layout.addLayout(self.fc_6h_vert_lay_1[self.fc_6h_nbr1])
    self.fc_6h_bt_1[self.fc_6h_nbr1].clicked.connect(lambda: self.display_6h_forecast_details(dt_list))
    self.fc_6h_nbr1 += 1


def clean_1h_forecast_widgets(self):
    clear_layout(self.prev1h_layout_1)
    clear_layout(self.prev1h_layout_2)
    clear_layout(self.prev1h_layout_3)
    clear_layout(self.prev1h_layout_4)
    self.fc_1h_vert_lay_1 = []
    self.fc_1h_lb_1 = []
    self.fc_1h_lb_2 = []
    self.fc_1h_bt_1 = []
    self.fc_1h_fr_1 = []
    self.fc_1h_nbr1 = 0


def clean_6h_forecast_widgets(self):
    clear_layout(self.prev6h_layout_1)
    clear_layout(self.prev6h_layout_2)
    self.fc_6h_vert_lay_1 = []
    self.fc_6h_lb_1 = []
    self.fc_6h_lb_2 = []
    self.fc_6h_bt_1 = []
    self.fc_6h_fr_1 = []
    self.fc_6h_nbr1 = 0
