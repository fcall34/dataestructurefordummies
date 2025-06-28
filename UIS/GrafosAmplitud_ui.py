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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_GrafosAmplitud(object):
    def setupUi(self, GrafosAmplitud):
        if not GrafosAmplitud.objectName():
            GrafosAmplitud.setObjectName(u"GrafosAmplitud")
        GrafosAmplitud.resize(815, 559)
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
        self.label_6.setPixmap(QPixmap(u"../Sources/Images/Tipos-Grafos.png"))
        self.btnVolver = QPushButton(self.page)
        self.btnVolver.setObjectName(u"btnVolver")
        self.btnVolver.setGeometry(QRect(40, 500, 75, 24))
        GrafosAmplitud.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 40, 371, 101))
        self.label.setWordWrap(True)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 140, 501, 321))
        self.label_7.setPixmap(QPixmap(u"../Sources/Images/Camino-grafos.png"))
        self.btnNext = QPushButton(self.page_2)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(680, 490, 75, 24))
        self.btnVolver_2 = QPushButton(self.page_2)
        self.btnVolver_2.setObjectName(u"btnVolver_2")
        self.btnVolver_2.setGeometry(QRect(60, 490, 75, 24))
        GrafosAmplitud.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 80, 141, 16))
        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 40, 231, 16))
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 100, 501, 211))
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 300, 181, 21))
        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 330, 421, 121))
        self.btnNext_2 = QPushButton(self.page_4)
        self.btnNext_2.setObjectName(u"btnNext_2")
        self.btnNext_2.setGeometry(QRect(670, 500, 75, 24))
        GrafosAmplitud.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.vistaGrafo = QGraphicsView(self.page_3)
        self.vistaGrafo.setObjectName(u"vistaGrafo")
        self.vistaGrafo.setGeometry(QRect(15, 21, 771, 471))
        self.vistaGrafo.setStyleSheet(u"background-color: \"grey\"")
        self.btnReiniciar = QPushButton(self.page_3)
        self.btnReiniciar.setObjectName(u"btnReiniciar")
        self.btnReiniciar.setGeometry(QRect(670, 520, 75, 24))
        self.lblRecorridoTerminado = QLabel(self.page_3)
        self.lblRecorridoTerminado.setObjectName(u"lblRecorridoTerminado")
        self.lblRecorridoTerminado.setGeometry(QRect(210, 510, 49, 16))
        GrafosAmplitud.addWidget(self.page_3)

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
        self.btnVolver.setText(QCoreApplication.translate("GrafosAmplitud", u"Volver", None))
        self.label.setText(QCoreApplication.translate("GrafosAmplitud", u"El camino en un grafo se puede representar como el conjutno de vertices recorridos para llegar a un vertice dado", None))
        self.label_7.setText("")
        self.btnNext.setText(QCoreApplication.translate("GrafosAmplitud", u"Siguiente", None))
        self.btnVolver_2.setText(QCoreApplication.translate("GrafosAmplitud", u"Volver", None))
        self.label_8.setText(QCoreApplication.translate("GrafosAmplitud", u"C\u00f3mo Funciona", None))
        self.label_9.setText(QCoreApplication.translate("GrafosAmplitud", u"Recorrido En Amplitud", None))
        self.label_10.setText(QCoreApplication.translate("GrafosAmplitud", u"Se inicia desde un nodo origen.\n"
"\n"
"Se visitan todos los vecinos inmediatos (adyacentes).\n"
"\n"
"Luego se visitan los vecinos de esos vecinos, y as\u00ed sucesivamente.\n"
"\n"
"Utiliza una cola (FIFO) para mantener el orden de visita.\n"
"\n"
"Se marca cada nodo como visitado para evitar ciclos o repeticiones.", None))
        self.label_11.setText(QCoreApplication.translate("GrafosAmplitud", u"Estructuras necesarias", None))
        self.label_12.setText(QCoreApplication.translate("GrafosAmplitud", u"Cola (queue) para almacenar los nodos por visitar.\n"
"\n"
"Conjunto o lista de visitados para evitar repetir nodos.\n"
"\n"
"El grafo, representado como lista de adyacencia o matriz.", None))
        self.btnNext_2.setText(QCoreApplication.translate("GrafosAmplitud", u"Siguiente", None))
        self.btnReiniciar.setText(QCoreApplication.translate("GrafosAmplitud", u"Reiniciar", None))
        self.lblRecorridoTerminado.setText("")
    # retranslateUi

