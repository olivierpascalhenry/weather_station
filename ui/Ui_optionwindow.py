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
        optionWindow.resize(600, 364)
        optionWindow.setMinimumSize(QtCore.QSize(0, 0))
        optionWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        optionWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/option_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        optionWindow.setWindowIcon(icon)
        optionWindow.setStyleSheet("QWidget#optionWindow {\n"
"    background-color: rgb(230,230,230);\n"
"    border: 1px solid rgb(75,75,75);\n"
"}")
        self.gridLayout_13 = QtWidgets.QGridLayout(optionWindow)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.ow_splitter = QtWidgets.QSplitter(optionWindow)
        self.ow_splitter.setStyleSheet("QSplitter::handle {\n"
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
        self.ow_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.ow_splitter.setObjectName("ow_splitter")
        self.ow_section_list = QtWidgets.QListWidget(self.ow_splitter)
        self.ow_section_list.setEnabled(True)
        self.ow_section_list.setMinimumSize(QtCore.QSize(0, 0))
        self.ow_section_list.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_section_list.setFont(font)
        self.ow_section_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ow_section_list.setStyleSheet("QListWidget {\n"
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
        self.ow_section_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_section_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.ow_section_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ow_section_list.setObjectName("ow_section_list")
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.ow_section_list.addItem(item)
        self.ow_stacked_widget = QtWidgets.QStackedWidget(self.ow_splitter)
        self.ow_stacked_widget.setObjectName("ow_stacked_widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_12.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.ow_scroll_area_4 = QtWidgets.QScrollArea(self.page_1)
        self.ow_scroll_area_4.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }")
        self.ow_scroll_area_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_4.setWidgetResizable(True)
        self.ow_scroll_area_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_4.setObjectName("ow_scroll_area_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 378, 266))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.ow_vertical_layout_4 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_4.setObjectName("ow_vertical_layout_4")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.ow_label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ow_label_32.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_32.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_32.setFont(font)
        self.ow_label_32.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_32.setObjectName("ow_label_32")
        self.horizontalLayout_21.addWidget(self.ow_label_32)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem)
        self.ow_vertical_layout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.ow_label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ow_label_33.setMinimumSize(QtCore.QSize(0, 40))
        self.ow_label_33.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_33.setFont(font)
        self.ow_label_33.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_33.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_33.setObjectName("ow_label_33")
        self.horizontalLayout_22.addWidget(self.ow_label_33)
        self.ow_line_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.ow_line_7.setMinimumSize(QtCore.QSize(70, 40))
        self.ow_line_7.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_7.setFont(font)
        self.ow_line_7.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_7.setText("")
        self.ow_line_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_line_7.setReadOnly(False)
        self.ow_line_7.setObjectName("ow_line_7")
        self.horizontalLayout_22.addWidget(self.ow_line_7)
        self.ow_label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.ow_label_34.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_34.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_34.setFont(font)
        self.ow_label_34.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_34.setObjectName("ow_label_34")
        self.horizontalLayout_22.addWidget(self.ow_label_34)
        self.ow_edit_bt_5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_4)
        self.ow_edit_bt_5.setMinimumSize(QtCore.QSize(40, 40))
        self.ow_edit_bt_5.setMaximumSize(QtCore.QSize(40, 40))
        self.ow_edit_bt_5.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/edit_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_edit_bt_5.setIcon(icon1)
        self.ow_edit_bt_5.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_5.setObjectName("ow_edit_bt_5")
        self.horizontalLayout_22.addWidget(self.ow_edit_bt_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem2)
        self.ow_vertical_layout_4.addLayout(self.horizontalLayout_22)
        self.gridLayout_10.addLayout(self.ow_vertical_layout_4, 0, 0, 1, 1)
        self.ow_scroll_area_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_12.addWidget(self.ow_scroll_area_4, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ow_scroll_area_1 = QtWidgets.QScrollArea(self.page_2)
        self.ow_scroll_area_1.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }")
        self.ow_scroll_area_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_1.setWidgetResizable(True)
        self.ow_scroll_area_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_1.setObjectName("ow_scroll_area_1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 378, 266))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ow_vertical_layout = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout.setObjectName("ow_vertical_layout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ow_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_1.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_1.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_1.setFont(font)
        self.ow_label_1.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_1.setObjectName("ow_label_1")
        self.horizontalLayout_3.addWidget(self.ow_label_1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.ow_vertical_layout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ow_line_1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ow_line_1.setMinimumSize(QtCore.QSize(0, 40))
        self.ow_line_1.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_1.setFont(font)
        self.ow_line_1.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_1.setObjectName("ow_line_1")
        self.horizontalLayout.addWidget(self.ow_line_1)
        self.ow_openButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.ow_openButton.setMinimumSize(QtCore.QSize(40, 40))
        self.ow_openButton.setMaximumSize(QtCore.QSize(40, 40))
        self.ow_openButton.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_openButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/open_popup_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_openButton.setIcon(icon2)
        self.ow_openButton.setIconSize(QtCore.QSize(36, 36))
        self.ow_openButton.setAutoRaise(False)
        self.ow_openButton.setObjectName("ow_openButton")
        self.horizontalLayout.addWidget(self.ow_openButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.ow_label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.ow_label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_3.setFont(font)
        self.ow_label_3.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_3.setObjectName("ow_label_3")
        self.gridLayout_3.addWidget(self.ow_label_3, 1, 0, 1, 1)
        self.ow_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ow_label_2.setMinimumSize(QtCore.QSize(0, 39))
        self.ow_label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_2.setFont(font)
        self.ow_label_2.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_2.setObjectName("ow_label_2")
        self.gridLayout_3.addWidget(self.ow_label_2, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ow_combobox_1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.ow_combobox_1.setMinimumSize(QtCore.QSize(120, 40))
        self.ow_combobox_1.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_combobox_1.setFont(font)
        self.ow_combobox_1.setStyleSheet("QComboBox {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    padding-left: 5px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
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
"    background: #f0f0f0;\n"
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
        self.ow_combobox_1.setObjectName("ow_combobox_1")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.ow_combobox_1.addItem("")
        self.horizontalLayout_7.addWidget(self.ow_combobox_1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)
        self.ow_vertical_layout.addLayout(self.horizontalLayout_6)
        self.gridLayout_6.addLayout(self.ow_vertical_layout, 0, 0, 1, 1)
        self.ow_scroll_area_1.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.ow_scroll_area_1, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_9.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ow_scroll_area_3 = QtWidgets.QScrollArea(self.page_3)
        self.ow_scroll_area_3.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.ow_scroll_area_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_3.setWidgetResizable(True)
        self.ow_scroll_area_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_3.setObjectName("ow_scroll_area_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 485, 286))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.ow_vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_3.setObjectName("ow_vertical_layout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ow_label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_9.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_9.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_9.setFont(font)
        self.ow_label_9.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_9.setObjectName("ow_label_9")
        self.horizontalLayout_8.addWidget(self.ow_label_9)
        self.ow_search_button = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.ow_search_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ow_search_button.sizePolicy().hasHeightForWidth())
        self.ow_search_button.setSizePolicy(sizePolicy)
        self.ow_search_button.setMinimumSize(QtCore.QSize(160, 40))
        self.ow_search_button.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ow_search_button.setFont(font)
        self.ow_search_button.setStyleSheet("QToolButton {\n"
"    border: 1px solid #acacac;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f0f0f0, stop: 1 #e5e5e5);\n"
"    color: rgb(45,45,45);\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color:  rgb(200,200,200);\n"
"    color: rgb(145,145,145);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    border: 1px solid #7eb4ea;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ecf4fc, stop: 1 #dcecfc);\n"
"}\n"
"\n"
"\n"
"QToolButton:pressed {\n"
"    border: 1px solid #579de5;\n"
"    border-radius: 1px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #daecfc, stop: 1 #c4e0fc);\n"
"}")
        self.ow_search_button.setObjectName("ow_search_button")
        self.horizontalLayout_8.addWidget(self.ow_search_button)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ow_line_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.ow_line_4.setMinimumSize(QtCore.QSize(250, 40))
        self.ow_line_4.setMaximumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_4.setFont(font)
        self.ow_line_4.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_4.setText("")
        self.ow_line_4.setReadOnly(False)
        self.ow_line_4.setObjectName("ow_line_4")
        self.horizontalLayout_10.addWidget(self.ow_line_4)
        self.ow_edit_bt_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.ow_edit_bt_3.setMinimumSize(QtCore.QSize(40, 40))
        self.ow_edit_bt_3.setMaximumSize(QtCore.QSize(40, 40))
        self.ow_edit_bt_3.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_3.setText("")
        self.ow_edit_bt_3.setIcon(icon1)
        self.ow_edit_bt_3.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_3.setObjectName("ow_edit_bt_3")
        self.horizontalLayout_10.addWidget(self.ow_edit_bt_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)
        self.ow_label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_10.setMinimumSize(QtCore.QSize(0, 40))
        self.ow_label_10.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_10.setFont(font)
        self.ow_label_10.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_10.setObjectName("ow_label_10")
        self.gridLayout_4.addWidget(self.ow_label_10, 0, 0, 1, 1)
        self.ow_label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_13.setMinimumSize(QtCore.QSize(80, 40))
        self.ow_label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_13.setFont(font)
        self.ow_label_13.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_13.setText("")
        self.ow_label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_13.setObjectName("ow_label_13")
        self.gridLayout_4.addWidget(self.ow_label_13, 1, 1, 1, 1)
        self.ow_label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_11.setMinimumSize(QtCore.QSize(0, 40))
        self.ow_label_11.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_11.setFont(font)
        self.ow_label_11.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_11.setObjectName("ow_label_11")
        self.gridLayout_4.addWidget(self.ow_label_11, 1, 0, 1, 1)
        self.ow_label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_14.setMinimumSize(QtCore.QSize(250, 40))
        self.ow_label_14.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_14.setFont(font)
        self.ow_label_14.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_14.setText("")
        self.ow_label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_14.setObjectName("ow_label_14")
        self.gridLayout_4.addWidget(self.ow_label_14, 2, 1, 1, 1)
        self.ow_label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_12.setMinimumSize(QtCore.QSize(0, 40))
        self.ow_label_12.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_12.setFont(font)
        self.ow_label_12.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_12.setObjectName("ow_label_12")
        self.gridLayout_4.addWidget(self.ow_label_12, 2, 0, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout_4)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ow_label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_15.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_15.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_15.setFont(font)
        self.ow_label_15.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_15.setObjectName("ow_label_15")
        self.horizontalLayout_11.addWidget(self.ow_label_15)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.ow_label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_16.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_16.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
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
        self.ow_line_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.ow_line_5.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_line_5.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_5.setFont(font)
        self.ow_line_5.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_5.setText("")
        self.ow_line_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_line_5.setObjectName("ow_line_5")
        self.horizontalLayout_12.addWidget(self.ow_line_5)
        self.ow_label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.ow_label_17.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_17.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
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
        self.ow_edit_bt_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_3)
        self.ow_edit_bt_4.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_4.setMaximumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_4.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_4.setText("")
        self.ow_edit_bt_4.setIcon(icon1)
        self.ow_edit_bt_4.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_4.setObjectName("ow_edit_bt_4")
        self.horizontalLayout_12.addWidget(self.ow_edit_bt_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.ow_vertical_layout_3.addLayout(self.horizontalLayout_12)
        self.gridLayout_8.addLayout(self.ow_vertical_layout_3, 0, 0, 1, 1)
        self.ow_scroll_area_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_9.addWidget(self.ow_scroll_area_3, 0, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_2.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ow_scroll_area_2 = QtWidgets.QScrollArea(self.page_4)
        self.ow_scroll_area_2.setStyleSheet("QScrollArea { background: transparent; }\n"
"\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"")
        self.ow_scroll_area_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ow_scroll_area_2.setWidgetResizable(True)
        self.ow_scroll_area_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ow_scroll_area_2.setObjectName("ow_scroll_area_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 419, 333))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ow_vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.ow_vertical_layout_2.setObjectName("ow_vertical_layout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ow_label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_6.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_6.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_6.setFont(font)
        self.ow_label_6.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_6.setObjectName("ow_label_6")
        self.horizontalLayout_4.addWidget(self.ow_label_6)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ow_label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_7.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_7.setFont(font)
        self.ow_label_7.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_7.setObjectName("ow_label_7")
        self.gridLayout.addWidget(self.ow_label_7, 0, 2, 1, 1)
        self.ow_label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_8.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_8.setFont(font)
        self.ow_label_8.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_8.setObjectName("ow_label_8")
        self.gridLayout.addWidget(self.ow_label_8, 1, 2, 1, 1)
        self.ow_label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_4.setMinimumSize(QtCore.QSize(0, 55))
        self.ow_label_4.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_4.setFont(font)
        self.ow_label_4.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_4.setWordWrap(True)
        self.ow_label_4.setObjectName("ow_label_4")
        self.gridLayout.addWidget(self.ow_label_4, 0, 0, 1, 1)
        self.ow_label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_5.setMinimumSize(QtCore.QSize(0, 60))
        self.ow_label_5.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_5.setFont(font)
        self.ow_label_5.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_5.setWordWrap(True)
        self.ow_label_5.setObjectName("ow_label_5")
        self.gridLayout.addWidget(self.ow_label_5, 1, 0, 1, 1)
        self.ow_line_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ow_line_2.setMinimumSize(QtCore.QSize(50, 40))
        self.ow_line_2.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_2.setFont(font)
        self.ow_line_2.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_2.setText("")
        self.ow_line_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_line_2.setObjectName("ow_line_2")
        self.gridLayout.addWidget(self.ow_line_2, 0, 1, 1, 1)
        self.ow_line_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ow_line_3.setMinimumSize(QtCore.QSize(50, 40))
        self.ow_line_3.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_3.setFont(font)
        self.ow_line_3.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_3.setText("")
        self.ow_line_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_line_3.setObjectName("ow_line_3")
        self.gridLayout.addWidget(self.ow_line_3, 1, 1, 1, 1)
        self.ow_edit_bt_1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_edit_bt_1.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_1.setMaximumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_1.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_1.setText("")
        self.ow_edit_bt_1.setIcon(icon1)
        self.ow_edit_bt_1.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_1.setObjectName("ow_edit_bt_1")
        self.gridLayout.addWidget(self.ow_edit_bt_1, 0, 3, 1, 1)
        self.ow_edit_bt_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_edit_bt_2.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_2.setMaximumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_2.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_2.setText("")
        self.ow_edit_bt_2.setIcon(icon1)
        self.ow_edit_bt_2.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_2.setObjectName("ow_edit_bt_2")
        self.gridLayout.addWidget(self.ow_edit_bt_2, 1, 3, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        spacerItem14 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.ow_label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_21.setMinimumSize(QtCore.QSize(0, 27))
        self.ow_label_21.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setItalic(True)
        font.setUnderline(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_21.setFont(font)
        self.ow_label_21.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_21.setObjectName("ow_label_21")
        self.horizontalLayout_15.addWidget(self.ow_label_21)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.ow_label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_18.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_18.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_18.setFont(font)
        self.ow_label_18.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_18.setObjectName("ow_label_18")
        self.gridLayout_11.addWidget(self.ow_label_18, 0, 2, 1, 1)
        self.ow_label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_19.setMinimumSize(QtCore.QSize(0, 50))
        self.ow_label_19.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_19.setFont(font)
        self.ow_label_19.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ow_label_19.setObjectName("ow_label_19")
        self.gridLayout_11.addWidget(self.ow_label_19, 1, 2, 1, 1)
        self.ow_label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_20.setMinimumSize(QtCore.QSize(0, 55))
        self.ow_label_20.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_20.setFont(font)
        self.ow_label_20.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_20.setWordWrap(True)
        self.ow_label_20.setObjectName("ow_label_20")
        self.gridLayout_11.addWidget(self.ow_label_20, 0, 0, 1, 1)
        self.ow_label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.ow_label_22.setMinimumSize(QtCore.QSize(0, 60))
        self.ow_label_22.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_label_22.setFont(font)
        self.ow_label_22.setStyleSheet("QLabel {\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_label_22.setWordWrap(True)
        self.ow_label_22.setObjectName("ow_label_22")
        self.gridLayout_11.addWidget(self.ow_label_22, 1, 0, 1, 1)
        self.ow_line_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ow_line_6.setMinimumSize(QtCore.QSize(50, 40))
        self.ow_line_6.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_6.setFont(font)
        self.ow_line_6.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_6.setText("")
        self.ow_line_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_line_6.setObjectName("ow_line_6")
        self.gridLayout_11.addWidget(self.ow_line_6, 0, 1, 1, 1)
        self.ow_line_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ow_line_8.setMinimumSize(QtCore.QSize(50, 40))
        self.ow_line_8.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_line_8.setFont(font)
        self.ow_line_8.setStyleSheet("QLineEdit {\n"
"    border-radius: 3px;\n"
"    padding: 1px 4px 1px 4px;\n"
"    background-color:  rgb(240, 240, 240);\n"
"    color: rgb(45,45,45);\n"
"}")
        self.ow_line_8.setText("")
        self.ow_line_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ow_line_8.setObjectName("ow_line_8")
        self.gridLayout_11.addWidget(self.ow_line_8, 1, 1, 1, 1)
        self.ow_edit_bt_6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_edit_bt_6.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_6.setMaximumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_6.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_6.setText("")
        self.ow_edit_bt_6.setIcon(icon1)
        self.ow_edit_bt_6.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_6.setObjectName("ow_edit_bt_6")
        self.gridLayout_11.addWidget(self.ow_edit_bt_6, 0, 3, 1, 1)
        self.ow_edit_bt_7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        self.ow_edit_bt_7.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_7.setMaximumSize(QtCore.QSize(50, 50))
        self.ow_edit_bt_7.setStyleSheet("QToolButton {\n"
"    border: 1px solid transparent;\n"
"    background-color: transparent;\n"
"    width: 27px;\n"
"    height: 27px;\n"
"}\n"
"\n"
"QToolButton:flat {\n"
"    border: none;\n"
"}")
        self.ow_edit_bt_7.setText("")
        self.ow_edit_bt_7.setIcon(icon1)
        self.ow_edit_bt_7.setIconSize(QtCore.QSize(36, 36))
        self.ow_edit_bt_7.setObjectName("ow_edit_bt_7")
        self.gridLayout_11.addWidget(self.ow_edit_bt_7, 1, 3, 1, 1)
        self.horizontalLayout_13.addLayout(self.gridLayout_11)
        spacerItem17 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem17)
        self.ow_vertical_layout_2.addLayout(self.horizontalLayout_13)
        self.gridLayout_7.addLayout(self.ow_vertical_layout_2, 0, 0, 1, 1)
        self.ow_scroll_area_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.ow_scroll_area_2, 1, 0, 1, 1)
        self.ow_stacked_widget.addWidget(self.page_4)
        self.gridLayout_13.addWidget(self.ow_splitter, 0, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_13.addItem(spacerItem18, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ow_ok_button = QtWidgets.QToolButton(optionWindow)
        self.ow_ok_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ow_ok_button.sizePolicy().hasHeightForWidth())
        self.ow_ok_button.setSizePolicy(sizePolicy)
        self.ow_ok_button.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_ok_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_ok_button.setFont(font)
        self.ow_ok_button.setStyleSheet("QToolButton {\n"
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
        self.ow_ok_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/validate_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_ok_button.setIcon(icon3)
        self.ow_ok_button.setIconSize(QtCore.QSize(45, 45))
        self.ow_ok_button.setObjectName("ow_ok_button")
        self.horizontalLayout_2.addWidget(self.ow_ok_button)
        spacerItem19 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem19)
        self.ow_cancel_button = QtWidgets.QToolButton(optionWindow)
        self.ow_cancel_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ow_cancel_button.sizePolicy().hasHeightForWidth())
        self.ow_cancel_button.setSizePolicy(sizePolicy)
        self.ow_cancel_button.setMinimumSize(QtCore.QSize(50, 50))
        self.ow_cancel_button.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ow_cancel_button.setFont(font)
        self.ow_cancel_button.setStyleSheet("QToolButton {\n"
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
        self.ow_cancel_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/del_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ow_cancel_button.setIcon(icon4)
        self.ow_cancel_button.setIconSize(QtCore.QSize(45, 45))
        self.ow_cancel_button.setObjectName("ow_cancel_button")
        self.horizontalLayout_2.addWidget(self.ow_cancel_button)
        spacerItem20 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.gridLayout_13.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(optionWindow)
        self.ow_stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "Options"))
        __sortingEnabled = self.ow_section_list.isSortingEnabled()
        self.ow_section_list.setSortingEnabled(False)
        item = self.ow_section_list.item(0)
        item.setText(_translate("optionWindow", "Calculs"))
        item = self.ow_section_list.item(1)
        item.setText(_translate("optionWindow", "Log"))
        item = self.ow_section_list.item(2)
        item.setText(_translate("optionWindow", "Météo-France"))
        item = self.ow_section_list.item(3)
        item.setText(_translate("optionWindow", "Système"))
        self.ow_section_list.setSortingEnabled(__sortingEnabled)
        self.ow_label_32.setText(_translate("optionWindow", "Calcul pression au niveau de la mer :"))
        self.ow_label_33.setText(_translate("optionWindow", "Altitude :"))
        self.ow_label_34.setText(_translate("optionWindow", "mètres"))
        self.ow_label_1.setText(_translate("optionWindow", "Options de log :"))
        self.ow_label_3.setText(_translate("optionWindow", "Chemin du log :"))
        self.ow_label_2.setText(_translate("optionWindow", "Niveau de log :"))
        self.ow_combobox_1.setItemText(0, _translate("optionWindow", "DEBUG"))
        self.ow_combobox_1.setItemText(1, _translate("optionWindow", "INFO"))
        self.ow_combobox_1.setItemText(2, _translate("optionWindow", "WARNING"))
        self.ow_combobox_1.setItemText(3, _translate("optionWindow", "CRITICAL"))
        self.ow_combobox_1.setItemText(4, _translate("optionWindow", "ERROR"))
        self.ow_label_9.setText(_translate("optionWindow", "Rechercher une ville :"))
        self.ow_search_button.setText(_translate("optionWindow", "Rechercher"))
        self.ow_label_10.setText(_translate("optionWindow", "Ville :"))
        self.ow_label_11.setText(_translate("optionWindow", "Code postal :"))
        self.ow_label_12.setText(_translate("optionWindow", "Département :"))
        self.ow_label_15.setText(_translate("optionWindow", "Requête des prévisions météo:"))
        self.ow_label_16.setText(_translate("optionWindow", "Intervalle :"))
        self.ow_label_17.setText(_translate("optionWindow", "minutes"))
        self.ow_label_6.setText(_translate("optionWindow", "Capteur intérieur :"))
        self.ow_label_7.setText(_translate("optionWindow", "secondes"))
        self.ow_label_8.setText(_translate("optionWindow", "secondes"))
        self.ow_label_4.setText(_translate("optionWindow", "Rafraichissement des sondes :"))
        self.ow_label_5.setText(_translate("optionWindow", "Rafraichissement de l\'affichage :"))
        self.ow_label_21.setText(_translate("optionWindow", "Capteur extérieur :"))
        self.ow_label_18.setText(_translate("optionWindow", "secondes"))
        self.ow_label_19.setText(_translate("optionWindow", "secondes"))
        self.ow_label_20.setText(_translate("optionWindow", "Rafraichissement des sondes :"))
        self.ow_label_22.setText(_translate("optionWindow", "Rafraichissement de l\'affichage :"))
