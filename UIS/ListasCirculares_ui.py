# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListasCirculares.ui'
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
        font.setFamilies([u"Caprasimo"])
        font.setPointSize(32)
        StackedWidget.setFont(font)
        StackedWidget.setStyleSheet(u"background-color: rgb(85, 0, 255);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(85, 0, 255);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 391, 41))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(32)
        font1.setBold(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 90, 571, 221))
        font2 = QFont()
        font2.setFamilies([u"Caprasimo"])
        font2.setPointSize(12)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 20, 401, 41))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:transparent;color:black")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnNext = QPushButton(self.page)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(660, 480, 75, 24))
        self.btnNext.setStyleSheet(u"background-color:rgb(50, 7, 100)")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(300, 300, 171, 181))
        self.label_7.setPixmap(QPixmap(u"Sources/Images/silla.png"))
        self.label_7.setScaledContents(True)
        StackedWidget.addWidget(self.page)
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btnNext.raise_()
        self.label_7.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 320, 201, 191))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/Sillas Circulares.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 80, 651, 131))
        font3 = QFont()
        font3.setFamilies([u"Caprasimo"])
        font3.setPointSize(12)
        self.label_6.setFont(font3)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 230, 441, 71))
        font4 = QFont()
        font4.setFamilies([u"Caprasimo"])
        font4.setPointSize(11)
        font4.setItalic(False)
        self.label_4.setFont(font4)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(False)
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 20, 401, 41))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color:transparent;color:black")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 20, 391, 41))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color:transparent;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btnEnd = QPushButton(self.page_2)
        self.btnEnd.setObjectName(u"btnEnd")
        self.btnEnd.setGeometry(QRect(660, 480, 75, 24))
        self.btnEnd.setStyleSheet(u"background-color:rgb(50, 7, 100)")
        StackedWidget.addWidget(self.page_2)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Listas Circulares", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Recuerdas el juego de la silla?, imagina que estas en una competencia jugando el juego de la silla musical, pero, en esta version nunca se acaba el juego porque las sillas est\u00e1n organizadas en un c\u00edrculo y nunca se quita ninguna.\n"
"\n"
"En las sillas musicales normales, las sillas est\u00e1n en una fila y cuando termina la m\u00fasica, alguien se queda sin silla.\n"
"\n"
"Pero en nuestra versi\u00f3n circular, las sillas est\u00e1n pegadas formando un c\u00edrculo, as\u00ed que despu\u00e9s de la \u00faltima silla, \u00a1volvemos a la primera!\n"
"", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Listas Circulares", None))
        self.btnNext.setText(QCoreApplication.translate("StackedWidget", u"SIGUIENTE", None))
        self.label_7.setText("")
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"No hay \"principio\" ni \"final\":\n"
"En una fila normal, hay una primera silla y una \u00faltima.\n"
"En el c\u00edrculo, no hay \u00faltimo, porque despu\u00e9s de la \u00faltima... \u00a1vuelves al principio!\n"
"\u00bfC\u00f3mo recorremos las sillas?\n"
"Si empiezas en una silla y vas pasando, nunca terminas, porque siempre hay una siguiente.\n"
"Es como un bucle infinito (pero controlado, porque sabemos cu\u00e1ntas sillas hay).", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Por ejemplo:\n"
"\n"
"Si est\u00e1s en la Silla 4, la siguiente es la Silla 5, luego la Silla 1, luego la Silla 2, y as\u00ed...", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"Listas Circulares", None))
        self.label_9.setText(QCoreApplication.translate("StackedWidget", u"Listas Circulares", None))
        self.btnEnd.setText(QCoreApplication.translate("StackedWidget", u"TERMINAR", None))
    # retranslateUi

