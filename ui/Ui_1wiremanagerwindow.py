# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1wire_manager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sensormanagerWindow(object):
    def setupUi(self, sensormanagerWindow):
        sensormanagerWindow.setObjectName("sensormanagerWindow")
        sensormanagerWindow.resize(800, 386)
        sensormanagerWindow.setMinimumSize(QtCore.QSize(0, 0))
        sensormanagerWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        sensormanagerWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sensormanagerWindow.setWindowIcon(icon)
        sensormanagerWindow.setStyleSheet("QWidget#sensormanagerWindow {\n"
"    background-color: rgb(230,230,230);\n"
"    border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(sensormanagerWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(sensormanagerWindow)
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/plus_2_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_sensor.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_sensor.setIcon(icon2)
        self.del_sensor.setIconSize(QtCore.QSize(45, 45))
        self.del_sensor.setObjectName("del_sensor")
        self.verticalLayout.addWidget(self.del_sensor)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.section_list = QtWidgets.QListWidget(self.layoutWidget)
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
        self.section_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.section_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.section_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.section_list.setObjectName("section_list")
        self.horizontalLayout_6.addWidget(self.section_list)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.name_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.name_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name_lb.setFont(font)
        self.name_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.name_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.name_ln.setEnabled(False)
        self.name_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.name_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name_ln.setFont(font)
        self.name_ln.setStyleSheet("QLineEdit {\n"
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
        self.name_ln.setText("")
        self.name_ln.setReadOnly(False)
        self.name_ln.setObjectName("name_ln")
        self.horizontalLayout.addWidget(self.name_ln)
        self.name_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.name_bt.setEnabled(False)
        self.name_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.name_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.name_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.name_bt.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_bt.setIcon(icon3)
        self.name_bt.setIconSize(QtCore.QSize(36, 36))
        self.name_bt.setObjectName("name_bt")
        self.horizontalLayout.addWidget(self.name_bt)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.id_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.id_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.id_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_lb.setFont(font)
        self.id_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.id_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_lb.setObjectName("id_lb")
        self.gridLayout.addWidget(self.id_lb, 1, 0, 1, 1)
        self.id_ln = QtWidgets.QLabel(self.layoutWidget1)
        self.id_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.id_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_ln.setFont(font)
        self.id_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.id_ln.setText("")
        self.id_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.id_ln.setObjectName("id_ln")
        self.gridLayout.addWidget(self.id_ln, 1, 1, 1, 1)
        self.refresh_lb_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.refresh_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.refresh_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.refresh_lb_1.setFont(font)
        self.refresh_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.refresh_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refresh_lb_1.setObjectName("refresh_lb_1")
        self.gridLayout.addWidget(self.refresh_lb_1, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.refresh_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.refresh_ln.setEnabled(False)
        self.refresh_ln.setMinimumSize(QtCore.QSize(50, 40))
        self.refresh_ln.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.refresh_ln.setFont(font)
        self.refresh_ln.setStyleSheet("QLineEdit {\n"
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
        self.refresh_ln.setText("")
        self.refresh_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refresh_ln.setReadOnly(False)
        self.refresh_ln.setObjectName("refresh_ln")
        self.horizontalLayout_3.addWidget(self.refresh_ln)
        self.refresh_lb_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.refresh_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.refresh_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.refresh_lb_2.setFont(font)
        self.refresh_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.refresh_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refresh_lb_2.setObjectName("refresh_lb_2")
        self.horizontalLayout_3.addWidget(self.refresh_lb_2)
        self.refresh_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.refresh_bt.setEnabled(False)
        self.refresh_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.refresh_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.refresh_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.refresh_bt.setText("")
        self.refresh_bt.setIcon(icon3)
        self.refresh_bt.setIconSize(QtCore.QSize(36, 36))
        self.refresh_bt.setObjectName("refresh_bt")
        self.horizontalLayout_3.addWidget(self.refresh_bt)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.table_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.table_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.table_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.table_lb.setFont(font)
        self.table_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.table_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.table_lb.setObjectName("table_lb")
        self.gridLayout.addWidget(self.table_lb, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.table_ln.setEnabled(False)
        self.table_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.table_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.table_ln.setFont(font)
        self.table_ln.setStyleSheet("QLineEdit {\n"
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
        self.table_ln.setText("")
        self.table_ln.setReadOnly(False)
        self.table_ln.setObjectName("table_ln")
        self.horizontalLayout_4.addWidget(self.table_ln)
        self.table_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.table_bt.setEnabled(False)
        self.table_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.table_bt.setMaximumSize(QtCore.QSize(50, 50))
        self.table_bt.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.table_bt.setText("")
        self.table_bt.setIcon(icon3)
        self.table_bt.setIconSize(QtCore.QSize(36, 36))
        self.table_bt.setObjectName("table_bt")
        self.horizontalLayout_4.addWidget(self.table_bt)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.store_lb_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.store_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.store_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_lb_1.setFont(font)
        self.store_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.store_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_lb_1.setObjectName("store_lb_1")
        self.gridLayout.addWidget(self.store_lb_1, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.store_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.store_ln.setEnabled(False)
        self.store_ln.setMinimumSize(QtCore.QSize(50, 40))
        self.store_ln.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_ln.setFont(font)
        self.store_ln.setStyleSheet("QLineEdit {\n"
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
        self.store_ln.setText("")
        self.store_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_ln.setReadOnly(False)
        self.store_ln.setObjectName("store_ln")
        self.horizontalLayout_5.addWidget(self.store_ln)
        self.store_lb_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.store_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.store_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_lb_2.setFont(font)
        self.store_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.store_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_lb_2.setObjectName("store_lb_2")
        self.horizontalLayout_5.addWidget(self.store_lb_2)
        self.store_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.store_bt.setEnabled(False)
        self.store_bt.setMinimumSize(QtCore.QSize(50, 50))
        self.store_bt.setMaximumSize(QtCore.QSize(50, 50))
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
        self.store_bt.setIcon(icon3)
        self.store_bt.setIconSize(QtCore.QSize(36, 36))
        self.store_bt.setObjectName("store_bt")
        self.horizontalLayout_5.addWidget(self.store_bt)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ok_button = QtWidgets.QToolButton(sensormanagerWindow)
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon4)
        self.ok_button.setIconSize(QtCore.QSize(45, 45))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.cancel_button = QtWidgets.QToolButton(sensormanagerWindow)
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
        self.cancel_button.setIconSize(QtCore.QSize(45, 45))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem5 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(sensormanagerWindow)
        QtCore.QMetaObject.connectSlotsByName(sensormanagerWindow)

    def retranslateUi(self, sensormanagerWindow):
        _translate = QtCore.QCoreApplication.translate
        sensormanagerWindow.setWindowTitle(_translate("sensormanagerWindow", "Options"))
        self.name_lb.setText(_translate("sensormanagerWindow", "Nom :"))
        self.id_lb.setText(_translate("sensormanagerWindow", "ID :"))
        self.refresh_lb_1.setText(_translate("sensormanagerWindow", "Rafraichissement :"))
        self.refresh_lb_2.setText(_translate("sensormanagerWindow", "secondes"))
        self.table_lb.setText(_translate("sensormanagerWindow", "Nom de la table :"))
        self.store_lb_1.setText(_translate("sensormanagerWindow", "Rétention :"))
        self.store_lb_2.setText(_translate("sensormanagerWindow", "heures"))
