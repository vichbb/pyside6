# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trans.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(568, 422)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.twoInputEditLine = QLineEdit(Form)
        self.twoInputEditLine.setObjectName(u"twoInputEditLine")
        self.twoInputEditLine.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputEditLine, 4, 2, 1, 1)

        self.oneInputEditLine = QLineEdit(Form)
        self.oneInputEditLine.setObjectName(u"oneInputEditLine")
        self.oneInputEditLine.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.oneInputEditLine, 3, 2, 1, 1)

        self.twoInputComboBox = QComboBox(Form)
        self.twoInputComboBox.setObjectName(u"twoInputComboBox")
        self.twoInputComboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.twoInputComboBox, 4, 3, 1, 1)

        self.oneInputComboBox = QComboBox(Form)
        self.oneInputComboBox.setObjectName(u"oneInputComboBox")
        self.oneInputComboBox.setMinimumSize(QSize(260, 40))

        self.gridLayout.addWidget(self.oneInputComboBox, 3, 3, 1, 1)

        self.originDataLabel = QLabel(Form)
        self.originDataLabel.setObjectName(u"originDataLabel")
        self.originDataLabel.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(12)
        font.setBold(True)
        self.originDataLabel.setFont(font)
        self.originDataLabel.setStyleSheet(u"color: rgb(91, 91, 91);")

        self.gridLayout.addWidget(self.originDataLabel, 0, 2, 1, 1)

        self.transDataLabel = QLabel(Form)
        self.transDataLabel.setObjectName(u"transDataLabel")
        self.transDataLabel.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(29)
        font1.setBold(True)
        self.transDataLabel.setFont(font1)

        self.gridLayout.addWidget(self.transDataLabel, 1, 2, 1, 1)

        self.dataTypeComboBox = QComboBox(Form)
        self.dataTypeComboBox.setObjectName(u"dataTypeComboBox")
        self.dataTypeComboBox.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.dataTypeComboBox, 2, 2, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.calcBtn = QPushButton(Form)
        self.calcBtn.setObjectName(u"calcBtn")
        self.calcBtn.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.calcBtn, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8fdb\u5236\u8f6c\u6362\u5668", None))
        self.originDataLabel.setText(QCoreApplication.translate("Form", u"0=", None))
        self.transDataLabel.setText(QCoreApplication.translate("Form", u"0", None))
        self.calcBtn.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
    # retranslateUi

