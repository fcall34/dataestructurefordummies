from UIS.menuListas import Ui_ListasWindow
from PySide6.QtWidgets import QMainWindow

class VentanaListas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_ListasWindow()
        self.ui.setupUi(self)