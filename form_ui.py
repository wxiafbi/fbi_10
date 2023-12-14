# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QMdiArea, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 60, 181, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(162, 255, 41);")
        self.lcdNumber = QLCDNumber(Widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(440, 60, 131, 51))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 60, 75, 24))
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(610, 90, 75, 24))
        self.mdiArea = QMdiArea(Widget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(160, 330, 200, 160))
        self.subwindow = QWidget()
        self.subwindow.setObjectName(u"subwindow")
        self.mdiArea.addSubWindow(self.subwindow)
        self.lcdNumber_2 = QLCDNumber(Widget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(260, 210, 431, 51))

        self.retranslateUi(Widget)
        self.pushButton_2.clicked.connect(Widget.add)
        self.pushButton_3.clicked.connect(Widget.red)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u81ea\u589e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u81ea\u51cf", None))
        self.subwindow.setWindowTitle(QCoreApplication.translate("Widget", u"\u5b50\u7a97\u53e3", None))
    # retranslateUi

