# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算器.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(462, 507)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton_back = QPushButton(Form)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.verticalLayout.addWidget(self.pushButton_back)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.pushButton_div = QPushButton(Form)
        self.pushButton_div.setObjectName(u"pushButton_div")

        self.horizontalLayout.addWidget(self.pushButton_div)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_mul = QPushButton(Form)
        self.pushButton_mul.setObjectName(u"pushButton_mul")

        self.horizontalLayout_2.addWidget(self.pushButton_mul)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_sub = QPushButton(Form)
        self.pushButton_sub.setObjectName(u"pushButton_sub")

        self.horizontalLayout_3.addWidget(self.pushButton_sub)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.horizontalLayout_4.addWidget(self.pushButton_0)

        self.pushButton_dot = QPushButton(Form)
        self.pushButton_dot.setObjectName(u"pushButton_dot")

        self.horizontalLayout_4.addWidget(self.pushButton_dot)

        self.pushButton_enter = QPushButton(Form)
        self.pushButton_enter.setObjectName(u"pushButton_enter")

        self.horizontalLayout_4.addWidget(self.pushButton_enter)

        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.horizontalLayout_4.addWidget(self.pushButton_add)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_clear = QPushButton(Form)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.verticalLayout_2.addWidget(self.pushButton_clear)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"\u56de\u9000", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_mul.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_enter.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
    # retranslateUi

