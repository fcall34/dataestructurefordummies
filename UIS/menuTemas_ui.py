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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MenuTemas(object):
    def setupUi(self, MenuTemas):
        if not MenuTemas.objectName():
            MenuTemas.setObjectName(u"MenuTemas")
        MenuTemas.resize(800, 600)
        MenuTemas.setStyleSheet(u"background-color: #D8BFD8;")
        self.centralwidget = QWidget(MenuTemas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnListas = QPushButton(self.centralwidget)
        self.btnListas.setObjectName(u"btnListas")
        self.btnListas.setGeometry(QRect(590, 350, 151, 71))
        font = QFont()
        font.setFamilies([u"Caprasimo"])
        font.setPointSize(12)
        self.btnListas.setFont(font)
        self.btnListas.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.btnArboles = QPushButton(self.centralwidget)
        self.btnArboles.setObjectName(u"btnArboles")
        self.btnArboles.setGeometry(QRect(400, 170, 161, 71))
        self.btnArboles.setFont(font)
        self.btnArboles.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.btnHash = QPushButton(self.centralwidget)
        self.btnHash.setObjectName(u"btnHash")
        self.btnHash.setGeometry(QRect(400, 260, 161, 71))
        self.btnHash.setFont(font)
        self.btnHash.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.btnGrafos = QPushButton(self.centralwidget)
        self.btnGrafos.setObjectName(u"btnGrafos")
        self.btnGrafos.setGeometry(QRect(590, 170, 151, 71))
        self.btnGrafos.setFont(font)
        self.btnGrafos.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.btnOrdenamiento = QPushButton(self.centralwidget)
        self.btnOrdenamiento.setObjectName(u"btnOrdenamiento")
        self.btnOrdenamiento.setGeometry(QRect(590, 260, 151, 71))
        self.btnOrdenamiento.setFont(font)
        self.btnOrdenamiento.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.btnStrassen = QPushButton(self.centralwidget)
        self.btnStrassen.setObjectName(u"btnStrassen")
        self.btnStrassen.setGeometry(QRect(400, 350, 161, 71))
        self.btnStrassen.setFont(font)
        self.btnStrassen.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 541, 141))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(36)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 20, 531, 141))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: transparent;color:black")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 160, 301, 271))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/compu.png"))
        self.label_3.setScaledContents(True)
        self.btnSalir = QPushButton(self.centralwidget)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setGeometry(QRect(320, 460, 161, 71))
        self.btnSalir.setFont(font)
        self.btnSalir.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        MenuTemas.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.btnListas.raise_()
        self.btnArboles.raise_()
        self.btnHash.raise_()
        self.btnGrafos.raise_()
        self.btnOrdenamiento.raise_()
        self.btnStrassen.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.btnSalir.raise_()
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
        self.label.setText(QCoreApplication.translate("MenuTemas", u"DATA STRUCTURE \n"
"FOR DUMMIES", None))
        self.label_2.setText(QCoreApplication.translate("MenuTemas", u"DATA STRUCTURE \n"
"FOR DUMMIES", None))
        self.label_3.setText("")
        self.btnSalir.setText(QCoreApplication.translate("MenuTemas", u"SALIR", None))
    # retranslateUi

