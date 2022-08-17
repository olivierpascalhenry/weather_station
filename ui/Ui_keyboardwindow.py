# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions.gui_widgets import QDoublePushButton


class Ui_keyboardWindow(object):
    def setupUi(self, keyboardWindow):
        keyboardWindow.setObjectName("keyboardWindow")
        keyboardWindow.resize(614, 428)
        keyboardWindow.setMinimumSize(QtCore.QSize(0, 0))
        keyboardWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        keyboardWindow.setFont(font)
        keyboardWindow.setStyleSheet("QWidget#keyboardWindow {\n"
"   background-color: rgb(240,240,240);\n"
"   border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(keyboardWindow)
        self.gridLayout_2.setContentsMargins(11, -1, -1, -1)
        self.gridLayout_2.setVerticalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.num_line = QtWidgets.QLineEdit(keyboardWindow)
        self.num_line.setMinimumSize(QtCore.QSize(0, 40))
        self.num_line.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.num_line.setFont(font)
        self.num_line.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.num_line.setText("")
        self.num_line.setFrame(True)
        self.num_line.setCursorPosition(0)
        self.num_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num_line.setReadOnly(True)
        self.num_line.setClearButtonEnabled(False)
        self.num_line.setObjectName("num_line")
        self.gridLayout_2.addWidget(self.num_line, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.button_1 = QtWidgets.QToolButton(keyboardWindow)
        self.button_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy)
        self.button_1.setMinimumSize(QtCore.QSize(50, 50))
        self.button_1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 0, 0, 1, 1)
        self.button_2 = QtWidgets.QToolButton(keyboardWindow)
        self.button_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy)
        self.button_2.setMinimumSize(QtCore.QSize(50, 50))
        self.button_2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 0, 1, 1, 1)
        self.button_3 = QtWidgets.QToolButton(keyboardWindow)
        self.button_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy)
        self.button_3.setMinimumSize(QtCore.QSize(50, 50))
        self.button_3.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 0, 2, 1, 1)
        self.button_4 = QtWidgets.QToolButton(keyboardWindow)
        self.button_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy)
        self.button_4.setMinimumSize(QtCore.QSize(50, 50))
        self.button_4.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 0, 3, 1, 1)
        self.button_5 = QtWidgets.QToolButton(keyboardWindow)
        self.button_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy)
        self.button_5.setMinimumSize(QtCore.QSize(50, 50))
        self.button_5.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 0, 4, 1, 1)
        self.button_6 = QtWidgets.QToolButton(keyboardWindow)
        self.button_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy)
        self.button_6.setMinimumSize(QtCore.QSize(50, 50))
        self.button_6.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 0, 5, 1, 1)
        self.button_7 = QtWidgets.QToolButton(keyboardWindow)
        self.button_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy)
        self.button_7.setMinimumSize(QtCore.QSize(50, 50))
        self.button_7.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 0, 6, 1, 1)
        self.button_8 = QtWidgets.QToolButton(keyboardWindow)
        self.button_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy)
        self.button_8.setMinimumSize(QtCore.QSize(50, 50))
        self.button_8.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 0, 7, 1, 1)
        self.button_9 = QtWidgets.QToolButton(keyboardWindow)
        self.button_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy)
        self.button_9.setMinimumSize(QtCore.QSize(50, 50))
        self.button_9.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 0, 8, 1, 1)
        self.button_0 = QtWidgets.QToolButton(keyboardWindow)
        self.button_0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy)
        self.button_0.setMinimumSize(QtCore.QSize(50, 50))
        self.button_0.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 0, 9, 1, 1)
        self.button_a = QtWidgets.QToolButton(keyboardWindow)
        self.button_a.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_a.sizePolicy().hasHeightForWidth())
        self.button_a.setSizePolicy(sizePolicy)
        self.button_a.setMinimumSize(QtCore.QSize(50, 50))
        self.button_a.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_a.setFont(font)
        self.button_a.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_a.setObjectName("button_a")
        self.gridLayout.addWidget(self.button_a, 1, 0, 1, 1)
        self.button_z = QtWidgets.QToolButton(keyboardWindow)
        self.button_z.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_z.sizePolicy().hasHeightForWidth())
        self.button_z.setSizePolicy(sizePolicy)
        self.button_z.setMinimumSize(QtCore.QSize(50, 50))
        self.button_z.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_z.setFont(font)
        self.button_z.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_z.setObjectName("button_z")
        self.gridLayout.addWidget(self.button_z, 1, 1, 1, 1)
        self.button_e = QtWidgets.QToolButton(keyboardWindow)
        self.button_e.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_e.sizePolicy().hasHeightForWidth())
        self.button_e.setSizePolicy(sizePolicy)
        self.button_e.setMinimumSize(QtCore.QSize(50, 50))
        self.button_e.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_e.setFont(font)
        self.button_e.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_e.setObjectName("button_e")
        self.gridLayout.addWidget(self.button_e, 1, 2, 1, 1)
        self.button_r = QtWidgets.QToolButton(keyboardWindow)
        self.button_r.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_r.sizePolicy().hasHeightForWidth())
        self.button_r.setSizePolicy(sizePolicy)
        self.button_r.setMinimumSize(QtCore.QSize(50, 50))
        self.button_r.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_r.setFont(font)
        self.button_r.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_r.setObjectName("button_r")
        self.gridLayout.addWidget(self.button_r, 1, 3, 1, 1)
        self.button_t = QtWidgets.QToolButton(keyboardWindow)
        self.button_t.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_t.sizePolicy().hasHeightForWidth())
        self.button_t.setSizePolicy(sizePolicy)
        self.button_t.setMinimumSize(QtCore.QSize(50, 50))
        self.button_t.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_t.setFont(font)
        self.button_t.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_t.setObjectName("button_t")
        self.gridLayout.addWidget(self.button_t, 1, 4, 1, 1)
        self.button_y = QtWidgets.QToolButton(keyboardWindow)
        self.button_y.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_y.sizePolicy().hasHeightForWidth())
        self.button_y.setSizePolicy(sizePolicy)
        self.button_y.setMinimumSize(QtCore.QSize(50, 50))
        self.button_y.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_y.setFont(font)
        self.button_y.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_y.setObjectName("button_y")
        self.gridLayout.addWidget(self.button_y, 1, 5, 1, 1)
        self.button_u = QtWidgets.QToolButton(keyboardWindow)
        self.button_u.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_u.sizePolicy().hasHeightForWidth())
        self.button_u.setSizePolicy(sizePolicy)
        self.button_u.setMinimumSize(QtCore.QSize(50, 50))
        self.button_u.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_u.setFont(font)
        self.button_u.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_u.setObjectName("button_u")
        self.gridLayout.addWidget(self.button_u, 1, 6, 1, 1)
        self.button_i = QtWidgets.QToolButton(keyboardWindow)
        self.button_i.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_i.sizePolicy().hasHeightForWidth())
        self.button_i.setSizePolicy(sizePolicy)
        self.button_i.setMinimumSize(QtCore.QSize(50, 50))
        self.button_i.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_i.setFont(font)
        self.button_i.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_i.setObjectName("button_i")
        self.gridLayout.addWidget(self.button_i, 1, 7, 1, 1)
        self.button_o = QtWidgets.QToolButton(keyboardWindow)
        self.button_o.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_o.sizePolicy().hasHeightForWidth())
        self.button_o.setSizePolicy(sizePolicy)
        self.button_o.setMinimumSize(QtCore.QSize(50, 50))
        self.button_o.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_o.setFont(font)
        self.button_o.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_o.setObjectName("button_o")
        self.gridLayout.addWidget(self.button_o, 1, 8, 1, 1)
        self.button_p = QtWidgets.QToolButton(keyboardWindow)
        self.button_p.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_p.sizePolicy().hasHeightForWidth())
        self.button_p.setSizePolicy(sizePolicy)
        self.button_p.setMinimumSize(QtCore.QSize(50, 50))
        self.button_p.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_p.setFont(font)
        self.button_p.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_p.setObjectName("button_p")
        self.gridLayout.addWidget(self.button_p, 1, 9, 1, 1)
        self.button_q = QtWidgets.QToolButton(keyboardWindow)
        self.button_q.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_q.sizePolicy().hasHeightForWidth())
        self.button_q.setSizePolicy(sizePolicy)
        self.button_q.setMinimumSize(QtCore.QSize(50, 50))
        self.button_q.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_q.setFont(font)
        self.button_q.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_q.setObjectName("button_q")
        self.gridLayout.addWidget(self.button_q, 2, 0, 1, 1)
        self.button_s = QtWidgets.QToolButton(keyboardWindow)
        self.button_s.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_s.sizePolicy().hasHeightForWidth())
        self.button_s.setSizePolicy(sizePolicy)
        self.button_s.setMinimumSize(QtCore.QSize(50, 50))
        self.button_s.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_s.setFont(font)
        self.button_s.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_s.setObjectName("button_s")
        self.gridLayout.addWidget(self.button_s, 2, 1, 1, 1)
        self.button_d = QtWidgets.QToolButton(keyboardWindow)
        self.button_d.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_d.sizePolicy().hasHeightForWidth())
        self.button_d.setSizePolicy(sizePolicy)
        self.button_d.setMinimumSize(QtCore.QSize(50, 50))
        self.button_d.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_d.setFont(font)
        self.button_d.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_d.setObjectName("button_d")
        self.gridLayout.addWidget(self.button_d, 2, 2, 1, 1)
        self.button_f = QtWidgets.QToolButton(keyboardWindow)
        self.button_f.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_f.sizePolicy().hasHeightForWidth())
        self.button_f.setSizePolicy(sizePolicy)
        self.button_f.setMinimumSize(QtCore.QSize(50, 50))
        self.button_f.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_f.setFont(font)
        self.button_f.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_f.setObjectName("button_f")
        self.gridLayout.addWidget(self.button_f, 2, 3, 1, 1)
        self.button_g = QtWidgets.QToolButton(keyboardWindow)
        self.button_g.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_g.sizePolicy().hasHeightForWidth())
        self.button_g.setSizePolicy(sizePolicy)
        self.button_g.setMinimumSize(QtCore.QSize(50, 50))
        self.button_g.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_g.setFont(font)
        self.button_g.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_g.setObjectName("button_g")
        self.gridLayout.addWidget(self.button_g, 2, 4, 1, 1)
        self.button_h = QtWidgets.QToolButton(keyboardWindow)
        self.button_h.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_h.sizePolicy().hasHeightForWidth())
        self.button_h.setSizePolicy(sizePolicy)
        self.button_h.setMinimumSize(QtCore.QSize(50, 50))
        self.button_h.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_h.setFont(font)
        self.button_h.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_h.setObjectName("button_h")
        self.gridLayout.addWidget(self.button_h, 2, 5, 1, 1)
        self.button_j = QtWidgets.QToolButton(keyboardWindow)
        self.button_j.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_j.sizePolicy().hasHeightForWidth())
        self.button_j.setSizePolicy(sizePolicy)
        self.button_j.setMinimumSize(QtCore.QSize(50, 50))
        self.button_j.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_j.setFont(font)
        self.button_j.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_j.setObjectName("button_j")
        self.gridLayout.addWidget(self.button_j, 2, 6, 1, 1)
        self.button_k = QtWidgets.QToolButton(keyboardWindow)
        self.button_k.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_k.sizePolicy().hasHeightForWidth())
        self.button_k.setSizePolicy(sizePolicy)
        self.button_k.setMinimumSize(QtCore.QSize(50, 50))
        self.button_k.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_k.setFont(font)
        self.button_k.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_k.setObjectName("button_k")
        self.gridLayout.addWidget(self.button_k, 2, 7, 1, 1)
        self.button_l = QtWidgets.QToolButton(keyboardWindow)
        self.button_l.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_l.sizePolicy().hasHeightForWidth())
        self.button_l.setSizePolicy(sizePolicy)
        self.button_l.setMinimumSize(QtCore.QSize(50, 50))
        self.button_l.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_l.setFont(font)
        self.button_l.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_l.setObjectName("button_l")
        self.gridLayout.addWidget(self.button_l, 2, 8, 1, 1)
        self.button_m = QtWidgets.QToolButton(keyboardWindow)
        self.button_m.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_m.sizePolicy().hasHeightForWidth())
        self.button_m.setSizePolicy(sizePolicy)
        self.button_m.setMinimumSize(QtCore.QSize(50, 50))
        self.button_m.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_m.setFont(font)
        self.button_m.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_m.setObjectName("button_m")
        self.gridLayout.addWidget(self.button_m, 2, 9, 1, 1)
        self.button_w = QtWidgets.QToolButton(keyboardWindow)
        self.button_w.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_w.sizePolicy().hasHeightForWidth())
        self.button_w.setSizePolicy(sizePolicy)
        self.button_w.setMinimumSize(QtCore.QSize(50, 50))
        self.button_w.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_w.setFont(font)
        self.button_w.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_w.setObjectName("button_w")
        self.gridLayout.addWidget(self.button_w, 3, 0, 1, 1)
        self.button_x = QtWidgets.QToolButton(keyboardWindow)
        self.button_x.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_x.sizePolicy().hasHeightForWidth())
        self.button_x.setSizePolicy(sizePolicy)
        self.button_x.setMinimumSize(QtCore.QSize(50, 50))
        self.button_x.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_x.setFont(font)
        self.button_x.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_x.setObjectName("button_x")
        self.gridLayout.addWidget(self.button_x, 3, 1, 1, 1)
        self.button_c = QtWidgets.QToolButton(keyboardWindow)
        self.button_c.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_c.sizePolicy().hasHeightForWidth())
        self.button_c.setSizePolicy(sizePolicy)
        self.button_c.setMinimumSize(QtCore.QSize(50, 50))
        self.button_c.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_c.setFont(font)
        self.button_c.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_c.setObjectName("button_c")
        self.gridLayout.addWidget(self.button_c, 3, 2, 1, 1)
        self.button_v = QtWidgets.QToolButton(keyboardWindow)
        self.button_v.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_v.sizePolicy().hasHeightForWidth())
        self.button_v.setSizePolicy(sizePolicy)
        self.button_v.setMinimumSize(QtCore.QSize(50, 50))
        self.button_v.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_v.setFont(font)
        self.button_v.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_v.setObjectName("button_v")
        self.gridLayout.addWidget(self.button_v, 3, 3, 1, 1)
        self.button_b = QtWidgets.QToolButton(keyboardWindow)
        self.button_b.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_b.sizePolicy().hasHeightForWidth())
        self.button_b.setSizePolicy(sizePolicy)
        self.button_b.setMinimumSize(QtCore.QSize(50, 50))
        self.button_b.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_b.setFont(font)
        self.button_b.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_b.setObjectName("button_b")
        self.gridLayout.addWidget(self.button_b, 3, 4, 1, 1)
        self.button_n = QtWidgets.QToolButton(keyboardWindow)
        self.button_n.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_n.sizePolicy().hasHeightForWidth())
        self.button_n.setSizePolicy(sizePolicy)
        self.button_n.setMinimumSize(QtCore.QSize(50, 50))
        self.button_n.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_n.setFont(font)
        self.button_n.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_n.setObjectName("button_n")
        self.gridLayout.addWidget(self.button_n, 3, 5, 1, 1)
        self.button_2p = QtWidgets.QToolButton(keyboardWindow)
        self.button_2p.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_2p.sizePolicy().hasHeightForWidth())
        self.button_2p.setSizePolicy(sizePolicy)
        self.button_2p.setMinimumSize(QtCore.QSize(50, 50))
        self.button_2p.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_2p.setFont(font)
        self.button_2p.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_2p.setObjectName("button_2p")
        self.gridLayout.addWidget(self.button_2p, 3, 6, 1, 1)
        self.button_pt = QtWidgets.QToolButton(keyboardWindow)
        self.button_pt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pt.sizePolicy().hasHeightForWidth())
        self.button_pt.setSizePolicy(sizePolicy)
        self.button_pt.setMinimumSize(QtCore.QSize(50, 50))
        self.button_pt.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_pt.setFont(font)
        self.button_pt.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_pt.setObjectName("button_pt")
        self.gridLayout.addWidget(self.button_pt, 3, 7, 1, 1)
        self.button_us = QtWidgets.QToolButton(keyboardWindow)
        self.button_us.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_us.sizePolicy().hasHeightForWidth())
        self.button_us.setSizePolicy(sizePolicy)
        self.button_us.setMinimumSize(QtCore.QSize(50, 50))
        self.button_us.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_us.setFont(font)
        self.button_us.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_us.setObjectName("button_us")
        self.gridLayout.addWidget(self.button_us, 3, 8, 1, 1)
        self.button_ti = QtWidgets.QToolButton(keyboardWindow)
        self.button_ti.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ti.sizePolicy().hasHeightForWidth())
        self.button_ti.setSizePolicy(sizePolicy)
        self.button_ti.setMinimumSize(QtCore.QSize(50, 50))
        self.button_ti.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_ti.setFont(font)
        self.button_ti.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_ti.setObjectName("button_ti")
        self.gridLayout.addWidget(self.button_ti, 3, 9, 1, 1)
        self.button_up = QDoublePushButton(keyboardWindow)  # QtWidgets.QToolButton(keyboardWindow)
        self.button_up.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy)
        self.button_up.setMinimumSize(QtCore.QSize(110, 50))
        self.button_up.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_up.setFont(font)
        self.button_up.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/up_arrow_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_up.setIcon(icon)
        self.button_up.setObjectName("button_up")
        self.gridLayout.addWidget(self.button_up, 4, 0, 1, 2)
        self.button_sp = QtWidgets.QToolButton(keyboardWindow)
        self.button_sp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sp.sizePolicy().hasHeightForWidth())
        self.button_sp.setSizePolicy(sizePolicy)
        self.button_sp.setMinimumSize(QtCore.QSize(290, 50))
        self.button_sp.setMaximumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_sp.setFont(font)
        self.button_sp.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_sp.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/escape_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_sp.setIcon(icon1)
        self.button_sp.setIconSize(QtCore.QSize(107, 40))
        self.button_sp.setObjectName("button_sp")
        self.gridLayout.addWidget(self.button_sp, 4, 2, 1, 5)
        self.button_sl = QtWidgets.QToolButton(keyboardWindow)
        self.button_sl.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_sl.sizePolicy().hasHeightForWidth())
        self.button_sl.setSizePolicy(sizePolicy)
        self.button_sl.setMinimumSize(QtCore.QSize(50, 50))
        self.button_sl.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_sl.setFont(font)
        self.button_sl.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_sl.setObjectName("button_sl")
        self.gridLayout.addWidget(self.button_sl, 4, 7, 1, 1)
        self.button_ret = QtWidgets.QToolButton(keyboardWindow)
        self.button_ret.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ret.sizePolicy().hasHeightForWidth())
        self.button_ret.setSizePolicy(sizePolicy)
        self.button_ret.setMinimumSize(QtCore.QSize(110, 50))
        self.button_ret.setMaximumSize(QtCore.QSize(110, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_ret.setFont(font)
        self.button_ret.setStyleSheet("QToolButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:pressed  {\n"
"    transform: translateY(10px);\n"
"    background-color: rgb(96,96,96);\n"
"}")
        self.button_ret.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/bwd_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ret.setIcon(icon2)
        self.button_ret.setIconSize(QtCore.QSize(40, 45))
        self.button_ret.setArrowType(QtCore.Qt.NoArrow)
        self.button_ret.setObjectName("button_ret")
        self.gridLayout.addWidget(self.button_ret, 4, 8, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ok_button = QtWidgets.QToolButton(keyboardWindow)
        self.ok_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(50, 50))
        self.ok_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ok_button.setFont(font)
        self.ok_button.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ok_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon3)
        self.ok_button.setIconSize(QtCore.QSize(45, 45))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_4.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cancel_button = QtWidgets.QToolButton(keyboardWindow)
        self.cancel_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMinimumSize(QtCore.QSize(50, 50))
        self.cancel_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.cancel_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon4)
        self.cancel_button.setIconSize(QtCore.QSize(45, 45))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_4.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 2)

        self.retranslateUi(keyboardWindow)
        QtCore.QMetaObject.connectSlotsByName(keyboardWindow)

    def retranslateUi(self, keyboardWindow):
        _translate = QtCore.QCoreApplication.translate
        self.button_1.setText(_translate("keyboardWindow", "1"))
        self.button_2.setText(_translate("keyboardWindow", "2"))
        self.button_3.setText(_translate("keyboardWindow", "3"))
        self.button_4.setText(_translate("keyboardWindow", "4"))
        self.button_5.setText(_translate("keyboardWindow", "5"))
        self.button_6.setText(_translate("keyboardWindow", "6"))
        self.button_7.setText(_translate("keyboardWindow", "7"))
        self.button_8.setText(_translate("keyboardWindow", "8"))
        self.button_9.setText(_translate("keyboardWindow", "9"))
        self.button_0.setText(_translate("keyboardWindow", "0"))
        self.button_a.setText(_translate("keyboardWindow", "a"))
        self.button_z.setText(_translate("keyboardWindow", "z"))
        self.button_e.setText(_translate("keyboardWindow", "e"))
        self.button_r.setText(_translate("keyboardWindow", "r"))
        self.button_t.setText(_translate("keyboardWindow", "t"))
        self.button_y.setText(_translate("keyboardWindow", "y"))
        self.button_u.setText(_translate("keyboardWindow", "u"))
        self.button_i.setText(_translate("keyboardWindow", "i"))
        self.button_o.setText(_translate("keyboardWindow", "o"))
        self.button_p.setText(_translate("keyboardWindow", "p"))
        self.button_q.setText(_translate("keyboardWindow", "q"))
        self.button_s.setText(_translate("keyboardWindow", "s"))
        self.button_d.setText(_translate("keyboardWindow", "d"))
        self.button_f.setText(_translate("keyboardWindow", "f"))
        self.button_g.setText(_translate("keyboardWindow", "g"))
        self.button_h.setText(_translate("keyboardWindow", "h"))
        self.button_j.setText(_translate("keyboardWindow", "j"))
        self.button_k.setText(_translate("keyboardWindow", "k"))
        self.button_l.setText(_translate("keyboardWindow", "l"))
        self.button_m.setText(_translate("keyboardWindow", "m"))
        self.button_w.setText(_translate("keyboardWindow", "w"))
        self.button_x.setText(_translate("keyboardWindow", "x"))
        self.button_c.setText(_translate("keyboardWindow", "c"))
        self.button_v.setText(_translate("keyboardWindow", "v"))
        self.button_b.setText(_translate("keyboardWindow", "b"))
        self.button_n.setText(_translate("keyboardWindow", "n"))
        self.button_2p.setText(_translate("keyboardWindow", ":"))
        self.button_pt.setText(_translate("keyboardWindow", "."))
        self.button_us.setText(_translate("keyboardWindow", "_"))
        self.button_ti.setText(_translate("keyboardWindow", "-"))
        self.button_up.setText(_translate("keyboardWindow", "^"))
        self.button_sl.setText(_translate("keyboardWindow", "/"))
