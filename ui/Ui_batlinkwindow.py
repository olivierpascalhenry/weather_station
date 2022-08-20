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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.batterie_ln = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batterie_ln.sizePolicy().hasHeightForWidth())
        self.batterie_ln.setSizePolicy(sizePolicy)
        self.batterie_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.batterie_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.batterie_ln.setFont(font)
        self.batterie_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.batterie_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.batterie_ln.setWordWrap(True)
        self.batterie_ln.setObjectName("batterie_ln")
        self.horizontalLayout_2.addWidget(self.batterie_ln)
        self.batterie_unit = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.batterie_unit.sizePolicy().hasHeightForWidth())
        self.batterie_unit.setSizePolicy(sizePolicy)
        self.batterie_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.batterie_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.batterie_unit.setFont(font)
        self.batterie_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.batterie_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.batterie_unit.setWordWrap(True)
        self.batterie_unit.setObjectName("batterie_unit")
        self.horizontalLayout_2.addWidget(self.batterie_unit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.signal_ln = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signal_ln.sizePolicy().hasHeightForWidth())
        self.signal_ln.setSizePolicy(sizePolicy)
        self.signal_ln.setMinimumSize(QtCore.QSize(0, 0))
        self.signal_ln.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.signal_ln.setFont(font)
        self.signal_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.signal_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.signal_ln.setWordWrap(True)
        self.signal_ln.setObjectName("signal_ln")
        self.horizontalLayout_3.addWidget(self.signal_ln)
        self.signal_unit = QtWidgets.QLabel(batlinkWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signal_unit.sizePolicy().hasHeightForWidth())
        self.signal_unit.setSizePolicy(sizePolicy)
        self.signal_unit.setMinimumSize(QtCore.QSize(0, 0))
        self.signal_unit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.signal_unit.setFont(font)
        self.signal_unit.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    border: 0px solid rgb(75,75,75);\n"
"}")
        self.signal_unit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.signal_unit.setWordWrap(True)
        self.signal_unit.setObjectName("signal_unit")
        self.horizontalLayout_3.addWidget(self.signal_unit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
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
        self.batterie_ln.setText(_translate("batlinkWindow", "ND"))
        self.batterie_unit.setText(_translate("batlinkWindow", "%"))
        self.signal_lb.setText(_translate("batlinkWindow", "Qualité signal :"))
        self.signal_ln.setText(_translate("batlinkWindow", "ND"))
        self.signal_unit.setText(_translate("batlinkWindow", "%"))
