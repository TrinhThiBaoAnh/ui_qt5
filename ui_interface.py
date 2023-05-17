# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacenzphPZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 640)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}\n"
"#header{\n"
"background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"	background-color: #071e26;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"	align: left;\n"
"}\n"
"QComboBox{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"	align: left;\n"
"}\n"
"#main_body{\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}\n"
"#pushButton_view{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_contact{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_config{\n"
"	text-align: left;\n"
"}\n"
"#comboBox{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_xmdt{\n"
"	text-align: left;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1021, 639))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame_3)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(0, 30))
        self.menuButton.setMaximumSize(QSize(16777215, 50))
        self.menuButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Ubuntu Condensed\";")
        self.menuButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menuButton)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 71, 21))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.side_menu = QCustomSlideMenu(self.main_body)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(200, 0))
        self.side_menu.setLayoutDirection(Qt.LeftToRight)
        self.vboxLayout = QVBoxLayout(self.side_menu)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.side_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolBox_3 = QToolBox(self.frame_9)
        self.toolBox_3.setObjectName(u"toolBox_3")
        sizePolicy.setHeightForWidth(self.toolBox_3.sizePolicy().hasHeightForWidth())
        self.toolBox_3.setSizePolicy(sizePolicy)
        self.toolBox_3.setMinimumSize(QSize(200, 40))
        self.toolBox_3.setMaximumSize(QSize(200, 16777215))
        self.toolBox_3.setStyleSheet(u"QToolBox{\n"
"icon-size: 32px;\n"
"border-top:5px;\n"
"background-color: #071e26;\n"
"border-top:15px;\n"
"}\n"
"QToolBox::tab{\n"
"icon-size: 32px;\n"
"border-top:15px;\n"
"background-color: #040f13;\n"
"}")
        self.menu_view_2 = QWidget()
        self.menu_view_2.setObjectName(u"menu_view_2")
        self.menu_view_2.setGeometry(QRect(0, 0, 200, 68))
        icon = QIcon()
        icon.addFile(u":/icons/icons/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_view_2, icon, u"Hi\u1ec3n th\u1ecb")
        self.menu_function_2 = QWidget()
        self.menu_function_2.setObjectName(u"menu_function_2")
        self.menu_function_2.setGeometry(QRect(0, 0, 200, 68))
        self.verticalLayout_7 = QVBoxLayout(self.menu_function_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.button_function = QPushButton(self.menu_function_2)
        self.button_function.setObjectName(u"button_function")
        self.button_function.setMaximumSize(QSize(16777215, 40))
        self.button_function.setStyleSheet(u"text-align: left;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/otp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_function.setIcon(icon1)
        self.button_function.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.button_function)

        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/project-management.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_function_2, icon2, u"Ch\u1ee9c n\u0103ng ch\u00ednh")
        self.menu_config_2 = QWidget()
        self.menu_config_2.setObjectName(u"menu_config_2")
        self.menu_config_2.setGeometry(QRect(0, 0, 200, 68))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/testing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_config_2, icon3, u"C\u1ea5u h\u00ecnh h\u1ec7 th\u1ed1ng")
        self.menu_contact = QWidget()
        self.menu_contact.setObjectName(u"menu_contact")
        self.menu_contact.setGeometry(QRect(0, 0, 200, 68))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/contacts.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_contact, icon4, u"Li\u00ean h\u1ec7")

        self.verticalLayout_5.addWidget(self.toolBox_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.vboxLayout.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.side_menu)

        self.content = QFrame(self.main_body)
        self.content.setObjectName(u"content")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy1)
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: rgb(4, 15, 19);")
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.verticalLayout_4 = QVBoxLayout(self.page_view)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget = QTableWidget(self.page_view)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_view)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.frame_7 = QFrame(self.page_config)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 10, 751, 511))
        self.frame_7.setStyleSheet(u"background-color: rgb(4, 15, 19);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.comboBox_20 = QComboBox(self.frame_7)
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setGeometry(QRect(448, 16, 295, 40))
        self.comboBox_20.setMinimumSize(QSize(0, 40))
        self.comboBox_20.setMaximumSize(QSize(16777215, 40))
        self.comboBox_20.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(392, 10, 50, 53))
        self.label_24.setMinimumSize(QSize(40, 0))
        self.label_24.setMaximumSize(QSize(50, 16777215))
        self.comboBox_19 = QComboBox(self.frame_7)
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setGeometry(QRect(36, 16, 350, 40))
        self.comboBox_19.setMinimumSize(QSize(350, 40))
        self.comboBox_19.setMaximumSize(QSize(350, 40))
        self.comboBox_19.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 10, 20, 53))
        self.label_23.setMinimumSize(QSize(20, 0))
        self.label_23.setMaximumSize(QSize(20, 16777215))
        self.stackedWidget.addWidget(self.page_config)
        self.page_function = QWidget()
        self.page_function.setObjectName(u"page_function")
        self.page_function.setStyleSheet(u"background-color: rgb(4, 15, 19);")
        self.frame_6 = QFrame(self.page_function)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 801, 521))
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setSizeIncrement(QSize(30, 0))
        self.frame_6.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 67, 17))
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 80, 67, 17))
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 130, 81, 17))
        self.comboBox_8 = QComboBox(self.frame_6)
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(110, 20, 351, 40))
        self.comboBox_8.setMinimumSize(QSize(0, 40))
        self.comboBox_8.setMaximumSize(QSize(16777215, 40))
        self.comboBox_8.setSizeIncrement(QSize(0, 0))
        self.comboBox_8.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.comboBox_9 = QComboBox(self.frame_6)
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(110, 70, 131, 40))
        self.comboBox_9.setMinimumSize(QSize(0, 40))
        self.comboBox_9.setMaximumSize(QSize(16777215, 40))
        self.comboBox_9.setSizeIncrement(QSize(0, 0))
        self.comboBox_9.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.radioButton_7 = QRadioButton(self.frame_6)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(90, 130, 151, 16))
        self.radioButton_7.setStyleSheet(u"selection-color: rgb(138, 226, 52);")
        self.comboBox_14 = QComboBox(self.frame_6)
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setGeometry(QRect(480, 20, 261, 40))
        self.comboBox_14.setMinimumSize(QSize(0, 40))
        self.comboBox_14.setMaximumSize(QSize(16777215, 40))
        self.comboBox_14.setSizeIncrement(QSize(0, 0))
        self.comboBox_14.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 170, 81, 17))
        self.comboBox_15 = QComboBox(self.frame_6)
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setGeometry(QRect(110, 160, 631, 40))
        self.comboBox_15.setMinimumSize(QSize(0, 40))
        self.comboBox_15.setMaximumSize(QSize(16777215, 40))
        self.comboBox_15.setSizeIncrement(QSize(30, 0))
        self.comboBox_15.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 80, 31, 17))
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 220, 81, 17))
        self.radioButton_8 = QRadioButton(self.frame_6)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(240, 130, 101, 23))
        self.radioButton_9 = QRadioButton(self.frame_6)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setGeometry(QRect(340, 130, 81, 23))
        self.radioButton_10 = QRadioButton(self.frame_6)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setGeometry(QRect(420, 130, 121, 23))
        self.radioButton_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.radioButton_11 = QRadioButton(self.frame_6)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setGeometry(QRect(540, 130, 121, 23))
        self.radioButton_12 = QRadioButton(self.frame_6)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(660, 130, 91, 23))
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 270, 81, 17))
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 320, 81, 17))
        self.comboBox_16 = QComboBox(self.frame_6)
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setGeometry(QRect(110, 310, 631, 40))
        self.comboBox_16.setMinimumSize(QSize(0, 40))
        self.comboBox_16.setMaximumSize(QSize(16777215, 40))
        self.comboBox_16.setSizeIncrement(QSize(0, 0))
        self.comboBox_16.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.textEdit_4 = QTextEdit(self.frame_6)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(110, 260, 0, 30))
        self.textEdit_4.setMinimumSize(QSize(0, 30))
        self.textEdit_4.setMaximumSize(QSize(16777215, 30))
        self.textEdit_4.setSizeIncrement(QSize(0, 0))
        self.textEdit_5 = QTextEdit(self.frame_6)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setGeometry(QRect(110, 260, 631, 40))
        self.textEdit_5.setMinimumSize(QSize(0, 40))
        self.textEdit_5.setMaximumSize(QSize(16777215, 40))
        self.textEdit_5.setStyleSheet(u"\n"
"background-color: rgb(46, 52, 54);\n"
"")
        self.textEdit_7 = QTextEdit(self.frame_6)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setGeometry(QRect(110, 210, 631, 40))
        self.textEdit_7.setMinimumSize(QSize(0, 40))
        self.textEdit_7.setMaximumSize(QSize(16777215, 40))
        self.textEdit_7.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.textEdit_8 = QTextEdit(self.frame_6)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setGeometry(QRect(290, 70, 451, 40))
        self.textEdit_8.setMinimumSize(QSize(0, 40))
        self.textEdit_8.setMaximumSize(QSize(16777215, 40))
        self.textEdit_8.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.comboBox_6 = QComboBox(self.frame_6)
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(500, 410, 241, 40))
        self.comboBox_6.setMinimumSize(QSize(0, 40))
        self.comboBox_6.setMaximumSize(QSize(16777215, 40))
        self.comboBox_6.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.comboBox_7 = QComboBox(self.frame_6)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(110, 360, 381, 40))
        self.comboBox_7.setMinimumSize(QSize(0, 40))
        self.comboBox_7.setMaximumSize(QSize(16777215, 40))
        self.comboBox_7.setStyleSheet(u"\n"
"background-color: rgb(46, 52, 54);\n"
"")
        self.comboBox_11 = QComboBox(self.frame_6)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setGeometry(QRect(110, 460, 381, 40))
        self.comboBox_11.setMinimumSize(QSize(0, 40))
        self.comboBox_11.setMaximumSize(QSize(16777215, 40))
        self.comboBox_11.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 470, 91, 17))
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 420, 81, 17))
        self.comboBox_12 = QComboBox(self.frame_6)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(110, 410, 381, 40))
        self.comboBox_12.setMinimumSize(QSize(0, 40))
        self.comboBox_12.setMaximumSize(QSize(16777215, 40))
        self.comboBox_12.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.comboBox_13 = QComboBox(self.frame_6)
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setGeometry(QRect(500, 460, 241, 40))
        self.comboBox_13.setMinimumSize(QSize(0, 40))
        self.comboBox_13.setMaximumSize(QSize(16777215, 40))
        self.comboBox_13.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 370, 81, 17))
        self.stackedWidget.addWidget(self.page_function)
        self.page_contact = QWidget()
        self.page_contact.setObjectName(u"page_contact")
        self.frame_8 = QFrame(self.page_contact)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 761, 521))
        self.frame_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(4, 15, 19);\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stackedWidget.addWidget(self.page_contact)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.content)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox_3.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MY APP", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_view_2), QCoreApplication.translate("MainWindow", u"Hi\u1ec3n th\u1ecb", None))
        self.button_function.setText(QCoreApplication.translate("MainWindow", u"G\u1eedi XMDT", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_function_2), QCoreApplication.translate("MainWindow", u"Ch\u1ee9c n\u0103ng ch\u00ednh", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_config_2), QCoreApplication.translate("MainWindow", u"C\u1ea5u h\u00ecnh h\u1ec7 th\u1ed1ng", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_contact), QCoreApplication.translate("MainWindow", u"Li\u00ean h\u1ec7", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Col1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Col2", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"https://m.facebook.com/", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Up Avatar:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Capcha:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OTP Phone:", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"C\u00f3", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Anycapcha", None))

        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Chothuesimcode", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"Capcha Text", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 m\u1ea1ng:", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Key OTP:", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Viotp.com", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Otpmm", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"Codetextnow", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Tempsms.com", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Primeotp", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"List mail:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Get s\u1ed1, mail:", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"3 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))

        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">M\u1edf list hotmail 1</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"G\u1eedi 902 up ph\u00f4i", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh \u1edf ph\u00f4i", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ph\u00f4i", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"6 [Ph\u00f4i Vi\u1ec7t Nam, B\u1eb1ng l\u00e1i A1]", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3u XMDT", None))
    # retranslateUi

