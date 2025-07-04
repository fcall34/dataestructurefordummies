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
        ListasWindow.setStyleSheet(u"background-color: #D8BFD8;")
        self.centralwidget = QWidget(ListasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnListasDobles = QPushButton(self.centralwidget)
        self.btnListasDobles.setObjectName(u"btnListasDobles")
        self.btnListasDobles.setGeometry(QRect(470, 330, 191, 81))
        font = QFont()
        font.setFamilies([u"Caprasimo"])
        font.setPointSize(12)
        self.btnListasDobles.setFont(font)
        self.btnListasDobles.setStyleSheet(u"background-color:black;")
        self.btnListasLigadas = QPushButton(self.centralwidget)
        self.btnListasLigadas.setObjectName(u"btnListasLigadas")
        self.btnListasLigadas.setGeometry(QRect(580, 150, 151, 71))
        self.btnListasLigadas.setFont(font)
        self.btnListasLigadas.setStyleSheet(u"background-color:black;")
        self.btnPilas = QPushButton(self.centralwidget)
        self.btnPilas.setObjectName(u"btnPilas")
        self.btnPilas.setGeometry(QRect(400, 150, 161, 71))
        self.btnPilas.setFont(font)
        self.btnPilas.setStyleSheet(u"background-color:black;")
        self.btnListasCirculares = QPushButton(self.centralwidget)
        self.btnListasCirculares.setObjectName(u"btnListasCirculares")
        self.btnListasCirculares.setGeometry(QRect(580, 240, 151, 71))
        self.btnListasCirculares.setFont(font)
        self.btnListasCirculares.setStyleSheet(u"background-color:black;")
        self.btnColas = QPushButton(self.centralwidget)
        self.btnColas.setObjectName(u"btnColas")
        self.btnColas.setGeometry(QRect(400, 240, 161, 71))
        self.btnColas.setFont(font)
        self.btnColas.setStyleSheet(u"background-color:black;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 30, 551, 81))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(33)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:transparent")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 30, 561, 81))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color:transparent;color:black")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 170, 261, 281))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/tren.png"))
        self.label_3.setScaledContents(True)
        self.btnAtras = QPushButton(self.centralwidget)
        self.btnAtras.setObjectName(u"btnAtras")
        self.btnAtras.setGeometry(QRect(490, 430, 161, 81))
        self.btnAtras.setFont(font)
        self.btnAtras.setStyleSheet(u"background-color:black;")
        ListasWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.btnListasDobles.raise_()
        self.btnListasLigadas.raise_()
        self.btnPilas.raise_()
        self.btnListasCirculares.raise_()
        self.btnColas.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.btnAtras.raise_()
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
        self.btnListasDobles.setText(QCoreApplication.translate("ListasWindow", u"Listas doblemente \n"
"enlazadas", None))
        self.btnListasLigadas.setText(QCoreApplication.translate("ListasWindow", u"Listas ligadas \n"
"simples", None))
        self.btnPilas.setText(QCoreApplication.translate("ListasWindow", u"Pilas", None))
        self.btnListasCirculares.setText(QCoreApplication.translate("ListasWindow", u"Listas circulares", None))
        self.btnColas.setText(QCoreApplication.translate("ListasWindow", u"Colas", None))
        self.label.setText(QCoreApplication.translate("ListasWindow", u"LISTAS ,PILAS Y COLAS", None))
        self.label_2.setText(QCoreApplication.translate("ListasWindow", u"LISTAS ,PILAS Y COLAS", None))
        self.label_3.setText("")
        self.btnAtras.setText(QCoreApplication.translate("ListasWindow", u"ATRAS", None))
    # retranslateUi

