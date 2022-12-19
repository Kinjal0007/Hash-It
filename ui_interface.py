# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceKmqGGS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1238, 804)
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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/icons/Icon/placeholder.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.frame = QFrame(self.page)
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
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setReadOnly(False)

        self.verticalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.checkBox = QCheckBox(self.page)
        self.checkBox.setObjectName(u"checkBox")
        font3 = QFont()
        font3.setPointSize(9)
        self.checkBox.setFont(font3)

        self.verticalLayout_3.addWidget(self.checkBox, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font2)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setUnderline(True)
        self.pushButton_2.setFont(font4)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 441, 356, 41))
        self.pushButton_3.setFont(font4)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(46, 185, 264, 24))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(114, 138, 128, 40))
        self.label_6.setFont(font)
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 230, 356, 131))
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
        self.lineEdit_11.setDragEnabled(False)
        self.lineEdit_11.setReadOnly(False)

        self.verticalLayout_7.addWidget(self.lineEdit_11)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 393, 356, 41))
        self.pushButton_4.setFont(font2)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 0, 171, 131))
        self.label_7.setPixmap(QPixmap(u":/icons/Icon/check-user-logo-icon-design-vector-22953776.jpg"))
        self.label_7.setScaledContents(True)
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 489, 75, 18))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)

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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Already registered? Login", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hash It Pvt", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Not registered? Register", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Enter Your Information Below", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hash It Pvt", None))
    # retranslateUi

