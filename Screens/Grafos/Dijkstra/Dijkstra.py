from UIS.Dijkstra_ui import Ui_dijkstraVista
from PySide6.QtWidgets import QStackedWidget

class VentanDijkstra(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_dijkstraVista()
        self.ui.setupUi(self)

        self.ui.btnNext.clicked.connect(self.nextPage)
        self.ui.btnNext_2.clicked.connect(self.nextPage)
        self.ui.btnNext_3.clicked.connect(self.nextPage)
        self.ui.btnNext_4.clicked.connect(self.nextPage)
        self.ui.btnNext_5.clicked.connect(self.nextPage)
        self.ui.btnNext_6.clicked.connect(self.nextPage)
        self.ui.btnTerminar.clicked.connect(self.finish)

    def nextPage(self):
        currentPage = self.currentIndex()
        totalPages = self.count()

        if currentPage < totalPages - 1:
            self.setCurrentIndex(currentPage+1)

    def finish(self):
        self.hide()