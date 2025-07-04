# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grafosMenu.ui'
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

class Ui_GrafosWindow(object):
    def setupUi(self, GrafosWindow):
        if not GrafosWindow.objectName():
            GrafosWindow.setObjectName(u"GrafosWindow")
        GrafosWindow.resize(800, 600)
        GrafosWindow.setStyleSheet(u"background-color: rgb(62, 25, 189)")
        self.centralwidget = QWidget(GrafosWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnAmplitud = QPushButton(self.centralwidget)
        self.btnAmplitud.setObjectName(u"btnAmplitud")
        self.btnAmplitud.setGeometry(QRect(50, 110, 151, 61))
        self.btnAmplitud.setStyleSheet(u"background-color: rgb(50, 76, 239)")
        self.btnPrim = QPushButton(self.centralwidget)
        self.btnPrim.setObjectName(u"btnPrim")
        self.btnPrim.setGeometry(QRect(410, 310, 161, 51))
        self.btnPrim.setStyleSheet(u"background-color: rgb(239, 73, 56)")
        self.btnProfundida = QPushButton(self.centralwidget)
        self.btnProfundida.setObjectName(u"btnProfundida")
        self.btnProfundida.setGeometry(QRect(50, 310, 151, 61))
        self.btnProfundida.setStyleSheet(u"background-color: rgb(50, 76, 239)")
        self.btnKruskal = QPushButton(self.centralwidget)
        self.btnKruskal.setObjectName(u"btnKruskal")
        self.btnKruskal.setGeometry(QRect(590, 420, 151, 61))
        self.btnKruskal.setStyleSheet(u"background-color: rgb(239, 73, 56)")
        self.btnBellman = QPushButton(self.centralwidget)
        self.btnBellman.setObjectName(u"btnBellman")
        self.btnBellman.setGeometry(QRect(530, 110, 151, 61))
        self.btnBellman.setStyleSheet(u"background-color: rgb(239, 73, 56)")
        self.btndijkstra = QPushButton(self.centralwidget)
        self.btndijkstra.setObjectName(u"btndijkstra")
        self.btndijkstra.setGeometry(QRect(250, 440, 151, 61))
        self.btndijkstra.setStyleSheet(u"background-color: rgb(50, 76, 239)")
        self.btnFord = QPushButton(self.centralwidget)
        self.btnFord.setObjectName(u"btnFord")
        self.btnFord.setGeometry(QRect(620, 240, 151, 61))
        self.btnFord.setStyleSheet(u"background-color: rgb(239, 73, 56)")
        self.btnFloyd = QPushButton(self.centralwidget)
        self.btnFloyd.setObjectName(u"btnFloyd")
        self.btnFloyd.setGeometry(QRect(280, 30, 151, 61))
        self.btnFloyd.setStyleSheet(u"background-color: rgb(239, 73, 56)")
        self.btnAestrella = QPushButton(self.centralwidget)
        self.btnAestrella.setObjectName(u"btnAestrella")
        self.btnAestrella.setGeometry(QRect(290, 190, 151, 61))
        self.btnAestrella.setStyleSheet(u"background-color: rgb(239, 73, 56)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 30, 241, 21))
        self.label.setStyleSheet(u"font: bold; font-size: 12pt")
        GrafosWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GrafosWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        GrafosWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GrafosWindow)
        self.statusbar.setObjectName(u"statusbar")
        GrafosWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GrafosWindow)

        QMetaObject.connectSlotsByName(GrafosWindow)
    # setupUi

    def retranslateUi(self, GrafosWindow):
        GrafosWindow.setWindowTitle(QCoreApplication.translate("GrafosWindow", u"MainWindow", None))
        self.btnAmplitud.setText(QCoreApplication.translate("GrafosWindow", u"Recorrido en Amplitud", None))
        self.btnPrim.setText(QCoreApplication.translate("GrafosWindow", u"Prim", None))
        self.btnProfundida.setText(QCoreApplication.translate("GrafosWindow", u"Recorrido en profundidad", None))
        self.btnKruskal.setText(QCoreApplication.translate("GrafosWindow", u"Kruskal", None))
        self.btnBellman.setText(QCoreApplication.translate("GrafosWindow", u"Bellman-Ford", None))
        self.btndijkstra.setText(QCoreApplication.translate("GrafosWindow", u"Dijkstra", None))
        self.btnFord.setText(QCoreApplication.translate("GrafosWindow", u"Ford-Fulkerson", None))
        self.btnFloyd.setText(QCoreApplication.translate("GrafosWindow", u"Floyd-Warshall", None))
        self.btnAestrella.setText(QCoreApplication.translate("GrafosWindow", u"A*", None))
        self.label.setText(QCoreApplication.translate("GrafosWindow", u"Sigue la ruta MAS rapida", None))
    # retranslateUi

