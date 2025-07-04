from UIS.listasdobles import Ui_StackedWidget
from PySide6.QtWidgets import QStackedWidget

class ventanalistas(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_StackedWidget()
        self.ui.setupUi(self)