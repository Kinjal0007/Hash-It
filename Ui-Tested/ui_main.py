# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1198, 793)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1201, 801))
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color:qlineargradient(spread:repeat, x1:0, y1:0.011, x2:0.98005, y2:1, stop:0.308458 rgb(255, 130, 212), stop:0.885572 rgba(255, 255, 255, 255));}")
        self.error = QLabel(self.widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(390, 530, 371, 41))
        self.error.setStyleSheet(u"\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 0, 0)")
        self.welcome = QLabel(self.widget)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(250, 40, 571, 81))
        self.welcome.setStyleSheet(u"font: 90 40pt \"Segoe Print\";color:rgbrgb(0, 0, 0);\n"
"text-decoration: underline;")
        self.welcome_3 = QLabel(self.widget)
        self.welcome_3.setObjectName(u"welcome_3")
        self.welcome_3.setGeometry(QRect(100, 40, 251, 81))
        self.welcome_3.setStyleSheet(u"font: 90 40pt \"Segoe Print\";color:rgbrgb(0, 0, 0);\n"
"text-decoration: underline;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.error.setText("")
        self.welcome.setText("")
        self.welcome_3.setText(QCoreApplication.translate("Dialog", u"Hey,", None))
    # retranslateUi

