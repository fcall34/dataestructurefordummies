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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(816, 751)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(85, 0, 255);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 0, 201, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 801, 321))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 470, 441, 71))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setItalic(False)
        self.label_4.setFont(font2)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 400, 251, 261))
        self.label_3.setPixmap(QPixmap(u"../Sources/Images/Sillas Circulares.jpeg"))
        self.label_3.setScaledContents(True)
        StackedWidget.addWidget(self.page)

        self.retranslateUi(StackedWidget)

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
"\n"
"No hay \"principio\" ni \"final\":\n"
"En una fila normal, hay una primera silla y una \u00faltima.\n"
"\n"
"En el c\u00edrculo, no hay \u00faltimo, porque despu\u00e9s de la \u00faltima... \u00a1vuelves al principio!\n"
"\n"
"\u00bfC\u00f3mo recorremos las sillas?\n"
"Si empiezas en una silla y vas pasando, nunca terminas, porque siempre hay una siguiente.\n"
"\n"
"Es como un bucle infinito (pero controlado, porque sabemos cu\u00e1ntas sillas hay).", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Por ejemplo:\n"
"\n"
"Si est\u00e1s en la Silla 4, la siguiente es la Silla 5, luego la Silla 1, luego la Silla 2, y as\u00ed...", None))
        self.label_3.setText("")
    # retranslateUi

