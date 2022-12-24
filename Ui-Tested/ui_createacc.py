# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createacc.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

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
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 70, 331, 81))
        self.label.setStyleSheet(u"font: 90 45pt \"Segoe Print\";color:rgbrgb(0, 0, 0);\n"
"text-decoration: underline;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 200, 621, 71))
        self.label_2.setStyleSheet(u"font: 75 26pt \"Sitka Subheading\";")
        self.signup = QPushButton(self.widget)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(390, 620, 381, 51))
        self.signup.setStyleSheet(u"border-radius:20px;\n"
"font: 75 24pt \"Times New Roman\";\n"
"background-color:rgb(32, 237, 255);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(390, 300, 91, 31))
        self.label_3.setStyleSheet(u"font: 75 12pt \"Nirmala UI\";")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(390, 400, 81, 16))
        self.label_4.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.usernamefield = QLineEdit(self.widget)
        self.usernamefield.setObjectName(u"usernamefield")
        self.usernamefield.setGeometry(QRect(390, 330, 381, 51))
        self.usernamefield.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.passwordfield = QLineEdit(self.widget)
        self.passwordfield.setObjectName(u"passwordfield")
        self.passwordfield.setGeometry(QRect(390, 420, 381, 51))
        self.passwordfield.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.error = QLabel(self.widget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(390, 570, 371, 41))
        self.error.setStyleSheet(u"\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color:rgb(255, 0, 0)")
        self.confirmpasswordfield = QLineEdit(self.widget)
        self.confirmpasswordfield.setObjectName(u"confirmpasswordfield")
        self.confirmpasswordfield.setGeometry(QRect(390, 510, 381, 51))
        self.confirmpasswordfield.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 490, 141, 20))
        self.label_5.setStyleSheet(u"\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.success = QLabel(self.widget)
        self.success.setObjectName(u"success")
        self.success.setGeometry(QRect(390, 570, 371, 41))
        self.success.setStyleSheet(u"\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color:rgb(0, 255, 0)")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Register a Brand New Account", None))
        self.signup.setText(QCoreApplication.translate("Dialog", u"SIGN UP", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.error.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
        self.success.setText("")
    # retranslateUi

