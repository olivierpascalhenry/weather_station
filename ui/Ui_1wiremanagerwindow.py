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
        sensormanagerWindow.resize(800, 362)
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
"    background-color: rgb(240,240,240);\n"
"    border: 1px solid rgb(75,75,75);\n"
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
        self.gridLayout_2 = QtWidgets.QGridLayout(sensormanagerWindow)
        self.gridLayout_2.setVerticalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ok_button.setIcon(icon1)
        self.ok_button.setIconSize(QtCore.QSize(50, 50))
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_2.addWidget(self.ok_button)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_button.setIcon(icon2)
        self.cancel_button.setIconSize(QtCore.QSize(50, 50))
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        spacerItem1 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(sensormanagerWindow)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/plus_2_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_sensor.setIcon(icon3)
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
        self.del_sensor.setIcon(icon2)
        self.del_sensor.setIconSize(QtCore.QSize(50, 50))
        self.del_sensor.setObjectName("del_sensor")
        self.verticalLayout.addWidget(self.del_sensor)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.section_list = QtWidgets.QListWidget(self.layoutWidget)
        self.section_list.setEnabled(True)
        self.section_list.setMinimumSize(QtCore.QSize(0, 0))
        self.section_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
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
        self.horizontalLayout_6.addWidget(self.section_list)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(10, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.active_ck = QtWidgets.QCheckBox(self.layoutWidget1)
        self.active_ck.setEnabled(False)
        self.active_ck.setMinimumSize(QtCore.QSize(0, 40))
        self.active_ck.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.horizontalLayout_7.addWidget(self.active_ck)
        spacerItem3 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 2)
        self.name_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.name_lb.setEnabled(False)
        self.name_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.name_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name_lb.setFont(font)
        self.name_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.name_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.name_ln.setEnabled(False)
        self.name_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.name_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name_ln.setFont(font)
        self.name_ln.setStyleSheet("QLineEdit {\n"
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
        self.name_ln.setText("")
        self.name_ln.setReadOnly(False)
        self.name_ln.setObjectName("name_ln")
        self.horizontalLayout.addWidget(self.name_ln)
        self.name_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.name_bt.setEnabled(False)
        self.name_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.name_bt.setMaximumSize(QtCore.QSize(40, 40))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_bt.setIcon(icon4)
        self.name_bt.setIconSize(QtCore.QSize(40, 40))
        self.name_bt.setObjectName("name_bt")
        self.horizontalLayout.addWidget(self.name_bt)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.id_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.id_lb.setEnabled(False)
        self.id_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.id_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_lb.setFont(font)
        self.id_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.id_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_lb.setObjectName("id_lb")
        self.gridLayout.addWidget(self.id_lb, 2, 0, 1, 1)
        self.id_ln = QtWidgets.QLabel(self.layoutWidget1)
        self.id_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.id_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.id_ln.setFont(font)
        self.id_ln.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.id_ln.setText("")
        self.id_ln.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.id_ln.setObjectName("id_ln")
        self.gridLayout.addWidget(self.id_ln, 2, 1, 1, 1)
        self.refresh_lb_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.refresh_lb_1.setEnabled(False)
        self.refresh_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.refresh_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.refresh_lb_1.setFont(font)
        self.refresh_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.refresh_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refresh_lb_1.setObjectName("refresh_lb_1")
        self.gridLayout.addWidget(self.refresh_lb_1, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.refresh_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.refresh_ln.setEnabled(False)
        self.refresh_ln.setMinimumSize(QtCore.QSize(50, 40))
        self.refresh_ln.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.refresh_ln.setFont(font)
        self.refresh_ln.setStyleSheet("QLineEdit {\n"
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
        self.refresh_ln.setText("")
        self.refresh_ln.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refresh_ln.setReadOnly(False)
        self.refresh_ln.setObjectName("refresh_ln")
        self.horizontalLayout_3.addWidget(self.refresh_ln)
        self.refresh_lb_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.refresh_lb_2.setEnabled(False)
        self.refresh_lb_2.setMinimumSize(QtCore.QSize(0, 40))
        self.refresh_lb_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.refresh_lb_2.setFont(font)
        self.refresh_lb_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.refresh_lb_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.refresh_lb_2.setObjectName("refresh_lb_2")
        self.horizontalLayout_3.addWidget(self.refresh_lb_2)
        self.refresh_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.refresh_bt.setEnabled(False)
        self.refresh_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.refresh_bt.setMaximumSize(QtCore.QSize(40, 40))
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
        self.refresh_bt.setIcon(icon4)
        self.refresh_bt.setIconSize(QtCore.QSize(40, 40))
        self.refresh_bt.setObjectName("refresh_bt")
        self.horizontalLayout_3.addWidget(self.refresh_bt)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.table_lb = QtWidgets.QLabel(self.layoutWidget1)
        self.table_lb.setEnabled(False)
        self.table_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.table_lb.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.table_lb.setFont(font)
        self.table_lb.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.table_lb.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.table_lb.setObjectName("table_lb")
        self.gridLayout.addWidget(self.table_lb, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_ln = QtWidgets.QLineEdit(self.layoutWidget1)
        self.table_ln.setEnabled(False)
        self.table_ln.setMinimumSize(QtCore.QSize(0, 40))
        self.table_ln.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.table_ln.setFont(font)
        self.table_ln.setStyleSheet("QLineEdit {\n"
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
        self.table_ln.setText("")
        self.table_ln.setReadOnly(False)
        self.table_ln.setObjectName("table_ln")
        self.horizontalLayout_4.addWidget(self.table_ln)
        self.table_bt = QtWidgets.QToolButton(self.layoutWidget1)
        self.table_bt.setEnabled(False)
        self.table_bt.setMinimumSize(QtCore.QSize(40, 40))
        self.table_bt.setMaximumSize(QtCore.QSize(40, 40))
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
        self.table_bt.setIcon(icon4)
        self.table_bt.setIconSize(QtCore.QSize(40, 40))
        self.table_bt.setObjectName("table_bt")
        self.horizontalLayout_4.addWidget(self.table_bt)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.store_lb_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.store_lb_1.setEnabled(False)
        self.store_lb_1.setMinimumSize(QtCore.QSize(0, 40))
        self.store_lb_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(18)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.store_lb_1.setFont(font)
        self.store_lb_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"    color: rgb(145,145,145);\n"
"}")
        self.store_lb_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.store_lb_1.setObjectName("store_lb_1")
        self.gridLayout.addWidget(self.store_lb_1, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.store_ln = QtWidgets.QLineEdit(self.layoutWidget1)
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
        self.horizontalLayout_5.addWidget(self.store_ln)
        self.store_lb_2 = QtWidgets.QLabel(self.layoutWidget1)
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
        self.horizontalLayout_5.addWidget(self.store_lb_2)
        self.store_bt = QtWidgets.QToolButton(self.layoutWidget1)
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
        self.store_bt.setIcon(icon4)
        self.store_bt.setIconSize(QtCore.QSize(40, 40))
        self.store_bt.setObjectName("store_bt")
        self.horizontalLayout_5.addWidget(self.store_bt)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(sensormanagerWindow)
        QtCore.QMetaObject.connectSlotsByName(sensormanagerWindow)

    def retranslateUi(self, sensormanagerWindow):
        _translate = QtCore.QCoreApplication.translate
        sensormanagerWindow.setWindowTitle(_translate("sensormanagerWindow", "Options"))
        self.active_ck.setText(_translate("sensormanagerWindow", "Capteur activé ?"))
        self.name_lb.setText(_translate("sensormanagerWindow", "Nom :"))
        self.id_lb.setText(_translate("sensormanagerWindow", "ID :"))
        self.refresh_lb_1.setText(_translate("sensormanagerWindow", "Rafraichissement :"))
        self.refresh_lb_2.setText(_translate("sensormanagerWindow", "secondes"))
        self.table_lb.setText(_translate("sensormanagerWindow", "Nom de la table :"))
        self.store_lb_1.setText(_translate("sensormanagerWindow", "Rétention :"))
        self.store_lb_2.setText(_translate("sensormanagerWindow", "heures"))
