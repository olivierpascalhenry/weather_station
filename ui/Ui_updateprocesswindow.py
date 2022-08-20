# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_process.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_updateprocessWindow(object):
    def setupUi(self, updateprocessWindow):
        updateprocessWindow.setObjectName("updateprocessWindow")
        updateprocessWindow.resize(600, 340)
        updateprocessWindow.setMinimumSize(QtCore.QSize(0, 0))
        updateprocessWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        updateprocessWindow.setFont(font)
        updateprocessWindow.setStyleSheet("QWidget#updateprocessWindow {\n"
"    background-color: rgb(240,240,240);\n"
"    border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(updateprocessWindow)
        self.gridLayout.setVerticalSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.browser = QtWidgets.QTextEdit(updateprocessWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy)
        self.browser.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.browser.setFont(font)
        self.browser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.browser.setAcceptDrops(False)
        self.browser.setStyleSheet("QTextEdit {\n"
"    border-radius: 3px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  border-left: 0px solid white;\n"
"  background-color: rgb(255, 255, 255);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(255, 255, 255);\n"
"  height: 20px;\n"
"  margin: 0px 21px 0px 21px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"  background-color: rgb(205, 205, 205);\n"
"  min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:hover {\n"
"  background-color: rgb(166, 166, 166);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 21px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 21px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"  border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"  image: url(icons/up_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical {\n"
"  image: url(icons/down_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
" background-color: rgb(240, 240, 240);\n"
"  width: 21px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"  border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
" background-color: rgb(240, 240, 240);\n"
"  width: 21px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"border-bottom-left-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"  image: url(icons/left_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal {\n"
"  image: url(icons/right_arrow_icon.svg); \n"
"  width: 16px;\n"
"  height: 16px;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal:pressed {\n"
"  right: -1px;\n"
"  bottom: -1px;\n"
"}")
        self.browser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.browser.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.browser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.browser.setObjectName("browser")
        self.gridLayout.addWidget(self.browser, 0, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(updateprocessWindow)
        self.progress_bar.setMinimumSize(QtCore.QSize(0, 30))
        self.progress_bar.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progress_bar.setFont(font)
        self.progress_bar.setStyleSheet("QProgressBar {\n"
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
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QToolButton(updateprocessWindow)
        self.cancel_button.setMinimumSize(QtCore.QSize(100, 50))
        self.cancel_button.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QToolButton {\n"
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
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(updateprocessWindow)
        QtCore.QMetaObject.connectSlotsByName(updateprocessWindow)

    def retranslateUi(self, updateprocessWindow):
        _translate = QtCore.QCoreApplication.translate
        self.browser.setHtml(_translate("updateprocessWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Source Sans Pro\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.progress_bar.setFormat(_translate("updateprocessWindow", "%p %"))
        self.cancel_button.setText(_translate("updateprocessWindow", "Cancel"))
