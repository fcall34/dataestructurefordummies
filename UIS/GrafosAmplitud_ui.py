# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Grafo-Amplitud.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_GrafosAmplitud(object):
    def setupUi(self, GrafosAmplitud):
        if not GrafosAmplitud.objectName():
            GrafosAmplitud.setObjectName(u"GrafosAmplitud")
        GrafosAmplitud.resize(773, 539)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.btnComenzar = QPushButton(self.page)
        self.btnComenzar.setObjectName(u"btnComenzar")
        self.btnComenzar.setGeometry(QRect(680, 500, 75, 24))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 50, 651, 41))
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 110, 571, 71))
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 180, 281, 91))
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 180, 281, 91))
        self.label_5.setWordWrap(True)
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 270, 651, 211))
        self.label_6.setPixmap(QPixmap(u"../../../../Im\u00e1genes/Capturas de pantalla/Screenshot 2025-06-27 221253.png"))
        GrafosAmplitud.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 40, 371, 101))
        self.label.setWordWrap(True)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 160, 501, 321))
        self.label_7.setPixmap(QPixmap(u"../../../../Im\u00e1genes/Capturas de pantalla/Screenshot 2025-06-27 223559.png"))
        self.btnNext = QPushButton(self.page_2)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(680, 490, 75, 24))
        GrafosAmplitud.addWidget(self.page_2)

        self.retranslateUi(GrafosAmplitud)

        GrafosAmplitud.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(GrafosAmplitud)
    # setupUi

    def retranslateUi(self, GrafosAmplitud):
        GrafosAmplitud.setWindowTitle(QCoreApplication.translate("GrafosAmplitud", u"StackedWidget", None))
        self.btnComenzar.setText(QCoreApplication.translate("GrafosAmplitud", u"Siguiente", None))
        self.label_2.setText(QCoreApplication.translate("GrafosAmplitud", u"Recordemos que un grafo es una estrcutra que contiene vertices (Nodos ) y aristas, los cuales pueden o no estar conectados, su relacion se da como G(v,a)", None))
        self.label_3.setText(QCoreApplication.translate("GrafosAmplitud", u"Un arco o arista representa la relacion que existe entre un vertice y otro, esta relacion se da como (u,v), u siendo nuestro nodo actual y v nuestro nodo adyacente o vecino a u", None))
        self.label_4.setText(QCoreApplication.translate("GrafosAmplitud", u"Un grafo puede ser no dirigido, esto es cuando la relacion o arista que une a dos nodos u,v no tiene algun sentido y se representa como u-v", None))
        self.label_5.setText(QCoreApplication.translate("GrafosAmplitud", u"Un grafo dirigido es cuando la relacion entre u y v, tiene una direccion y puede detonarse con una fleche u->v", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("GrafosAmplitud", u"El camino en un grafo se puede representar como el conjutno de vertices recorridos para llegar a un vertice dado", None))
        self.label_7.setText("")
        self.btnNext.setText(QCoreApplication.translate("GrafosAmplitud", u"Siguiente", None))
    # retranslateUi

