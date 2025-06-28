from UIS.grafosMenu import Ui_GrafosWindow
from Screens.Grafos.Amplitud.GrafosAmplitud import VentanaGrafosAmplitud
from PySide6.QtWidgets import QMainWindow

class VentanaGrafos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_GrafosWindow()
        self.ui.setupUi(self)

        self.ui.btnAmplitud.clicked.connect(self.abrir_Amplitud)


    def abrir_Amplitud(self):
        self.Amplitud = VentanaGrafosAmplitud()
        self.Amplitud.show()

