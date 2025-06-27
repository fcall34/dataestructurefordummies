# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listasMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_ListasWindow(object):
    def setupUi(self, ListasWindow):
        if not ListasWindow.objectName():
            ListasWindow.setObjectName(u"ListasWindow")
        ListasWindow.resize(800, 600)
        self.centralwidget = QWidget(ListasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnListasDobles = QPushButton(self.centralwidget)
        self.btnListasDobles.setObjectName(u"btnListasDobles")
        self.btnListasDobles.setGeometry(QRect(290, 110, 161, 91))
        self.btnListasLigadas = QPushButton(self.centralwidget)
        self.btnListasLigadas.setObjectName(u"btnListasLigadas")
        self.btnListasLigadas.setGeometry(QRect(40, 40, 161, 91))
        self.btnPilas = QPushButton(self.centralwidget)
        self.btnPilas.setObjectName(u"btnPilas")
        self.btnPilas.setGeometry(QRect(360, 350, 161, 91))
        self.btnListasCirculares = QPushButton(self.centralwidget)
        self.btnListasCirculares.setObjectName(u"btnListasCirculares")
        self.btnListasCirculares.setGeometry(QRect(530, 210, 161, 91))
        self.btnColas = QPushButton(self.centralwidget)
        self.btnColas.setObjectName(u"btnColas")
        self.btnColas.setGeometry(QRect(90, 280, 161, 91))
        self.listaslabel = QLabel(self.centralwidget)
        self.listaslabel.setObjectName(u"listaslabel")
        self.listaslabel.setGeometry(QRect(510, 50, 191, 61))
        self.listaslabel.setTextFormat(Qt.TextFormat.PlainText)
        self.listaslabel.setIndent(30)
        ListasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ListasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        ListasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ListasWindow)
        self.statusbar.setObjectName(u"statusbar")
        ListasWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListasWindow)

        QMetaObject.connectSlotsByName(ListasWindow)
    # setupUi

    def retranslateUi(self, ListasWindow):
        ListasWindow.setWindowTitle(QCoreApplication.translate("ListasWindow", u"MainWindow", None))
        self.btnListasDobles.setText(QCoreApplication.translate("ListasWindow", u"Listas doblemente enlazadas", None))
        self.btnListasLigadas.setText(QCoreApplication.translate("ListasWindow", u"Listas ligadas simples", None))
        self.btnPilas.setText(QCoreApplication.translate("ListasWindow", u"Pilas", None))
        self.btnListasCirculares.setText(QCoreApplication.translate("ListasWindow", u"Listas circulares", None))
        self.btnColas.setText(QCoreApplication.translate("ListasWindow", u"Colas", None))
        self.listaslabel.setText(QCoreApplication.translate("ListasWindow", u"Sigue el camino recomendado!!", None))
    # retranslateUi

