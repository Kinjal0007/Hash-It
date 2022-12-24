# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcomescreen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1201, 800)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1201, 801))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0.011, x2:0.98005, y2:1, stop:0.308458 rgb(255, 130, 212), stop:0.885572 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 90, 421, 81))
        self.label.setStyleSheet(u"font: 90 45pt \"Segoe Print\";color:rgbrgb(0, 0, 0);\n"
"text-decoration: underline;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 240, 621, 71))
        self.label_2.setStyleSheet(u"font: 75 26pt \"Sitka Subheading\";")
        self.create = QPushButton(self.widget)
        self.create.setObjectName(u"create")
        self.create.setGeometry(QRect(400, 520, 381, 51))
        self.create.setStyleSheet(u"border-radius:20px;\n"
"font: 75 24pt \"Times New Roman\";\n"
"background-color:rgb(32, 237, 255);")
        self.login = QPushButton(self.widget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(400, 420, 381, 51))
        self.login.setStyleSheet(u"border-radius:20px;\n"
"font: 75 24pt \"Times New Roman\";\n"
"background-color:rgb(32, 237, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"WELCOME", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"SIGN IN OR CREATE ACCOUNT:-", None))
        self.create.setText(QCoreApplication.translate("Dialog", u"Create a New Account", None))
        self.login.setText(QCoreApplication.translate("Dialog", u"Log In", None))
    # retranslateUi

