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
        numpadWindow.resize(246, 298)
        numpadWindow.setMinimumSize(QtCore.QSize(0, 0))
        numpadWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        numpadWindow.setFont(font)
        numpadWindow.setStyleSheet("QWidget#numpadWindow {\n"
"   background-color: rgb(230,230,230);\n"
"   border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(numpadWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_1.setFont(font)
        self.button_1.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_1.setObjectName("button_1")
        self.horizontalLayout.addWidget(self.button_1)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_2.setFont(font)
        self.button_2.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_2.setObjectName("button_2")
        self.horizontalLayout.addWidget(self.button_2)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_3.setFont(font)
        self.button_3.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_3.setObjectName("button_3")
        self.horizontalLayout.addWidget(self.button_3)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_4.setFont(font)
        self.button_4.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_4.setObjectName("button_4")
        self.horizontalLayout.addWidget(self.button_4)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_9.setFont(font)
        self.button_9.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_9.setObjectName("button_9")
        self.horizontalLayout_3.addWidget(self.button_9)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_0.setFont(font)
        self.button_0.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_0.setObjectName("button_0")
        self.horizontalLayout_3.addWidget(self.button_0)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_ret.setFont(font)
        self.button_ret.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_ret.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/bwd_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_ret.setIcon(icon)
        self.button_ret.setIconSize(QtCore.QSize(40, 45))
        self.button_ret.setArrowType(QtCore.Qt.NoArrow)
        self.button_ret.setObjectName("button_ret")
        self.horizontalLayout_3.addWidget(self.button_ret)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
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
        self.ok_button.setIconSize(QtCore.QSize(45, 45))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_4.addWidget(self.ok_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
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
        self.cancel_button.setIconSize(QtCore.QSize(45, 45))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_4.addWidget(self.cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_5.setFont(font)
        self.button_5.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_5.setObjectName("button_5")
        self.horizontalLayout_2.addWidget(self.button_5)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_6.setFont(font)
        self.button_6.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_6.setObjectName("button_6")
        self.horizontalLayout_2.addWidget(self.button_6)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_7.setFont(font)
        self.button_7.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_2.addWidget(self.button_7)
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
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.button_8.setFont(font)
        self.button_8.setStyleSheet("QToolButton {\n"
"    border: 0px solid rgb(75,75,75);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(200,200,200);\n"
"    width: 27px;\n"
"    height: 27px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.button_8.setObjectName("button_8")
        self.horizontalLayout_2.addWidget(self.button_8)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.num_line = QtWidgets.QLineEdit(numpadWindow)
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
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.num_line.setText("")
        self.num_line.setFrame(True)
        self.num_line.setCursorPosition(0)
        self.num_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.num_line.setReadOnly(True)
        self.num_line.setClearButtonEnabled(False)
        self.num_line.setObjectName("num_line")
        self.gridLayout.addWidget(self.num_line, 0, 0, 1, 1)

        self.retranslateUi(numpadWindow)
        QtCore.QMetaObject.connectSlotsByName(numpadWindow)

    def retranslateUi(self, numpadWindow):
        _translate = QtCore.QCoreApplication.translate
        self.button_1.setText(_translate("numpadWindow", "1"))
        self.button_2.setText(_translate("numpadWindow", "2"))
        self.button_3.setText(_translate("numpadWindow", "3"))
        self.button_4.setText(_translate("numpadWindow", "4"))
        self.button_9.setText(_translate("numpadWindow", "9"))
        self.button_0.setText(_translate("numpadWindow", "0"))
        self.button_5.setText(_translate("numpadWindow", "5"))
        self.button_6.setText(_translate("numpadWindow", "6"))
        self.button_7.setText(_translate("numpadWindow", "7"))
        self.button_8.setText(_translate("numpadWindow", "8"))
