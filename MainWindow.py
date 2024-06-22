# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.qqButton = QRadioButton(self.centralwidget)
        self.buttonGroup1 = QButtonGroup(MainWindow)
        self.buttonGroup1.setObjectName(u"buttonGroup1")
        self.buttonGroup1.addButton(self.qqButton)
        self.qqButton.setObjectName(u"qqButton")
        self.qqButton.setGeometry(QRect(30, 30, 95, 41))
        self.usernameButton = QRadioButton(self.centralwidget)
        self.buttonGroup1.addButton(self.usernameButton)
        self.usernameButton.setObjectName(u"usernameButton")
        self.usernameButton.setGeometry(QRect(30, 70, 95, 41))
        self.qq = QLineEdit(self.centralwidget)
        self.qq.setObjectName(u"qq")
        self.qq.setGeometry(QRect(120, 40, 113, 21))
        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(120, 80, 113, 21))
        self.b40 = QRadioButton(self.centralwidget)
        self.buttonGroup2 = QButtonGroup(MainWindow)
        self.buttonGroup2.setObjectName(u"buttonGroup2")
        self.buttonGroup2.addButton(self.b40)
        self.b40.setObjectName(u"b40")
        self.b40.setGeometry(QRect(290, 30, 95, 41))
        self.b50 = QRadioButton(self.centralwidget)
        self.buttonGroup2.addButton(self.b50)
        self.b50.setObjectName(u"b50")
        self.b50.setGeometry(QRect(290, 70, 95, 41))
        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(160, 160, 91, 41))
        font = QFont()
        font.setPointSize(16)
        self.generate.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"maimai\u67e5\u5206\u5668", None))
        self.qqButton.setText(QCoreApplication.translate("MainWindow", u"QQ", None))
        self.usernameButton.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.b40.setText(QCoreApplication.translate("MainWindow", u"b40", None))
        self.b50.setText(QCoreApplication.translate("MainWindow", u"b50", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
    # retranslateUi

