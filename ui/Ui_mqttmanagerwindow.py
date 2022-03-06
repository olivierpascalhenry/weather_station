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
"    background-color: rgb(230,230,230);\n"
"    border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout_5 = QtWidgets.QGridLayout(mqttmanagerWindow)
        self.gridLayout_5.setContentsMargins(-1, 4, 4, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.conn_gb = QtWidgets.QGroupBox(mqttmanagerWindow)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.conn_gb.setFont(font)
        self.conn_gb.setStyleSheet("QGroupBox{\n"
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
        self.conn_gb.setObjectName("conn_gb")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.conn_gb)
        self.gridLayout_3.setContentsMargins(10, 8, 0, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.username_lb = QtWidgets.QLabel(self.conn_gb)
        self.username_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.username_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
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
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.username_ln.setFont(font)
        self.username_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
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
        self.username_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.username_bt.setMaximumSize(QtCore.QSize(50, 50))
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
        self.username_bt.setIconSize(QtCore.QSize(36, 36))
        self.username_bt.setObjectName("username_bt")
        self.gridLayout_2.addWidget(self.username_bt, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.password_lb = QtWidgets.QLabel(self.conn_gb)
        self.password_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.password_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
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
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.password_ln.setFont(font)
        self.password_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
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
        self.password_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.password_bt.setMaximumSize(QtCore.QSize(50, 50))
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
        self.password_bt.setIconSize(QtCore.QSize(36, 36))
        self.password_bt.setObjectName("password_bt")
        self.gridLayout_2.addWidget(self.password_bt, 0, 6, 1, 1)
        self.address_lb = QtWidgets.QLabel(self.conn_gb)
        self.address_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.address_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
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
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.address_ln.setFont(font)
        self.address_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
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
        self.address_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.address_bt.setMaximumSize(QtCore.QSize(50, 50))
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
        self.address_bt.setIconSize(QtCore.QSize(36, 36))
        self.address_bt.setObjectName("address_bt")
        self.gridLayout_2.addWidget(self.address_bt, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 3, 1, 1)
        self.main_topic_lb = QtWidgets.QLabel(self.conn_gb)
        self.main_topic_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.main_topic_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
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
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.main_topic_ln.setFont(font)
        self.main_topic_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
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
        self.main_topic_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.main_topic_bt.setMaximumSize(QtCore.QSize(50, 50))
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
        self.main_topic_bt.setIconSize(QtCore.QSize(36, 36))
        self.main_topic_bt.setObjectName("main_topic_bt")
        self.gridLayout_2.addWidget(self.main_topic_bt, 1, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.conn_gb, 0, 0, 1, 1)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(45, 45))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon2)
        self.cancel_button.setIconSize(QtCore.QSize(45, 45))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem3 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.man_gb = QtWidgets.QGroupBox(mqttmanagerWindow)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro SemiBold")
        font.setPointSize(14)
        self.man_gb.setFont(font)
        self.man_gb.setStyleSheet("QGroupBox{\n"
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
        self.man_gb.setObjectName("man_gb")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.man_gb)
        self.gridLayout_4.setContentsMargins(10, 8, 0, 7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.man_gb)
        self.splitter.setStyleSheet("QSplitter::handle {\n"
"    background: rgb(220,220,220);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 5px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 5px;\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/plus_2_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_sensor.setIcon(icon3)
        self.add_sensor.setIconSize(QtCore.QSize(45, 45))
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
        self.del_sensor.setIcon(icon2)
        self.del_sensor.setIconSize(QtCore.QSize(45, 45))
        self.del_sensor.setObjectName("del_sensor")
        self.verticalLayout.addWidget(self.del_sensor)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.sensor_list = QtWidgets.QListWidget(self.layoutWidget)
        self.sensor_list.setEnabled(True)
        self.sensor_list.setMinimumSize(QtCore.QSize(0, 0))
        self.sensor_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.sensor_list.setFont(font)
        self.sensor_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sensor_list.setStyleSheet("QListWidget {\n"
"    border-radius: 0px;\n"
"    background-color:  rgb(240, 240, 240);\n"
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
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.temperature_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.temperature_lb.setEnabled(False)
        self.temperature_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.temperature_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temperature_lb.setFont(font)
        self.temperature_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.temperature_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.temperature_lb.setObjectName("temperature_lb")
        self.gridLayout.addWidget(self.temperature_lb, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.temperature_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.temperature_ln.setEnabled(False)
        self.temperature_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.temperature_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.temperature_ln.setFont(font)
        self.temperature_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.temperature_ln.setText("")
        self.temperature_ln.setReadOnly(False)
        self.temperature_ln.setObjectName("temperature_ln")
        self.horizontalLayout.addWidget(self.temperature_ln)
        self.temperature_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.temperature_bt.setEnabled(False)
        self.temperature_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.temperature_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.temperature_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.temperature_bt.setText("")
        self.temperature_bt.setIcon(icon)
        self.temperature_bt.setIconSize(QtCore.QSize(36, 36))
        self.temperature_bt.setObjectName("temperature_bt")
        self.horizontalLayout.addWidget(self.temperature_bt)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.humidity_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.humidity_lb.setEnabled(False)
        self.humidity_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.humidity_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.humidity_lb.setFont(font)
        self.humidity_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.humidity_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.humidity_lb.setObjectName("humidity_lb")
        self.gridLayout.addWidget(self.humidity_lb, 1, 0, 1, 1)
        self.pressure_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.pressure_lb.setEnabled(False)
        self.pressure_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.pressure_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_lb.setFont(font)
        self.pressure_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.pressure_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pressure_lb.setObjectName("pressure_lb")
        self.gridLayout.addWidget(self.pressure_lb, 2, 0, 1, 1)
        self.battery_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.battery_lb.setEnabled(False)
        self.battery_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.battery_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.battery_lb.setFont(font)
        self.battery_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.battery_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.battery_lb.setObjectName("battery_lb")
        self.gridLayout.addWidget(self.battery_lb, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.battery_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.battery_ln.setEnabled(False)
        self.battery_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.battery_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.battery_ln.setFont(font)
        self.battery_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.battery_ln.setText("")
        self.battery_ln.setReadOnly(False)
        self.battery_ln.setObjectName("battery_ln")
        self.horizontalLayout_4.addWidget(self.battery_ln)
        self.battery_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.battery_bt.setEnabled(False)
        self.battery_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.battery_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.battery_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.battery_bt.setText("")
        self.battery_bt.setIcon(icon)
        self.battery_bt.setIconSize(QtCore.QSize(36, 36))
        self.battery_bt.setObjectName("battery_bt")
        self.horizontalLayout_4.addWidget(self.battery_bt)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.signal_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.signal_lb.setEnabled(False)
        self.signal_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.signal_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.signal_lb.setFont(font)
        self.signal_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.signal_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.signal_lb.setObjectName("signal_lb")
        self.gridLayout.addWidget(self.signal_lb, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.humidity_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.humidity_ln.setEnabled(False)
        self.humidity_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.humidity_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.humidity_ln.setFont(font)
        self.humidity_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.humidity_ln.setText("")
        self.humidity_ln.setReadOnly(False)
        self.humidity_ln.setObjectName("humidity_ln")
        self.horizontalLayout_7.addWidget(self.humidity_ln)
        self.humidity_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.humidity_bt.setEnabled(False)
        self.humidity_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.humidity_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.humidity_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.humidity_bt.setText("")
        self.humidity_bt.setIcon(icon)
        self.humidity_bt.setIconSize(QtCore.QSize(36, 36))
        self.humidity_bt.setObjectName("humidity_bt")
        self.horizontalLayout_7.addWidget(self.humidity_bt)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pressure_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pressure_ln.setEnabled(False)
        self.pressure_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.pressure_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pressure_ln.setFont(font)
        self.pressure_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.pressure_ln.setText("")
        self.pressure_ln.setReadOnly(False)
        self.pressure_ln.setObjectName("pressure_ln")
        self.horizontalLayout_8.addWidget(self.pressure_ln)
        self.pressure_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.pressure_bt.setEnabled(False)
        self.pressure_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.pressure_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.pressure_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.pressure_bt.setText("")
        self.pressure_bt.setIcon(icon)
        self.pressure_bt.setIconSize(QtCore.QSize(36, 36))
        self.pressure_bt.setObjectName("pressure_bt")
        self.horizontalLayout_8.addWidget(self.pressure_bt)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.signal_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.signal_ln.setEnabled(False)
        self.signal_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.signal_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.signal_ln.setFont(font)
        self.signal_ln.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}")
        self.signal_ln.setText("")
        self.signal_ln.setReadOnly(False)
        self.signal_ln.setObjectName("signal_ln")
        self.horizontalLayout_9.addWidget(self.signal_ln)
        self.signal_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.signal_bt.setEnabled(False)
        self.signal_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.signal_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.signal_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.signal_bt.setText("")
        self.signal_bt.setIcon(icon)
        self.signal_bt.setIconSize(QtCore.QSize(36, 36))
        self.signal_bt.setObjectName("signal_bt")
        self.horizontalLayout_9.addWidget(self.signal_bt)
        self.gridLayout.addLayout(self.horizontalLayout_9, 4, 1, 1, 1)
        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.man_gb, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 2, 0, 1, 1)
        self.man_gb.raise_()
        self.conn_gb.raise_()

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
        self.temperature_lb.setText(_translate("mqttmanagerWindow", "Température :"))
        self.humidity_lb.setText(_translate("mqttmanagerWindow", "Humidité :"))
        self.pressure_lb.setText(_translate("mqttmanagerWindow", "Pression :"))
        self.battery_lb.setText(_translate("mqttmanagerWindow", "Batterie :"))
        self.signal_lb.setText(_translate("mqttmanagerWindow", "Signal :"))
