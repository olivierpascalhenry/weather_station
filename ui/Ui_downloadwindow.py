# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_downloadWindow(object):
    def setupUi(self, downloadWindow):
        downloadWindow.setObjectName("downloadWindow")
        downloadWindow.resize(550, 176)
        downloadWindow.setMinimumSize(QtCore.QSize(0, 0))
        downloadWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        downloadWindow.setStyleSheet("QWidget#downloadWindow {\n"
"    background-color: rgb(240,240,240);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(downloadWindow)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.dw_progress_bar = QtWidgets.QProgressBar(downloadWindow)
        self.dw_progress_bar.setMinimumSize(QtCore.QSize(0, 30))
        self.dw_progress_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_progress_bar.setFont(font)
        self.dw_progress_bar.setStyleSheet("QProgressBar {\n"
"   border: 0px solid black;\n"
"   border-radius: 3px;\n"
"   background: rgb(220,220,220);\n"
"   color: rgb(45,45,45);\n"
"   text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"   border: 0px solid black;\n"
"   border-radius: 3px;\n"
"   background: rgb(0,200,0);\n"
" }")
        self.dw_progress_bar.setProperty("value", 0)
        self.dw_progress_bar.setTextVisible(True)
        self.dw_progress_bar.setObjectName("dw_progress_bar")
        self.gridLayout.addWidget(self.dw_progress_bar, 0, 0, 1, 1)
        self.dw_label = QtWidgets.QLabel(downloadWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dw_label.sizePolicy().hasHeightForWidth())
        self.dw_label.setSizePolicy(sizePolicy)
        self.dw_label.setMinimumSize(QtCore.QSize(0, 50))
        self.dw_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.dw_label.setFont(font)
        self.dw_label.setStyleSheet("QLabel {\n"
"    margin-top: 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.dw_label.setAlignment(QtCore.Qt.AlignCenter)
        self.dw_label.setWordWrap(True)
        self.dw_label.setObjectName("dw_label")
        self.gridLayout.addWidget(self.dw_label, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dw_button = QtWidgets.QToolButton(downloadWindow)
        self.dw_button.setMinimumSize(QtCore.QSize(100, 50))
        self.dw_button.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.dw_button.setFont(font)
        self.dw_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: rgb(230,230,230);\n"
"    color: rgb(45,45,45)\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgb(220,220,220);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210,210,210);\n"
"}")
        self.dw_button.setObjectName("dw_button")
        self.horizontalLayout.addWidget(self.dw_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(downloadWindow)
        QtCore.QMetaObject.connectSlotsByName(downloadWindow)

    def retranslateUi(self, downloadWindow):
        _translate = QtCore.QCoreApplication.translate
        self.dw_progress_bar.setFormat(_translate("downloadWindow", "%p %"))
        self.dw_label.setText(_translate("downloadWindow", "Downloading..."))
        self.dw_button.setText(_translate("downloadWindow", "Cancel"))
