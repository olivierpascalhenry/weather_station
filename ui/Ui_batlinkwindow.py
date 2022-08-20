# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bat_link_details.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_batlinkWindow(object):
    def setupUi(self, batlinkWindow):
        batlinkWindow.setObjectName("batlinkWindow")
        batlinkWindow.resize(306, 200)
        batlinkWindow.setMinimumSize(QtCore.QSize(0, 0))
        batlinkWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        batlinkWindow.setFont(font)
        batlinkWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        batlinkWindow.setWindowTitle("")
        batlinkWindow.setStyleSheet("QWidget {\n"
"    background-color: #DEEBF7;\n"
"    border: 1px solid rgb(75,75,75);\n"
"}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(batlinkWindow)
        self.gridLayout_2.setVerticalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.batterie_lb = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batterie_lb.sizePolicy().hasHeightForWidth())
        self.batterie_lb.setSizePolicy(sizePolicy)
        self.batterie_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.batterie_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.batterie_lb.setFont(font)
        self.batterie_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.batterie_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.batterie_lb.setWordWrap(True)
        self.batterie_lb.setObjectName("batterie_lb")
        self.gridLayout.addWidget(self.batterie_lb, 0, 0, 1, 1)
        self.batterie_lb_2 = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batterie_lb_2.sizePolicy().hasHeightForWidth())
        self.batterie_lb_2.setSizePolicy(sizePolicy)
        self.batterie_lb_2.setMinimumSize(QtCore.QSize(0, 0))
        self.batterie_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.batterie_lb_2.setFont(font)
        self.batterie_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.batterie_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.batterie_lb_2.setWordWrap(True)
        self.batterie_lb_2.setObjectName("batterie_lb_2")
        self.gridLayout.addWidget(self.batterie_lb_2, 0, 1, 1, 1)
        self.signal_lb = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signal_lb.sizePolicy().hasHeightForWidth())
        self.signal_lb.setSizePolicy(sizePolicy)
        self.signal_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.signal_lb.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.signal_lb.setFont(font)
        self.signal_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.signal_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.signal_lb.setWordWrap(True)
        self.signal_lb.setObjectName("signal_lb")
        self.gridLayout.addWidget(self.signal_lb, 1, 0, 1, 1)
        self.signal_lb_3 = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signal_lb_3.sizePolicy().hasHeightForWidth())
        self.signal_lb_3.setSizePolicy(sizePolicy)
        self.signal_lb_3.setMinimumSize(QtCore.QSize(0, 0))
        self.signal_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.signal_lb_3.setFont(font)
        self.signal_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.signal_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_lb_3.setWordWrap(True)
        self.signal_lb_3.setObjectName("signal_lb_3")
        self.gridLayout.addWidget(self.signal_lb_3, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_button = QtWidgets.QToolButton(batlinkWindow)
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

        self.retranslateUi(batlinkWindow)
        QtCore.QMetaObject.connectSlotsByName(batlinkWindow)

    def retranslateUi(self, batlinkWindow):
        _translate = QtCore.QCoreApplication.translate
        self.batterie_lb.setText(_translate("batlinkWindow", "Batterie :"))
        self.batterie_lb_2.setText(_translate("batlinkWindow", "100 %"))
        self.signal_lb.setText(_translate("batlinkWindow", "Qualité signal :"))
        self.signal_lb_3.setText(_translate("batlinkWindow", "100 %"))
