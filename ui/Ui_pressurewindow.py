# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pressure_details.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pressureWindow(object):
    def setupUi(self, pressureWindow):
        pressureWindow.setObjectName("pressureWindow")
        pressureWindow.resize(574, 239)
        pressureWindow.setMinimumSize(QtCore.QSize(0, 0))
        pressureWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        pressureWindow.setFont(font)
        pressureWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        pressureWindow.setWindowTitle("")
        pressureWindow.setStyleSheet("QWidget {\n"
"    background-color: #DEEBF7;\n"
"    border: 1px solid rgb(75,75,75);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(pressureWindow)
        self.gridLayout_2.setVerticalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pressure_lb = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_lb.sizePolicy().hasHeightForWidth())
        self.pressure_lb.setSizePolicy(sizePolicy)
        self.pressure_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb.setFont(font)
        self.pressure_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_lb.setWordWrap(True)
        self.pressure_lb.setObjectName("pressure_lb")
        self.gridLayout.addWidget(self.pressure_lb, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pressure_ln = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_ln.sizePolicy().hasHeightForWidth())
        self.pressure_ln.setSizePolicy(sizePolicy)
        self.pressure_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_ln.setFont(font)
        self.pressure_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_ln.setWordWrap(True)
        self.pressure_ln.setObjectName("pressure_ln")
        self.horizontalLayout_2.addWidget(self.pressure_ln)
        self.pressure_unit = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_unit.sizePolicy().hasHeightForWidth())
        self.pressure_unit.setSizePolicy(sizePolicy)
        self.pressure_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_unit.setFont(font)
        self.pressure_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pressure_unit.setWordWrap(True)
        self.pressure_unit.setObjectName("pressure_unit")
        self.horizontalLayout_2.addWidget(self.pressure_unit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.pressuresl_lb = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressuresl_lb.sizePolicy().hasHeightForWidth())
        self.pressuresl_lb.setSizePolicy(sizePolicy)
        self.pressuresl_lb.setMinimumSize(QtCore.QSize(390, 0))
        self.pressuresl_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressuresl_lb.setFont(font)
        self.pressuresl_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressuresl_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressuresl_lb.setWordWrap(True)
        self.pressuresl_lb.setObjectName("pressuresl_lb")
        self.gridLayout.addWidget(self.pressuresl_lb, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pressuresl_ln = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressuresl_ln.sizePolicy().hasHeightForWidth())
        self.pressuresl_ln.setSizePolicy(sizePolicy)
        self.pressuresl_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.pressuresl_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressuresl_ln.setFont(font)
        self.pressuresl_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressuresl_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressuresl_ln.setWordWrap(True)
        self.pressuresl_ln.setObjectName("pressuresl_ln")
        self.horizontalLayout_3.addWidget(self.pressuresl_ln)
        self.pressuresl_unit = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressuresl_unit.sizePolicy().hasHeightForWidth())
        self.pressuresl_unit.setSizePolicy(sizePolicy)
        self.pressuresl_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.pressuresl_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressuresl_unit.setFont(font)
        self.pressuresl_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressuresl_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pressuresl_unit.setWordWrap(True)
        self.pressuresl_unit.setObjectName("pressuresl_unit")
        self.horizontalLayout_3.addWidget(self.pressuresl_unit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.altitude_lb = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.altitude_lb.sizePolicy().hasHeightForWidth())
        self.altitude_lb.setSizePolicy(sizePolicy)
        self.altitude_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.altitude_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.altitude_lb.setFont(font)
        self.altitude_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.altitude_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.altitude_lb.setWordWrap(True)
        self.altitude_lb.setObjectName("altitude_lb")
        self.gridLayout.addWidget(self.altitude_lb, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.altitude_ln = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.altitude_ln.sizePolicy().hasHeightForWidth())
        self.altitude_ln.setSizePolicy(sizePolicy)
        self.altitude_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.altitude_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.altitude_ln.setFont(font)
        self.altitude_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.altitude_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.altitude_ln.setWordWrap(True)
        self.altitude_ln.setObjectName("altitude_ln")
        self.horizontalLayout_4.addWidget(self.altitude_ln)
        self.altitude_unit = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.altitude_unit.sizePolicy().hasHeightForWidth())
        self.altitude_unit.setSizePolicy(sizePolicy)
        self.altitude_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.altitude_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.altitude_unit.setFont(font)
        self.altitude_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.altitude_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.altitude_unit.setWordWrap(True)
        self.altitude_unit.setObjectName("altitude_unit")
        self.horizontalLayout_4.addWidget(self.altitude_unit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QToolButton(pressureWindow)
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
        icon.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(pressureWindow)
        QtCore.QMetaObject.connectSlotsByName(pressureWindow)

    def retranslateUi(self, pressureWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pressure_lb.setText(_translate("pressureWindow", "Pression atmosphérique :"))
        self.pressure_ln.setText(_translate("pressureWindow", "ND"))
        self.pressure_unit.setText(_translate("pressureWindow", "hPa"))
        self.pressuresl_lb.setText(_translate("pressureWindow", "Pression atmosphérique MSL :"))
        self.pressuresl_ln.setText(_translate("pressureWindow", "ND"))
        self.pressuresl_unit.setText(_translate("pressureWindow", "hPa"))
        self.altitude_lb.setText(_translate("pressureWindow", "Altitude de la station :"))
        self.altitude_ln.setText(_translate("pressureWindow", "ND"))
        self.altitude_unit.setText(_translate("pressureWindow", "m"))
