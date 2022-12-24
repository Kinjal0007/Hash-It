# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceqPMXFS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import QSS_Resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 835)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background:transparent;\n"
"padding:0;\n"
"margin:0;\n"
"opacity:0.6;\n"
"color:#fff;\n"
"}\n"
"#centralwidget{\n"
"background-color: ;\n"
"\n"
"background-image:url(:/images/Images/abstract-purple-wave-background-dynamic-shapes-composition_467446-11.jpeg);\n"
"}\n"
"#widget{\n"
"background-color:rgb(9,27,68);\n"
"border-radius:20px;\n"
"}\n"
"QLineEdit{\n"
"background-color:rgb(9,10,37);\n"
"padding:5px 3px;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"background-color:rgb(9,10,37);\n"
"padding:10px 5px;\n"
"border-radius:5px;\n"
"}\n"
"#to_login, #to_register{\n"
"	background-color: transparent;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(400, 550))
        self.widget.setMaximumSize(QSize(400, 550))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.registerPage = QWidget()
        self.registerPage.setObjectName(u"registerPage")
        self.verticalLayout_3 = QVBoxLayout(self.registerPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.registerPage)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/Icon/placeholder.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.registerPage)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.registerPage)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.registerPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setPointSize(10)
        self.lineEdit.setFont(font2)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.lineEdit_3)

        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setPointSize(9)
        self.checkBox.setFont(font3)

        self.verticalLayout_4.addWidget(self.checkBox, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.registerBtn = QPushButton(self.registerPage)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setFont(font2)

        self.verticalLayout_3.addWidget(self.registerBtn)

        self.to_login = QPushButton(self.registerPage)
        self.to_login.setObjectName(u"to_login")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setUnderline(True)
        self.to_login.setFont(font4)

        self.verticalLayout_3.addWidget(self.to_login)

        self.label_4 = QLabel(self.registerPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.registerPage)
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.to_register = QPushButton(self.loginPage)
        self.to_register.setObjectName(u"to_register")
        self.to_register.setGeometry(QRect(0, 441, 356, 41))
        self.to_register.setFont(font4)
        self.label_5 = QLabel(self.loginPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 210, 264, 24))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.loginPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(114, 138, 128, 40))
        self.label_6.setFont(font)
        self.frame_2 = QFrame(self.loginPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 230, 371, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lineEdit_10 = QLineEdit(self.frame_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font2)
        self.lineEdit_10.setDragEnabled(False)
        self.lineEdit_10.setReadOnly(False)

        self.verticalLayout_7.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.frame_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font2)
        self.lineEdit_11.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_11.setDragEnabled(False)
        self.lineEdit_11.setReadOnly(False)

        self.verticalLayout_7.addWidget(self.lineEdit_11)

        self.loginBtn = QPushButton(self.loginPage)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(10, 380, 356, 51))
        self.loginBtn.setFont(font2)
        self.label_7 = QLabel(self.loginPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(110, 0, 171, 131))
        self.label_7.setPixmap(QPixmap(u":/icons/Icon/user-check.png"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.loginPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 489, 75, 18))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.loginPage)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirm Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"I've read terms and conditions", None))
        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.to_login.setText(QCoreApplication.translate("MainWindow", u"Already registered? Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hash It Pvt", None))
        self.to_register.setText(QCoreApplication.translate("MainWindow", u"Not registered? Register", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Enter Your information below", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hash It Pvt", None))
    # retranslateUi

