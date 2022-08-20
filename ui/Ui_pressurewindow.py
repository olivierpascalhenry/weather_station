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
        self.pressure_lb_4 = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_lb_4.sizePolicy().hasHeightForWidth())
        self.pressure_lb_4.setSizePolicy(sizePolicy)
        self.pressure_lb_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_lb_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb_4.setFont(font)
        self.pressure_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_lb_4.setWordWrap(True)
        self.pressure_lb_4.setObjectName("pressure_lb_4")
        self.gridLayout.addWidget(self.pressure_lb_4, 0, 1, 1, 1)
        self.pressure_lb_2 = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_lb_2.sizePolicy().hasHeightForWidth())
        self.pressure_lb_2.setSizePolicy(sizePolicy)
        self.pressure_lb_2.setMinimumSize(QtCore.QSize(390, 0))
        self.pressure_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb_2.setFont(font)
        self.pressure_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_lb_2.setWordWrap(True)
        self.pressure_lb_2.setObjectName("pressure_lb_2")
        self.gridLayout.addWidget(self.pressure_lb_2, 1, 0, 1, 1)
        self.pressure_lb_5 = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_lb_5.sizePolicy().hasHeightForWidth())
        self.pressure_lb_5.setSizePolicy(sizePolicy)
        self.pressure_lb_5.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_lb_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb_5.setFont(font)
        self.pressure_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_lb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_lb_5.setWordWrap(True)
        self.pressure_lb_5.setObjectName("pressure_lb_5")
        self.gridLayout.addWidget(self.pressure_lb_5, 1, 1, 1, 1)
        self.pressure_lb_3 = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_lb_3.sizePolicy().hasHeightForWidth())
        self.pressure_lb_3.setSizePolicy(sizePolicy)
        self.pressure_lb_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb_3.setFont(font)
        self.pressure_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_lb_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_lb_3.setWordWrap(True)
        self.pressure_lb_3.setObjectName("pressure_lb_3")
        self.gridLayout.addWidget(self.pressure_lb_3, 2, 0, 1, 1)
        self.pressure_lb_6 = QtWidgets.QLabel(pressureWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pressure_lb_6.sizePolicy().hasHeightForWidth())
        self.pressure_lb_6.setSizePolicy(sizePolicy)
        self.pressure_lb_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pressure_lb_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb_6.setFont(font)
        self.pressure_lb_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.pressure_lb_6.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_lb_6.setWordWrap(True)
        self.pressure_lb_6.setObjectName("pressure_lb_6")
        self.gridLayout.addWidget(self.pressure_lb_6, 2, 1, 1, 1)
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
        self.pressure_lb_4.setText(_translate("pressureWindow", "ND"))
        self.pressure_lb_2.setText(_translate("pressureWindow", "Pression atmosphérique MSL :"))
        self.pressure_lb_5.setText(_translate("pressureWindow", "ND"))
        self.pressure_lb_3.setText(_translate("pressureWindow", "Altitude de la station :"))
        self.pressure_lb_6.setText(_translate("pressureWindow", "ND"))
