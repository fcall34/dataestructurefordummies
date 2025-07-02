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
        self.label.setGeometry(QRect(90, 20, 621, 91))
        font = QFont()
        font.setFamilies([u"Caprasimo"])
        font.setPointSize(28)
        font.setBold(False)
        self.label.setFont(font)
        self.QUICKSORT = QPushButton(self.centralwidget)
        self.QUICKSORT.setObjectName(u"QUICKSORT")
        self.QUICKSORT.setGeometry(QRect(560, 110, 191, 81))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(16)
        self.QUICKSORT.setFont(font1)
        self.QUICKSORT.setStyleSheet(u"background-color: black;\n"
"")
        self.MERGESORT = QPushButton(self.centralwidget)
        self.MERGESORT.setObjectName(u"MERGESORT")
        self.MERGESORT.setGeometry(QRect(570, 310, 181, 81))
        self.MERGESORT.setFont(font1)
        self.MERGESORT.setStyleSheet(u"background-color: black;\n"
"")
        self.HEAPSORT = QPushButton(self.centralwidget)
        self.HEAPSORT.setObjectName(u"HEAPSORT")
        self.HEAPSORT.setGeometry(QRect(490, 410, 181, 81))
        self.HEAPSORT.setFont(font1)
        self.HEAPSORT.setStyleSheet(u"background-color: black;\n"
"")
        self.COUNTINGSORT = QPushButton(self.centralwidget)
        self.COUNTINGSORT.setObjectName(u"COUNTINGSORT")
        self.COUNTINGSORT.setGeometry(QRect(470, 210, 211, 81))
        self.COUNTINGSORT.setFont(font1)
        self.COUNTINGSORT.setStyleSheet(u"background-color: black;\n"
"")
        self.ATRAS = QPushButton(self.centralwidget)
        self.ATRAS.setObjectName(u"ATRAS")
        self.ATRAS.setGeometry(QRect(644, 513, 131, 31))
        font2 = QFont()
        font2.setFamilies([u"Caprasimo"])
        self.ATRAS.setFont(font2)
        self.ATRAS.setStyleSheet(u"background-color:black;\n"
"\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 130, 361, 351))
        self.label_2.setPixmap(QPixmap(u"Sources/Images/cubo.png"))
        self.label_2.setScaledContents(True)
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
        self.label_2.setText("")
    # retranslateUi

