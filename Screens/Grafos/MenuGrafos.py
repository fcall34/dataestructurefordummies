from UIS.grafosMenu import Ui_GrafosWindow
from PySide6.QtWidgets import QMainWindow

class VentanaGrafos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_GrafosWindow()
        self.ui.setupUi(self)