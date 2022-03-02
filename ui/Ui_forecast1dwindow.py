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
        forecast1dWindow.resize(480, 380)
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
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.date_label = QtWidgets.QLabel(forecast1dWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
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
        self.horizontalLayout_2.addWidget(self.date_label)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphic_materials/pictogrammes/averses_orageuses.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.weather_lb.setIcon(icon)
        self.weather_lb.setIconSize(QtCore.QSize(80, 80))
        self.weather_lb.setObjectName("weather_lb")
        self.verticalLayout.addWidget(self.weather_lb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.ok_button = QtWidgets.QToolButton(forecast1dWindow)
        self.ok_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(80, 80))
        self.ok_button.setMaximumSize(QtCore.QSize(16777215, 80))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.verticalLayout.addWidget(self.ok_button)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.temp_lb = QtWidgets.QLabel(forecast1dWindow)
        self.temp_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.temp_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.temp_ln = QtWidgets.QLabel(forecast1dWindow)
        self.temp_ln.setMinimumSize(QtCore.QSize(155, 50))
        self.temp_ln.setMaximumSize(QtCore.QSize(155, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.temp_ln, 0, 1, 1, 1)
        self.pres_lb = QtWidgets.QLabel(forecast1dWindow)
        self.pres_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.pres_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.pres_ln = QtWidgets.QLabel(forecast1dWindow)
        self.pres_ln.setMinimumSize(QtCore.QSize(155, 50))
        self.pres_ln.setMaximumSize(QtCore.QSize(155, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.pres_ln, 1, 1, 1, 1)
        self.wind_lb = QtWidgets.QLabel(forecast1dWindow)
        self.wind_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.wind_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.wind_lb, 2, 0, 1, 1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("graphic_materials/pictogrammes/wind_direction.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dir_ln.setIcon(icon2)
        self.dir_ln.setIconSize(QtCore.QSize(40, 40))
        self.dir_ln.setObjectName("dir_ln")
        self.horizontalLayout.addWidget(self.dir_ln)
        self.speed_ln = QtWidgets.QLabel(forecast1dWindow)
        self.speed_ln.setMinimumSize(QtCore.QSize(0, 50))
        self.speed_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.cover_lb = QtWidgets.QLabel(forecast1dWindow)
        self.cover_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.cover_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.cover_lb, 3, 0, 1, 1)
        self.cover_ln = QtWidgets.QLabel(forecast1dWindow)
        self.cover_ln.setMinimumSize(QtCore.QSize(155, 50))
        self.cover_ln.setMaximumSize(QtCore.QSize(155, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.cover_ln, 3, 1, 1, 1)
        self.rain_lb = QtWidgets.QLabel(forecast1dWindow)
        self.rain_lb.setMinimumSize(QtCore.QSize(190, 50))
        self.rain_lb.setMaximumSize(QtCore.QSize(190, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.rain_lb, 4, 0, 1, 1)
        self.rain_ln = QtWidgets.QLabel(forecast1dWindow)
        self.rain_ln.setMinimumSize(QtCore.QSize(155, 50))
        self.rain_ln.setMaximumSize(QtCore.QSize(155, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.gridLayout.addWidget(self.rain_ln, 4, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.retranslateUi(forecast1dWindow)
        QtCore.QMetaObject.connectSlotsByName(forecast1dWindow)

    def retranslateUi(self, forecast1dWindow):
        _translate = QtCore.QCoreApplication.translate
        self.date_label.setText(_translate("forecast1dWindow", "Dimanche 31 Septembre"))
        self.temp_lb.setText(_translate("forecast1dWindow", "Températures :"))
        self.temp_ln.setText(_translate("forecast1dWindow", "12°C / 18°C"))
        self.pres_lb.setText(_translate("forecast1dWindow", "Pression :"))
        self.pres_ln.setText(_translate("forecast1dWindow", "1019 hPa"))
        self.wind_lb.setText(_translate("forecast1dWindow", "Vent :"))
        self.speed_ln.setText(_translate("forecast1dWindow", "25 km/h"))
        self.cover_lb.setText(_translate("forecast1dWindow", "Couverture :"))
        self.cover_ln.setText(_translate("forecast1dWindow", "50 %"))
        self.rain_lb.setText(_translate("forecast1dWindow", "Pluie :"))
        self.rain_ln.setText(_translate("forecast1dWindow", "50 %"))
