# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fillprofile.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import placeholder_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet(u"QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 50, 471, 71))
        self.label.setStyleSheet(u"font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 140, 761, 41))
        self.label_2.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.signup = QPushButton(self.bgwidget)
        self.signup.setObjectName(u"signup")
        self.signup.setGeometry(QRect(430, 650, 341, 51))
        self.signup.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.username = QLineEdit(self.bgwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(180, 370, 341, 51))
        self.username.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.firstname = QLineEdit(self.bgwidget)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(180, 450, 341, 51))
        self.firstname.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(self.bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 370, 81, 20))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(self.bgwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 450, 81, 20))
        self.label_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.error = QLabel(self.bgwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(440, 456, 341, 20))
        self.error.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.label_5 = QLabel(self.bgwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 450, 81, 20))
        self.label_5.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.lastname = QLineEdit(self.bgwidget)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(680, 450, 341, 51))
        self.lastname.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.birthday = QDateEdit(self.bgwidget)
        self.birthday.setObjectName(u"birthday")
        self.birthday.setGeometry(QRect(180, 530, 341, 51))
        self.birthday.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_6 = QLabel(self.bgwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 530, 81, 20))
        self.label_6.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.image = QLabel(self.bgwidget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(80, 190, 151, 141))
        self.image.setStyleSheet(u"border-radius:50%;")
        self.image.setScaledContents(True)
        self.pushButton = QPushButton(self.bgwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 200, 93, 28))
        self.pushButton.setStyleSheet(u"border-color: rgb(85, 0, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.comboBox = QComboBox(self.bgwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(680, 530, 111, 51))
        self.comboBox.setStyleSheet(u"border-color: rgb(0, 0, 127);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8 = QLabel(self.bgwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(580, 530, 81, 20))
        self.label_8.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Fill in your profile", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Now that you've created an account, please fill in your profile.", None))
        self.signup.setText(QCoreApplication.translate("Dialog", u"Continue", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.error.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Birthday", None))
        self.image.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Upload ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Man", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Woman", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Non-binary", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))

        self.label_8.setText(QCoreApplication.translate("Dialog", u"Gender", None))
    # retranslateUi

