# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListaDobleEnlazada.ui'
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
        StackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color:rgb(6, 78, 134);")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 631, 31))
        font = QFont()
        font.setFamilies([u"Caprasimo"])
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color:transparent")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 651, 191))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 280, 411, 131))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/ListasDoblementeEnlazadas.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 420, 141, 20))
        font2 = QFont()
        font2.setFamilies([u"Caprasimo"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 20, 641, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color:transparent;color:black")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 450, 91, 31))
        font3 = QFont()
        font3.setFamilies([u"Caprasimo"])
        font3.setPointSize(12)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color:rgb(59, 20, 141)")
        StackedWidget.addWidget(self.page)
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Listas Doblemente Enlazadas", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Vuelve a imaginarte de nuevo una fila de ni\u00f1os  pero esta vez cada ni\u00f1o tiene dos manos libres para se\u00f1alar.\n"
"\n"
"\"Una mano se\u00f1ala al siguiente ni\u00f1o (adelante)\".\n"
"\n"
"\"La otra mano se\u00f1ala al ni\u00f1o de atr\u00e1s (atr\u00e1s).\"\n"
"\n"
"Muy similar a la lista simple solo que esta vez como su nombre lo dice: Ahora hay 2 manitas disponibles, con las cuales puedes pasar tu nombre delante o atras de tu compa\u00f1ero(claro siempre y cuando tengas un compa\u00f1ero delante o detras).", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Sencillo verdad?", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Listas Doblemente Enlazadas", None))
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"SALIR", None))
    # retranslateUi

