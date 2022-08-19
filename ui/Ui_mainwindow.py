# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("QMainWindow {\n"
"   background: rgb(240,240,240);\n"
"\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_21.setContentsMargins(0, 8, 0, 0)
        self.gridLayout_21.setHorizontalSpacing(7)
        self.gridLayout_21.setVerticalSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, -1, -1, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit_button = QtWidgets.QToolButton(self.centralwidget)
        self.exit_button.setMinimumSize(QtCore.QSize(55, 55))
        self.exit_button.setMaximumSize(QtCore.QSize(55, 55))
        self.exit_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.exit_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/exit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QtCore.QSize(50, 50))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.separator = QtWidgets.QToolButton(self.centralwidget)
        self.separator.setEnabled(True)
        self.separator.setMinimumSize(QtCore.QSize(16, 55))
        self.separator.setMaximumSize(QtCore.QSize(16, 55))
        self.separator.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.separator.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/separator_icon_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.separator.setIcon(icon1)
        self.separator.setIconSize(QtCore.QSize(20, 50))
        self.separator.setObjectName("separator")
        self.horizontalLayout.addWidget(self.separator)
        self.option_button = QtWidgets.QToolButton(self.centralwidget)
        self.option_button.setEnabled(True)
        self.option_button.setMinimumSize(QtCore.QSize(55, 55))
        self.option_button.setMaximumSize(QtCore.QSize(55, 55))
        self.option_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.option_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.option_button.setIcon(icon2)
        self.option_button.setIconSize(QtCore.QSize(50, 50))
        self.option_button.setObjectName("option_button")
        self.horizontalLayout.addWidget(self.option_button)
        self.about_button = QtWidgets.QToolButton(self.centralwidget)
        self.about_button.setEnabled(True)
        self.about_button.setMinimumSize(QtCore.QSize(55, 55))
        self.about_button.setMaximumSize(QtCore.QSize(55, 55))
        self.about_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.about_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/about_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_button.setIcon(icon3)
        self.about_button.setIconSize(QtCore.QSize(50, 50))
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        self.warning_button = QtWidgets.QToolButton(self.centralwidget)
        self.warning_button.setEnabled(True)
        self.warning_button.setMinimumSize(QtCore.QSize(55, 55))
        self.warning_button.setMaximumSize(QtCore.QSize(55, 55))
        self.warning_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.warning_button.setText("")
        self.warning_button.setIconSize(QtCore.QSize(55, 55))
        self.warning_button.setObjectName("warning_button")
        self.horizontalLayout.addWidget(self.warning_button)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setMinimumSize(QtCore.QSize(120, 55))
        self.time_label.setMaximumSize(QtCore.QSize(150, 55))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setWordWrap(True)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setMinimumSize(QtCore.QSize(180, 55))
        self.date_label.setMaximumSize(QtCore.QSize(120, 55))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setWordWrap(True)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout.addWidget(self.date_label)
        self.gridLayout_21.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_21.addItem(spacerItem2, 1, 0, 1, 1)
        self.horizontal_line = QtWidgets.QFrame(self.centralwidget)
        self.horizontal_line.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"}")
        self.horizontal_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_line.setObjectName("horizontal_line")
        self.gridLayout_21.addWidget(self.horizontal_line, 2, 0, 2, 3)
        self.vertical_line = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   height: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: -50px;\n"
"}")
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setObjectName("vertical_line")
        self.gridLayout_21.addWidget(self.vertical_line, 3, 1, 2, 2)
        self.menu_scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_scroll_area.sizePolicy().hasHeightForWidth())
        self.menu_scroll_area.setSizePolicy(sizePolicy)
        self.menu_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QScrollBar:vertical {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  margin: 21px 0px 21px 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"  border: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
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
"  background-color: rgb(167, 167, 167);\n"
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
"  background-color: rgb(167, 167, 167);\n"
"}\n"
"\n"
"QScrollBar:handle:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"  border-top: 0px solid rgb(240,240,240);\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: bottom;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid rgb(240,240,240);\n"
"  background-color: rgb(240, 240, 240);\n"
"  height: 20px;\n"
"  subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
"  border-top: 0px solid white;\n"
"  border-left: 0px solid rgb(240,240,240);\n"
"  border-right: 0px solid white;\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: right;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"  background-color: rgb(96, 96, 96);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"  border-top: 0px solid white;\n"
"  border-left: 0px solid white;\n"
"  border-right: 0px solid rgb(240,240,240);\n"
"  border-bottom: 0px solid white;\n"
"  background-color: rgb(240, 240, 240);\n"
"  width: 20px;\n"
"  subcontrol-position: left;\n"
"  subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"  background-color: rgb(219, 219, 219);\n"
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
        self.menu_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menu_scroll_area.setLineWidth(0)
        self.menu_scroll_area.setWidgetResizable(True)
        self.menu_scroll_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.menu_scroll_area.setObjectName("menu_scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 135, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.menu_layout = QtWidgets.QVBoxLayout()
        self.menu_layout.setContentsMargins(6, -1, 0, 4)
        self.menu_layout.setSpacing(4)
        self.menu_layout.setObjectName("menu_layout")
        self.in_out_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.in_out_bt.setMinimumSize(QtCore.QSize(128, 100))
        self.in_out_bt.setMaximumSize(QtCore.QSize(128, 100))
        self.in_out_bt.setStyleSheet("QToolButton {\n"
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
        self.in_out_bt.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/int_ext_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.in_out_bt.setIcon(icon4)
        self.in_out_bt.setIconSize(QtCore.QSize(110, 110))
        self.in_out_bt.setObjectName("in_out_bt")
        self.menu_layout.addWidget(self.in_out_bt)
        self.ephemeride_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ephemeride_bt.setMinimumSize(QtCore.QSize(128, 100))
        self.ephemeride_bt.setMaximumSize(QtCore.QSize(128, 100))
        self.ephemeride_bt.setStyleSheet("QToolButton {\n"
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
        self.ephemeride_bt.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/ephemeride_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ephemeride_bt.setIcon(icon5)
        self.ephemeride_bt.setIconSize(QtCore.QSize(90, 90))
        self.ephemeride_bt.setObjectName("ephemeride_bt")
        self.menu_layout.addWidget(self.ephemeride_bt)
        self.time_series_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.time_series_bt.setMinimumSize(QtCore.QSize(128, 100))
        self.time_series_bt.setMaximumSize(QtCore.QSize(128, 100))
        self.time_series_bt.setStyleSheet("QToolButton {\n"
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
        self.time_series_bt.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/time_series_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.time_series_bt.setIcon(icon6)
        self.time_series_bt.setIconSize(QtCore.QSize(110, 110))
        self.time_series_bt.setObjectName("time_series_bt")
        self.menu_layout.addWidget(self.time_series_bt)
        self.h1_prev_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.h1_prev_bt.setMinimumSize(QtCore.QSize(128, 100))
        self.h1_prev_bt.setMaximumSize(QtCore.QSize(128, 100))
        self.h1_prev_bt.setStyleSheet("QToolButton {\n"
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
        self.h1_prev_bt.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/prev_1h_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.h1_prev_bt.setIcon(icon7)
        self.h1_prev_bt.setIconSize(QtCore.QSize(110, 110))
        self.h1_prev_bt.setObjectName("h1_prev_bt")
        self.menu_layout.addWidget(self.h1_prev_bt)
        self.h6_prev_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.h6_prev_bt.setMinimumSize(QtCore.QSize(128, 100))
        self.h6_prev_bt.setMaximumSize(QtCore.QSize(128, 100))
        self.h6_prev_bt.setStyleSheet("QToolButton {\n"
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
        self.h6_prev_bt.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/prev_6h_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.h6_prev_bt.setIcon(icon8)
        self.h6_prev_bt.setIconSize(QtCore.QSize(110, 110))
        self.h6_prev_bt.setObjectName("h6_prev_bt")
        self.menu_layout.addWidget(self.h6_prev_bt)
        self.gridLayout.addLayout(self.menu_layout, 0, 0, 1, 1)
        self.menu_scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_21.addWidget(self.menu_scroll_area, 4, 0, 1, 1)
        self.main_stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_stacked_widget.sizePolicy().hasHeightForWidth())
        self.main_stacked_widget.setSizePolicy(sizePolicy)
        self.main_stacked_widget.setObjectName("main_stacked_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_3.setContentsMargins(6, 10, 5, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_frame = QtWidgets.QFrame(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_frame.sizePolicy().hasHeightForWidth())
        self.in_frame.setSizePolicy(sizePolicy)
        self.in_frame.setStyleSheet("QFrame#in_frame {\n"
"   background: #E2F0D9;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.in_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_frame.setObjectName("in_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.in_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.in_old_data = QtWidgets.QLabel(self.in_frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_old_data.setFont(font)
        self.in_old_data.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.in_old_data.setText("")
        self.in_old_data.setAlignment(QtCore.Qt.AlignCenter)
        self.in_old_data.setObjectName("in_old_data")
        self.gridLayout_4.addWidget(self.in_old_data, 5, 0, 1, 1)
        self.in_label_3 = QtWidgets.QLabel(self.in_frame)
        self.in_label_3.setMinimumSize(QtCore.QSize(150, 50))
        self.in_label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_label_3.setFont(font)
        self.in_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.in_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label_3.setWordWrap(True)
        self.in_label_3.setObjectName("in_label_3")
        self.gridLayout_4.addWidget(self.in_label_3, 7, 0, 1, 1)
        self.in_label_2 = QtWidgets.QLabel(self.in_frame)
        self.in_label_2.setMinimumSize(QtCore.QSize(150, 50))
        self.in_label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_label_2.setFont(font)
        self.in_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.in_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label_2.setWordWrap(True)
        self.in_label_2.setObjectName("in_label_2")
        self.gridLayout_4.addWidget(self.in_label_2, 6, 0, 1, 1)
        self.in_humidity_bt = QtWidgets.QToolButton(self.in_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_humidity_bt.sizePolicy().hasHeightForWidth())
        self.in_humidity_bt.setSizePolicy(sizePolicy)
        self.in_humidity_bt.setMinimumSize(QtCore.QSize(150, 45))
        self.in_humidity_bt.setMaximumSize(QtCore.QSize(393, 45))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_humidity_bt.setFont(font)
        self.in_humidity_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.in_humidity_bt.setObjectName("in_humidity_bt")
        self.gridLayout_4.addWidget(self.in_humidity_bt, 1, 0, 1, 1)
        self.in_lab_frame = QtWidgets.QFrame(self.in_frame)
        self.in_lab_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.in_lab_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.in_lab_frame.setStyleSheet("QFrame#in_lab_frame {\n"
"    border-top: 1px solid rgb(75,75,75);\n"
"    border-bottom: 1px solid rgb(75,75,75);\n"
"}")
        self.in_lab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_lab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_lab_frame.setObjectName("in_lab_frame")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.in_lab_frame)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.in_signal_bt = QtWidgets.QToolButton(self.in_lab_frame)
        self.in_signal_bt.setEnabled(False)
        self.in_signal_bt.setMinimumSize(QtCore.QSize(45, 45))
        self.in_signal_bt.setMaximumSize(QtCore.QSize(45, 45))
        self.in_signal_bt.setStyleSheet("QToolButton {\n"
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
        self.in_signal_bt.setText("")
        self.in_signal_bt.setIconSize(QtCore.QSize(30, 30))
        self.in_signal_bt.setObjectName("in_signal_bt")
        self.gridLayout_20.addWidget(self.in_signal_bt, 0, 0, 1, 1)
        self.in_label_1 = QtWidgets.QLabel(self.in_lab_frame)
        self.in_label_1.setMinimumSize(QtCore.QSize(150, 25))
        self.in_label_1.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_label_1.setFont(font)
        self.in_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.in_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label_1.setWordWrap(True)
        self.in_label_1.setObjectName("in_label_1")
        self.gridLayout_20.addWidget(self.in_label_1, 0, 1, 1, 1)
        self.in_battery_bt = QtWidgets.QToolButton(self.in_lab_frame)
        self.in_battery_bt.setEnabled(False)
        self.in_battery_bt.setMinimumSize(QtCore.QSize(45, 45))
        self.in_battery_bt.setMaximumSize(QtCore.QSize(45, 45))
        self.in_battery_bt.setStyleSheet("QToolButton {\n"
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
        self.in_battery_bt.setText("")
        self.in_battery_bt.setIconSize(QtCore.QSize(30, 30))
        self.in_battery_bt.setObjectName("in_battery_bt")
        self.gridLayout_20.addWidget(self.in_battery_bt, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.in_lab_frame, 0, 0, 1, 1)
        self.in_temperature_label = QtWidgets.QLabel(self.in_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_temperature_label.sizePolicy().hasHeightForWidth())
        self.in_temperature_label.setSizePolicy(sizePolicy)
        self.in_temperature_label.setMinimumSize(QtCore.QSize(150, 50))
        self.in_temperature_label.setMaximumSize(QtCore.QSize(393, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(68)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_temperature_label.setFont(font)
        self.in_temperature_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.in_temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.in_temperature_label.setWordWrap(True)
        self.in_temperature_label.setObjectName("in_temperature_label")
        self.gridLayout_4.addWidget(self.in_temperature_label, 4, 0, 1, 1)
        self.in_pressure_bt = QtWidgets.QToolButton(self.in_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.in_pressure_bt.sizePolicy().hasHeightForWidth())
        self.in_pressure_bt.setSizePolicy(sizePolicy)
        self.in_pressure_bt.setMinimumSize(QtCore.QSize(150, 45))
        self.in_pressure_bt.setMaximumSize(QtCore.QSize(393, 45))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_pressure_bt.setFont(font)
        self.in_pressure_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.in_pressure_bt.setObjectName("in_pressure_bt")
        self.gridLayout_4.addWidget(self.in_pressure_bt, 2, 0, 1, 1)
        self.in_no_data = QtWidgets.QLabel(self.in_frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.in_no_data.setFont(font)
        self.in_no_data.setText("")
        self.in_no_data.setObjectName("in_no_data")
        self.gridLayout_4.addWidget(self.in_no_data, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.in_frame, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.out_frame = QtWidgets.QFrame(self.page_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_frame.sizePolicy().hasHeightForWidth())
        self.out_frame.setSizePolicy(sizePolicy)
        self.out_frame.setStyleSheet("QFrame#out_frame {\n"
"   background: #FBE5D6;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.out_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_frame.setObjectName("out_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.out_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.out_humidity_bt = QtWidgets.QToolButton(self.out_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_humidity_bt.sizePolicy().hasHeightForWidth())
        self.out_humidity_bt.setSizePolicy(sizePolicy)
        self.out_humidity_bt.setMinimumSize(QtCore.QSize(150, 45))
        self.out_humidity_bt.setMaximumSize(QtCore.QSize(393, 45))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_humidity_bt.setFont(font)
        self.out_humidity_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.out_humidity_bt.setObjectName("out_humidity_bt")
        self.gridLayout_5.addWidget(self.out_humidity_bt, 1, 0, 1, 1)
        self.out_old_data = QtWidgets.QLabel(self.out_frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setItalic(True)
        self.out_old_data.setFont(font)
        self.out_old_data.setText("")
        self.out_old_data.setAlignment(QtCore.Qt.AlignCenter)
        self.out_old_data.setObjectName("out_old_data")
        self.gridLayout_5.addWidget(self.out_old_data, 5, 0, 1, 1)
        self.out_label_3 = QtWidgets.QLabel(self.out_frame)
        self.out_label_3.setMinimumSize(QtCore.QSize(150, 50))
        self.out_label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_label_3.setFont(font)
        self.out_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.out_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.out_label_3.setWordWrap(True)
        self.out_label_3.setObjectName("out_label_3")
        self.gridLayout_5.addWidget(self.out_label_3, 7, 0, 1, 1)
        self.out_lab_frame = QtWidgets.QFrame(self.out_frame)
        self.out_lab_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.out_lab_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.out_lab_frame.setStyleSheet("QFrame#out_lab_frame {\n"
"    border-top: 1px solid rgb(75,75,75);\n"
"    border-bottom: 1px solid rgb(75,75,75);\n"
"}")
        self.out_lab_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_lab_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_lab_frame.setObjectName("out_lab_frame")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.out_lab_frame)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.out_battery_bt = QtWidgets.QToolButton(self.out_lab_frame)
        self.out_battery_bt.setEnabled(False)
        self.out_battery_bt.setMinimumSize(QtCore.QSize(45, 45))
        self.out_battery_bt.setMaximumSize(QtCore.QSize(45, 45))
        self.out_battery_bt.setStyleSheet("QToolButton {\n"
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
        self.out_battery_bt.setText("")
        self.out_battery_bt.setIconSize(QtCore.QSize(30, 30))
        self.out_battery_bt.setObjectName("out_battery_bt")
        self.gridLayout_23.addWidget(self.out_battery_bt, 0, 2, 1, 1)
        self.out_label_1 = QtWidgets.QLabel(self.out_lab_frame)
        self.out_label_1.setMinimumSize(QtCore.QSize(150, 25))
        self.out_label_1.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_label_1.setFont(font)
        self.out_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.out_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.out_label_1.setWordWrap(True)
        self.out_label_1.setObjectName("out_label_1")
        self.gridLayout_23.addWidget(self.out_label_1, 0, 1, 1, 1)
        self.out_signal_bt = QtWidgets.QToolButton(self.out_lab_frame)
        self.out_signal_bt.setEnabled(False)
        self.out_signal_bt.setMinimumSize(QtCore.QSize(45, 45))
        self.out_signal_bt.setMaximumSize(QtCore.QSize(45, 45))
        self.out_signal_bt.setStyleSheet("QToolButton {\n"
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
        self.out_signal_bt.setText("")
        self.out_signal_bt.setIconSize(QtCore.QSize(30, 30))
        self.out_signal_bt.setObjectName("out_signal_bt")
        self.gridLayout_23.addWidget(self.out_signal_bt, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.out_lab_frame, 0, 0, 1, 1)
        self.out_temperature_label = QtWidgets.QLabel(self.out_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_temperature_label.sizePolicy().hasHeightForWidth())
        self.out_temperature_label.setSizePolicy(sizePolicy)
        self.out_temperature_label.setMinimumSize(QtCore.QSize(150, 50))
        self.out_temperature_label.setMaximumSize(QtCore.QSize(393, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(68)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_temperature_label.setFont(font)
        self.out_temperature_label.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.out_temperature_label.setAlignment(QtCore.Qt.AlignCenter)
        self.out_temperature_label.setWordWrap(True)
        self.out_temperature_label.setObjectName("out_temperature_label")
        self.gridLayout_5.addWidget(self.out_temperature_label, 4, 0, 1, 1)
        self.out_label_2 = QtWidgets.QLabel(self.out_frame)
        self.out_label_2.setMinimumSize(QtCore.QSize(150, 50))
        self.out_label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_label_2.setFont(font)
        self.out_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.out_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.out_label_2.setWordWrap(True)
        self.out_label_2.setObjectName("out_label_2")
        self.gridLayout_5.addWidget(self.out_label_2, 6, 0, 1, 1)
        self.out_pressure_bt = QtWidgets.QToolButton(self.out_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_pressure_bt.sizePolicy().hasHeightForWidth())
        self.out_pressure_bt.setSizePolicy(sizePolicy)
        self.out_pressure_bt.setMinimumSize(QtCore.QSize(150, 45))
        self.out_pressure_bt.setMaximumSize(QtCore.QSize(393, 45))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_pressure_bt.setFont(font)
        self.out_pressure_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.out_pressure_bt.setObjectName("out_pressure_bt")
        self.gridLayout_5.addWidget(self.out_pressure_bt, 2, 0, 1, 1)
        self.out_no_data = QtWidgets.QLabel(self.out_frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setItalic(True)
        self.out_no_data.setFont(font)
        self.out_no_data.setText("")
        self.out_no_data.setObjectName("out_no_data")
        self.gridLayout_5.addWidget(self.out_no_data, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.out_frame, 0, 2, 1, 1)
        self.main_stacked_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.day_box = QtWidgets.QGroupBox(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.day_box.setFont(font)
        self.day_box.setStyleSheet("QGroupBox{\n"
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
        self.day_box.setObjectName("day_box")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.day_box)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.day_lb_1 = QtWidgets.QLabel(self.day_box)
        self.day_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.day_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.day_lb_1.setFont(font)
        self.day_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.day_lb_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.day_lb_1.setWordWrap(True)
        self.day_lb_1.setObjectName("day_lb_1")
        self.horizontalLayout_5.addWidget(self.day_lb_1)
        self.day_lb_3 = QtWidgets.QLabel(self.day_box)
        self.day_lb_3.setMinimumSize(QtCore.QSize(0, 40))
        self.day_lb_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.day_lb_3.setFont(font)
        self.day_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.day_lb_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.day_lb_3.setWordWrap(True)
        self.day_lb_3.setObjectName("day_lb_3")
        self.horizontalLayout_5.addWidget(self.day_lb_3)
        self.gridLayout_25.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.day_lb_2 = QtWidgets.QLabel(self.day_box)
        self.day_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.day_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.day_lb_2.setFont(font)
        self.day_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.day_lb_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.day_lb_2.setWordWrap(True)
        self.day_lb_2.setObjectName("day_lb_2")
        self.gridLayout_25.addWidget(self.day_lb_2, 1, 0, 1, 1)
        self.gridLayout_26.addWidget(self.day_box, 0, 0, 1, 1)
        self.sun_box = QtWidgets.QGroupBox(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sun_box.setFont(font)
        self.sun_box.setStyleSheet("QGroupBox{\n"
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
        self.sun_box.setObjectName("sun_box")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.sun_box)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.sun_lb_1 = QtWidgets.QLabel(self.sun_box)
        self.sun_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.sun_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sun_lb_1.setFont(font)
        self.sun_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sun_lb_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sun_lb_1.setWordWrap(True)
        self.sun_lb_1.setObjectName("sun_lb_1")
        self.gridLayout_24.addWidget(self.sun_lb_1, 0, 0, 1, 1)
        self.sun_lb_2 = QtWidgets.QLabel(self.sun_box)
        self.sun_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.sun_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sun_lb_2.setFont(font)
        self.sun_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.sun_lb_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sun_lb_2.setWordWrap(True)
        self.sun_lb_2.setObjectName("sun_lb_2")
        self.gridLayout_24.addWidget(self.sun_lb_2, 1, 0, 1, 1)
        self.gridLayout_26.addWidget(self.sun_box, 1, 0, 1, 1)
        self.moon_box = QtWidgets.QGroupBox(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.moon_box.setFont(font)
        self.moon_box.setStyleSheet("QGroupBox{\n"
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
        self.moon_box.setObjectName("moon_box")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.moon_box)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.moon_lb_1 = QtWidgets.QLabel(self.moon_box)
        self.moon_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.moon_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.moon_lb_1.setFont(font)
        self.moon_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.moon_lb_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.moon_lb_1.setWordWrap(True)
        self.moon_lb_1.setObjectName("moon_lb_1")
        self.gridLayout_22.addWidget(self.moon_lb_1, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.moon_lb_2 = QtWidgets.QLabel(self.moon_box)
        self.moon_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.moon_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.moon_lb_2.setFont(font)
        self.moon_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.moon_lb_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.moon_lb_2.setWordWrap(True)
        self.moon_lb_2.setObjectName("moon_lb_2")
        self.horizontalLayout_4.addWidget(self.moon_lb_2)
        self.moon_lb_3 = QtWidgets.QLabel(self.moon_box)
        self.moon_lb_3.setMinimumSize(QtCore.QSize(0, 40))
        self.moon_lb_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.moon_lb_3.setFont(font)
        self.moon_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.moon_lb_3.setText("")
        self.moon_lb_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.moon_lb_3.setWordWrap(True)
        self.moon_lb_3.setObjectName("moon_lb_3")
        self.horizontalLayout_4.addWidget(self.moon_lb_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout_22.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_26.addWidget(self.moon_box, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 69, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem5, 3, 0, 1, 1)
        self.main_stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setContentsMargins(6, 10, 10, 5)
        self.gridLayout_8.setHorizontalSpacing(7)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.time_series_stack = QtWidgets.QStackedWidget(self.page_3)
        self.time_series_stack.setObjectName("time_series_stack")
        self.ts_page_1 = QtWidgets.QWidget()
        self.ts_page_1.setObjectName("ts_page_1")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ts_page_1)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ts_frame_1 = QtWidgets.QFrame(self.ts_page_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ts_frame_1.sizePolicy().hasHeightForWidth())
        self.ts_frame_1.setSizePolicy(sizePolicy)
        self.ts_frame_1.setStyleSheet("QFrame {\n"
"   background: #E2F0D9;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.ts_frame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ts_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ts_frame_1.setObjectName("ts_frame_1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.ts_frame_1)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.in_label_4 = QtWidgets.QLabel(self.ts_frame_1)
        self.in_label_4.setMinimumSize(QtCore.QSize(150, 40))
        self.in_label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.in_label_4.setFont(font)
        self.in_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(75,75,75);\n"
"    border-bottom: 1px solid rgb(75,75,75);\n"
"    margin-left: 270px;\n"
"    margin-right: 270px;\n"
"    margin-top: 5px;\n"
"    border-radius: 0px;\n"
"}")
        self.in_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.in_label_4.setWordWrap(True)
        self.in_label_4.setIndent(0)
        self.in_label_4.setObjectName("in_label_4")
        self.gridLayout_6.addWidget(self.in_label_4, 0, 0, 1, 1)
        self.plot_layout_1 = QtWidgets.QVBoxLayout()
        self.plot_layout_1.setContentsMargins(-1, -1, -1, 20)
        self.plot_layout_1.setObjectName("plot_layout_1")
        self.gridLayout_6.addLayout(self.plot_layout_1, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.ts_frame_1, 0, 0, 1, 1)
        self.time_series_stack.addWidget(self.ts_page_1)
        self.ts_page_2 = QtWidgets.QWidget()
        self.ts_page_2.setObjectName("ts_page_2")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.ts_page_2)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.ts_frame_2 = QtWidgets.QFrame(self.ts_page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ts_frame_2.sizePolicy().hasHeightForWidth())
        self.ts_frame_2.setSizePolicy(sizePolicy)
        self.ts_frame_2.setStyleSheet("QFrame {\n"
"   background: #FBE5D6;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.ts_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ts_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ts_frame_2.setObjectName("ts_frame_2")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.ts_frame_2)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.out_label_5 = QtWidgets.QLabel(self.ts_frame_2)
        self.out_label_5.setMinimumSize(QtCore.QSize(150, 40))
        self.out_label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.out_label_5.setFont(font)
        self.out_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"    background: transparent;\n"
"    border-top: 1px solid rgb(75,75,75);\n"
"    border-bottom: 1px solid rgb(75,75,75);\n"
"    margin-left: 270px;\n"
"    margin-right: 270px;\n"
"    margin-top: 5px;\n"
"    border-radius: 0px;\n"
"}")
        self.out_label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.out_label_5.setWordWrap(True)
        self.out_label_5.setIndent(0)
        self.out_label_5.setObjectName("out_label_5")
        self.gridLayout_15.addWidget(self.out_label_5, 0, 0, 1, 1)
        self.plot_layout_3 = QtWidgets.QVBoxLayout()
        self.plot_layout_3.setContentsMargins(-1, -1, -1, 20)
        self.plot_layout_3.setObjectName("plot_layout_3")
        self.gridLayout_15.addLayout(self.plot_layout_3, 1, 0, 1, 1)
        self.gridLayout_16.addWidget(self.ts_frame_2, 0, 0, 1, 1)
        self.time_series_stack.addWidget(self.ts_page_2)
        self.gridLayout_8.addWidget(self.time_series_stack, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_ts_button = QtWidgets.QToolButton(self.page_3)
        self.left_ts_button.setMinimumSize(QtCore.QSize(55, 55))
        self.left_ts_button.setMaximumSize(QtCore.QSize(55, 55))
        self.left_ts_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.left_ts_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/left_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_ts_button.setIcon(icon9)
        self.left_ts_button.setIconSize(QtCore.QSize(50, 50))
        self.left_ts_button.setArrowType(QtCore.Qt.NoArrow)
        self.left_ts_button.setObjectName("left_ts_button")
        self.horizontalLayout_2.addWidget(self.left_ts_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.ts_page_marker_1 = QtWidgets.QToolButton(self.page_3)
        self.ts_page_marker_1.setEnabled(False)
        self.ts_page_marker_1.setMinimumSize(QtCore.QSize(55, 55))
        self.ts_page_marker_1.setMaximumSize(QtCore.QSize(55, 55))
        self.ts_page_marker_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ts_page_marker_1.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/filled_circle_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("icons/filled_circle_icon.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.ts_page_marker_1.setIcon(icon10)
        self.ts_page_marker_1.setObjectName("ts_page_marker_1")
        self.horizontalLayout_2.addWidget(self.ts_page_marker_1)
        self.ts_page_marker_2 = QtWidgets.QToolButton(self.page_3)
        self.ts_page_marker_2.setEnabled(False)
        self.ts_page_marker_2.setMinimumSize(QtCore.QSize(55, 55))
        self.ts_page_marker_2.setMaximumSize(QtCore.QSize(55, 55))
        self.ts_page_marker_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ts_page_marker_2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/empty_circle_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("icons/empty_circle_icon.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("icons/empty_circle_icon.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.ts_page_marker_2.setIcon(icon11)
        self.ts_page_marker_2.setObjectName("ts_page_marker_2")
        self.horizontalLayout_2.addWidget(self.ts_page_marker_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.right_ts_button = QtWidgets.QToolButton(self.page_3)
        self.right_ts_button.setMinimumSize(QtCore.QSize(55, 55))
        self.right_ts_button.setMaximumSize(QtCore.QSize(55, 55))
        self.right_ts_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.right_ts_button.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/right_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.right_ts_button.setIcon(icon12)
        self.right_ts_button.setIconSize(QtCore.QSize(50, 50))
        self.right_ts_button.setArrowType(QtCore.Qt.NoArrow)
        self.right_ts_button.setObjectName("right_ts_button")
        self.horizontalLayout_2.addWidget(self.right_ts_button)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.main_stacked_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_2.setContentsMargins(6, 10, 10, 5)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.forecast_1h_stack = QtWidgets.QStackedWidget(self.page_4)
        self.forecast_1h_stack.setStyleSheet("")
        self.forecast_1h_stack.setObjectName("forecast_1h_stack")
        self.fc_page_1 = QtWidgets.QWidget()
        self.fc_page_1.setObjectName("fc_page_1")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.fc_page_1)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem8 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_11.addItem(spacerItem8, 1, 0, 1, 1)
        self.prev1h_frame_2 = QtWidgets.QFrame(self.fc_page_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev1h_frame_2.sizePolicy().hasHeightForWidth())
        self.prev1h_frame_2.setSizePolicy(sizePolicy)
        self.prev1h_frame_2.setStyleSheet("QFrame {\n"
"   background: #DEEBF7;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.prev1h_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prev1h_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev1h_frame_2.setObjectName("prev1h_frame_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.prev1h_frame_2)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.prev1h_layout_2 = QtWidgets.QHBoxLayout()
        self.prev1h_layout_2.setObjectName("prev1h_layout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.fc_hour_lb_7 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_hour_lb_7.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_7.setFont(font)
        self.fc_hour_lb_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_7.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_7.setWordWrap(True)
        self.fc_hour_lb_7.setObjectName("fc_hour_lb_7")
        self.verticalLayout_7.addWidget(self.fc_hour_lb_7)
        self.fc_weat_bt_7 = QtWidgets.QToolButton(self.prev1h_frame_2)
        self.fc_weat_bt_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_7.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_7.setSizePolicy(sizePolicy)
        self.fc_weat_bt_7.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_7.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_7.setFont(font)
        self.fc_weat_bt_7.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_7.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_7.setObjectName("fc_weat_bt_7")
        self.verticalLayout_7.addWidget(self.fc_weat_bt_7)
        self.fc_temp_lb_7 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_temp_lb_7.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_7.setFont(font)
        self.fc_temp_lb_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_7.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_7.setWordWrap(True)
        self.fc_temp_lb_7.setObjectName("fc_temp_lb_7")
        self.verticalLayout_7.addWidget(self.fc_temp_lb_7)
        self.prev1h_layout_2.addLayout(self.verticalLayout_7)
        self.fc_line_6 = QtWidgets.QFrame(self.prev1h_frame_2)
        self.fc_line_6.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_6.setObjectName("fc_line_6")
        self.prev1h_layout_2.addWidget(self.fc_line_6)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fc_hour_lb_8 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_hour_lb_8.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_8.setFont(font)
        self.fc_hour_lb_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_8.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_8.setWordWrap(True)
        self.fc_hour_lb_8.setObjectName("fc_hour_lb_8")
        self.verticalLayout_8.addWidget(self.fc_hour_lb_8)
        self.fc_weat_bt_8 = QtWidgets.QToolButton(self.prev1h_frame_2)
        self.fc_weat_bt_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_8.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_8.setSizePolicy(sizePolicy)
        self.fc_weat_bt_8.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_8.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_8.setFont(font)
        self.fc_weat_bt_8.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_8.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_8.setObjectName("fc_weat_bt_8")
        self.verticalLayout_8.addWidget(self.fc_weat_bt_8)
        self.fc_temp_lb_8 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_temp_lb_8.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_8.setFont(font)
        self.fc_temp_lb_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_8.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_8.setWordWrap(True)
        self.fc_temp_lb_8.setObjectName("fc_temp_lb_8")
        self.verticalLayout_8.addWidget(self.fc_temp_lb_8)
        self.prev1h_layout_2.addLayout(self.verticalLayout_8)
        self.fc_line_7 = QtWidgets.QFrame(self.prev1h_frame_2)
        self.fc_line_7.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_7.setObjectName("fc_line_7")
        self.prev1h_layout_2.addWidget(self.fc_line_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.fc_hour_lb_9 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_hour_lb_9.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_9.setFont(font)
        self.fc_hour_lb_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_9.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_9.setWordWrap(True)
        self.fc_hour_lb_9.setObjectName("fc_hour_lb_9")
        self.verticalLayout_9.addWidget(self.fc_hour_lb_9)
        self.fc_weat_bt_9 = QtWidgets.QToolButton(self.prev1h_frame_2)
        self.fc_weat_bt_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_9.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_9.setSizePolicy(sizePolicy)
        self.fc_weat_bt_9.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_9.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_9.setFont(font)
        self.fc_weat_bt_9.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_9.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_9.setObjectName("fc_weat_bt_9")
        self.verticalLayout_9.addWidget(self.fc_weat_bt_9)
        self.fc_temp_lb_9 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_temp_lb_9.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_9.setFont(font)
        self.fc_temp_lb_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_9.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_9.setWordWrap(True)
        self.fc_temp_lb_9.setObjectName("fc_temp_lb_9")
        self.verticalLayout_9.addWidget(self.fc_temp_lb_9)
        self.prev1h_layout_2.addLayout(self.verticalLayout_9)
        self.fc_line_8 = QtWidgets.QFrame(self.prev1h_frame_2)
        self.fc_line_8.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_8.setObjectName("fc_line_8")
        self.prev1h_layout_2.addWidget(self.fc_line_8)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.fc_hour_lb_10 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_hour_lb_10.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_10.setFont(font)
        self.fc_hour_lb_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_10.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_10.setWordWrap(True)
        self.fc_hour_lb_10.setObjectName("fc_hour_lb_10")
        self.verticalLayout_10.addWidget(self.fc_hour_lb_10)
        self.fc_weat_bt_10 = QtWidgets.QToolButton(self.prev1h_frame_2)
        self.fc_weat_bt_10.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_10.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_10.setSizePolicy(sizePolicy)
        self.fc_weat_bt_10.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_10.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_10.setFont(font)
        self.fc_weat_bt_10.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_10.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_10.setObjectName("fc_weat_bt_10")
        self.verticalLayout_10.addWidget(self.fc_weat_bt_10)
        self.fc_temp_lb_10 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_temp_lb_10.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_10.setFont(font)
        self.fc_temp_lb_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_10.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_10.setWordWrap(True)
        self.fc_temp_lb_10.setObjectName("fc_temp_lb_10")
        self.verticalLayout_10.addWidget(self.fc_temp_lb_10)
        self.prev1h_layout_2.addLayout(self.verticalLayout_10)
        self.fc_line_9 = QtWidgets.QFrame(self.prev1h_frame_2)
        self.fc_line_9.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_9.setObjectName("fc_line_9")
        self.prev1h_layout_2.addWidget(self.fc_line_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.fc_hour_lb_11 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_hour_lb_11.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_11.setFont(font)
        self.fc_hour_lb_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_11.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_11.setWordWrap(True)
        self.fc_hour_lb_11.setObjectName("fc_hour_lb_11")
        self.verticalLayout_11.addWidget(self.fc_hour_lb_11)
        self.fc_weat_bt_11 = QtWidgets.QToolButton(self.prev1h_frame_2)
        self.fc_weat_bt_11.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_11.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_11.setSizePolicy(sizePolicy)
        self.fc_weat_bt_11.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_11.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_11.setFont(font)
        self.fc_weat_bt_11.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_11.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_11.setObjectName("fc_weat_bt_11")
        self.verticalLayout_11.addWidget(self.fc_weat_bt_11)
        self.fc_temp_lb_11 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_temp_lb_11.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_11.setFont(font)
        self.fc_temp_lb_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_11.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_11.setWordWrap(True)
        self.fc_temp_lb_11.setObjectName("fc_temp_lb_11")
        self.verticalLayout_11.addWidget(self.fc_temp_lb_11)
        self.prev1h_layout_2.addLayout(self.verticalLayout_11)
        self.fc_line_10 = QtWidgets.QFrame(self.prev1h_frame_2)
        self.fc_line_10.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_10.setObjectName("fc_line_10")
        self.prev1h_layout_2.addWidget(self.fc_line_10)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.fc_hour_lb_12 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_hour_lb_12.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_12.setFont(font)
        self.fc_hour_lb_12.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_12.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_12.setWordWrap(True)
        self.fc_hour_lb_12.setObjectName("fc_hour_lb_12")
        self.verticalLayout_12.addWidget(self.fc_hour_lb_12)
        self.fc_weat_bt_12 = QtWidgets.QToolButton(self.prev1h_frame_2)
        self.fc_weat_bt_12.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_12.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_12.setSizePolicy(sizePolicy)
        self.fc_weat_bt_12.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_12.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_12.setFont(font)
        self.fc_weat_bt_12.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_12.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_12.setObjectName("fc_weat_bt_12")
        self.verticalLayout_12.addWidget(self.fc_weat_bt_12)
        self.fc_temp_lb_12 = QtWidgets.QLabel(self.prev1h_frame_2)
        self.fc_temp_lb_12.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_12.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_12.setFont(font)
        self.fc_temp_lb_12.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_12.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_12.setWordWrap(True)
        self.fc_temp_lb_12.setObjectName("fc_temp_lb_12")
        self.verticalLayout_12.addWidget(self.fc_temp_lb_12)
        self.prev1h_layout_2.addLayout(self.verticalLayout_12)
        self.gridLayout_9.addLayout(self.prev1h_layout_2, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.prev1h_frame_2, 2, 0, 1, 1)
        self.prev1h_frame_1 = QtWidgets.QFrame(self.fc_page_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev1h_frame_1.sizePolicy().hasHeightForWidth())
        self.prev1h_frame_1.setSizePolicy(sizePolicy)
        self.prev1h_frame_1.setStyleSheet("QFrame {\n"
"   background: #DEEBF7;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.prev1h_frame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prev1h_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev1h_frame_1.setObjectName("prev1h_frame_1")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.prev1h_frame_1)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.prev1h_layout_1 = QtWidgets.QHBoxLayout()
        self.prev1h_layout_1.setObjectName("prev1h_layout_1")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.fc_hour_lb_1 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_hour_lb_1.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_1.setFont(font)
        self.fc_hour_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_1.setWordWrap(True)
        self.fc_hour_lb_1.setObjectName("fc_hour_lb_1")
        self.verticalLayout.addWidget(self.fc_hour_lb_1)
        self.fc_weat_bt_1 = QtWidgets.QToolButton(self.prev1h_frame_1)
        self.fc_weat_bt_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_1.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_1.setSizePolicy(sizePolicy)
        self.fc_weat_bt_1.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_1.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_1.setFont(font)
        self.fc_weat_bt_1.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_1.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_1.setObjectName("fc_weat_bt_1")
        self.verticalLayout.addWidget(self.fc_weat_bt_1)
        self.fc_temp_lb_1 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_temp_lb_1.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_1.setFont(font)
        self.fc_temp_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_1.setWordWrap(True)
        self.fc_temp_lb_1.setObjectName("fc_temp_lb_1")
        self.verticalLayout.addWidget(self.fc_temp_lb_1)
        self.prev1h_layout_1.addLayout(self.verticalLayout)
        self.fc_line_2 = QtWidgets.QFrame(self.prev1h_frame_1)
        self.fc_line_2.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_2.setObjectName("fc_line_2")
        self.prev1h_layout_1.addWidget(self.fc_line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fc_hour_lb_2 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_hour_lb_2.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_2.setFont(font)
        self.fc_hour_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_2.setWordWrap(True)
        self.fc_hour_lb_2.setObjectName("fc_hour_lb_2")
        self.verticalLayout_2.addWidget(self.fc_hour_lb_2)
        self.fc_weat_bt_2 = QtWidgets.QToolButton(self.prev1h_frame_1)
        self.fc_weat_bt_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_2.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_2.setSizePolicy(sizePolicy)
        self.fc_weat_bt_2.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_2.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_2.setFont(font)
        self.fc_weat_bt_2.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_2.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_2.setObjectName("fc_weat_bt_2")
        self.verticalLayout_2.addWidget(self.fc_weat_bt_2)
        self.fc_temp_lb_2 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_temp_lb_2.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_2.setFont(font)
        self.fc_temp_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_2.setWordWrap(True)
        self.fc_temp_lb_2.setObjectName("fc_temp_lb_2")
        self.verticalLayout_2.addWidget(self.fc_temp_lb_2)
        self.prev1h_layout_1.addLayout(self.verticalLayout_2)
        self.fc_line_3 = QtWidgets.QFrame(self.prev1h_frame_1)
        self.fc_line_3.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_3.setObjectName("fc_line_3")
        self.prev1h_layout_1.addWidget(self.fc_line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fc_hour_lb_3 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_hour_lb_3.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_3.setFont(font)
        self.fc_hour_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_3.setWordWrap(True)
        self.fc_hour_lb_3.setObjectName("fc_hour_lb_3")
        self.verticalLayout_3.addWidget(self.fc_hour_lb_3)
        self.fc_weat_bt_3 = QtWidgets.QToolButton(self.prev1h_frame_1)
        self.fc_weat_bt_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_3.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_3.setSizePolicy(sizePolicy)
        self.fc_weat_bt_3.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_3.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_3.setFont(font)
        self.fc_weat_bt_3.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_3.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_3.setObjectName("fc_weat_bt_3")
        self.verticalLayout_3.addWidget(self.fc_weat_bt_3)
        self.fc_temp_lb_3 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_temp_lb_3.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_3.setFont(font)
        self.fc_temp_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_3.setWordWrap(True)
        self.fc_temp_lb_3.setObjectName("fc_temp_lb_3")
        self.verticalLayout_3.addWidget(self.fc_temp_lb_3)
        self.prev1h_layout_1.addLayout(self.verticalLayout_3)
        self.fc_line_1 = QtWidgets.QFrame(self.prev1h_frame_1)
        self.fc_line_1.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_1.setObjectName("fc_line_1")
        self.prev1h_layout_1.addWidget(self.fc_line_1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fc_hour_lb_4 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_hour_lb_4.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_4.setFont(font)
        self.fc_hour_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_4.setWordWrap(True)
        self.fc_hour_lb_4.setObjectName("fc_hour_lb_4")
        self.verticalLayout_4.addWidget(self.fc_hour_lb_4)
        self.fc_weat_bt_4 = QtWidgets.QToolButton(self.prev1h_frame_1)
        self.fc_weat_bt_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_4.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_4.setSizePolicy(sizePolicy)
        self.fc_weat_bt_4.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_4.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_4.setFont(font)
        self.fc_weat_bt_4.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_4.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_4.setObjectName("fc_weat_bt_4")
        self.verticalLayout_4.addWidget(self.fc_weat_bt_4)
        self.fc_temp_lb_4 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_temp_lb_4.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_4.setFont(font)
        self.fc_temp_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_4.setWordWrap(True)
        self.fc_temp_lb_4.setObjectName("fc_temp_lb_4")
        self.verticalLayout_4.addWidget(self.fc_temp_lb_4)
        self.prev1h_layout_1.addLayout(self.verticalLayout_4)
        self.fc_line_4 = QtWidgets.QFrame(self.prev1h_frame_1)
        self.fc_line_4.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_4.setObjectName("fc_line_4")
        self.prev1h_layout_1.addWidget(self.fc_line_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.fc_hour_lb_5 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_hour_lb_5.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_5.setFont(font)
        self.fc_hour_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_5.setWordWrap(True)
        self.fc_hour_lb_5.setObjectName("fc_hour_lb_5")
        self.verticalLayout_5.addWidget(self.fc_hour_lb_5)
        self.fc_weat_bt_5 = QtWidgets.QToolButton(self.prev1h_frame_1)
        self.fc_weat_bt_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_5.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_5.setSizePolicy(sizePolicy)
        self.fc_weat_bt_5.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_5.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_5.setFont(font)
        self.fc_weat_bt_5.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_5.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_5.setObjectName("fc_weat_bt_5")
        self.verticalLayout_5.addWidget(self.fc_weat_bt_5)
        self.fc_temp_lb_5 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_temp_lb_5.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_5.setFont(font)
        self.fc_temp_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_5.setWordWrap(True)
        self.fc_temp_lb_5.setObjectName("fc_temp_lb_5")
        self.verticalLayout_5.addWidget(self.fc_temp_lb_5)
        self.prev1h_layout_1.addLayout(self.verticalLayout_5)
        self.fc_line_5 = QtWidgets.QFrame(self.prev1h_frame_1)
        self.fc_line_5.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_5.setObjectName("fc_line_5")
        self.prev1h_layout_1.addWidget(self.fc_line_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.fc_hour_lb_6 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_hour_lb_6.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_6.setFont(font)
        self.fc_hour_lb_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_6.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_6.setWordWrap(True)
        self.fc_hour_lb_6.setObjectName("fc_hour_lb_6")
        self.verticalLayout_6.addWidget(self.fc_hour_lb_6)
        self.fc_weat_bt_6 = QtWidgets.QToolButton(self.prev1h_frame_1)
        self.fc_weat_bt_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_6.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_6.setSizePolicy(sizePolicy)
        self.fc_weat_bt_6.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_6.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_6.setFont(font)
        self.fc_weat_bt_6.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_6.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_6.setObjectName("fc_weat_bt_6")
        self.verticalLayout_6.addWidget(self.fc_weat_bt_6)
        self.fc_temp_lb_6 = QtWidgets.QLabel(self.prev1h_frame_1)
        self.fc_temp_lb_6.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_6.setFont(font)
        self.fc_temp_lb_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_6.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_6.setWordWrap(True)
        self.fc_temp_lb_6.setObjectName("fc_temp_lb_6")
        self.verticalLayout_6.addWidget(self.fc_temp_lb_6)
        self.prev1h_layout_1.addLayout(self.verticalLayout_6)
        self.gridLayout_10.addLayout(self.prev1h_layout_1, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.prev1h_frame_1, 0, 0, 1, 1)
        self.forecast_1h_stack.addWidget(self.fc_page_1)
        self.fc_page_2 = QtWidgets.QWidget()
        self.fc_page_2.setObjectName("fc_page_2")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.fc_page_2)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 10)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.prev1h_frame_3 = QtWidgets.QFrame(self.fc_page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev1h_frame_3.sizePolicy().hasHeightForWidth())
        self.prev1h_frame_3.setSizePolicy(sizePolicy)
        self.prev1h_frame_3.setStyleSheet("QFrame {\n"
"   background: #DEEBF7;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.prev1h_frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prev1h_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev1h_frame_3.setObjectName("prev1h_frame_3")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.prev1h_frame_3)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.prev1h_layout_3 = QtWidgets.QHBoxLayout()
        self.prev1h_layout_3.setObjectName("prev1h_layout_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.fc_hour_lb_13 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_hour_lb_13.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_13.setFont(font)
        self.fc_hour_lb_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_13.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_13.setWordWrap(True)
        self.fc_hour_lb_13.setObjectName("fc_hour_lb_13")
        self.verticalLayout_13.addWidget(self.fc_hour_lb_13)
        self.fc_weat_bt_13 = QtWidgets.QToolButton(self.prev1h_frame_3)
        self.fc_weat_bt_13.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_13.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_13.setSizePolicy(sizePolicy)
        self.fc_weat_bt_13.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_13.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_13.setFont(font)
        self.fc_weat_bt_13.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_13.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_13.setObjectName("fc_weat_bt_13")
        self.verticalLayout_13.addWidget(self.fc_weat_bt_13)
        self.fc_temp_lb_13 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_temp_lb_13.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_13.setFont(font)
        self.fc_temp_lb_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_13.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_13.setWordWrap(True)
        self.fc_temp_lb_13.setObjectName("fc_temp_lb_13")
        self.verticalLayout_13.addWidget(self.fc_temp_lb_13)
        self.prev1h_layout_3.addLayout(self.verticalLayout_13)
        self.fc_line_11 = QtWidgets.QFrame(self.prev1h_frame_3)
        self.fc_line_11.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_11.setObjectName("fc_line_11")
        self.prev1h_layout_3.addWidget(self.fc_line_11)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.fc_hour_lb_14 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_hour_lb_14.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_14.setFont(font)
        self.fc_hour_lb_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_14.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_14.setWordWrap(True)
        self.fc_hour_lb_14.setObjectName("fc_hour_lb_14")
        self.verticalLayout_14.addWidget(self.fc_hour_lb_14)
        self.fc_weat_bt_14 = QtWidgets.QToolButton(self.prev1h_frame_3)
        self.fc_weat_bt_14.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_14.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_14.setSizePolicy(sizePolicy)
        self.fc_weat_bt_14.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_14.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_14.setFont(font)
        self.fc_weat_bt_14.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_14.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_14.setObjectName("fc_weat_bt_14")
        self.verticalLayout_14.addWidget(self.fc_weat_bt_14)
        self.fc_temp_lb_14 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_temp_lb_14.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_14.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_14.setFont(font)
        self.fc_temp_lb_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_14.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_14.setWordWrap(True)
        self.fc_temp_lb_14.setObjectName("fc_temp_lb_14")
        self.verticalLayout_14.addWidget(self.fc_temp_lb_14)
        self.prev1h_layout_3.addLayout(self.verticalLayout_14)
        self.fc_line_12 = QtWidgets.QFrame(self.prev1h_frame_3)
        self.fc_line_12.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_12.setObjectName("fc_line_12")
        self.prev1h_layout_3.addWidget(self.fc_line_12)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.fc_hour_lb_15 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_hour_lb_15.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_15.setFont(font)
        self.fc_hour_lb_15.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_15.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_15.setWordWrap(True)
        self.fc_hour_lb_15.setObjectName("fc_hour_lb_15")
        self.verticalLayout_15.addWidget(self.fc_hour_lb_15)
        self.fc_weat_bt_15 = QtWidgets.QToolButton(self.prev1h_frame_3)
        self.fc_weat_bt_15.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_15.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_15.setSizePolicy(sizePolicy)
        self.fc_weat_bt_15.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_15.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_15.setFont(font)
        self.fc_weat_bt_15.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_15.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_15.setObjectName("fc_weat_bt_15")
        self.verticalLayout_15.addWidget(self.fc_weat_bt_15)
        self.fc_temp_lb_15 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_temp_lb_15.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_15.setFont(font)
        self.fc_temp_lb_15.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_15.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_15.setWordWrap(True)
        self.fc_temp_lb_15.setObjectName("fc_temp_lb_15")
        self.verticalLayout_15.addWidget(self.fc_temp_lb_15)
        self.prev1h_layout_3.addLayout(self.verticalLayout_15)
        self.fc_line_13 = QtWidgets.QFrame(self.prev1h_frame_3)
        self.fc_line_13.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_13.setObjectName("fc_line_13")
        self.prev1h_layout_3.addWidget(self.fc_line_13)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.fc_hour_lb_16 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_hour_lb_16.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_16.setFont(font)
        self.fc_hour_lb_16.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_16.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_16.setWordWrap(True)
        self.fc_hour_lb_16.setObjectName("fc_hour_lb_16")
        self.verticalLayout_16.addWidget(self.fc_hour_lb_16)
        self.fc_weat_bt_16 = QtWidgets.QToolButton(self.prev1h_frame_3)
        self.fc_weat_bt_16.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_16.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_16.setSizePolicy(sizePolicy)
        self.fc_weat_bt_16.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_16.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_16.setFont(font)
        self.fc_weat_bt_16.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_16.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_16.setObjectName("fc_weat_bt_16")
        self.verticalLayout_16.addWidget(self.fc_weat_bt_16)
        self.fc_temp_lb_16 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_temp_lb_16.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_16.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_16.setFont(font)
        self.fc_temp_lb_16.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_16.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_16.setWordWrap(True)
        self.fc_temp_lb_16.setObjectName("fc_temp_lb_16")
        self.verticalLayout_16.addWidget(self.fc_temp_lb_16)
        self.prev1h_layout_3.addLayout(self.verticalLayout_16)
        self.fc_line_14 = QtWidgets.QFrame(self.prev1h_frame_3)
        self.fc_line_14.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_14.setObjectName("fc_line_14")
        self.prev1h_layout_3.addWidget(self.fc_line_14)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.fc_hour_lb_17 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_hour_lb_17.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_17.setFont(font)
        self.fc_hour_lb_17.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_17.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_17.setWordWrap(True)
        self.fc_hour_lb_17.setObjectName("fc_hour_lb_17")
        self.verticalLayout_17.addWidget(self.fc_hour_lb_17)
        self.fc_weat_bt_17 = QtWidgets.QToolButton(self.prev1h_frame_3)
        self.fc_weat_bt_17.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_17.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_17.setSizePolicy(sizePolicy)
        self.fc_weat_bt_17.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_17.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_17.setFont(font)
        self.fc_weat_bt_17.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_17.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_17.setObjectName("fc_weat_bt_17")
        self.verticalLayout_17.addWidget(self.fc_weat_bt_17)
        self.fc_temp_lb_17 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_temp_lb_17.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_17.setFont(font)
        self.fc_temp_lb_17.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_17.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_17.setWordWrap(True)
        self.fc_temp_lb_17.setObjectName("fc_temp_lb_17")
        self.verticalLayout_17.addWidget(self.fc_temp_lb_17)
        self.prev1h_layout_3.addLayout(self.verticalLayout_17)
        self.fc_line_15 = QtWidgets.QFrame(self.prev1h_frame_3)
        self.fc_line_15.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_15.setObjectName("fc_line_15")
        self.prev1h_layout_3.addWidget(self.fc_line_15)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.fc_hour_lb_18 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_hour_lb_18.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_18.setFont(font)
        self.fc_hour_lb_18.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_18.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_18.setWordWrap(True)
        self.fc_hour_lb_18.setObjectName("fc_hour_lb_18")
        self.verticalLayout_18.addWidget(self.fc_hour_lb_18)
        self.fc_weat_bt_18 = QtWidgets.QToolButton(self.prev1h_frame_3)
        self.fc_weat_bt_18.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_18.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_18.setSizePolicy(sizePolicy)
        self.fc_weat_bt_18.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_18.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_18.setFont(font)
        self.fc_weat_bt_18.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_18.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_18.setObjectName("fc_weat_bt_18")
        self.verticalLayout_18.addWidget(self.fc_weat_bt_18)
        self.fc_temp_lb_18 = QtWidgets.QLabel(self.prev1h_frame_3)
        self.fc_temp_lb_18.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_18.setFont(font)
        self.fc_temp_lb_18.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_18.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_18.setWordWrap(True)
        self.fc_temp_lb_18.setObjectName("fc_temp_lb_18")
        self.verticalLayout_18.addWidget(self.fc_temp_lb_18)
        self.prev1h_layout_3.addLayout(self.verticalLayout_18)
        self.gridLayout_17.addLayout(self.prev1h_layout_3, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.prev1h_frame_3, 0, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_19.addItem(spacerItem9, 1, 0, 1, 1)
        self.prev1h_frame_4 = QtWidgets.QFrame(self.fc_page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev1h_frame_4.sizePolicy().hasHeightForWidth())
        self.prev1h_frame_4.setSizePolicy(sizePolicy)
        self.prev1h_frame_4.setStyleSheet("QFrame {\n"
"   background: #DEEBF7;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.prev1h_frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prev1h_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev1h_frame_4.setObjectName("prev1h_frame_4")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.prev1h_frame_4)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.prev1h_layout_4 = QtWidgets.QHBoxLayout()
        self.prev1h_layout_4.setObjectName("prev1h_layout_4")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.fc_hour_lb_19 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_hour_lb_19.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_19.setFont(font)
        self.fc_hour_lb_19.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_19.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_19.setWordWrap(True)
        self.fc_hour_lb_19.setObjectName("fc_hour_lb_19")
        self.verticalLayout_19.addWidget(self.fc_hour_lb_19)
        self.fc_weat_bt_19 = QtWidgets.QToolButton(self.prev1h_frame_4)
        self.fc_weat_bt_19.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_19.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_19.setSizePolicy(sizePolicy)
        self.fc_weat_bt_19.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_19.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_19.setFont(font)
        self.fc_weat_bt_19.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_19.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_19.setObjectName("fc_weat_bt_19")
        self.verticalLayout_19.addWidget(self.fc_weat_bt_19)
        self.fc_temp_lb_19 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_temp_lb_19.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_19.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_19.setFont(font)
        self.fc_temp_lb_19.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_19.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_19.setWordWrap(True)
        self.fc_temp_lb_19.setObjectName("fc_temp_lb_19")
        self.verticalLayout_19.addWidget(self.fc_temp_lb_19)
        self.prev1h_layout_4.addLayout(self.verticalLayout_19)
        self.fc_line_16 = QtWidgets.QFrame(self.prev1h_frame_4)
        self.fc_line_16.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_16.setObjectName("fc_line_16")
        self.prev1h_layout_4.addWidget(self.fc_line_16)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.fc_hour_lb_20 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_hour_lb_20.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_20.setFont(font)
        self.fc_hour_lb_20.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_20.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_20.setWordWrap(True)
        self.fc_hour_lb_20.setObjectName("fc_hour_lb_20")
        self.verticalLayout_20.addWidget(self.fc_hour_lb_20)
        self.fc_weat_bt_20 = QtWidgets.QToolButton(self.prev1h_frame_4)
        self.fc_weat_bt_20.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_20.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_20.setSizePolicy(sizePolicy)
        self.fc_weat_bt_20.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_20.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_20.setFont(font)
        self.fc_weat_bt_20.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_20.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_20.setObjectName("fc_weat_bt_20")
        self.verticalLayout_20.addWidget(self.fc_weat_bt_20)
        self.fc_temp_lb_20 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_temp_lb_20.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_20.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_20.setFont(font)
        self.fc_temp_lb_20.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_20.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_20.setWordWrap(True)
        self.fc_temp_lb_20.setObjectName("fc_temp_lb_20")
        self.verticalLayout_20.addWidget(self.fc_temp_lb_20)
        self.prev1h_layout_4.addLayout(self.verticalLayout_20)
        self.fc_line_17 = QtWidgets.QFrame(self.prev1h_frame_4)
        self.fc_line_17.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_17.setObjectName("fc_line_17")
        self.prev1h_layout_4.addWidget(self.fc_line_17)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.fc_hour_lb_21 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_hour_lb_21.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_21.setFont(font)
        self.fc_hour_lb_21.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_21.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_21.setWordWrap(True)
        self.fc_hour_lb_21.setObjectName("fc_hour_lb_21")
        self.verticalLayout_21.addWidget(self.fc_hour_lb_21)
        self.fc_weat_bt_21 = QtWidgets.QToolButton(self.prev1h_frame_4)
        self.fc_weat_bt_21.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_21.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_21.setSizePolicy(sizePolicy)
        self.fc_weat_bt_21.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_21.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_21.setFont(font)
        self.fc_weat_bt_21.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_21.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_21.setObjectName("fc_weat_bt_21")
        self.verticalLayout_21.addWidget(self.fc_weat_bt_21)
        self.fc_temp_lb_21 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_temp_lb_21.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_21.setFont(font)
        self.fc_temp_lb_21.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_21.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_21.setWordWrap(True)
        self.fc_temp_lb_21.setObjectName("fc_temp_lb_21")
        self.verticalLayout_21.addWidget(self.fc_temp_lb_21)
        self.prev1h_layout_4.addLayout(self.verticalLayout_21)
        self.fc_line_18 = QtWidgets.QFrame(self.prev1h_frame_4)
        self.fc_line_18.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_18.setObjectName("fc_line_18")
        self.prev1h_layout_4.addWidget(self.fc_line_18)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.fc_hour_lb_22 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_hour_lb_22.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_22.setFont(font)
        self.fc_hour_lb_22.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_22.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_22.setWordWrap(True)
        self.fc_hour_lb_22.setObjectName("fc_hour_lb_22")
        self.verticalLayout_22.addWidget(self.fc_hour_lb_22)
        self.fc_weat_bt_22 = QtWidgets.QToolButton(self.prev1h_frame_4)
        self.fc_weat_bt_22.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_22.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_22.setSizePolicy(sizePolicy)
        self.fc_weat_bt_22.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_22.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_22.setFont(font)
        self.fc_weat_bt_22.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_22.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_22.setObjectName("fc_weat_bt_22")
        self.verticalLayout_22.addWidget(self.fc_weat_bt_22)
        self.fc_temp_lb_22 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_temp_lb_22.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_22.setFont(font)
        self.fc_temp_lb_22.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_22.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_22.setWordWrap(True)
        self.fc_temp_lb_22.setObjectName("fc_temp_lb_22")
        self.verticalLayout_22.addWidget(self.fc_temp_lb_22)
        self.prev1h_layout_4.addLayout(self.verticalLayout_22)
        self.fc_line_19 = QtWidgets.QFrame(self.prev1h_frame_4)
        self.fc_line_19.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_19.setObjectName("fc_line_19")
        self.prev1h_layout_4.addWidget(self.fc_line_19)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.fc_hour_lb_23 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_hour_lb_23.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_23.setFont(font)
        self.fc_hour_lb_23.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_23.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_23.setWordWrap(True)
        self.fc_hour_lb_23.setObjectName("fc_hour_lb_23")
        self.verticalLayout_23.addWidget(self.fc_hour_lb_23)
        self.fc_weat_bt_23 = QtWidgets.QToolButton(self.prev1h_frame_4)
        self.fc_weat_bt_23.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_23.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_23.setSizePolicy(sizePolicy)
        self.fc_weat_bt_23.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_23.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_23.setFont(font)
        self.fc_weat_bt_23.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_23.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_23.setObjectName("fc_weat_bt_23")
        self.verticalLayout_23.addWidget(self.fc_weat_bt_23)
        self.fc_temp_lb_23 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_temp_lb_23.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_23.setFont(font)
        self.fc_temp_lb_23.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_23.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_23.setWordWrap(True)
        self.fc_temp_lb_23.setObjectName("fc_temp_lb_23")
        self.verticalLayout_23.addWidget(self.fc_temp_lb_23)
        self.prev1h_layout_4.addLayout(self.verticalLayout_23)
        self.fc_line_20 = QtWidgets.QFrame(self.prev1h_frame_4)
        self.fc_line_20.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_20.setObjectName("fc_line_20")
        self.prev1h_layout_4.addWidget(self.fc_line_20)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.fc_hour_lb_24 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_hour_lb_24.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_hour_lb_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_hour_lb_24.setFont(font)
        self.fc_hour_lb_24.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_hour_lb_24.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_hour_lb_24.setWordWrap(True)
        self.fc_hour_lb_24.setObjectName("fc_hour_lb_24")
        self.verticalLayout_24.addWidget(self.fc_hour_lb_24)
        self.fc_weat_bt_24 = QtWidgets.QToolButton(self.prev1h_frame_4)
        self.fc_weat_bt_24.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_weat_bt_24.sizePolicy().hasHeightForWidth())
        self.fc_weat_bt_24.setSizePolicy(sizePolicy)
        self.fc_weat_bt_24.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_24.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        self.fc_weat_bt_24.setFont(font)
        self.fc_weat_bt_24.setStyleSheet("QToolButton {\n"
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
        self.fc_weat_bt_24.setIconSize(QtCore.QSize(80, 80))
        self.fc_weat_bt_24.setObjectName("fc_weat_bt_24")
        self.verticalLayout_24.addWidget(self.fc_weat_bt_24)
        self.fc_temp_lb_24 = QtWidgets.QLabel(self.prev1h_frame_4)
        self.fc_temp_lb_24.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_temp_lb_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_temp_lb_24.setFont(font)
        self.fc_temp_lb_24.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_temp_lb_24.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_temp_lb_24.setWordWrap(True)
        self.fc_temp_lb_24.setObjectName("fc_temp_lb_24")
        self.verticalLayout_24.addWidget(self.fc_temp_lb_24)
        self.prev1h_layout_4.addLayout(self.verticalLayout_24)
        self.gridLayout_18.addLayout(self.prev1h_layout_4, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.prev1h_frame_4, 2, 0, 1, 1)
        self.forecast_1h_stack.addWidget(self.fc_page_2)
        self.gridLayout_2.addWidget(self.forecast_1h_stack, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_fc_button = QtWidgets.QToolButton(self.page_4)
        self.left_fc_button.setMinimumSize(QtCore.QSize(55, 55))
        self.left_fc_button.setMaximumSize(QtCore.QSize(55, 55))
        self.left_fc_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.left_fc_button.setText("")
        self.left_fc_button.setIcon(icon9)
        self.left_fc_button.setIconSize(QtCore.QSize(50, 50))
        self.left_fc_button.setArrowType(QtCore.Qt.NoArrow)
        self.left_fc_button.setObjectName("left_fc_button")
        self.horizontalLayout_3.addWidget(self.left_fc_button)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.fc_page_marker_1 = QtWidgets.QToolButton(self.page_4)
        self.fc_page_marker_1.setEnabled(False)
        self.fc_page_marker_1.setMinimumSize(QtCore.QSize(55, 55))
        self.fc_page_marker_1.setMaximumSize(QtCore.QSize(55, 55))
        self.fc_page_marker_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.fc_page_marker_1.setText("")
        self.fc_page_marker_1.setIcon(icon10)
        self.fc_page_marker_1.setObjectName("fc_page_marker_1")
        self.horizontalLayout_3.addWidget(self.fc_page_marker_1)
        self.fc_page_marker_2 = QtWidgets.QToolButton(self.page_4)
        self.fc_page_marker_2.setEnabled(False)
        self.fc_page_marker_2.setMinimumSize(QtCore.QSize(55, 55))
        self.fc_page_marker_2.setMaximumSize(QtCore.QSize(55, 55))
        self.fc_page_marker_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.fc_page_marker_2.setText("")
        self.fc_page_marker_2.setIcon(icon11)
        self.fc_page_marker_2.setObjectName("fc_page_marker_2")
        self.horizontalLayout_3.addWidget(self.fc_page_marker_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.right_fc_button = QtWidgets.QToolButton(self.page_4)
        self.right_fc_button.setMinimumSize(QtCore.QSize(55, 55))
        self.right_fc_button.setMaximumSize(QtCore.QSize(55, 55))
        self.right_fc_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.right_fc_button.setText("")
        self.right_fc_button.setIcon(icon12)
        self.right_fc_button.setIconSize(QtCore.QSize(50, 50))
        self.right_fc_button.setArrowType(QtCore.Qt.NoArrow)
        self.right_fc_button.setObjectName("right_fc_button")
        self.horizontalLayout_3.addWidget(self.right_fc_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.main_stacked_widget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_14.setContentsMargins(6, 10, 10, -1)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.prev6h_frame_1 = QtWidgets.QFrame(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev6h_frame_1.sizePolicy().hasHeightForWidth())
        self.prev6h_frame_1.setSizePolicy(sizePolicy)
        self.prev6h_frame_1.setStyleSheet("QFrame {\n"
"   background: #DEEBF7;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.prev6h_frame_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prev6h_frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev6h_frame_1.setObjectName("prev6h_frame_1")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.prev6h_frame_1)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.prev6h_layout_1 = QtWidgets.QHBoxLayout()
        self.prev6h_layout_1.setObjectName("prev6h_layout_1")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.fc_day_lb_1 = QtWidgets.QLabel(self.prev6h_frame_1)
        self.fc_day_lb_1.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_day_lb_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_day_lb_1.setFont(font)
        self.fc_day_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_day_lb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_day_lb_1.setWordWrap(True)
        self.fc_day_lb_1.setObjectName("fc_day_lb_1")
        self.verticalLayout_25.addWidget(self.fc_day_lb_1)
        self.fc_dweat_bt_1 = QtWidgets.QToolButton(self.prev6h_frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_dweat_bt_1.sizePolicy().hasHeightForWidth())
        self.fc_dweat_bt_1.setSizePolicy(sizePolicy)
        self.fc_dweat_bt_1.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_1.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_dweat_bt_1.setFont(font)
        self.fc_dweat_bt_1.setStyleSheet("QToolButton {\n"
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
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("pictogrammes/averses_orageuses.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fc_dweat_bt_1.setIcon(icon13)
        self.fc_dweat_bt_1.setIconSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_1.setObjectName("fc_dweat_bt_1")
        self.verticalLayout_25.addWidget(self.fc_dweat_bt_1)
        self.fc_mmtemp_lb_1 = QtWidgets.QLabel(self.prev6h_frame_1)
        self.fc_mmtemp_lb_1.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_mmtemp_lb_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_mmtemp_lb_1.setFont(font)
        self.fc_mmtemp_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_mmtemp_lb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_mmtemp_lb_1.setWordWrap(True)
        self.fc_mmtemp_lb_1.setObjectName("fc_mmtemp_lb_1")
        self.verticalLayout_25.addWidget(self.fc_mmtemp_lb_1)
        self.prev6h_layout_1.addLayout(self.verticalLayout_25)
        self.fc_line_21 = QtWidgets.QFrame(self.prev6h_frame_1)
        self.fc_line_21.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_21.setObjectName("fc_line_21")
        self.prev6h_layout_1.addWidget(self.fc_line_21)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.fc_day_lb_2 = QtWidgets.QLabel(self.prev6h_frame_1)
        self.fc_day_lb_2.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_day_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_day_lb_2.setFont(font)
        self.fc_day_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_day_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_day_lb_2.setWordWrap(True)
        self.fc_day_lb_2.setObjectName("fc_day_lb_2")
        self.verticalLayout_26.addWidget(self.fc_day_lb_2)
        self.fc_dweat_bt_2 = QtWidgets.QToolButton(self.prev6h_frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_dweat_bt_2.sizePolicy().hasHeightForWidth())
        self.fc_dweat_bt_2.setSizePolicy(sizePolicy)
        self.fc_dweat_bt_2.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_2.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_dweat_bt_2.setFont(font)
        self.fc_dweat_bt_2.setStyleSheet("QToolButton {\n"
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
        self.fc_dweat_bt_2.setIcon(icon13)
        self.fc_dweat_bt_2.setIconSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_2.setObjectName("fc_dweat_bt_2")
        self.verticalLayout_26.addWidget(self.fc_dweat_bt_2)
        self.fc_mmtemp_lb_2 = QtWidgets.QLabel(self.prev6h_frame_1)
        self.fc_mmtemp_lb_2.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_mmtemp_lb_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_mmtemp_lb_2.setFont(font)
        self.fc_mmtemp_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_mmtemp_lb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_mmtemp_lb_2.setWordWrap(True)
        self.fc_mmtemp_lb_2.setObjectName("fc_mmtemp_lb_2")
        self.verticalLayout_26.addWidget(self.fc_mmtemp_lb_2)
        self.prev6h_layout_1.addLayout(self.verticalLayout_26)
        self.fc_line_22 = QtWidgets.QFrame(self.prev6h_frame_1)
        self.fc_line_22.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_22.setObjectName("fc_line_22")
        self.prev6h_layout_1.addWidget(self.fc_line_22)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.fc_day_lb_3 = QtWidgets.QLabel(self.prev6h_frame_1)
        self.fc_day_lb_3.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_day_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_day_lb_3.setFont(font)
        self.fc_day_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_day_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_day_lb_3.setWordWrap(True)
        self.fc_day_lb_3.setObjectName("fc_day_lb_3")
        self.verticalLayout_27.addWidget(self.fc_day_lb_3)
        self.fc_dweat_bt_3 = QtWidgets.QToolButton(self.prev6h_frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_dweat_bt_3.sizePolicy().hasHeightForWidth())
        self.fc_dweat_bt_3.setSizePolicy(sizePolicy)
        self.fc_dweat_bt_3.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_3.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_dweat_bt_3.setFont(font)
        self.fc_dweat_bt_3.setStyleSheet("QToolButton {\n"
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
        self.fc_dweat_bt_3.setIcon(icon13)
        self.fc_dweat_bt_3.setIconSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_3.setObjectName("fc_dweat_bt_3")
        self.verticalLayout_27.addWidget(self.fc_dweat_bt_3)
        self.fc_mmtemp_lb_3 = QtWidgets.QLabel(self.prev6h_frame_1)
        self.fc_mmtemp_lb_3.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_mmtemp_lb_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_mmtemp_lb_3.setFont(font)
        self.fc_mmtemp_lb_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_mmtemp_lb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_mmtemp_lb_3.setWordWrap(True)
        self.fc_mmtemp_lb_3.setObjectName("fc_mmtemp_lb_3")
        self.verticalLayout_27.addWidget(self.fc_mmtemp_lb_3)
        self.prev6h_layout_1.addLayout(self.verticalLayout_27)
        self.gridLayout_13.addLayout(self.prev6h_layout_1, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.prev6h_frame_1, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_14.addItem(spacerItem12, 1, 0, 1, 1)
        self.prev6h_frame_2 = QtWidgets.QFrame(self.page_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev6h_frame_2.sizePolicy().hasHeightForWidth())
        self.prev6h_frame_2.setSizePolicy(sizePolicy)
        self.prev6h_frame_2.setStyleSheet("QFrame {\n"
"   background: #DEEBF7;\n"
"   border: 0px solid black;\n"
"   border-radius: 20px;\n"
"}")
        self.prev6h_frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.prev6h_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.prev6h_frame_2.setObjectName("prev6h_frame_2")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.prev6h_frame_2)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.prev6h_layout_2 = QtWidgets.QHBoxLayout()
        self.prev6h_layout_2.setObjectName("prev6h_layout_2")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.fc_day_lb_4 = QtWidgets.QLabel(self.prev6h_frame_2)
        self.fc_day_lb_4.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_day_lb_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_day_lb_4.setFont(font)
        self.fc_day_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_day_lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_day_lb_4.setWordWrap(True)
        self.fc_day_lb_4.setObjectName("fc_day_lb_4")
        self.verticalLayout_28.addWidget(self.fc_day_lb_4)
        self.fc_dweat_bt_4 = QtWidgets.QToolButton(self.prev6h_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_dweat_bt_4.sizePolicy().hasHeightForWidth())
        self.fc_dweat_bt_4.setSizePolicy(sizePolicy)
        self.fc_dweat_bt_4.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_4.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_dweat_bt_4.setFont(font)
        self.fc_dweat_bt_4.setStyleSheet("QToolButton {\n"
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
        self.fc_dweat_bt_4.setIcon(icon13)
        self.fc_dweat_bt_4.setIconSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_4.setObjectName("fc_dweat_bt_4")
        self.verticalLayout_28.addWidget(self.fc_dweat_bt_4)
        self.fc_mmtemp_lb_4 = QtWidgets.QLabel(self.prev6h_frame_2)
        self.fc_mmtemp_lb_4.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_mmtemp_lb_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_mmtemp_lb_4.setFont(font)
        self.fc_mmtemp_lb_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_mmtemp_lb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_mmtemp_lb_4.setWordWrap(True)
        self.fc_mmtemp_lb_4.setObjectName("fc_mmtemp_lb_4")
        self.verticalLayout_28.addWidget(self.fc_mmtemp_lb_4)
        self.prev6h_layout_2.addLayout(self.verticalLayout_28)
        self.fc_line_23 = QtWidgets.QFrame(self.prev6h_frame_2)
        self.fc_line_23.setStyleSheet("QFrame {\n"
"   background: rgb(190,190,190);\n"
"   width: 5px;\n"
"   border: 0px solid black;\n"
"   margin-top: 10px;\n"
"   margin-bottom: 10px;\n"
"}")
        self.fc_line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.fc_line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fc_line_23.setObjectName("fc_line_23")
        self.prev6h_layout_2.addWidget(self.fc_line_23)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.fc_day_lb_5 = QtWidgets.QLabel(self.prev6h_frame_2)
        self.fc_day_lb_5.setMinimumSize(QtCore.QSize(0, 0))
        self.fc_day_lb_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_day_lb_5.setFont(font)
        self.fc_day_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_day_lb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_day_lb_5.setWordWrap(True)
        self.fc_day_lb_5.setObjectName("fc_day_lb_5")
        self.verticalLayout_29.addWidget(self.fc_day_lb_5)
        self.fc_dweat_bt_5 = QtWidgets.QToolButton(self.prev6h_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fc_dweat_bt_5.sizePolicy().hasHeightForWidth())
        self.fc_dweat_bt_5.setSizePolicy(sizePolicy)
        self.fc_dweat_bt_5.setMinimumSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_5.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_dweat_bt_5.setFont(font)
        self.fc_dweat_bt_5.setStyleSheet("QToolButton {\n"
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
        self.fc_dweat_bt_5.setIcon(icon13)
        self.fc_dweat_bt_5.setIconSize(QtCore.QSize(80, 80))
        self.fc_dweat_bt_5.setObjectName("fc_dweat_bt_5")
        self.verticalLayout_29.addWidget(self.fc_dweat_bt_5)
        self.fc_mmtemp_lb_5 = QtWidgets.QLabel(self.prev6h_frame_2)
        self.fc_mmtemp_lb_5.setMinimumSize(QtCore.QSize(0, 50))
        self.fc_mmtemp_lb_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fc_mmtemp_lb_5.setFont(font)
        self.fc_mmtemp_lb_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.fc_mmtemp_lb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.fc_mmtemp_lb_5.setWordWrap(True)
        self.fc_mmtemp_lb_5.setObjectName("fc_mmtemp_lb_5")
        self.verticalLayout_29.addWidget(self.fc_mmtemp_lb_5)
        self.prev6h_layout_2.addLayout(self.verticalLayout_29)
        self.gridLayout_12.addLayout(self.prev6h_layout_2, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.prev6h_frame_2, 2, 0, 1, 1)
        self.main_stacked_widget.addWidget(self.page_5)
        self.gridLayout_21.addWidget(self.main_stacked_widget, 4, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_stacked_widget.setCurrentIndex(0)
        self.time_series_stack.setCurrentIndex(0)
        self.forecast_1h_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.time_label.setText(_translate("MainWindow", "XX:XX:XX"))
        self.date_label.setText(_translate("MainWindow", "Vendredi 30 Septembre 2021"))
        self.in_label_3.setText(_translate("MainWindow", "No data / No data"))
        self.in_label_2.setText(_translate("MainWindow", "Min / Max"))
        self.in_humidity_bt.setText(_translate("MainWindow", "Humidité : No data"))
        self.in_label_1.setText(_translate("MainWindow", "Intérieur"))
        self.in_temperature_label.setText(_translate("MainWindow", "No data"))
        self.in_pressure_bt.setText(_translate("MainWindow", "Pression : No data"))
        self.out_humidity_bt.setText(_translate("MainWindow", "Humidité : No data"))
        self.out_label_3.setText(_translate("MainWindow", "No data / No data"))
        self.out_label_1.setText(_translate("MainWindow", "Extérieur"))
        self.out_temperature_label.setText(_translate("MainWindow", "No data"))
        self.out_label_2.setText(_translate("MainWindow", "Min / Max"))
        self.out_pressure_bt.setText(_translate("MainWindow", "Pression : No data"))
        self.day_box.setTitle(_translate("MainWindow", "No data"))
        self.day_lb_1.setText(_translate("MainWindow", "No data ème jour de l’année"))
        self.day_lb_3.setText(_translate("MainWindow", "No data"))
        self.day_lb_2.setText(_translate("MainWindow", "Semaine No data"))
        self.sun_box.setTitle(_translate("MainWindow", "Soleil"))
        self.sun_lb_1.setText(_translate("MainWindow", "Le Soleil se lève à No data et se couche à No data"))
        self.sun_lb_2.setText(_translate("MainWindow", "Durée d’ensoleillement: No data"))
        self.moon_box.setTitle(_translate("MainWindow", "Lune"))
        self.moon_lb_1.setText(_translate("MainWindow", "La Lune se lève à No data et se couche à No data"))
        self.moon_lb_2.setText(_translate("MainWindow", "Phase de la Lune :"))
        self.in_label_4.setText(_translate("MainWindow", "Intérieur"))
        self.out_label_5.setText(_translate("MainWindow", "Extérieur"))
        self.fc_hour_lb_7.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_7.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_7.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_8.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_8.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_8.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_9.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_9.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_9.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_10.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_10.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_10.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_11.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_11.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_11.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_12.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_12.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_12.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_1.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_1.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_1.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_2.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_2.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_2.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_3.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_3.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_3.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_4.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_4.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_4.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_5.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_5.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_5.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_6.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_6.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_6.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_13.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_13.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_13.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_14.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_14.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_14.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_15.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_15.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_15.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_16.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_16.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_16.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_17.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_17.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_17.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_18.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_18.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_18.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_19.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_19.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_19.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_20.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_20.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_20.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_21.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_21.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_21.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_22.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_22.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_22.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_23.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_23.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_23.setText(_translate("MainWindow", "ND"))
        self.fc_hour_lb_24.setText(_translate("MainWindow", "No data"))
        self.fc_weat_bt_24.setText(_translate("MainWindow", "No\n"
"data"))
        self.fc_temp_lb_24.setText(_translate("MainWindow", "ND"))
        self.fc_day_lb_1.setText(_translate("MainWindow", "No data"))
        self.fc_dweat_bt_1.setText(_translate("MainWindow", "No data"))
        self.fc_mmtemp_lb_1.setText(_translate("MainWindow", "ND / ND"))
        self.fc_day_lb_2.setText(_translate("MainWindow", "No data"))
        self.fc_dweat_bt_2.setText(_translate("MainWindow", "No data"))
        self.fc_mmtemp_lb_2.setText(_translate("MainWindow", "ND / ND"))
        self.fc_day_lb_3.setText(_translate("MainWindow", "No data"))
        self.fc_dweat_bt_3.setText(_translate("MainWindow", "No data"))
        self.fc_mmtemp_lb_3.setText(_translate("MainWindow", "ND / ND"))
        self.fc_day_lb_4.setText(_translate("MainWindow", "No data"))
        self.fc_dweat_bt_4.setText(_translate("MainWindow", "No data"))
        self.fc_mmtemp_lb_4.setText(_translate("MainWindow", "ND / ND"))
        self.fc_day_lb_5.setText(_translate("MainWindow", "No data"))
        self.fc_dweat_bt_5.setText(_translate("MainWindow", "No data"))
        self.fc_mmtemp_lb_5.setText(_translate("MainWindow", "ND / ND"))
