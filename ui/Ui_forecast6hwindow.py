# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6hforecast_details.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forecast6hWindow(object):
    def setupUi(self, forecast6hWindow, gui_path=''):
        forecast6hWindow.setObjectName("forecast6hWindow")
        forecast6hWindow.resize(920, 380)
        forecast6hWindow.setMinimumSize(QtCore.QSize(0, 0))
        forecast6hWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        forecast6hWindow.setFont(font)
        forecast6hWindow.setWindowTitle("")
        forecast6hWindow.setStyleSheet("QWidget {\n"
"    background-color: #DEEBF7;\n"
"    border: 1px solid rgb(75,75,75);\n"
"}\n"
"")
        self.gridLayout_5 = QtWidgets.QGridLayout(forecast6hWindow)
        self.gridLayout_5.setVerticalSpacing(10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.date_label = QtWidgets.QLabel(forecast6hWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMinimumSize(QtCore.QSize(0, 0))
        self.date_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setWordWrap(True)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_9.addWidget(self.date_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.ok_button = QtWidgets.QToolButton(forecast6hWindow)
        self.ok_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(50, 50))
        self.ok_button.setMaximumSize(QtCore.QSize(50, 50))
        self.ok_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ok_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(gui_path + "icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_10.addWidget(self.ok_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.gridLayout_5.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.hour_label_1 = QtWidgets.QLabel(forecast6hWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_label_1.sizePolicy().hasHeightForWidth())
        self.hour_label_1.setSizePolicy(sizePolicy)
        self.hour_label_1.setMinimumSize(QtCore.QSize(100, 50))
        self.hour_label_1.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hour_label_1.setFont(font)
        self.hour_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hour_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label_1.setWordWrap(True)
        self.hour_label_1.setObjectName("hour_label_1")
        self.horizontalLayout.addWidget(self.hour_label_1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.weather_lb_1 = QtWidgets.QToolButton(forecast6hWindow)
        self.weather_lb_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_lb_1.sizePolicy().hasHeightForWidth())
        self.weather_lb_1.setSizePolicy(sizePolicy)
        self.weather_lb_1.setMinimumSize(QtCore.QSize(80, 80))
        self.weather_lb_1.setMaximumSize(QtCore.QSize(16777215, 80))
        self.weather_lb_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.weather_lb_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("graphic_materials/pictogrammes/averses_orageuses.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_lb_1.setIcon(icon1)
        self.weather_lb_1.setIconSize(QtCore.QSize(80, 80))
        self.weather_lb_1.setObjectName("weather_lb_1")
        self.gridLayout.addWidget(self.weather_lb_1, 0, 0, 2, 1)
        self.temp_ln_1 = QtWidgets.QLabel(forecast6hWindow)
        self.temp_ln_1.setMinimumSize(QtCore.QSize(100, 50))
        self.temp_ln_1.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_ln_1.setFont(font)
        self.temp_ln_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_ln_1.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_ln_1.setWordWrap(True)
        self.temp_ln_1.setObjectName("temp_ln_1")
        self.gridLayout.addWidget(self.temp_ln_1, 0, 1, 1, 1)
        self.pres_ln_1 = QtWidgets.QLabel(forecast6hWindow)
        self.pres_ln_1.setMinimumSize(QtCore.QSize(120, 50))
        self.pres_ln_1.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_ln_1.setFont(font)
        self.pres_ln_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_ln_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pres_ln_1.setWordWrap(True)
        self.pres_ln_1.setObjectName("pres_ln_1")
        self.gridLayout.addWidget(self.pres_ln_1, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.dir_ln_1 = QtWidgets.QToolButton(forecast6hWindow)
        self.dir_ln_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_ln_1.sizePolicy().hasHeightForWidth())
        self.dir_ln_1.setSizePolicy(sizePolicy)
        self.dir_ln_1.setMinimumSize(QtCore.QSize(40, 40))
        self.dir_ln_1.setMaximumSize(QtCore.QSize(40, 40))
        self.dir_ln_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.dir_ln_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("graphic_materials/pictogrammes/wind_direction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dir_ln_1.setIcon(icon2)
        self.dir_ln_1.setIconSize(QtCore.QSize(40, 40))
        self.dir_ln_1.setObjectName("dir_ln_1")
        self.horizontalLayout_5.addWidget(self.dir_ln_1)
        self.speed_ln_1 = QtWidgets.QLabel(forecast6hWindow)
        self.speed_ln_1.setMinimumSize(QtCore.QSize(0, 50))
        self.speed_ln_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.speed_ln_1.setFont(font)
        self.speed_ln_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.speed_ln_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_ln_1.setWordWrap(True)
        self.speed_ln_1.setObjectName("speed_ln_1")
        self.horizontalLayout_5.addWidget(self.speed_ln_1)
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        self.vertical_line_2 = QtWidgets.QFrame(forecast6hWindow)
        self.vertical_line_2.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.vertical_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_2.setObjectName("vertical_line_2")
        self.horizontalLayout_11.addWidget(self.vertical_line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.hour_label_2 = QtWidgets.QLabel(forecast6hWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_label_2.sizePolicy().hasHeightForWidth())
        self.hour_label_2.setSizePolicy(sizePolicy)
        self.hour_label_2.setMinimumSize(QtCore.QSize(100, 50))
        self.hour_label_2.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hour_label_2.setFont(font)
        self.hour_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hour_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label_2.setWordWrap(True)
        self.hour_label_2.setObjectName("hour_label_2")
        self.horizontalLayout_2.addWidget(self.hour_label_2)
        spacerItem9 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.weather_lb_2 = QtWidgets.QToolButton(forecast6hWindow)
        self.weather_lb_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_lb_2.sizePolicy().hasHeightForWidth())
        self.weather_lb_2.setSizePolicy(sizePolicy)
        self.weather_lb_2.setMinimumSize(QtCore.QSize(80, 80))
        self.weather_lb_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.weather_lb_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.weather_lb_2.setText("")
        self.weather_lb_2.setIcon(icon1)
        self.weather_lb_2.setIconSize(QtCore.QSize(80, 80))
        self.weather_lb_2.setObjectName("weather_lb_2")
        self.gridLayout_2.addWidget(self.weather_lb_2, 0, 0, 2, 1)
        self.temp_ln_2 = QtWidgets.QLabel(forecast6hWindow)
        self.temp_ln_2.setMinimumSize(QtCore.QSize(100, 50))
        self.temp_ln_2.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_ln_2.setFont(font)
        self.temp_ln_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_ln_2.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_ln_2.setWordWrap(True)
        self.temp_ln_2.setObjectName("temp_ln_2")
        self.gridLayout_2.addWidget(self.temp_ln_2, 0, 1, 1, 1)
        self.pres_ln_2 = QtWidgets.QLabel(forecast6hWindow)
        self.pres_ln_2.setMinimumSize(QtCore.QSize(120, 50))
        self.pres_ln_2.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_ln_2.setFont(font)
        self.pres_ln_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_ln_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pres_ln_2.setWordWrap(True)
        self.pres_ln_2.setObjectName("pres_ln_2")
        self.gridLayout_2.addWidget(self.pres_ln_2, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.dir_ln_2 = QtWidgets.QToolButton(forecast6hWindow)
        self.dir_ln_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_ln_2.sizePolicy().hasHeightForWidth())
        self.dir_ln_2.setSizePolicy(sizePolicy)
        self.dir_ln_2.setMinimumSize(QtCore.QSize(40, 40))
        self.dir_ln_2.setMaximumSize(QtCore.QSize(40, 40))
        self.dir_ln_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.dir_ln_2.setText("")
        self.dir_ln_2.setIcon(icon2)
        self.dir_ln_2.setIconSize(QtCore.QSize(40, 40))
        self.dir_ln_2.setObjectName("dir_ln_2")
        self.horizontalLayout_6.addWidget(self.dir_ln_2)
        self.speed_ln_2 = QtWidgets.QLabel(forecast6hWindow)
        self.speed_ln_2.setMinimumSize(QtCore.QSize(0, 50))
        self.speed_ln_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.speed_ln_2.setFont(font)
        self.speed_ln_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.speed_ln_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_ln_2.setWordWrap(True)
        self.speed_ln_2.setObjectName("speed_ln_2")
        self.horizontalLayout_6.addWidget(self.speed_ln_2)
        spacerItem11 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.vertical_line_3 = QtWidgets.QFrame(forecast6hWindow)
        self.vertical_line_3.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.vertical_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_3.setObjectName("vertical_line_3")
        self.horizontalLayout_11.addWidget(self.vertical_line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.hour_label_3 = QtWidgets.QLabel(forecast6hWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_label_3.sizePolicy().hasHeightForWidth())
        self.hour_label_3.setSizePolicy(sizePolicy)
        self.hour_label_3.setMinimumSize(QtCore.QSize(100, 50))
        self.hour_label_3.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hour_label_3.setFont(font)
        self.hour_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hour_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label_3.setWordWrap(True)
        self.hour_label_3.setObjectName("hour_label_3")
        self.horizontalLayout_3.addWidget(self.hour_label_3)
        spacerItem13 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.weather_lb_3 = QtWidgets.QToolButton(forecast6hWindow)
        self.weather_lb_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_lb_3.sizePolicy().hasHeightForWidth())
        self.weather_lb_3.setSizePolicy(sizePolicy)
        self.weather_lb_3.setMinimumSize(QtCore.QSize(80, 80))
        self.weather_lb_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.weather_lb_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.weather_lb_3.setText("")
        self.weather_lb_3.setIcon(icon1)
        self.weather_lb_3.setIconSize(QtCore.QSize(80, 80))
        self.weather_lb_3.setObjectName("weather_lb_3")
        self.gridLayout_3.addWidget(self.weather_lb_3, 0, 0, 2, 1)
        self.temp_ln_3 = QtWidgets.QLabel(forecast6hWindow)
        self.temp_ln_3.setMinimumSize(QtCore.QSize(100, 50))
        self.temp_ln_3.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_ln_3.setFont(font)
        self.temp_ln_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_ln_3.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_ln_3.setWordWrap(True)
        self.temp_ln_3.setObjectName("temp_ln_3")
        self.gridLayout_3.addWidget(self.temp_ln_3, 0, 1, 1, 1)
        self.pres_ln_3 = QtWidgets.QLabel(forecast6hWindow)
        self.pres_ln_3.setMinimumSize(QtCore.QSize(120, 50))
        self.pres_ln_3.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_ln_3.setFont(font)
        self.pres_ln_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_ln_3.setAlignment(QtCore.Qt.AlignCenter)
        self.pres_ln_3.setWordWrap(True)
        self.pres_ln_3.setObjectName("pres_ln_3")
        self.gridLayout_3.addWidget(self.pres_ln_3, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem14 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.dir_ln_3 = QtWidgets.QToolButton(forecast6hWindow)
        self.dir_ln_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_ln_3.sizePolicy().hasHeightForWidth())
        self.dir_ln_3.setSizePolicy(sizePolicy)
        self.dir_ln_3.setMinimumSize(QtCore.QSize(40, 40))
        self.dir_ln_3.setMaximumSize(QtCore.QSize(40, 40))
        self.dir_ln_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.dir_ln_3.setText("")
        self.dir_ln_3.setIcon(icon2)
        self.dir_ln_3.setIconSize(QtCore.QSize(40, 40))
        self.dir_ln_3.setObjectName("dir_ln_3")
        self.horizontalLayout_7.addWidget(self.dir_ln_3)
        self.speed_ln_3 = QtWidgets.QLabel(forecast6hWindow)
        self.speed_ln_3.setMinimumSize(QtCore.QSize(0, 50))
        self.speed_ln_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.speed_ln_3.setFont(font)
        self.speed_ln_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.speed_ln_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_ln_3.setWordWrap(True)
        self.speed_ln_3.setObjectName("speed_ln_3")
        self.horizontalLayout_7.addWidget(self.speed_ln_3)
        spacerItem15 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11.addLayout(self.verticalLayout_2)
        self.vertical_line_4 = QtWidgets.QFrame(forecast6hWindow)
        self.vertical_line_4.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.vertical_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line_4.setObjectName("vertical_line_4")
        self.horizontalLayout_11.addWidget(self.vertical_line_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem16 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.hour_label_4 = QtWidgets.QLabel(forecast6hWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hour_label_4.sizePolicy().hasHeightForWidth())
        self.hour_label_4.setSizePolicy(sizePolicy)
        self.hour_label_4.setMinimumSize(QtCore.QSize(100, 50))
        self.hour_label_4.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hour_label_4.setFont(font)
        self.hour_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hour_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.hour_label_4.setWordWrap(True)
        self.hour_label_4.setObjectName("hour_label_4")
        self.horizontalLayout_4.addWidget(self.hour_label_4)
        spacerItem17 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.weather_lb_4 = QtWidgets.QToolButton(forecast6hWindow)
        self.weather_lb_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_lb_4.sizePolicy().hasHeightForWidth())
        self.weather_lb_4.setSizePolicy(sizePolicy)
        self.weather_lb_4.setMinimumSize(QtCore.QSize(80, 80))
        self.weather_lb_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.weather_lb_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.weather_lb_4.setText("")
        self.weather_lb_4.setIcon(icon1)
        self.weather_lb_4.setIconSize(QtCore.QSize(80, 80))
        self.weather_lb_4.setObjectName("weather_lb_4")
        self.gridLayout_4.addWidget(self.weather_lb_4, 0, 0, 2, 1)
        self.temp_ln_4 = QtWidgets.QLabel(forecast6hWindow)
        self.temp_ln_4.setMinimumSize(QtCore.QSize(100, 50))
        self.temp_ln_4.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_ln_4.setFont(font)
        self.temp_ln_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_ln_4.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_ln_4.setWordWrap(True)
        self.temp_ln_4.setObjectName("temp_ln_4")
        self.gridLayout_4.addWidget(self.temp_ln_4, 0, 1, 1, 1)
        self.pres_ln_4 = QtWidgets.QLabel(forecast6hWindow)
        self.pres_ln_4.setMinimumSize(QtCore.QSize(120, 50))
        self.pres_ln_4.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_ln_4.setFont(font)
        self.pres_ln_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_ln_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pres_ln_4.setWordWrap(True)
        self.pres_ln_4.setObjectName("pres_ln_4")
        self.gridLayout_4.addWidget(self.pres_ln_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem18 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.dir_ln_4 = QtWidgets.QToolButton(forecast6hWindow)
        self.dir_ln_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_ln_4.sizePolicy().hasHeightForWidth())
        self.dir_ln_4.setSizePolicy(sizePolicy)
        self.dir_ln_4.setMinimumSize(QtCore.QSize(40, 40))
        self.dir_ln_4.setMaximumSize(QtCore.QSize(40, 40))
        self.dir_ln_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.dir_ln_4.setText("")
        self.dir_ln_4.setIcon(icon2)
        self.dir_ln_4.setIconSize(QtCore.QSize(40, 40))
        self.dir_ln_4.setArrowType(QtCore.Qt.NoArrow)
        self.dir_ln_4.setObjectName("dir_ln_4")
        self.horizontalLayout_8.addWidget(self.dir_ln_4)
        self.speed_ln_4 = QtWidgets.QLabel(forecast6hWindow)
        self.speed_ln_4.setMinimumSize(QtCore.QSize(0, 50))
        self.speed_ln_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.speed_ln_4.setFont(font)
        self.speed_ln_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.speed_ln_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_ln_4.setWordWrap(True)
        self.speed_ln_4.setObjectName("speed_ln_4")
        self.horizontalLayout_8.addWidget(self.speed_ln_4)
        spacerItem19 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem19)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout)
        self.gridLayout_5.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.retranslateUi(forecast6hWindow)
        QtCore.QMetaObject.connectSlotsByName(forecast6hWindow)

    def retranslateUi(self, forecast6hWindow):
        _translate = QtCore.QCoreApplication.translate
        self.date_label.setText(_translate("forecast6hWindow", "Vendredi 9 Août"))
        self.hour_label_1.setText(_translate("forecast6hWindow", "00h00"))
        self.temp_ln_1.setText(_translate("forecast6hWindow", "22°C"))
        self.pres_ln_1.setText(_translate("forecast6hWindow", "1019 hPa"))
        self.speed_ln_1.setText(_translate("forecast6hWindow", "25 km/h"))
        self.hour_label_2.setText(_translate("forecast6hWindow", "06h00"))
        self.temp_ln_2.setText(_translate("forecast6hWindow", "22°C"))
        self.pres_ln_2.setText(_translate("forecast6hWindow", "1019 hPa"))
        self.speed_ln_2.setText(_translate("forecast6hWindow", "25 km/h"))
        self.hour_label_3.setText(_translate("forecast6hWindow", "12h00"))
        self.temp_ln_3.setText(_translate("forecast6hWindow", "22°C"))
        self.pres_ln_3.setText(_translate("forecast6hWindow", "1019 hPa"))
        self.speed_ln_3.setText(_translate("forecast6hWindow", "25 km/h"))
        self.hour_label_4.setText(_translate("forecast6hWindow", "18h00"))
        self.temp_ln_4.setText(_translate("forecast6hWindow", "22°C"))
        self.pres_ln_4.setText(_translate("forecast6hWindow", "1019 hPa"))
        self.speed_ln_4.setText(_translate("forecast6hWindow", "25 km/h"))
