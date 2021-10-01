# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waitwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_waitWindow(object):
    def setupUi(self, waitWindow):
        waitWindow.setObjectName("waitWindow")
        waitWindow.resize(128, 90)
        waitWindow.setMinimumSize(QtCore.QSize(0, 0))
        waitWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        waitWindow.setFont(font)
        waitWindow.setStyleSheet("QWidget#waitWindow {\n"
"    background-color: rgb(230,230,230);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(waitWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(waitWindow)
        QtCore.QMetaObject.connectSlotsByName(waitWindow)

    def retranslateUi(self, waitWindow):
        pass
