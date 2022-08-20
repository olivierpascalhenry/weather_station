# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mqtt_manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mqttmanagerWindow(object):
    def setupUi(self, mqttmanagerWindow):
        mqttmanagerWindow.setObjectName("mqttmanagerWindow")
        mqttmanagerWindow.resize(860, 570)
        mqttmanagerWindow.setMinimumSize(QtCore.QSize(0, 0))
        mqttmanagerWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        mqttmanagerWindow.setFont(font)
        mqttmanagerWindow.setStyleSheet("QWidget#mqttmanagerWindow {\n"
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
"}")
        self.gridLayout_5 = QtWidgets.QGridLayout(mqttmanagerWindow)
        self.gridLayout_5.setVerticalSpacing(11)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.conn_gb = QtWidgets.QGroupBox(mqttmanagerWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conn_gb.sizePolicy().hasHeightForWidth())
        self.conn_gb.setSizePolicy(sizePolicy)
        self.conn_gb.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        self.conn_gb.setFont(font)
        self.conn_gb.setStyleSheet("QGroupBox{\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.conn_gb.setObjectName("conn_gb")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.conn_gb)
        self.gridLayout_3.setContentsMargins(10, 11, 10, 11)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.username_lb = QtWidgets.QLabel(self.conn_gb)
        self.username_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.username_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.username_lb.setFont(font)
        self.username_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.username_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_lb.setObjectName("username_lb")
        self.gridLayout_2.addWidget(self.username_lb, 0, 0, 1, 1)
        self.username_ln = QtWidgets.QLineEdit(self.conn_gb)
        self.username_ln.setEnabled(True)
        self.username_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.username_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.username_ln.setFont(font)
        self.username_ln.setStyleSheet("QLineEdit {\n"
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
        self.username_ln.setText("")
        self.username_ln.setReadOnly(False)
        self.username_ln.setObjectName("username_ln")
        self.gridLayout_2.addWidget(self.username_ln, 0, 1, 1, 1)
        self.username_bt = QtWidgets.QToolButton(self.conn_gb)
        self.username_bt.setEnabled(True)
        self.username_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.username_bt.setMaximumSize(QtCore.QSize(40, 40))
        self.username_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.username_bt.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.username_bt.setIcon(icon)
        self.username_bt.setIconSize(QtCore.QSize(40, 40))
        self.username_bt.setObjectName("username_bt")
        self.gridLayout_2.addWidget(self.username_bt, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.password_lb = QtWidgets.QLabel(self.conn_gb)
        self.password_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.password_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.password_lb.setFont(font)
        self.password_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.password_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_lb.setObjectName("password_lb")
        self.gridLayout_2.addWidget(self.password_lb, 0, 4, 1, 1)
        self.password_ln = QtWidgets.QLineEdit(self.conn_gb)
        self.password_ln.setEnabled(True)
        self.password_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.password_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.password_ln.setFont(font)
        self.password_ln.setStyleSheet("QLineEdit {\n"
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
        self.password_ln.setText("")
        self.password_ln.setReadOnly(False)
        self.password_ln.setObjectName("password_ln")
        self.gridLayout_2.addWidget(self.password_ln, 0, 5, 1, 1)
        self.password_bt = QtWidgets.QToolButton(self.conn_gb)
        self.password_bt.setEnabled(True)
        self.password_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.password_bt.setMaximumSize(QtCore.QSize(40, 40))
        self.password_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.password_bt.setText("")
        self.password_bt.setIcon(icon)
        self.password_bt.setIconSize(QtCore.QSize(40, 40))
        self.password_bt.setObjectName("password_bt")
        self.gridLayout_2.addWidget(self.password_bt, 0, 6, 1, 1)
        self.address_lb = QtWidgets.QLabel(self.conn_gb)
        self.address_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.address_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.address_lb.setFont(font)
        self.address_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.address_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address_lb.setObjectName("address_lb")
        self.gridLayout_2.addWidget(self.address_lb, 1, 0, 1, 1)
        self.address_ln = QtWidgets.QLineEdit(self.conn_gb)
        self.address_ln.setEnabled(True)
        self.address_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.address_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.address_ln.setFont(font)
        self.address_ln.setStyleSheet("QLineEdit {\n"
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
        self.address_ln.setText("")
        self.address_ln.setReadOnly(False)
        self.address_ln.setObjectName("address_ln")
        self.gridLayout_2.addWidget(self.address_ln, 1, 1, 1, 1)
        self.address_bt = QtWidgets.QToolButton(self.conn_gb)
        self.address_bt.setEnabled(True)
        self.address_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.address_bt.setMaximumSize(QtCore.QSize(40, 40))
        self.address_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.address_bt.setText("")
        self.address_bt.setIcon(icon)
        self.address_bt.setIconSize(QtCore.QSize(40, 40))
        self.address_bt.setObjectName("address_bt")
        self.gridLayout_2.addWidget(self.address_bt, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)
        self.main_topic_lb = QtWidgets.QLabel(self.conn_gb)
        self.main_topic_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.main_topic_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_topic_lb.setFont(font)
        self.main_topic_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.main_topic_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.main_topic_lb.setObjectName("main_topic_lb")
        self.gridLayout_2.addWidget(self.main_topic_lb, 1, 4, 1, 1)
        self.main_topic_ln = QtWidgets.QLineEdit(self.conn_gb)
        self.main_topic_ln.setEnabled(True)
        self.main_topic_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.main_topic_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_topic_ln.setFont(font)
        self.main_topic_ln.setStyleSheet("QLineEdit {\n"
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
        self.main_topic_ln.setText("")
        self.main_topic_ln.setReadOnly(False)
        self.main_topic_ln.setObjectName("main_topic_ln")
        self.gridLayout_2.addWidget(self.main_topic_ln, 1, 5, 1, 1)
        self.main_topic_bt = QtWidgets.QToolButton(self.conn_gb)
        self.main_topic_bt.setEnabled(True)
        self.main_topic_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.main_topic_bt.setMaximumSize(QtCore.QSize(40, 40))
        self.main_topic_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.main_topic_bt.setText("")
        self.main_topic_bt.setIcon(icon)
        self.main_topic_bt.setIconSize(QtCore.QSize(40, 40))
        self.main_topic_bt.setObjectName("main_topic_bt")
        self.gridLayout_2.addWidget(self.main_topic_bt, 1, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.conn_gb, 0, 0, 1, 1)
        self.man_gb = QtWidgets.QGroupBox(mqttmanagerWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.man_gb.sizePolicy().hasHeightForWidth())
        self.man_gb.setSizePolicy(sizePolicy)
        self.man_gb.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(18)
        self.man_gb.setFont(font)
        self.man_gb.setStyleSheet("QGroupBox {\n"
"    border: 1px solid grey;\n"
"    margin-top: 1.0em;\n"
"    padding-top: 8px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    top: -17px;\n"
"    left: 10px;\n"
"    color: rgb(45,45,45);\n"
"}")
        self.man_gb.setObjectName("man_gb")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.man_gb)
        self.gridLayout_4.setContentsMargins(10, 11, 0, 11)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.man_gb)
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
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_sensor = QtWidgets.QToolButton(self.layoutWidget)
        self.add_sensor.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_sensor.sizePolicy().hasHeightForWidth())
        self.add_sensor.setSizePolicy(sizePolicy)
        self.add_sensor.setMinimumSize(QtCore.QSize(50, 50))
        self.add_sensor.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.add_sensor.setFont(font)
        self.add_sensor.setStyleSheet("QToolButton {\n"
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
        self.add_sensor.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/plus_2_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_sensor.setIcon(icon1)
        self.add_sensor.setIconSize(QtCore.QSize(50, 50))
        self.add_sensor.setObjectName("add_sensor")
        self.verticalLayout.addWidget(self.add_sensor)
        self.del_sensor = QtWidgets.QToolButton(self.layoutWidget)
        self.del_sensor.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_sensor.sizePolicy().hasHeightForWidth())
        self.del_sensor.setSizePolicy(sizePolicy)
        self.del_sensor.setMinimumSize(QtCore.QSize(50, 50))
        self.del_sensor.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.del_sensor.setFont(font)
        self.del_sensor.setStyleSheet("QToolButton {\n"
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
        self.del_sensor.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_sensor.setIcon(icon2)
        self.del_sensor.setIconSize(QtCore.QSize(50, 50))
        self.del_sensor.setObjectName("del_sensor")
        self.verticalLayout.addWidget(self.del_sensor)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.sensor_list = QtWidgets.QListWidget(self.layoutWidget)
        self.sensor_list.setEnabled(True)
        self.sensor_list.setMinimumSize(QtCore.QSize(0, 0))
        self.sensor_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sensor_list.setFont(font)
        self.sensor_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sensor_list.setStyleSheet("QListWidget {\n"
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
        self.sensor_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sensor_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.sensor_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sensor_list.setObjectName("sensor_list")
        self.horizontalLayout_6.addWidget(self.sensor_list)
        self.info_scroll_area = QtWidgets.QScrollArea(self.splitter)
        self.info_scroll_area.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.info_scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info_scroll_area.setWidgetResizable(True)
        self.info_scroll_area.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_scroll_area.setObjectName("info_scroll_area")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 474, 289))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.active_ck = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.active_ck.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.active_ck.setFont(font)
        self.active_ck.setStyleSheet("QCheckBox {\n"
"    spacing: 10px;\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(145,145,145);\n"
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
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"    image: url(icons/checkbox_icon_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover:disabled {\n"
"    image: url(icons/checkbox_icon_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed:disabled {\n"
"    image: url(icons/checkbox_icon_unchecked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    image: url(icons/checkbox_icon_checked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover:disabled {\n"
"    image: url(icons/checkbox_icon_checked_disabled.svg);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed:disabled {\n"
"    image: url(icons/checkbox_icon_checked_disabled.svg);\n"
"}")
        self.active_ck.setObjectName("active_ck")
        self.horizontalLayout_3.addWidget(self.active_ck)
        spacerItem3 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.store_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.store_lb.setEnabled(False)
        self.store_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.store_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_lb.setFont(font)
        self.store_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.store_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_lb.setObjectName("store_lb")
        self.horizontalLayout.addWidget(self.store_lb)
        self.store_ln = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_5)
        self.store_ln.setEnabled(False)
        self.store_ln.setMinimumSize(QtCore.QSize(50, 40))
        self.store_ln.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_ln.setFont(font)
        self.store_ln.setStyleSheet("QLineEdit {\n"
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
        self.store_ln.setText("")
        self.store_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_ln.setReadOnly(False)
        self.store_ln.setObjectName("store_ln")
        self.horizontalLayout.addWidget(self.store_ln)
        self.store_lb_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.store_lb_2.setEnabled(False)
        self.store_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.store_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_lb_2.setFont(font)
        self.store_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.store_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_lb_2.setObjectName("store_lb_2")
        self.horizontalLayout.addWidget(self.store_lb_2)
        self.store_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.store_bt.setEnabled(False)
        self.store_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.store_bt.setMaximumSize(QtCore.QSize(40, 40))
        self.store_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.store_bt.setText("")
        self.store_bt.setIcon(icon)
        self.store_bt.setIconSize(QtCore.QSize(40, 40))
        self.store_bt.setObjectName("store_bt")
        self.horizontalLayout.addWidget(self.store_bt)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addtopic_cb = QtWidgets.QComboBox(self.scrollAreaWidgetContents_5)
        self.addtopic_cb.setEnabled(False)
        self.addtopic_cb.setMinimumSize(QtCore.QSize(220, 40))
        self.addtopic_cb.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.addtopic_cb.setFont(font)
        self.addtopic_cb.setStyleSheet("QComboBox {\n"
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
        self.addtopic_cb.setObjectName("addtopic_cb")
        self.addtopic_cb.addItem("")
        self.addtopic_cb.addItem("")
        self.addtopic_cb.addItem("")
        self.addtopic_cb.addItem("")
        self.addtopic_cb.addItem("")
        self.addtopic_cb.addItem("")
        self.horizontalLayout_4.addWidget(self.addtopic_cb)
        self.addtopic_bt = QtWidgets.QToolButton(self.scrollAreaWidgetContents_5)
        self.addtopic_bt.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addtopic_bt.sizePolicy().hasHeightForWidth())
        self.addtopic_bt.setSizePolicy(sizePolicy)
        self.addtopic_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.addtopic_bt.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.addtopic_bt.setFont(font)
        self.addtopic_bt.setStyleSheet("QToolButton {\n"
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
        self.addtopic_bt.setText("")
        self.addtopic_bt.setIcon(icon1)
        self.addtopic_bt.setIconSize(QtCore.QSize(40, 40))
        self.addtopic_bt.setObjectName("addtopic_bt")
        self.horizontalLayout_4.addWidget(self.addtopic_bt)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem7)
        self.topic_layout = QtWidgets.QVBoxLayout()
        self.topic_layout.setContentsMargins(-1, -1, 10, -1)
        self.topic_layout.setObjectName("topic_layout")
        self.verticalLayout_2.addLayout(self.topic_layout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.info_scroll_area.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.man_gb, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok_button = QtWidgets.QToolButton(mqttmanagerWindow)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon3)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.cancel_button = QtWidgets.QToolButton(mqttmanagerWindow)
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
        self.cancel_button.setIcon(icon2)
        self.cancel_button.setIconSize(QtCore.QSize(50, 50))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem9 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(mqttmanagerWindow)
        QtCore.QMetaObject.connectSlotsByName(mqttmanagerWindow)

    def retranslateUi(self, mqttmanagerWindow):
        _translate = QtCore.QCoreApplication.translate
        self.conn_gb.setTitle(_translate("mqttmanagerWindow", "Connexion au serveur MQTT local"))
        self.username_lb.setText(_translate("mqttmanagerWindow", "Utilisateur :"))
        self.password_lb.setText(_translate("mqttmanagerWindow", "Mot de passe :"))
        self.address_lb.setText(_translate("mqttmanagerWindow", "Adresse :"))
        self.main_topic_lb.setText(_translate("mqttmanagerWindow", "Topic principal :"))
        self.man_gb.setTitle(_translate("mqttmanagerWindow", "Manager"))
        self.active_ck.setText(_translate("mqttmanagerWindow", "Capteur activé ?"))
        self.store_lb.setText(_translate("mqttmanagerWindow", "Rétention :"))
        self.store_lb_2.setText(_translate("mqttmanagerWindow", "heures"))
        self.addtopic_cb.setItemText(0, _translate("mqttmanagerWindow", "Ajouter un topic"))
        self.addtopic_cb.setItemText(1, _translate("mqttmanagerWindow", "Batterie"))
        self.addtopic_cb.setItemText(2, _translate("mqttmanagerWindow", "Humidité"))
        self.addtopic_cb.setItemText(3, _translate("mqttmanagerWindow", "Pression"))
        self.addtopic_cb.setItemText(4, _translate("mqttmanagerWindow", "Signal"))
        self.addtopic_cb.setItemText(5, _translate("mqttmanagerWindow", "Température"))
