from UIS.PILAS_ui import Ui_StackedWidget
from PySide6.QtWidgets import QStackedWidget

class VentanaPilas(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_StackedWidget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.nextPage)
        self.ui.pushButton_2.clicked.connect(self.finish)

    def nextPage(self):
        current_page = self.currentIndex()
        total_pages = self.count()

        if current_page < total_pages - 1:
            self.setCurrentIndex(current_page+1)

    def finish(self):
        self.hide()