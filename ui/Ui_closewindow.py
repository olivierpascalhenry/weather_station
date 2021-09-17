# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closewindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_closeWindow(object):
    def setupUi(self, closeWindow):
        closeWindow.setObjectName("closeWindow")
        closeWindow.resize(286, 182)
        closeWindow.setMinimumSize(QtCore.QSize(0, 0))
        closeWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        closeWindow.setFont(font)
        closeWindow.setStyleSheet("QWidget#closeWindow {\n"
"    background-color: rgb(230,230,230);\n"
"    border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(closeWindow)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(46, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.exit_button = QtWidgets.QToolButton(closeWindow)
        self.exit_button.setMinimumSize(QtCore.QSize(150, 35))
        self.exit_button.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.exit_button.setFont(font)
        self.exit_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.reboot_button = QtWidgets.QToolButton(closeWindow)
        self.reboot_button.setMinimumSize(QtCore.QSize(150, 35))
        self.reboot_button.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.reboot_button.setFont(font)
        self.reboot_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.reboot_button.setObjectName("reboot_button")
        self.verticalLayout.addWidget(self.reboot_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.shutdown_button = QtWidgets.QToolButton(closeWindow)
        self.shutdown_button.setMinimumSize(QtCore.QSize(150, 35))
        self.shutdown_button.setMaximumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.shutdown_button.setFont(font)
        self.shutdown_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #f0f0f0, stop:1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #ecf4fc, stop:1 #dcecfc);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                    stop:0 #daecfc, stop:1 #c4e0fc);\n"
"}")
        self.shutdown_button.setObjectName("shutdown_button")
        self.verticalLayout.addWidget(self.shutdown_button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)

        self.retranslateUi(closeWindow)
        QtCore.QMetaObject.connectSlotsByName(closeWindow)

    def retranslateUi(self, closeWindow):
        _translate = QtCore.QCoreApplication.translate
        self.exit_button.setText(_translate("closeWindow", "Quitter"))
        self.reboot_button.setText(_translate("closeWindow", "Redémarrer"))
        self.shutdown_button.setText(_translate("closeWindow", "Eteindre"))
