# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PILAS.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(747, 579)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        StackedWidget.setFont(font)
        StackedWidget.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 0, 191, 41))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 40, 741, 61))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 130, 241, 291))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/APILAR.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(250, 100, 501, 341))
        self.label_4.setFont(font2)
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setAcceptDrops(False)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        StackedWidget.addWidget(self.page)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"PILAS(STACKS)", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"\u00bfRecuerdas la vez en la que llegabas con tus bros para la reta de tazos? y tu super pro presuminedoles tu nuevo porta tazos, lo que no sabes es que tu porta tazos es una pila y nisiquiera tu te lo esperabas, ahora veras por que lo digo:", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Solo puedes poner o sacar tazo por arriba de tu porta tazos:\n"
"\n"
"Cuando le ganas un tazo a tu contrincante, lo pones encima de la pila de tu porta tazos.\n"
"\n"
"Si tu necesitas sacar un tazo, tomas \u00fanicamente el que esta arriba (no puedes sacar el del medio ni el de hasta abajo).\n"
"\n"
"\u00a1As\u00ed funciona una pila! Solo puedes agregar (push) y sacar (pop) por el top (la parte de arriba).\n"
"\n"
"\"El \u00faltimo que entra, es el primero que sale\" (LIFO):\n"
"\u00bfAh que se refiere esto?\n"
"\n"
"Tienes 3 Tazos: Uno de charizard, pikachu y Bulbasaur.\n"
"El de Bulbasaur es el ultimo que ingresas a tu porta tazos y por ende es el primero que vas a sacar, ya sea para utilizarlo oh llegar a los otros tazos. ", None))
    # retranslateUi

