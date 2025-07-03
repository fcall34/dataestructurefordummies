# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuArboles.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #D8BFD8;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 30, 541, 41))
        font = QFont()
        font.setFamilies([u"Caprasimo"])
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 30, 531, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: transparent;color:black")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 140, 301, 321))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/arbol.png"))
        self.label_3.setScaledContents(True)
        self.ARBOLESBINARIOS = QPushButton(self.centralwidget)
        self.ARBOLESBINARIOS.setObjectName(u"ARBOLESBINARIOS")
        self.ARBOLESBINARIOS.setGeometry(QRect(420, 130, 321, 91))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(20)
        self.ARBOLESBINARIOS.setFont(font1)
        self.ARBOLESBINARIOS.setStyleSheet(u"background-color:blank;")
        self.ARBOLESAUTOBALANCEADOS = QPushButton(self.centralwidget)
        self.ARBOLESAUTOBALANCEADOS.setObjectName(u"ARBOLESAUTOBALANCEADOS")
        self.ARBOLESAUTOBALANCEADOS.setGeometry(QRect(420, 250, 321, 91))
        self.ARBOLESAUTOBALANCEADOS.setFont(font1)
        self.ARBOLESAUTOBALANCEADOS.setStyleSheet(u"background-color:blank;")
        self.ATRAS = QPushButton(self.centralwidget)
        self.ATRAS.setObjectName(u"ATRAS")
        self.ATRAS.setGeometry(QRect(510, 370, 141, 81))
        self.ATRAS.setFont(font1)
        self.ATRAS.setStyleSheet(u"background-color:blank;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.ARBOLESBINARIOS.raise_()
        self.ARBOLESAUTOBALANCEADOS.raise_()
        self.ATRAS.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ARBOLES BINARIOS", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ARBOLES BINARIOS", None))
        self.label_3.setText("")
        self.ARBOLESBINARIOS.setText(QCoreApplication.translate("MainWindow", u"ARBOLES BINARIOS \n"
"DE BUSQUEDA", None))
        self.ARBOLESAUTOBALANCEADOS.setText(QCoreApplication.translate("MainWindow", u"ARBOLES BINARIOS \n"
"AUTOBALANCEADOS", None))
        self.ATRAS.setText(QCoreApplication.translate("MainWindow", u"ATRAS", None))
    # retranslateUi

