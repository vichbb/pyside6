# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '登录框.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(399, 212)
        Form.setWindowOpacity(1.000000000000000)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 140, 51, 20))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 200, 54, 16))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 140, 113, 20))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 200, 113, 20))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 260, 75, 24))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55\u6846", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
    # retranslateUi

