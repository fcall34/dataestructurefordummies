# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ordenamiento.ui'
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
        self.label.setGeometry(QRect(140, -10, 551, 91))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.QUICKSORT = QPushButton(self.centralwidget)
        self.QUICKSORT.setObjectName(u"QUICKSORT")
        self.QUICKSORT.setGeometry(QRect(130, 170, 141, 61))
        self.QUICKSORT.setStyleSheet(u"background-color: black;\n"
"")
        self.MERGESORT = QPushButton(self.centralwidget)
        self.MERGESORT.setObjectName(u"MERGESORT")
        self.MERGESORT.setGeometry(QRect(520, 170, 141, 61))
        self.MERGESORT.setStyleSheet(u"background-color: black;\n"
"")
        self.HEAPSORT = QPushButton(self.centralwidget)
        self.HEAPSORT.setObjectName(u"HEAPSORT")
        self.HEAPSORT.setGeometry(QRect(520, 330, 141, 61))
        self.HEAPSORT.setStyleSheet(u"background-color: black;\n"
"")
        self.COUNTINGSORT = QPushButton(self.centralwidget)
        self.COUNTINGSORT.setObjectName(u"COUNTINGSORT")
        self.COUNTINGSORT.setGeometry(QRect(130, 330, 141, 61))
        self.COUNTINGSORT.setStyleSheet(u"background-color: black;\n"
"")
        self.ATRAS = QPushButton(self.centralwidget)
        self.ATRAS.setObjectName(u"ATRAS")
        self.ATRAS.setGeometry(QRect(700, 520, 75, 24))
        self.ATRAS.setStyleSheet(u"background-color:black;\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"METODOS DE ORDENAMIENTO", None))
        self.QUICKSORT.setText(QCoreApplication.translate("MainWindow", u"QUICKSORT", None))
        self.MERGESORT.setText(QCoreApplication.translate("MainWindow", u"MERGE SORT", None))
        self.HEAPSORT.setText(QCoreApplication.translate("MainWindow", u"HEAP SORT", None))
        self.COUNTINGSORT.setText(QCoreApplication.translate("MainWindow", u"COUNTING SORT", None))
        self.ATRAS.setText(QCoreApplication.translate("MainWindow", u"ATRAS", None))
    # retranslateUi

