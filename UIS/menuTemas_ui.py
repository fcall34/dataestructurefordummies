# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuTemas.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MenuTemas(object):
    def setupUi(self, MenuTemas):
        if not MenuTemas.objectName():
            MenuTemas.setObjectName(u"MenuTemas")
        MenuTemas.resize(800, 600)
        self.centralwidget = QWidget(MenuTemas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnListas = QPushButton(self.centralwidget)
        self.btnListas.setObjectName(u"btnListas")
        self.btnListas.setGeometry(QRect(50, 150, 141, 81))
        self.btnArboles = QPushButton(self.centralwidget)
        self.btnArboles.setObjectName(u"btnArboles")
        self.btnArboles.setGeometry(QRect(330, 150, 141, 81))
        self.btnHash = QPushButton(self.centralwidget)
        self.btnHash.setObjectName(u"btnHash")
        self.btnHash.setGeometry(QRect(190, 280, 141, 85))
        self.btnGrafos = QPushButton(self.centralwidget)
        self.btnGrafos.setObjectName(u"btnGrafos")
        self.btnGrafos.setGeometry(QRect(580, 150, 141, 81))
        self.btnOrdenamiento = QPushButton(self.centralwidget)
        self.btnOrdenamiento.setObjectName(u"btnOrdenamiento")
        self.btnOrdenamiento.setGeometry(QRect(470, 290, 141, 81))
        self.btnStrassen = QPushButton(self.centralwidget)
        self.btnStrassen.setObjectName(u"btnStrassen")
        self.btnStrassen.setGeometry(QRect(340, 410, 141, 81))
        MenuTemas.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MenuTemas)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MenuTemas.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MenuTemas)
        self.statusbar.setObjectName(u"statusbar")
        MenuTemas.setStatusBar(self.statusbar)

        self.retranslateUi(MenuTemas)

        QMetaObject.connectSlotsByName(MenuTemas)
    # setupUi

    def retranslateUi(self, MenuTemas):
        MenuTemas.setWindowTitle(QCoreApplication.translate("MenuTemas", u"MainWindow", None))
        self.btnListas.setText(QCoreApplication.translate("MenuTemas", u"Listas ligadas", None))
        self.btnArboles.setText(QCoreApplication.translate("MenuTemas", u"Arboles", None))
        self.btnHash.setText(QCoreApplication.translate("MenuTemas", u"Tablas Hash", None))
        self.btnGrafos.setText(QCoreApplication.translate("MenuTemas", u"Grafos", None))
        self.btnOrdenamiento.setText(QCoreApplication.translate("MenuTemas", u"Ordenamiento", None))
        self.btnStrassen.setText(QCoreApplication.translate("MenuTemas", u"Metodo Strassen", None))
    # retranslateUi

