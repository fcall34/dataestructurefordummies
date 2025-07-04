# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListaSimplementeEnlazada.ui'
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
        StackedWidget.resize(417, 486)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 0, 291, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 40, 411, 91))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 160, 411, 141))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setWordWrap(True)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 350, 421, 141))
        self.label_4.setPixmap(QPixmap(u"../Sources/Images/ListaSimpleEnlazada.jpeg"))
        self.label_4.setScaledContents(True)
        StackedWidget.addWidget(self.page)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"LISTA SIMPLE ENLAZADA", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Imagina que tenemos un grupo de ni\u00f1os jugando a pasarse un papelito. Cada ni\u00f1o sostiene un papel con su nombre y con la otra mano se\u00f1ala al siguiente ni\u00f1o que sigue en la fila.", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Cada ni\u00f1o representa un nodo.\n"
"\n"
"El papel que sostiene es el dato o valor.\n"
"\n"
"La mano que apunta al siguiente ni\u00f1o es el puntero al siguiente nodo.\n"
"\n"
"El \u00faltimo ni\u00f1o no se\u00f1ala a nadie (porque no hay nadie despu\u00e9s de \u00e9l), as\u00ed que su mano apunta al aire \u2014 \u00a1eso significa que es el final de la lista!\n"
"\n"
"", None))
        self.label_4.setText("")
    # retranslateUi

