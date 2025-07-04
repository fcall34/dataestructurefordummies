from UIS.ListaDobleEnlazada import Ui_StackedWidget
from PySide6.QtWidgets import QMainWindow
from Screens.Listas.ListaDobleEnlazada.ListaDoble import ventanalistas

class VentanaListas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_StackedWidget()
        self.ui.setupUi(self)

        self.ui.btnListasCirculares.clicked.connect(self.abrir_Simples)

    def abrir_Simples(self):
        print("Hola")
        self.ventana = ventanalistas()
        self.ventana.show()