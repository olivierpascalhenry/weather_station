# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_hum_details.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_temphumWindow(object):
    def setupUi(self, temphumWindow):
        temphumWindow.setObjectName("temphumWindow")
        temphumWindow.resize(340, 239)
        temphumWindow.setMinimumSize(QtCore.QSize(0, 0))
        temphumWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        temphumWindow.setFont(font)
        temphumWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        temphumWindow.setWindowTitle("")
        temphumWindow.setStyleSheet("QWidget {\n"
"    background-color: #DEEBF7;\n"
"    border: 1px solid rgb(75,75,75);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(temphumWindow)
        self.gridLayout_2.setVerticalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.hum_lb = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hum_lb.sizePolicy().hasHeightForWidth())
        self.hum_lb.setSizePolicy(sizePolicy)
        self.hum_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.hum_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hum_lb.setFont(font)
        self.hum_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hum_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hum_lb.setWordWrap(True)
        self.hum_lb.setObjectName("hum_lb")
        self.gridLayout.addWidget(self.hum_lb, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hum_ln = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hum_ln.sizePolicy().hasHeightForWidth())
        self.hum_ln.setSizePolicy(sizePolicy)
        self.hum_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.hum_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hum_ln.setFont(font)
        self.hum_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hum_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hum_ln.setWordWrap(True)
        self.hum_ln.setObjectName("hum_ln")
        self.horizontalLayout_2.addWidget(self.hum_ln)
        self.hum_unit = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hum_unit.sizePolicy().hasHeightForWidth())
        self.hum_unit.setSizePolicy(sizePolicy)
        self.hum_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.hum_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.hum_unit.setFont(font)
        self.hum_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.hum_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hum_unit.setWordWrap(True)
        self.hum_unit.setObjectName("hum_unit")
        self.horizontalLayout_2.addWidget(self.hum_unit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.temp_lb = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_lb.sizePolicy().hasHeightForWidth())
        self.temp_lb.setSizePolicy(sizePolicy)
        self.temp_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.temp_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.gridLayout.addWidget(self.temp_lb, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.temp_ln = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_ln.sizePolicy().hasHeightForWidth())
        self.temp_ln.setSizePolicy(sizePolicy)
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
        self.temp_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temp_ln.setWordWrap(True)
        self.temp_ln.setObjectName("temp_ln")
        self.horizontalLayout_3.addWidget(self.temp_ln)
        self.temp_unit = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_unit.sizePolicy().hasHeightForWidth())
        self.temp_unit.setSizePolicy(sizePolicy)
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
        self.horizontalLayout_3.addWidget(self.temp_unit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.dew_lb = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dew_lb.sizePolicy().hasHeightForWidth())
        self.dew_lb.setSizePolicy(sizePolicy)
        self.dew_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.dew_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dew_lb.setFont(font)
        self.dew_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.dew_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dew_lb.setWordWrap(True)
        self.dew_lb.setObjectName("dew_lb")
        self.gridLayout.addWidget(self.dew_lb, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dew_ln = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dew_ln.sizePolicy().hasHeightForWidth())
        self.dew_ln.setSizePolicy(sizePolicy)
        self.dew_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.dew_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dew_ln.setFont(font)
        self.dew_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.dew_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dew_ln.setWordWrap(True)
        self.dew_ln.setObjectName("dew_ln")
        self.horizontalLayout_4.addWidget(self.dew_ln)
        self.dew_unit = QtWidgets.QLabel(temphumWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dew_unit.sizePolicy().hasHeightForWidth())
        self.dew_unit.setSizePolicy(sizePolicy)
        self.dew_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.dew_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dew_unit.setFont(font)
        self.dew_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.dew_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dew_unit.setWordWrap(True)
        self.dew_unit.setObjectName("dew_unit")
        self.horizontalLayout_4.addWidget(self.dew_unit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QToolButton(temphumWindow)
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

        self.retranslateUi(temphumWindow)
        QtCore.QMetaObject.connectSlotsByName(temphumWindow)

    def retranslateUi(self, temphumWindow):
        _translate = QtCore.QCoreApplication.translate
        self.hum_lb.setText(_translate("temphumWindow", "Humidité :"))
        self.hum_ln.setText(_translate("temphumWindow", "ND"))
        self.hum_unit.setText(_translate("temphumWindow", "%"))
        self.temp_lb.setText(_translate("temphumWindow", "Température :"))
        self.temp_ln.setText(_translate("temphumWindow", "ND"))
        self.temp_unit.setText(_translate("temphumWindow", "°C"))
        self.dew_lb.setText(_translate("temphumWindow", "Point de rosée :"))
        self.dew_ln.setText(_translate("temphumWindow", "ND"))
        self.dew_unit.setText(_translate("temphumWindow", "°C"))
