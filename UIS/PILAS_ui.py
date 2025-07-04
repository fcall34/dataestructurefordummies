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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(761, 521)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        StackedWidget.setFont(font)
        StackedWidget.setStyleSheet(u"background-color: rgb(13, 157, 104)\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(13, 157, 104)")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 381, 61))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(32)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:transparent")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 651, 251))
        font2 = QFont()
        font2.setFamilies([u"Caprasimo"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 20, 391, 61))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:transparent;color:black")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 330, 191, 181))
        self.label_6.setPixmap(QPixmap(u"Sources/Images/tazo.png"))
        self.label_6.setScaledContents(True)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(660, 480, 75, 24))
        self.pushButton.setStyleSheet(u"background-color:rgb(1, 80, 51)")
        StackedWidget.addWidget(self.page)
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 140, 221, 271))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/APILAR.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(370, 90, 351, 271))
        self.label_4.setFont(font2)
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setAcceptDrops(False)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 20, 391, 61))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color:transparent;color:black")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(480, 390, 161, 61))
        self.pushButton_2.setStyleSheet(u"background-color:rgb(1, 80, 51)")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 20, 381, 61))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color:transparent")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        StackedWidget.addWidget(self.page_2)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"PILAS(STACKS)", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"\u00bfRecuerdas la vez en la que llegabas con tus bros para la reta de tazos? y tu super pro presuminedoles tu nuevo porta tazos, lo que no sabes es que tu porta tazos es una pila y nisiquiera tu te lo esperabas, ahora veras por que lo digo:Solo puedes poner o sacar tazo por arriba de tu porta tazos:\n"
"\n"
"Cuando le ganas un tazo a tu contrincante, lo pones encima de la pila de tu porta tazos.\n"
"\n"
"Si tu necesitas sacar un tazo, tomas \u00fanicamente el que esta arriba (no puedes sacar el del medio ni el de hasta abajo).\n"
"\n"
"\u00a1As\u00ed funciona una pila! ", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"PILAS(STACKS)", None))
        self.label_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"SIGUIENTE", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Solo puedes agregar (push) y sacar (pop) por el top (la parte de arriba).\n"
"\n"
"\"El \u00faltimo que entra, es el primero que sale\" (LIFO):\n"
"\u00bfAh que se refiere esto?\n"
"\n"
"Tienes 3 Tazos: Uno de charizard, pikachu y Bulbasaur.\n"
"El de Bulbasaur es el ultimo que ingresas a tu porta tazos y por ende es el primero que vas a sacar, ya sea para utilizarlo oh llegar a los otros tazos. ", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"PILAS(STACKS)", None))
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"TERMINADO", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"PILAS(STACKS)", None))
    # retranslateUi

