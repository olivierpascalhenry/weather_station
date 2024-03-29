# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1d_ow_forecast_details.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_forecast1dWindow(object):
    def setupUi(self, forecast1dWindow):
        forecast1dWindow.setObjectName("forecast1dWindow")
        forecast1dWindow.resize(507, 416)
        forecast1dWindow.setMinimumSize(QtCore.QSize(0, 0))
        forecast1dWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        forecast1dWindow.setFont(font)
        forecast1dWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        forecast1dWindow.setWindowTitle("")
        forecast1dWindow.setStyleSheet("QWidget {\n"
"    background-color: #DEEBF7;\n"
"    border: 1px solid rgb(75,75,75);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(forecast1dWindow)
        self.gridLayout_2.setSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.date_label = QtWidgets.QLabel(forecast1dWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMinimumSize(QtCore.QSize(300, 0))
        self.date_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_label.setWordWrap(True)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_2.addWidget(self.date_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.weather_lb = QtWidgets.QToolButton(forecast1dWindow)
        self.weather_lb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weather_lb.sizePolicy().hasHeightForWidth())
        self.weather_lb.setSizePolicy(sizePolicy)
        self.weather_lb.setMinimumSize(QtCore.QSize(80, 80))
        self.weather_lb.setMaximumSize(QtCore.QSize(16777215, 80))
        self.weather_lb.setStyleSheet("QToolButton {\n"
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
        self.weather_lb.setText("")
        self.weather_lb.setIconSize(QtCore.QSize(80, 80))
        self.weather_lb.setObjectName("weather_lb")
        self.verticalLayout.addWidget(self.weather_lb)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QToolButton(forecast1dWindow)
        self.ok_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(50, 50))
        self.ok_button.setMaximumSize(QtCore.QSize(16777215, 50))
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
        icon.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.verticalLayout.addWidget(self.ok_button)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.temp_lb = QtWidgets.QLabel(forecast1dWindow)
        self.temp_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.temp_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_lb.setFont(font)
        self.temp_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_lb.setWordWrap(True)
        self.temp_lb.setObjectName("temp_lb")
        self.gridLayout.addWidget(self.temp_lb, 0, 0, 1, 1)
        self.wind_lb = QtWidgets.QLabel(forecast1dWindow)
        self.wind_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.wind_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.wind_lb.setFont(font)
        self.wind_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.wind_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.wind_lb.setWordWrap(True)
        self.wind_lb.setObjectName("wind_lb")
        self.gridLayout.addWidget(self.wind_lb, 4, 0, 1, 1)
        self.pres_lb = QtWidgets.QLabel(forecast1dWindow)
        self.pres_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.pres_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_lb.setFont(font)
        self.pres_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pres_lb.setWordWrap(True)
        self.pres_lb.setObjectName("pres_lb")
        self.gridLayout.addWidget(self.pres_lb, 1, 0, 1, 1)
        self.cover_lb = QtWidgets.QLabel(forecast1dWindow)
        self.cover_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.cover_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cover_lb.setFont(font)
        self.cover_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.cover_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cover_lb.setWordWrap(True)
        self.cover_lb.setObjectName("cover_lb")
        self.gridLayout.addWidget(self.cover_lb, 2, 0, 1, 1)
        self.rain_lb = QtWidgets.QLabel(forecast1dWindow)
        self.rain_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.rain_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rain_lb.setFont(font)
        self.rain_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.rain_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rain_lb.setWordWrap(True)
        self.rain_lb.setObjectName("rain_lb")
        self.gridLayout.addWidget(self.rain_lb, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dir_ln = QtWidgets.QToolButton(forecast1dWindow)
        self.dir_ln.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dir_ln.sizePolicy().hasHeightForWidth())
        self.dir_ln.setSizePolicy(sizePolicy)
        self.dir_ln.setMinimumSize(QtCore.QSize(40, 40))
        self.dir_ln.setMaximumSize(QtCore.QSize(40, 40))
        self.dir_ln.setStyleSheet("QToolButton {\n"
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
        self.dir_ln.setText("")
        self.dir_ln.setIconSize(QtCore.QSize(40, 40))
        self.dir_ln.setObjectName("dir_ln")
        self.horizontalLayout.addWidget(self.dir_ln)
        self.speed_ln = QtWidgets.QLabel(forecast1dWindow)
        self.speed_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.speed_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.speed_ln.setFont(font)
        self.speed_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.speed_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_ln.setWordWrap(True)
        self.speed_ln.setObjectName("speed_ln")
        self.horizontalLayout.addWidget(self.speed_ln)
        self.speed_unit = QtWidgets.QLabel(forecast1dWindow)
        self.speed_unit.setMinimumSize(QtCore.QSize(90, 0))
        self.speed_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.speed_unit.setFont(font)
        self.speed_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.speed_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.speed_unit.setWordWrap(True)
        self.speed_unit.setObjectName("speed_unit")
        self.horizontalLayout.addWidget(self.speed_unit)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gust_icon = QtWidgets.QToolButton(forecast1dWindow)
        self.gust_icon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gust_icon.sizePolicy().hasHeightForWidth())
        self.gust_icon.setSizePolicy(sizePolicy)
        self.gust_icon.setMinimumSize(QtCore.QSize(40, 40))
        self.gust_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.gust_icon.setStyleSheet("QToolButton {\n"
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
        self.gust_icon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/gust_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gust_icon.setIcon(icon1)
        self.gust_icon.setIconSize(QtCore.QSize(40, 40))
        self.gust_icon.setObjectName("gust_icon")
        self.horizontalLayout_4.addWidget(self.gust_icon)
        self.gust_ln = QtWidgets.QLabel(forecast1dWindow)
        self.gust_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.gust_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gust_ln.setFont(font)
        self.gust_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.gust_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gust_ln.setWordWrap(True)
        self.gust_ln.setObjectName("gust_ln")
        self.horizontalLayout_4.addWidget(self.gust_ln)
        self.gust_unit = QtWidgets.QLabel(forecast1dWindow)
        self.gust_unit.setMinimumSize(QtCore.QSize(90, 0))
        self.gust_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.gust_unit.setFont(font)
        self.gust_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.gust_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gust_unit.setWordWrap(True)
        self.gust_unit.setObjectName("gust_unit")
        self.horizontalLayout_4.addWidget(self.gust_unit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.temp_ln = QtWidgets.QLabel(forecast1dWindow)
        self.temp_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.temp_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_ln.setFont(font)
        self.temp_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temp_ln.setWordWrap(True)
        self.temp_ln.setObjectName("temp_ln")
        self.horizontalLayout_7.addWidget(self.temp_ln)
        self.temp_unit = QtWidgets.QLabel(forecast1dWindow)
        self.temp_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.temp_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temp_unit.setFont(font)
        self.temp_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.temp_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temp_unit.setWordWrap(True)
        self.temp_unit.setObjectName("temp_unit")
        self.horizontalLayout_7.addWidget(self.temp_unit)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pres_ln = QtWidgets.QLabel(forecast1dWindow)
        self.pres_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.pres_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_ln.setFont(font)
        self.pres_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pres_ln.setWordWrap(True)
        self.pres_ln.setObjectName("pres_ln")
        self.horizontalLayout_6.addWidget(self.pres_ln)
        self.pres_unit = QtWidgets.QLabel(forecast1dWindow)
        self.pres_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.pres_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pres_unit.setFont(font)
        self.pres_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pres_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pres_unit.setWordWrap(True)
        self.pres_unit.setObjectName("pres_unit")
        self.horizontalLayout_6.addWidget(self.pres_unit)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cover_ln = QtWidgets.QLabel(forecast1dWindow)
        self.cover_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.cover_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cover_ln.setFont(font)
        self.cover_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.cover_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cover_ln.setWordWrap(True)
        self.cover_ln.setObjectName("cover_ln")
        self.horizontalLayout_5.addWidget(self.cover_ln)
        self.cover_unit = QtWidgets.QLabel(forecast1dWindow)
        self.cover_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.cover_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cover_unit.setFont(font)
        self.cover_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.cover_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cover_unit.setWordWrap(True)
        self.cover_unit.setObjectName("cover_unit")
        self.horizontalLayout_5.addWidget(self.cover_unit)
        spacerItem3 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rain_ln = QtWidgets.QLabel(forecast1dWindow)
        self.rain_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.rain_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rain_ln.setFont(font)
        self.rain_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.rain_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rain_ln.setWordWrap(True)
        self.rain_ln.setObjectName("rain_ln")
        self.horizontalLayout_3.addWidget(self.rain_ln)
        self.rain_unit = QtWidgets.QLabel(forecast1dWindow)
        self.rain_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.rain_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.rain_unit.setFont(font)
        self.rain_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.rain_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rain_unit.setWordWrap(True)
        self.rain_unit.setObjectName("rain_unit")
        self.horizontalLayout_3.addWidget(self.rain_unit)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.retranslateUi(forecast1dWindow)
        QtCore.QMetaObject.connectSlotsByName(forecast1dWindow)

    def retranslateUi(self, forecast1dWindow):
        _translate = QtCore.QCoreApplication.translate
        self.date_label.setText(_translate("forecast1dWindow", "ND"))
        self.temp_lb.setText(_translate("forecast1dWindow", "Température :"))
        self.wind_lb.setText(_translate("forecast1dWindow", "Vent :"))
        self.pres_lb.setText(_translate("forecast1dWindow", "Pression :"))
        self.cover_lb.setText(_translate("forecast1dWindow", "Couverture :"))
        self.rain_lb.setText(_translate("forecast1dWindow", "Pluie :"))
        self.speed_ln.setText(_translate("forecast1dWindow", "ND"))
        self.speed_unit.setText(_translate("forecast1dWindow", "km/h"))
        self.gust_ln.setText(_translate("forecast1dWindow", "ND"))
        self.gust_unit.setText(_translate("forecast1dWindow", "km/h"))
        self.temp_ln.setText(_translate("forecast1dWindow", "ND"))
        self.temp_unit.setText(_translate("forecast1dWindow", "°C"))
        self.pres_ln.setText(_translate("forecast1dWindow", "ND"))
        self.pres_unit.setText(_translate("forecast1dWindow", "hPa"))
        self.cover_ln.setText(_translate("forecast1dWindow", "ND"))
        self.cover_unit.setText(_translate("forecast1dWindow", "%"))
        self.rain_ln.setText(_translate("forecast1dWindow", "ND"))
        self.rain_unit.setText(_translate("forecast1dWindow", "mm"))
