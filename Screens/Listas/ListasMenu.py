from PySide6.QtWidgets import QMainWindow
from Screens.Listas.ListasSimples import VentanaListasSimple
from Screens.Listas.Listadobles import VentanaListasDobles
from Screens.Listas.ListasCirculares import VentanaCirculares
from Screens.Listas.Colas import VentanaColas
from Screens.Listas.Pilas import VentanaPilas
from UIS.listasMenu_ui import Ui_ListasWindow

class VentanaListas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_ListasWindow()
        self.ui.setupUi(self)

        self.ui.btnListasLigadas.clicked.connect(self.abrir_ListasSimples)
        self.ui.btnListasDobles.clicked.connect(self.abrir_ListasDobles)
        self.ui.btnListasCirculares.clicked.connect(self.abrir_ListasCirculares)
        self.ui.btnColas.clicked.connect(self.abrir_Colas)
        self.ui.btnPilas.clicked.connect(self.abrir_Pilas)
        self.ui.btnAtras.clicked.connect(self.finish)

    def abrir_Pilas(self):
        self.ventanaPilas = VentanaPilas()
        self.ventanaPilas.show()

    def abrir_Colas(self):
        self.ventanaColas = VentanaColas()
        self.ventanaColas.show()

    def abrir_ListasCirculares(self):
        self.ventanaCirculares = VentanaCirculares()
        self.ventanaCirculares.show()

    def abrir_ListasSimples(self):
        self.ventanaSimple = VentanaListasSimple()
        self.ventanaSimple.show()

    def abrir_ListasDobles(self):
        self.ventanaDoble = VentanaListasDobles()
        self.ventanaDoble.show()

    def finish(self):
        self.hide()