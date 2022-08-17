# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optionwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(934, 470)
        optionWindow.setMinimumSize(QtCore.QSize(0, 0))
        optionWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionWindow.setFont(font)
        optionWindow.setStyleSheet("QWidget#optionWindow {\n"
"    background-color: rgb(240,240,240);\n"
"    border: 1px solid rgb(75,75,75);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"  background-color: rgb(255, 255, 255);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
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
"  background-color: rgb(240, 240, 240);\n"
"  width: 21px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
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
"  background-color: rgb(240, 240, 240);\n"
"  width: 21px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
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
"}\n"
"\n"
"QComboBox {\n"
"    border: 1px solid rgb(170, 170, 170);\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(230,230,230);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(220,220,220);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 27px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/down_arrow_icon.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(icons/down_arrow_icon_deactivated.svg); \n"
"    width: 16px;\n"
"    height: 16px\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: rgb(230,230,230);\n"
"    border: 0px solid #f0f0f0;\n"
"    outline: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    margin: 3px 5px 3px 5px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.gridLayout_34 = QtWidgets.QGridLayout(optionWindow)
        self.gridLayout_34.setVerticalSpacing(11)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok_button = QtWidgets.QToolButton(optionWindow)
        self.ok_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_button.sizePolicy().hasHeightForWidth())
        self.ok_button.setSizePolicy(sizePolicy)
        self.ok_button.setMinimumSize(QtCore.QSize(50, 50))
        self.ok_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon)
        self.ok_button.setIconSize(QtCore.QSize(45, 45))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancel_button = QtWidgets.QToolButton(optionWindow)
        self.cancel_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        self.cancel_button.setMinimumSize(QtCore.QSize(50, 50))
        self.cancel_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon1)
        self.cancel_button.setIconSize(QtCore.QSize(45, 45))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_34.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(optionWindow)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.splitter.setFont(font)
        self.splitter.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 10px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 10px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background: rgb(190,190,190);\n"
"}")
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.section_list = QtWidgets.QListWidget(self.splitter)
        self.section_list.setEnabled(True)
        self.section_list.setMinimumSize(QtCore.QSize(0, 0))
        self.section_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.section_list.setFont(font)
        self.section_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.section_list.setStyleSheet("QListWidget {\n"
"    border-radius: 0px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QListWidget:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QListView::item {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"    padding: 1px 1px 1px 1px;\n"
"    margin: 3px 3px 3px 3px;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    border: 0px solid rgb(240,240,240);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(200,200,200);\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background: rgb(230,230,230);\n"
"    border-radius: 3px;\n"
"}")
        self.section_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.section_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.section_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.section_list.setObjectName("section_list")
        item = QtWidgets.QListWidgetItem()
        self.section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.section_list.addItem(item)
        self.stack_widget = QtWidgets.QStackedWidget(self.splitter)
        self.stack_widget.setObjectName("stack_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_2.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scroll_area_1 = QtWidgets.QScrollArea(self.page_1)
        self.scroll_area_1.setStyleSheet("QScrollArea { background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.scroll_area_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_1.setWidgetResizable(True)
        self.scroll_area_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_1.setObjectName("scroll_area_1")
        self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 598, 437))
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_1)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.af_vl = QtWidgets.QVBoxLayout()
        self.af_vl.setObjectName("af_vl")
        self.af_gb_int = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.af_gb_int.setFont(font)
        self.af_gb_int.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_int.setObjectName("af_gb_int")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.af_gb_int)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.af_gb_int_lb_1 = QtWidgets.QLabel(self.af_gb_int)
        self.af_gb_int_lb_1.setMinimumSize(QtCore.QSize(0, 60))
        self.af_gb_int_lb_1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_int_lb_1.setFont(font)
        self.af_gb_int_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_int_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.af_gb_int_lb_1.setWordWrap(True)
        self.af_gb_int_lb_1.setObjectName("af_gb_int_lb_1")
        self.gridLayout.addWidget(self.af_gb_int_lb_1, 0, 0, 1, 1)
        self.af_gb_int_cb_1 = QtWidgets.QComboBox(self.af_gb_int)
        self.af_gb_int_cb_1.setMinimumSize(QtCore.QSize(250, 40))
        self.af_gb_int_cb_1.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_int_cb_1.setFont(font)
        self.af_gb_int_cb_1.setStyleSheet("")
        self.af_gb_int_cb_1.setObjectName("af_gb_int_cb_1")
        self.af_gb_int_cb_1.addItem("")
        self.gridLayout.addWidget(self.af_gb_int_cb_1, 0, 1, 1, 1)
        self.af_gb_int_lb_2 = QtWidgets.QLabel(self.af_gb_int)
        self.af_gb_int_lb_2.setMinimumSize(QtCore.QSize(0, 60))
        self.af_gb_int_lb_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_int_lb_2.setFont(font)
        self.af_gb_int_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_int_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.af_gb_int_lb_2.setWordWrap(True)
        self.af_gb_int_lb_2.setObjectName("af_gb_int_lb_2")
        self.gridLayout.addWidget(self.af_gb_int_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.af_gb_int_ln_1 = QtWidgets.QLineEdit(self.af_gb_int)
        self.af_gb_int_ln_1.setMinimumSize(QtCore.QSize(50, 40))
        self.af_gb_int_ln_1.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_int_ln_1.setFont(font)
        self.af_gb_int_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_int_ln_1.setText("")
        self.af_gb_int_ln_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.af_gb_int_ln_1.setObjectName("af_gb_int_ln_1")
        self.horizontalLayout_4.addWidget(self.af_gb_int_ln_1)
        self.af_gb_int_lb_3 = QtWidgets.QLabel(self.af_gb_int)
        self.af_gb_int_lb_3.setMinimumSize(QtCore.QSize(0, 50))
        self.af_gb_int_lb_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_int_lb_3.setFont(font)
        self.af_gb_int_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_int_lb_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.af_gb_int_lb_3.setObjectName("af_gb_int_lb_3")
        self.horizontalLayout_4.addWidget(self.af_gb_int_lb_3)
        self.af_gb_int_bt_1 = QtWidgets.QToolButton(self.af_gb_int)
        self.af_gb_int_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.af_gb_int_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.af_gb_int_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.af_gb_int_bt_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.af_gb_int_bt_1.setIcon(icon2)
        self.af_gb_int_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.af_gb_int_bt_1.setObjectName("af_gb_int_bt_1")
        self.horizontalLayout_4.addWidget(self.af_gb_int_bt_1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.af_gb_int_ck_1 = QtWidgets.QCheckBox(self.af_gb_int)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_int_ck_1.setFont(font)
        self.af_gb_int_ck_1.setStyleSheet("QCheckBox {\n"
"    spacing: 10px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}")
        self.af_gb_int_ck_1.setObjectName("af_gb_int_ck_1")
        self.gridLayout_11.addWidget(self.af_gb_int_ck_1, 1, 0, 1, 1)
        self.af_vl.addWidget(self.af_gb_int)
        self.af_gb_ext = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.af_gb_ext.setFont(font)
        self.af_gb_ext.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_ext.setObjectName("af_gb_ext")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.af_gb_ext)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.af_gb_ext_lb_1 = QtWidgets.QLabel(self.af_gb_ext)
        self.af_gb_ext_lb_1.setMinimumSize(QtCore.QSize(0, 60))
        self.af_gb_ext_lb_1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_ext_lb_1.setFont(font)
        self.af_gb_ext_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_ext_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.af_gb_ext_lb_1.setWordWrap(True)
        self.af_gb_ext_lb_1.setObjectName("af_gb_ext_lb_1")
        self.gridLayout_14.addWidget(self.af_gb_ext_lb_1, 0, 0, 1, 1)
        self.af_gb_ext_cb_1 = QtWidgets.QComboBox(self.af_gb_ext)
        self.af_gb_ext_cb_1.setMinimumSize(QtCore.QSize(250, 40))
        self.af_gb_ext_cb_1.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_ext_cb_1.setFont(font)
        self.af_gb_ext_cb_1.setStyleSheet("")
        self.af_gb_ext_cb_1.setObjectName("af_gb_ext_cb_1")
        self.af_gb_ext_cb_1.addItem("")
        self.gridLayout_14.addWidget(self.af_gb_ext_cb_1, 0, 1, 1, 1)
        self.af_gb_ext_lb_2 = QtWidgets.QLabel(self.af_gb_ext)
        self.af_gb_ext_lb_2.setMinimumSize(QtCore.QSize(0, 60))
        self.af_gb_ext_lb_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_ext_lb_2.setFont(font)
        self.af_gb_ext_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_ext_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.af_gb_ext_lb_2.setWordWrap(True)
        self.af_gb_ext_lb_2.setObjectName("af_gb_ext_lb_2")
        self.gridLayout_14.addWidget(self.af_gb_ext_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.af_gb_ext_ln_1 = QtWidgets.QLineEdit(self.af_gb_ext)
        self.af_gb_ext_ln_1.setMinimumSize(QtCore.QSize(50, 40))
        self.af_gb_ext_ln_1.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_ext_ln_1.setFont(font)
        self.af_gb_ext_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_ext_ln_1.setText("")
        self.af_gb_ext_ln_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.af_gb_ext_ln_1.setObjectName("af_gb_ext_ln_1")
        self.horizontalLayout_5.addWidget(self.af_gb_ext_ln_1)
        self.af_gb_ext_lb_3 = QtWidgets.QLabel(self.af_gb_ext)
        self.af_gb_ext_lb_3.setMinimumSize(QtCore.QSize(0, 50))
        self.af_gb_ext_lb_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_ext_lb_3.setFont(font)
        self.af_gb_ext_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.af_gb_ext_lb_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.af_gb_ext_lb_3.setObjectName("af_gb_ext_lb_3")
        self.horizontalLayout_5.addWidget(self.af_gb_ext_lb_3)
        self.af_gb_ext_bt_1 = QtWidgets.QToolButton(self.af_gb_ext)
        self.af_gb_ext_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.af_gb_ext_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.af_gb_ext_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.af_gb_ext_bt_1.setText("")
        self.af_gb_ext_bt_1.setIcon(icon2)
        self.af_gb_ext_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.af_gb_ext_bt_1.setObjectName("af_gb_ext_bt_1")
        self.horizontalLayout_5.addWidget(self.af_gb_ext_bt_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout_14.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.af_gb_ext_ck_1 = QtWidgets.QCheckBox(self.af_gb_ext)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.af_gb_ext_ck_1.setFont(font)
        self.af_gb_ext_ck_1.setStyleSheet("QCheckBox {\n"
"    spacing: 10px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}")
        self.af_gb_ext_ck_1.setObjectName("af_gb_ext_ck_1")
        self.gridLayout_13.addWidget(self.af_gb_ext_ck_1, 1, 0, 1, 1)
        self.af_vl.addWidget(self.af_gb_ext)
        self.gridLayout_15.addLayout(self.af_vl, 0, 0, 1, 1)
        self.scroll_area_1.setWidget(self.scrollAreaWidgetContents_1)
        self.gridLayout_2.addWidget(self.scroll_area_1, 0, 0, 1, 1)
        self.stack_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_9.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scroll_area_4 = QtWidgets.QScrollArea(self.page_2)
        self.scroll_area_4.setStyleSheet("QScrollArea { background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.scroll_area_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_4.setWidgetResizable(True)
        self.scroll_area_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_4.setObjectName("scroll_area_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 598, 441))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ap_vl = QtWidgets.QVBoxLayout()
        self.ap_vl.setObjectName("ap_vl")
        self.ap_gb_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_1.setFont(font)
        self.ap_gb_1.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_1.setObjectName("ap_gb_1")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.ap_gb_1)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.ap_gb_rb_1 = QtWidgets.QRadioButton(self.ap_gb_1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_rb_1.setFont(font)
        self.ap_gb_rb_1.setStyleSheet("QRadioButton {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(icons/radiobox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(icons/radiobox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(icons/radiobox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(icons/radiobox_icon_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(icons/radiobox_icon_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    image: url(icons/radiobox_icon_checked.svg);\n"
"}")
        self.ap_gb_rb_1.setObjectName("ap_gb_rb_1")
        self.buttonGroup = QtWidgets.QButtonGroup(optionWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.ap_gb_rb_1)
        self.horizontalLayout_19.addWidget(self.ap_gb_rb_1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem4)
        self.gridLayout_21.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.ap_gb_rb_2 = QtWidgets.QRadioButton(self.ap_gb_1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_rb_2.setFont(font)
        self.ap_gb_rb_2.setStyleSheet("QRadioButton {\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(icons/radiobox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(icons/radiobox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(icons/radiobox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(icons/radiobox_icon_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(icons/radiobox_icon_checked.svg);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    image: url(icons/radiobox_icon_checked.svg);\n"
"}")
        self.ap_gb_rb_2.setObjectName("ap_gb_rb_2")
        self.buttonGroup.addButton(self.ap_gb_rb_2)
        self.horizontalLayout_18.addWidget(self.ap_gb_rb_2)
        self.ap_gb_bt_1 = QtWidgets.QToolButton(self.ap_gb_1)
        self.ap_gb_bt_1.setEnabled(False)
        self.ap_gb_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.ap_gb_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.ap_gb_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ap_gb_bt_1.setText("")
        self.ap_gb_bt_1.setIcon(icon2)
        self.ap_gb_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.ap_gb_bt_1.setObjectName("ap_gb_bt_1")
        self.horizontalLayout_18.addWidget(self.ap_gb_bt_1)
        self.ap_gb_lb_1 = QtWidgets.QLabel(self.ap_gb_1)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_lb_1.setFont(font)
        self.ap_gb_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_lb_1.setText("")
        self.ap_gb_lb_1.setObjectName("ap_gb_lb_1")
        self.horizontalLayout_18.addWidget(self.ap_gb_lb_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem5)
        self.gridLayout_21.addLayout(self.horizontalLayout_18, 1, 0, 1, 1)
        self.ap_vl.addWidget(self.ap_gb_1)
        self.ap_gb_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2.setFont(font)
        self.ap_gb_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_2.setObjectName("ap_gb_2")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.ap_gb_2)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ap_gb_2_ln_1 = QtWidgets.QLineEdit(self.ap_gb_2)
        self.ap_gb_2_ln_1.setEnabled(False)
        self.ap_gb_2_ln_1.setMinimumSize(QtCore.QSize(200, 40))
        self.ap_gb_2_ln_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2_ln_1.setFont(font)
        self.ap_gb_2_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ap_gb_2_ln_1.setText("")
        self.ap_gb_2_ln_1.setReadOnly(False)
        self.ap_gb_2_ln_1.setObjectName("ap_gb_2_ln_1")
        self.horizontalLayout_10.addWidget(self.ap_gb_2_ln_1)
        self.ap_gb_2_bt_1 = QtWidgets.QToolButton(self.ap_gb_2)
        self.ap_gb_2_bt_1.setEnabled(False)
        self.ap_gb_2_bt_1.setMinimumSize(QtCore.QSize(40, 40))
        self.ap_gb_2_bt_1.setMaximumSize(QtCore.QSize(40, 40))
        self.ap_gb_2_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ap_gb_2_bt_1.setText("")
        self.ap_gb_2_bt_1.setIcon(icon2)
        self.ap_gb_2_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.ap_gb_2_bt_1.setObjectName("ap_gb_2_bt_1")
        self.horizontalLayout_10.addWidget(self.ap_gb_2_bt_1)
        self.ap_gb_2_bt_2 = QtWidgets.QToolButton(self.ap_gb_2)
        self.ap_gb_2_bt_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ap_gb_2_bt_2.sizePolicy().hasHeightForWidth())
        self.ap_gb_2_bt_2.setSizePolicy(sizePolicy)
        self.ap_gb_2_bt_2.setMinimumSize(QtCore.QSize(160, 40))
        self.ap_gb_2_bt_2.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ap_gb_2_bt_2.setFont(font)
        self.ap_gb_2_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: rgb(230,230,230);\n"
"    color: rgb(45,45,45)\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgb(220,220,220);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210,210,210);\n"
"}")
        self.ap_gb_2_bt_2.setObjectName("ap_gb_2_bt_2")
        self.horizontalLayout_10.addWidget(self.ap_gb_2_bt_2)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)
        self.ap_gb_2_lb_1 = QtWidgets.QLabel(self.ap_gb_2)
        self.ap_gb_2_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.ap_gb_2_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2_lb_1.setFont(font)
        self.ap_gb_2_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_2_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ap_gb_2_lb_1.setObjectName("ap_gb_2_lb_1")
        self.gridLayout_4.addWidget(self.ap_gb_2_lb_1, 0, 0, 1, 1)
        self.ap_gb_2_lb_4 = QtWidgets.QLabel(self.ap_gb_2)
        self.ap_gb_2_lb_4.setMinimumSize(QtCore.QSize(80, 40))
        self.ap_gb_2_lb_4.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2_lb_4.setFont(font)
        self.ap_gb_2_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_2_lb_4.setText("")
        self.ap_gb_2_lb_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ap_gb_2_lb_4.setObjectName("ap_gb_2_lb_4")
        self.gridLayout_4.addWidget(self.ap_gb_2_lb_4, 1, 1, 1, 1)
        self.ap_gb_2_lb_2 = QtWidgets.QLabel(self.ap_gb_2)
        self.ap_gb_2_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.ap_gb_2_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2_lb_2.setFont(font)
        self.ap_gb_2_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_2_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ap_gb_2_lb_2.setObjectName("ap_gb_2_lb_2")
        self.gridLayout_4.addWidget(self.ap_gb_2_lb_2, 1, 0, 1, 1)
        self.ap_gb_2_lb_5 = QtWidgets.QLabel(self.ap_gb_2)
        self.ap_gb_2_lb_5.setMinimumSize(QtCore.QSize(250, 40))
        self.ap_gb_2_lb_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2_lb_5.setFont(font)
        self.ap_gb_2_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_2_lb_5.setText("")
        self.ap_gb_2_lb_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ap_gb_2_lb_5.setObjectName("ap_gb_2_lb_5")
        self.gridLayout_4.addWidget(self.ap_gb_2_lb_5, 2, 1, 1, 1)
        self.ap_gb_2_lb_3 = QtWidgets.QLabel(self.ap_gb_2)
        self.ap_gb_2_lb_3.setMinimumSize(QtCore.QSize(0, 40))
        self.ap_gb_2_lb_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_2_lb_3.setFont(font)
        self.ap_gb_2_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_2_lb_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ap_gb_2_lb_3.setObjectName("ap_gb_2_lb_3")
        self.gridLayout_4.addWidget(self.ap_gb_2_lb_3, 2, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.ap_vl.addWidget(self.ap_gb_2)
        self.ap_gb_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_5.setFont(font)
        self.ap_gb_5.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_5.setObjectName("ap_gb_5")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.ap_gb_5)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.ow_label_16 = QtWidgets.QLabel(self.ap_gb_5)
        self.ow_label_16.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_16.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_16.setFont(font)
        self.ow_label_16.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_16.setObjectName("ow_label_16")
        self.horizontalLayout_12.addWidget(self.ow_label_16)
        self.ap_gb_5_ln_1 = QtWidgets.QLineEdit(self.ap_gb_5)
        self.ap_gb_5_ln_1.setMinimumSize(QtCore.QSize(50, 50))
        self.ap_gb_5_ln_1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ap_gb_5_ln_1.setFont(font)
        self.ap_gb_5_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ap_gb_5_ln_1.setText("")
        self.ap_gb_5_ln_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ap_gb_5_ln_1.setObjectName("ap_gb_5_ln_1")
        self.horizontalLayout_12.addWidget(self.ap_gb_5_ln_1)
        self.ow_label_17 = QtWidgets.QLabel(self.ap_gb_5)
        self.ow_label_17.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_17.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_17.setFont(font)
        self.ow_label_17.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_17.setObjectName("ow_label_17")
        self.horizontalLayout_12.addWidget(self.ow_label_17)
        self.ap_gb_3_bt_1 = QtWidgets.QToolButton(self.ap_gb_5)
        self.ap_gb_3_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.ap_gb_3_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.ap_gb_3_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ap_gb_3_bt_1.setText("")
        self.ap_gb_3_bt_1.setIcon(icon2)
        self.ap_gb_3_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.ap_gb_3_bt_1.setObjectName("ap_gb_3_bt_1")
        self.horizontalLayout_12.addWidget(self.ap_gb_3_bt_1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.gridLayout_20.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.ap_vl.addWidget(self.ap_gb_5)
        self.gridLayout_8.addLayout(self.ap_vl, 0, 0, 1, 1)
        self.scroll_area_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_9.addWidget(self.scroll_area_4, 0, 0, 1, 1)
        self.stack_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_29.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.scroll_area_6 = QtWidgets.QScrollArea(self.page_3)
        self.scroll_area_6.setStyleSheet("QScrollArea { background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.scroll_area_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_6.setWidgetResizable(True)
        self.scroll_area_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_6.setObjectName("scroll_area_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 598, 436))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.db_vl = QtWidgets.QVBoxLayout()
        self.db_vl.setObjectName("db_vl")
        self.db_gb = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_gb.sizePolicy().hasHeightForWidth())
        self.db_gb.setSizePolicy(sizePolicy)
        self.db_gb.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.db_gb.setFont(font)
        self.db_gb.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb.setObjectName("db_gb")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.db_gb)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.gridLayout_30 = QtWidgets.QGridLayout()
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.db_gb_lb_2 = QtWidgets.QLabel(self.db_gb)
        self.db_gb_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_lb_2.setFont(font)
        self.db_gb_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_gb_lb_2.setObjectName("db_gb_lb_2")
        self.gridLayout_30.addWidget(self.db_gb_lb_2, 1, 0, 1, 1)
        self.db_gb_lb_1 = QtWidgets.QLabel(self.db_gb)
        self.db_gb_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_lb_1.setFont(font)
        self.db_gb_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_gb_lb_1.setObjectName("db_gb_lb_1")
        self.gridLayout_30.addWidget(self.db_gb_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.db_gb_ln_2 = QtWidgets.QLineEdit(self.db_gb)
        self.db_gb_ln_2.setEnabled(True)
        self.db_gb_ln_2.setMinimumSize(QtCore.QSize(300, 40))
        self.db_gb_ln_2.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_ln_2.setFont(font)
        self.db_gb_ln_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.db_gb_ln_2.setText("")
        self.db_gb_ln_2.setReadOnly(False)
        self.db_gb_ln_2.setObjectName("db_gb_ln_2")
        self.horizontalLayout_17.addWidget(self.db_gb_ln_2)
        self.db_gb_bt_2 = QtWidgets.QToolButton(self.db_gb)
        self.db_gb_bt_2.setEnabled(True)
        self.db_gb_bt_2.setMinimumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_2.setMaximumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.db_gb_bt_2.setText("")
        self.db_gb_bt_2.setIcon(icon2)
        self.db_gb_bt_2.setIconSize(QtCore.QSize(40, 40))
        self.db_gb_bt_2.setObjectName("db_gb_bt_2")
        self.horizontalLayout_17.addWidget(self.db_gb_bt_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem7)
        self.gridLayout_30.addLayout(self.horizontalLayout_17, 1, 1, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.db_gb_ln_1 = QtWidgets.QLineEdit(self.db_gb)
        self.db_gb_ln_1.setEnabled(True)
        self.db_gb_ln_1.setMinimumSize(QtCore.QSize(300, 40))
        self.db_gb_ln_1.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_ln_1.setFont(font)
        self.db_gb_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.db_gb_ln_1.setText("")
        self.db_gb_ln_1.setReadOnly(False)
        self.db_gb_ln_1.setObjectName("db_gb_ln_1")
        self.horizontalLayout_11.addWidget(self.db_gb_ln_1)
        self.db_gb_bt_1 = QtWidgets.QToolButton(self.db_gb)
        self.db_gb_bt_1.setEnabled(True)
        self.db_gb_bt_1.setMinimumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_1.setMaximumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.db_gb_bt_1.setText("")
        self.db_gb_bt_1.setIcon(icon2)
        self.db_gb_bt_1.setIconSize(QtCore.QSize(40, 40))
        self.db_gb_bt_1.setObjectName("db_gb_bt_1")
        self.horizontalLayout_11.addWidget(self.db_gb_bt_1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.gridLayout_30.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)
        self.db_gb_lb_3 = QtWidgets.QLabel(self.db_gb)
        self.db_gb_lb_3.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_lb_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_lb_3.setFont(font)
        self.db_gb_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_lb_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_gb_lb_3.setObjectName("db_gb_lb_3")
        self.gridLayout_30.addWidget(self.db_gb_lb_3, 2, 0, 1, 1)
        self.db_gb_lb_4 = QtWidgets.QLabel(self.db_gb)
        self.db_gb_lb_4.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_lb_4.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_lb_4.setFont(font)
        self.db_gb_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_lb_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_gb_lb_4.setObjectName("db_gb_lb_4")
        self.gridLayout_30.addWidget(self.db_gb_lb_4, 3, 0, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.db_gb_ln_4 = QtWidgets.QLineEdit(self.db_gb)
        self.db_gb_ln_4.setEnabled(True)
        self.db_gb_ln_4.setMinimumSize(QtCore.QSize(300, 40))
        self.db_gb_ln_4.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_ln_4.setFont(font)
        self.db_gb_ln_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.db_gb_ln_4.setText("")
        self.db_gb_ln_4.setReadOnly(False)
        self.db_gb_ln_4.setObjectName("db_gb_ln_4")
        self.horizontalLayout_21.addWidget(self.db_gb_ln_4)
        self.db_gb_bt_4 = QtWidgets.QToolButton(self.db_gb)
        self.db_gb_bt_4.setEnabled(True)
        self.db_gb_bt_4.setMinimumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_4.setMaximumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.db_gb_bt_4.setText("")
        self.db_gb_bt_4.setIcon(icon2)
        self.db_gb_bt_4.setIconSize(QtCore.QSize(40, 40))
        self.db_gb_bt_4.setObjectName("db_gb_bt_4")
        self.horizontalLayout_21.addWidget(self.db_gb_bt_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem9)
        self.gridLayout_30.addLayout(self.horizontalLayout_21, 3, 1, 1, 1)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.db_gb_ln_3 = QtWidgets.QLineEdit(self.db_gb)
        self.db_gb_ln_3.setEnabled(True)
        self.db_gb_ln_3.setMinimumSize(QtCore.QSize(300, 40))
        self.db_gb_ln_3.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_ln_3.setFont(font)
        self.db_gb_ln_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.db_gb_ln_3.setText("")
        self.db_gb_ln_3.setReadOnly(False)
        self.db_gb_ln_3.setObjectName("db_gb_ln_3")
        self.horizontalLayout_20.addWidget(self.db_gb_ln_3)
        self.db_gb_bt_3 = QtWidgets.QToolButton(self.db_gb)
        self.db_gb_bt_3.setEnabled(True)
        self.db_gb_bt_3.setMinimumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_3.setMaximumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.db_gb_bt_3.setText("")
        self.db_gb_bt_3.setIcon(icon2)
        self.db_gb_bt_3.setIconSize(QtCore.QSize(40, 40))
        self.db_gb_bt_3.setObjectName("db_gb_bt_3")
        self.horizontalLayout_20.addWidget(self.db_gb_bt_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem10)
        self.gridLayout_30.addLayout(self.horizontalLayout_20, 2, 1, 1, 1)
        self.db_gb_lb_5 = QtWidgets.QLabel(self.db_gb)
        self.db_gb_lb_5.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_lb_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_lb_5.setFont(font)
        self.db_gb_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_lb_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_gb_lb_5.setObjectName("db_gb_lb_5")
        self.gridLayout_30.addWidget(self.db_gb_lb_5, 4, 0, 1, 1)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.db_gb_ln_5 = QtWidgets.QLineEdit(self.db_gb)
        self.db_gb_ln_5.setEnabled(True)
        self.db_gb_ln_5.setMinimumSize(QtCore.QSize(100, 40))
        self.db_gb_ln_5.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_ln_5.setFont(font)
        self.db_gb_ln_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.db_gb_ln_5.setText("")
        self.db_gb_ln_5.setReadOnly(False)
        self.db_gb_ln_5.setObjectName("db_gb_ln_5")
        self.horizontalLayout_23.addWidget(self.db_gb_ln_5)
        self.db_gb_bt_5 = QtWidgets.QToolButton(self.db_gb)
        self.db_gb_bt_5.setEnabled(True)
        self.db_gb_bt_5.setMinimumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_5.setMaximumSize(QtCore.QSize(40, 40))
        self.db_gb_bt_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.db_gb_bt_5.setText("")
        self.db_gb_bt_5.setIcon(icon2)
        self.db_gb_bt_5.setIconSize(QtCore.QSize(40, 40))
        self.db_gb_bt_5.setObjectName("db_gb_bt_5")
        self.horizontalLayout_23.addWidget(self.db_gb_bt_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem11)
        self.gridLayout_30.addLayout(self.horizontalLayout_23, 4, 1, 1, 1)
        self.gridLayout_31.addLayout(self.gridLayout_30, 0, 0, 1, 1)
        self.db_vl.addWidget(self.db_gb)
        self.db_gb_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_gb_2.sizePolicy().hasHeightForWidth())
        self.db_gb_2.setSizePolicy(sizePolicy)
        self.db_gb_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.db_gb_2.setFont(font)
        self.db_gb_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_2.setObjectName("db_gb_2")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.db_gb_2)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.db_gb_2_lb_1 = QtWidgets.QLabel(self.db_gb_2)
        self.db_gb_2_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_2_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_2_lb_1.setFont(font)
        self.db_gb_2_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_2_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_gb_2_lb_1.setObjectName("db_gb_2_lb_1")
        self.horizontalLayout_24.addWidget(self.db_gb_2_lb_1)
        self.db_gb_2_cb_1 = QtWidgets.QComboBox(self.db_gb_2)
        self.db_gb_2_cb_1.setMinimumSize(QtCore.QSize(250, 40))
        self.db_gb_2_cb_1.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_2_cb_1.setFont(font)
        self.db_gb_2_cb_1.setStyleSheet("")
        self.db_gb_2_cb_1.setObjectName("db_gb_2_cb_1")
        self.db_gb_2_cb_1.addItem("")
        self.horizontalLayout_24.addWidget(self.db_gb_2_cb_1)
        spacerItem12 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem12)
        self.gridLayout_33.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.sy_gb_2_bt_2 = QtWidgets.QToolButton(self.db_gb_2)
        self.sy_gb_2_bt_2.setEnabled(False)
        self.sy_gb_2_bt_2.setMinimumSize(QtCore.QSize(250, 40))
        self.sy_gb_2_bt_2.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sy_gb_2_bt_2.setFont(font)
        self.sy_gb_2_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: rgb(230,230,230);\n"
"    color: rgb(45,45,45)\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgb(220,220,220);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210,210,210);\n"
"}")
        self.sy_gb_2_bt_2.setObjectName("sy_gb_2_bt_2")
        self.horizontalLayout_27.addWidget(self.sy_gb_2_bt_2)
        self.db_gb_2_lb_2 = QtWidgets.QLabel(self.db_gb_2)
        self.db_gb_2_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.db_gb_2_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.db_gb_2_lb_2.setFont(font)
        self.db_gb_2_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.db_gb_2_lb_2.setText("")
        self.db_gb_2_lb_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.db_gb_2_lb_2.setObjectName("db_gb_2_lb_2")
        self.horizontalLayout_27.addWidget(self.db_gb_2_lb_2)
        self.gridLayout_33.addLayout(self.horizontalLayout_27, 1, 0, 1, 1)
        self.db_vl.addWidget(self.db_gb_2)
        self.gridLayout_28.addLayout(self.db_vl, 0, 0, 1, 1)
        self.scroll_area_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_29.addWidget(self.scroll_area_6, 0, 0, 1, 1)
        self.stack_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_18.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.scroll_area_2 = QtWidgets.QScrollArea(self.page_4)
        self.scroll_area_2.setStyleSheet("QScrollArea { background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.scroll_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_2.setWidgetResizable(True)
        self.scroll_area_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_2.setObjectName("scroll_area_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 618, 380))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.ca_vl = QtWidgets.QVBoxLayout()
        self.ca_vl.setObjectName("ca_vl")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.ca_lb_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ca_lb_1.setMinimumSize(QtCore.QSize(0, 60))
        self.ca_lb_1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_lb_1.setFont(font)
        self.ca_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ca_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ca_lb_1.setWordWrap(True)
        self.ca_lb_1.setObjectName("ca_lb_1")
        self.horizontalLayout_13.addWidget(self.ca_lb_1)
        self.ca_ln_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ca_ln_1.setMinimumSize(QtCore.QSize(50, 40))
        self.ca_ln_1.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_ln_1.setFont(font)
        self.ca_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.ca_ln_1.setText("")
        self.ca_ln_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ca_ln_1.setObjectName("ca_ln_1")
        self.horizontalLayout_13.addWidget(self.ca_ln_1)
        self.ca_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ca_lb_2.setMinimumSize(QtCore.QSize(0, 50))
        self.ca_lb_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_lb_2.setFont(font)
        self.ca_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ca_lb_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ca_lb_2.setObjectName("ca_lb_2")
        self.horizontalLayout_13.addWidget(self.ca_lb_2)
        self.ca_bt_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ca_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.ca_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.ca_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ca_bt_1.setText("")
        self.ca_bt_1.setIcon(icon2)
        self.ca_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.ca_bt_1.setObjectName("ca_bt_1")
        self.horizontalLayout_13.addWidget(self.ca_bt_1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.ca_vl.addLayout(self.horizontalLayout_13)
        self.ca_gb_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_gb_1.setFont(font)
        self.ca_gb_1.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ca_gb_1.setObjectName("ca_gb_1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ca_gb_1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.ca_gc_lb_1 = QtWidgets.QLabel(self.ca_gb_1)
        self.ca_gc_lb_1.setMinimumSize(QtCore.QSize(0, 0))
        self.ca_gc_lb_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_gc_lb_1.setFont(font)
        self.ca_gc_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ca_gc_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ca_gc_lb_1.setWordWrap(True)
        self.ca_gc_lb_1.setObjectName("ca_gc_lb_1")
        self.gridLayout_23.addWidget(self.ca_gc_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ca_gc_bt_1 = QtWidgets.QToolButton(self.ca_gb_1)
        self.ca_gc_bt_1.setEnabled(True)
        self.ca_gc_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.ca_gc_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.ca_gc_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ca_gc_bt_1.setText("")
        self.ca_gc_bt_1.setIcon(icon2)
        self.ca_gc_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.ca_gc_bt_1.setObjectName("ca_gc_bt_1")
        self.horizontalLayout_8.addWidget(self.ca_gc_bt_1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.gridLayout_23.addLayout(self.horizontalLayout_8, 0, 1, 1, 1)
        self.ca_gc_lb_2 = QtWidgets.QLabel(self.ca_gb_1)
        self.ca_gc_lb_2.setMinimumSize(QtCore.QSize(0, 0))
        self.ca_gc_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_gc_lb_2.setFont(font)
        self.ca_gc_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ca_gc_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ca_gc_lb_2.setWordWrap(True)
        self.ca_gc_lb_2.setObjectName("ca_gc_lb_2")
        self.gridLayout_23.addWidget(self.ca_gc_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ca_gc_bt_2 = QtWidgets.QToolButton(self.ca_gb_1)
        self.ca_gc_bt_2.setEnabled(True)
        self.ca_gc_bt_2.setMinimumSize(QtCore.QSize(50, 50))
        self.ca_gc_bt_2.setMaximumSize(QtCore.QSize(50, 50))
        self.ca_gc_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ca_gc_bt_2.setText("")
        self.ca_gc_bt_2.setIcon(icon2)
        self.ca_gc_bt_2.setIconSize(QtCore.QSize(36, 36))
        self.ca_gc_bt_2.setObjectName("ca_gc_bt_2")
        self.horizontalLayout_6.addWidget(self.ca_gc_bt_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.gridLayout_23.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.ca_gc_lb_3 = QtWidgets.QLabel(self.ca_gb_1)
        self.ca_gc_lb_3.setMinimumSize(QtCore.QSize(0, 0))
        self.ca_gc_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ca_gc_lb_3.setFont(font)
        self.ca_gc_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ca_gc_lb_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ca_gc_lb_3.setWordWrap(True)
        self.ca_gc_lb_3.setObjectName("ca_gc_lb_3")
        self.gridLayout_23.addWidget(self.ca_gc_lb_3, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ca_gc_bt_3 = QtWidgets.QToolButton(self.ca_gb_1)
        self.ca_gc_bt_3.setEnabled(True)
        self.ca_gc_bt_3.setMinimumSize(QtCore.QSize(50, 50))
        self.ca_gc_bt_3.setMaximumSize(QtCore.QSize(50, 50))
        self.ca_gc_bt_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ca_gc_bt_3.setText("")
        self.ca_gc_bt_3.setIcon(icon2)
        self.ca_gc_bt_3.setIconSize(QtCore.QSize(36, 36))
        self.ca_gc_bt_3.setObjectName("ca_gc_bt_3")
        self.horizontalLayout_3.addWidget(self.ca_gc_bt_3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.gridLayout_23.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_23, 0, 0, 1, 1)
        self.ca_vl.addWidget(self.ca_gb_1)
        self.gridLayout_16.addLayout(self.ca_vl, 0, 0, 1, 1)
        self.scroll_area_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_18.addWidget(self.scroll_area_2, 0, 0, 1, 1)
        self.stack_widget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scroll_area_3 = QtWidgets.QScrollArea(self.page_5)
        self.scroll_area_3.setStyleSheet("QScrollArea { background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.scroll_area_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_3.setWidgetResizable(True)
        self.scroll_area_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_3.setObjectName("scroll_area_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 598, 400))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.st_vl = QtWidgets.QVBoxLayout()
        self.st_vl.setObjectName("st_vl")
        self.ts_gb_int = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.ts_gb_int.setFont(font)
        self.ts_gb_int.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ts_gb_int.setObjectName("ts_gb_int")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.ts_gb_int)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ts_gb_int_lb_1 = QtWidgets.QLabel(self.ts_gb_int)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ts_gb_int_lb_1.sizePolicy().hasHeightForWidth())
        self.ts_gb_int_lb_1.setSizePolicy(sizePolicy)
        self.ts_gb_int_lb_1.setMinimumSize(QtCore.QSize(0, 60))
        self.ts_gb_int_lb_1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_int_lb_1.setFont(font)
        self.ts_gb_int_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ts_gb_int_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ts_gb_int_lb_1.setWordWrap(True)
        self.ts_gb_int_lb_1.setObjectName("ts_gb_int_lb_1")
        self.gridLayout_5.addWidget(self.ts_gb_int_lb_1, 0, 0, 1, 1)
        self.ts_gb_int_lb_2 = QtWidgets.QLabel(self.ts_gb_int)
        self.ts_gb_int_lb_2.setMinimumSize(QtCore.QSize(0, 60))
        self.ts_gb_int_lb_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_int_lb_2.setFont(font)
        self.ts_gb_int_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ts_gb_int_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ts_gb_int_lb_2.setWordWrap(True)
        self.ts_gb_int_lb_2.setObjectName("ts_gb_int_lb_2")
        self.gridLayout_5.addWidget(self.ts_gb_int_lb_2, 1, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ts_gb_int_cb_1 = QtWidgets.QComboBox(self.ts_gb_int)
        self.ts_gb_int_cb_1.setMinimumSize(QtCore.QSize(250, 40))
        self.ts_gb_int_cb_1.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_int_cb_1.setFont(font)
        self.ts_gb_int_cb_1.setStyleSheet("")
        self.ts_gb_int_cb_1.setObjectName("ts_gb_int_cb_1")
        self.ts_gb_int_cb_1.addItem("")
        self.horizontalLayout_9.addWidget(self.ts_gb_int_cb_1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem17)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.ts_gb_int_cb_2 = QtWidgets.QComboBox(self.ts_gb_int)
        self.ts_gb_int_cb_2.setMinimumSize(QtCore.QSize(250, 40))
        self.ts_gb_int_cb_2.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_int_cb_2.setFont(font)
        self.ts_gb_int_cb_2.setStyleSheet("")
        self.ts_gb_int_cb_2.setObjectName("ts_gb_int_cb_2")
        self.ts_gb_int_cb_2.addItem("")
        self.horizontalLayout_14.addWidget(self.ts_gb_int_cb_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem18)
        self.gridLayout_5.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.st_vl.addWidget(self.ts_gb_int)
        self.ts_gb_ext = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.ts_gb_ext.setFont(font)
        self.ts_gb_ext.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ts_gb_ext.setObjectName("ts_gb_ext")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.ts_gb_ext)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.ts_gb_ext_cb_2 = QtWidgets.QComboBox(self.ts_gb_ext)
        self.ts_gb_ext_cb_2.setMinimumSize(QtCore.QSize(250, 40))
        self.ts_gb_ext_cb_2.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_ext_cb_2.setFont(font)
        self.ts_gb_ext_cb_2.setStyleSheet("")
        self.ts_gb_ext_cb_2.setObjectName("ts_gb_ext_cb_2")
        self.ts_gb_ext_cb_2.addItem("")
        self.horizontalLayout_16.addWidget(self.ts_gb_ext_cb_2)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem19)
        self.gridLayout_27.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)
        self.ts_gb_ext_lb_2 = QtWidgets.QLabel(self.ts_gb_ext)
        self.ts_gb_ext_lb_2.setMinimumSize(QtCore.QSize(0, 60))
        self.ts_gb_ext_lb_2.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_ext_lb_2.setFont(font)
        self.ts_gb_ext_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ts_gb_ext_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ts_gb_ext_lb_2.setWordWrap(True)
        self.ts_gb_ext_lb_2.setObjectName("ts_gb_ext_lb_2")
        self.gridLayout_27.addWidget(self.ts_gb_ext_lb_2, 1, 0, 1, 1)
        self.ts_gb_ext_lb_1 = QtWidgets.QLabel(self.ts_gb_ext)
        self.ts_gb_ext_lb_1.setMinimumSize(QtCore.QSize(0, 60))
        self.ts_gb_ext_lb_1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_ext_lb_1.setFont(font)
        self.ts_gb_ext_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ts_gb_ext_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ts_gb_ext_lb_1.setWordWrap(True)
        self.ts_gb_ext_lb_1.setObjectName("ts_gb_ext_lb_1")
        self.gridLayout_27.addWidget(self.ts_gb_ext_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.ts_gb_ext_cb_1 = QtWidgets.QComboBox(self.ts_gb_ext)
        self.ts_gb_ext_cb_1.setMinimumSize(QtCore.QSize(250, 40))
        self.ts_gb_ext_cb_1.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_ext_cb_1.setFont(font)
        self.ts_gb_ext_cb_1.setStyleSheet("")
        self.ts_gb_ext_cb_1.setObjectName("ts_gb_ext_cb_1")
        self.ts_gb_ext_cb_1.addItem("")
        self.horizontalLayout_15.addWidget(self.ts_gb_ext_cb_1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem20)
        self.gridLayout_27.addLayout(self.horizontalLayout_15, 0, 1, 1, 1)
        self.ts_gb_ext_ck_1 = QtWidgets.QCheckBox(self.ts_gb_ext)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ts_gb_ext_ck_1.setFont(font)
        self.ts_gb_ext_ck_1.setStyleSheet("QCheckBox {\n"
"    spacing: 10px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}")
        self.ts_gb_ext_ck_1.setObjectName("ts_gb_ext_ck_1")
        self.gridLayout_27.addWidget(self.ts_gb_ext_ck_1, 2, 1, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_27, 0, 0, 1, 1)
        self.st_vl.addWidget(self.ts_gb_ext)
        self.gridLayout_24.addLayout(self.st_vl, 0, 0, 1, 1)
        self.scroll_area_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_6.addWidget(self.scroll_area_3, 0, 0, 1, 1)
        self.stack_widget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_12.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.scroll_area_5 = QtWidgets.QScrollArea(self.page_6)
        self.scroll_area_5.setStyleSheet("QScrollArea { background: transparent;}\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.scroll_area_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area_5.setWidgetResizable(True)
        self.scroll_area_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scroll_area_5.setObjectName("scroll_area_5")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 598, 386))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.sy_vl = QtWidgets.QVBoxLayout()
        self.sy_vl.setObjectName("sy_vl")
        self.sy_gb_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sy_gb_1.setFont(font)
        self.sy_gb_1.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sy_gb_1.setObjectName("sy_gb_1")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.sy_gb_1)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.sy_gb_lb_1 = QtWidgets.QLabel(self.sy_gb_1)
        self.sy_gb_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.sy_gb_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sy_gb_lb_1.setFont(font)
        self.sy_gb_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sy_gb_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sy_gb_lb_1.setObjectName("sy_gb_lb_1")
        self.horizontalLayout_22.addWidget(self.sy_gb_lb_1)
        self.sy_gb_ln_1 = QtWidgets.QLineEdit(self.sy_gb_1)
        self.sy_gb_ln_1.setMinimumSize(QtCore.QSize(70, 40))
        self.sy_gb_ln_1.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sy_gb_ln_1.setFont(font)
        self.sy_gb_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.sy_gb_ln_1.setText("")
        self.sy_gb_ln_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sy_gb_ln_1.setReadOnly(False)
        self.sy_gb_ln_1.setObjectName("sy_gb_ln_1")
        self.horizontalLayout_22.addWidget(self.sy_gb_ln_1)
        self.sy_gb_lb_2 = QtWidgets.QLabel(self.sy_gb_1)
        self.sy_gb_lb_2.setMinimumSize(QtCore.QSize(0, 50))
        self.sy_gb_lb_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sy_gb_lb_2.setFont(font)
        self.sy_gb_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sy_gb_lb_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sy_gb_lb_2.setObjectName("sy_gb_lb_2")
        self.horizontalLayout_22.addWidget(self.sy_gb_lb_2)
        self.sy_gb_bt_1 = QtWidgets.QToolButton(self.sy_gb_1)
        self.sy_gb_bt_1.setMinimumSize(QtCore.QSize(40, 40))
        self.sy_gb_bt_1.setMaximumSize(QtCore.QSize(40, 40))
        self.sy_gb_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.sy_gb_bt_1.setText("")
        self.sy_gb_bt_1.setIcon(icon2)
        self.sy_gb_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.sy_gb_bt_1.setObjectName("sy_gb_bt_1")
        self.horizontalLayout_22.addWidget(self.sy_gb_bt_1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem21)
        self.gridLayout_19.addLayout(self.horizontalLayout_22, 0, 0, 1, 1)
        self.sy_vl.addWidget(self.sy_gb_1)
        self.lo_gb_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lo_gb_1.setFont(font)
        self.lo_gb_1.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.lo_gb_1.setObjectName("lo_gb_1")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.lo_gb_1)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lo_gb_lb_1 = QtWidgets.QLabel(self.lo_gb_1)
        self.lo_gb_lb_1.setMinimumSize(QtCore.QSize(0, 39))
        self.lo_gb_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lo_gb_lb_1.setFont(font)
        self.lo_gb_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.lo_gb_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lo_gb_lb_1.setObjectName("lo_gb_lb_1")
        self.gridLayout_3.addWidget(self.lo_gb_lb_1, 0, 0, 1, 1)
        self.lo_gb_lb_2 = QtWidgets.QLabel(self.lo_gb_1)
        self.lo_gb_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.lo_gb_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lo_gb_lb_2.setFont(font)
        self.lo_gb_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.lo_gb_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lo_gb_lb_2.setObjectName("lo_gb_lb_2")
        self.gridLayout_3.addWidget(self.lo_gb_lb_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lo_gb_ln_1 = QtWidgets.QLineEdit(self.lo_gb_1)
        self.lo_gb_ln_1.setMinimumSize(QtCore.QSize(0, 40))
        self.lo_gb_ln_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lo_gb_ln_1.setFont(font)
        self.lo_gb_ln_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color: white;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.lo_gb_ln_1.setObjectName("lo_gb_ln_1")
        self.horizontalLayout.addWidget(self.lo_gb_ln_1)
        self.lo_gb_bt_1 = QtWidgets.QToolButton(self.lo_gb_1)
        self.lo_gb_bt_1.setMinimumSize(QtCore.QSize(40, 40))
        self.lo_gb_bt_1.setMaximumSize(QtCore.QSize(40, 40))
        self.lo_gb_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.lo_gb_bt_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lo_gb_bt_1.setIcon(icon3)
        self.lo_gb_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.lo_gb_bt_1.setAutoRaise(False)
        self.lo_gb_bt_1.setObjectName("lo_gb_bt_1")
        self.horizontalLayout.addWidget(self.lo_gb_bt_1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lo_gb_cb_1 = QtWidgets.QComboBox(self.lo_gb_1)
        self.lo_gb_cb_1.setMinimumSize(QtCore.QSize(150, 40))
        self.lo_gb_cb_1.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lo_gb_cb_1.setFont(font)
        self.lo_gb_cb_1.setStyleSheet("")
        self.lo_gb_cb_1.setObjectName("lo_gb_cb_1")
        self.lo_gb_cb_1.addItem("")
        self.lo_gb_cb_1.addItem("")
        self.lo_gb_cb_1.addItem("")
        self.lo_gb_cb_1.addItem("")
        self.lo_gb_cb_1.addItem("")
        self.horizontalLayout_7.addWidget(self.lo_gb_cb_1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.sy_vl.addWidget(self.lo_gb_1)
        self.sy_gb_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sy_gb_2.setFont(font)
        self.sy_gb_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    margin-right: 8px;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sy_gb_2.setObjectName("sy_gb_2")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.sy_gb_2)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.sy_gb_2_ck_1 = QtWidgets.QCheckBox(self.sy_gb_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sy_gb_2_ck_1.setFont(font)
        self.sy_gb_2_ck_1.setStyleSheet("QCheckBox {\n"
"    spacing: 10px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    image: url(icons/checkbox_icon_unchecked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    image: url(icons/checkbox_icon_checked.svg);\n"
"}")
        self.sy_gb_2_ck_1.setObjectName("sy_gb_2_ck_1")
        self.horizontalLayout_25.addWidget(self.sy_gb_2_ck_1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem23)
        self.gridLayout_32.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem24 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem24)
        self.sy_gb_2_bt_1 = QtWidgets.QToolButton(self.sy_gb_2)
        self.sy_gb_2_bt_1.setMinimumSize(QtCore.QSize(250, 40))
        self.sy_gb_2_bt_1.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.sy_gb_2_bt_1.setFont(font)
        self.sy_gb_2_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: rgb(230,230,230);\n"
"    color: rgb(45,45,45)\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgb(220,220,220);\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: rgb(210,210,210);\n"
"}")
        self.sy_gb_2_bt_1.setObjectName("sy_gb_2_bt_1")
        self.horizontalLayout_26.addWidget(self.sy_gb_2_bt_1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem25)
        self.gridLayout_32.addLayout(self.horizontalLayout_26, 1, 0, 1, 1)
        self.sy_vl.addWidget(self.sy_gb_2)
        self.gridLayout_10.addLayout(self.sy_vl, 0, 0, 1, 1)
        self.scroll_area_5.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_12.addWidget(self.scroll_area_5, 0, 0, 1, 1)
        self.stack_widget.addWidget(self.page_6)
        self.gridLayout_34.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(optionWindow)
        self.stack_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = self.section_list.isSortingEnabled()
        self.section_list.setSortingEnabled(False)
        item = self.section_list.item(0)
        item.setText(_translate("optionWindow", "Affichage"))
        item = self.section_list.item(1)
        item.setText(_translate("optionWindow", "API Météo"))
        item = self.section_list.item(2)
        item.setText(_translate("optionWindow", "Base de données"))
        item = self.section_list.item(3)
        item.setText(_translate("optionWindow", "Capteurs"))
        item = self.section_list.item(4)
        item.setText(_translate("optionWindow", "Series temporelles"))
        item = self.section_list.item(5)
        item.setText(_translate("optionWindow", "Système"))
        self.section_list.setSortingEnabled(__sortingEnabled)
        self.af_gb_int.setTitle(_translate("optionWindow", "Intérieur"))
        self.af_gb_int_lb_1.setText(_translate("optionWindow", "Capteur :"))
        self.af_gb_int_cb_1.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.af_gb_int_lb_2.setText(_translate("optionWindow", "Rafraichissement :"))
        self.af_gb_int_lb_3.setText(_translate("optionWindow", "secondes"))
        self.af_gb_int_ck_1.setText(_translate("optionWindow", "Pression au niveau de la mer ?"))
        self.af_gb_ext.setTitle(_translate("optionWindow", "Extérieur"))
        self.af_gb_ext_lb_1.setText(_translate("optionWindow", "Capteur :"))
        self.af_gb_ext_cb_1.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.af_gb_ext_lb_2.setText(_translate("optionWindow", "Rafraichissement :"))
        self.af_gb_ext_lb_3.setText(_translate("optionWindow", "secondes"))
        self.af_gb_ext_ck_1.setText(_translate("optionWindow", "Pression au niveau de la mer ?"))
        self.ap_gb_1.setTitle(_translate("optionWindow", "API Météo"))
        self.ap_gb_rb_1.setText(_translate("optionWindow", "Météo France"))
        self.ap_gb_rb_2.setText(_translate("optionWindow", "OpenWeather"))
        self.ap_gb_2.setTitle(_translate("optionWindow", "Localisation"))
        self.ap_gb_2_bt_2.setText(_translate("optionWindow", "Rechercher"))
        self.ap_gb_2_lb_1.setText(_translate("optionWindow", "Ville :"))
        self.ap_gb_2_lb_2.setText(_translate("optionWindow", "Code postal :"))
        self.ap_gb_2_lb_3.setText(_translate("optionWindow", "Département :"))
        self.ap_gb_5.setTitle(_translate("optionWindow", "Requête des prévisions météo"))
        self.ow_label_16.setText(_translate("optionWindow", "Intervalle :"))
        self.ow_label_17.setText(_translate("optionWindow", "minutes"))
        self.db_gb.setTitle(_translate("optionWindow", "PostgreSQL"))
        self.db_gb_lb_2.setText(_translate("optionWindow", "Mot de passe :"))
        self.db_gb_lb_1.setText(_translate("optionWindow", "Utilisateur :"))
        self.db_gb_lb_3.setText(_translate("optionWindow", "Base de données :"))
        self.db_gb_lb_4.setText(_translate("optionWindow", "Hôte :"))
        self.db_gb_lb_5.setText(_translate("optionWindow", "Port :"))
        self.db_gb_2.setTitle(_translate("optionWindow", "Exporter"))
        self.db_gb_2_lb_1.setText(_translate("optionWindow", "Capteur(s) :"))
        self.db_gb_2_cb_1.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.sy_gb_2_bt_2.setText(_translate("optionWindow", "Exporter en CSV"))
        self.ca_lb_1.setText(_translate("optionWindow", "Rafraichissement :"))
        self.ca_lb_2.setText(_translate("optionWindow", "secondes"))
        self.ca_gb_1.setTitle(_translate("optionWindow", "Gestion des capteurs"))
        self.ca_gc_lb_1.setText(_translate("optionWindow", "Gestion DS18B20 :"))
        self.ca_gc_lb_2.setText(_translate("optionWindow", "Gestion BME280 :"))
        self.ca_gc_lb_3.setText(_translate("optionWindow", "Gestion MQTT :"))
        self.ts_gb_int.setTitle(_translate("optionWindow", "Intérieur"))
        self.ts_gb_int_lb_1.setText(_translate("optionWindow", "Température :"))
        self.ts_gb_int_lb_2.setText(_translate("optionWindow", "Humidité :"))
        self.ts_gb_int_cb_1.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.ts_gb_int_cb_2.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.ts_gb_ext.setTitle(_translate("optionWindow", "Extérieur"))
        self.ts_gb_ext_cb_2.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.ts_gb_ext_lb_2.setText(_translate("optionWindow", "Pression :"))
        self.ts_gb_ext_lb_1.setText(_translate("optionWindow", "Température :"))
        self.ts_gb_ext_cb_1.setItemText(0, _translate("optionWindow", "Pas de capteur"))
        self.ts_gb_ext_ck_1.setText(_translate("optionWindow", "Pression au niveau de la mer ?"))
        self.sy_gb_1.setTitle(_translate("optionWindow", "Calcul pression au niveau de la mer"))
        self.sy_gb_lb_1.setText(_translate("optionWindow", "Altitude :"))
        self.sy_gb_lb_2.setText(_translate("optionWindow", "mètres"))
        self.lo_gb_1.setTitle(_translate("optionWindow", "Options de log"))
        self.lo_gb_lb_1.setText(_translate("optionWindow", "Niveau de log :"))
        self.lo_gb_lb_2.setText(_translate("optionWindow", "Chemin du log :"))
        self.lo_gb_cb_1.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.lo_gb_cb_1.setItemText(1, _translate("optionWindow", "INFO"))
        self.lo_gb_cb_1.setItemText(2, _translate("optionWindow", "WARNING"))
        self.lo_gb_cb_1.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.lo_gb_cb_1.setItemText(4, _translate("optionWindow", "ERROR"))
        self.sy_gb_2.setTitle(_translate("optionWindow", "Mise à jour"))
        self.sy_gb_2_ck_1.setText(_translate("optionWindow", "Vérifier les mises à jour au démarrage"))
        self.sy_gb_2_bt_1.setText(_translate("optionWindow", "Vérifier maintenant"))
