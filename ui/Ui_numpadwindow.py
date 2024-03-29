# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numpad_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_numpadWindow(object):
    def setupUi(self, numpadWindow):
        numpadWindow.setObjectName("numpadWindow")
        numpadWindow.resize(254, 298)
        numpadWindow.setMinimumSize(QtCore.QSize(0, 0))
        numpadWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        numpadWindow.setFont(font)
        numpadWindow.setStyleSheet("QWidget#numpadWindow {\n"
"   background-color: rgb(240,240,240);\n"
"   border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(numpadWindow)
        self.gridLayout_2.setVerticalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.num_line = QtWidgets.QLineEdit(numpadWindow)
        self.num_line.setMinimumSize(QtCore.QSize(0, 40))
        self.num_line.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
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
        self.gridLayout_2.addWidget(self.num_line, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.button_1 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.button_2 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.button_3 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.button_4 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.button_5 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_5, 1, 0, 1, 1)
        self.button_6 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_6, 1, 1, 1, 1)
        self.button_7 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_7, 1, 2, 1, 1)
        self.button_8 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_8, 1, 3, 1, 1)
        self.button_9 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_9, 2, 0, 1, 1)
        self.button_0 = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_0, 2, 1, 1, 1)
        self.button_p = QtWidgets.QToolButton(numpadWindow)
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
        font.setPointSize(26)
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
        self.gridLayout.addWidget(self.button_p, 2, 2, 1, 1)
        self.button_ret = QtWidgets.QToolButton(numpadWindow)
        self.button_ret.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ret.sizePolicy().hasHeightForWidth())
        self.button_ret.setSizePolicy(sizePolicy)
        self.button_ret.setMinimumSize(QtCore.QSize(50, 50))
        self.button_ret.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(26)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bwd_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ret.setIcon(icon)
        self.button_ret.setIconSize(QtCore.QSize(40, 45))
        self.button_ret.setArrowType(QtCore.Qt.NoArrow)
        self.button_ret.setObjectName("button_ret")
        self.gridLayout.addWidget(self.button_ret, 2, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ok_button = QtWidgets.QToolButton(numpadWindow)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_4.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cancel_button = QtWidgets.QToolButton(numpadWindow)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon2)
        self.cancel_button.setIconSize(QtCore.QSize(50, 50))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_4.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.retranslateUi(numpadWindow)
        QtCore.QMetaObject.connectSlotsByName(numpadWindow)

    def retranslateUi(self, numpadWindow):
        _translate = QtCore.QCoreApplication.translate
        self.button_1.setText(_translate("numpadWindow", "1"))
        self.button_2.setText(_translate("numpadWindow", "2"))
        self.button_3.setText(_translate("numpadWindow", "3"))
        self.button_4.setText(_translate("numpadWindow", "4"))
        self.button_5.setText(_translate("numpadWindow", "5"))
        self.button_6.setText(_translate("numpadWindow", "6"))
        self.button_7.setText(_translate("numpadWindow", "7"))
        self.button_8.setText(_translate("numpadWindow", "8"))
        self.button_9.setText(_translate("numpadWindow", "9"))
        self.button_0.setText(_translate("numpadWindow", "0"))
        self.button_p.setText(_translate("numpadWindow", "."))
