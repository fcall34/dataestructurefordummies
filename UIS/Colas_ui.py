# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Colas.ui'
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
        StackedWidget.setEnabled(True)
        StackedWidget.resize(761, 521)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        StackedWidget.setFont(font)
        StackedWidget.setStyleSheet(u"background-color: rgb(59, 7, 112)")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 20, 401, 71))
        font1 = QFont()
        font1.setFamilies([u"Caprasimo"])
        font1.setPointSize(32)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color:transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 651, 141))
        font2 = QFont()
        font2.setFamilies([u"Caprasimo"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 220, 651, 251))
        self.label_3.setPixmap(QPixmap(u"Sources/Images/COLAS.jpg"))
        self.label_3.setScaledContents(True)
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 20, 411, 71))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color:transparent;color:black")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 490, 75, 24))
        self.pushButton.setStyleSheet(u"background-color:rgb(3, 116, 255)")
        StackedWidget.addWidget(self.page)
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 20, 411, 71))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color:transparent;color:black")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 20, 401, 71))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color:transparent;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 100, 291, 281))
        self.label_4.setFont(font2)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 100, 321, 281))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 410, 411, 91))
        self.label_9.setPixmap(QPixmap(u"Sources/Images/rusa.png"))
        self.label_9.setScaledContents(True)
        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(660, 470, 75, 24))
        self.pushButton_2.setStyleSheet(u"background-color:rgb(0, 111, 255)")
        StackedWidget.addWidget(self.page_2)

        self.retranslateUi(StackedWidget)

        StackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"COLAS (queues) ", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u" Las veces que has ido a un parque de atracciones ya sea SixFlags o Kataplum, apuesto lo que sea ah que has querido ser de los primeros en subirte a una atracccion, a veces tienes suerte y llegas primero, en otras tristemente te toca hasta la COLA.\n"
"Llegas a tu atraccion favorita y quieres subirte, \u00bfque es lo primero que vez? claro, no podria ser nada mas y nada menos que una fila de ni\u00f1os esperando su turno", None))
        self.label_3.setText("")
        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"COLAS (queues) ", None))
        self.pushButton.setText(QCoreApplication.translate("StackedWidget", u"SIGUIENTE", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"COLAS (queues) ", None))
        self.label_8.setText(QCoreApplication.translate("StackedWidget", u"COLAS (queues) ", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"\"El primero en llegar, es el primero en salir\" (FirtsIntFirstOut):\n"
"\n"
"El primer ni\u00f1o que lleg\u00f3 a la fila es el primero en subirse al juego.\n"
"\n"
"El \u00faltimo ni\u00f1o que lleg\u00f3 tendr\u00e1 que esperar hasta que todos los anteriores pasen.\n"
"\n"
"\u00a1As\u00ed funciona una cola! Solo puedes agregar al final (enqueue) y sacar al principio (dequeue).", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Cuando el juego empieza, Ni\u00f1o 1 sale primero.\n"
"\n"
"No puedes \"colarte\":\n"
"\n"
"En una cola no est\u00e1 permitido sacar a alguien del medio.\n"
"\n"
"\u00a1Tienes que esperar tu turno en orden! \n"
"\n"
"Si no hay nadie, la cola est\u00e1 vac\u00eda:\n"
"\n"
"Cuando todos los ni\u00f1os han subido al juego, la fila se queda vac\u00eda (\u00a1y ya no hay que esperar!).", None))
        self.label_9.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("StackedWidget", u"TERMINAR", None))
    # retranslateUi

