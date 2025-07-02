from UIS.menuTemas_ui import Ui_MenuTemas
from Screens.Grafos.MenuGrafos import VentanaGrafos
from Screens.HashTables.hashTables import VentanaHashTables
from PySide6.QtWidgets import QMainWindow
from Screens.Listas.ListasMenu import VentanaListas
from Screens.Ordenamiento.menuOrdenamiento import VentanaOrdenamiento

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MenuTemas()
        self.ui.setupUi(self)

        #Acciones de los botones
        self.ui.btnListas.clicked.connect(self.abrir_listas)
        self.ui.btnArboles.clicked.connect(self.abrir_arboles)
        self.ui.btnGrafos.clicked.connect(self.abrir_grafos)
        self.ui.btnOrdenamiento.clicked.connect(self.abrir_Ordenamiento)
        self.ui.btnHash.clicked.connect(self.abrir_hash)
        self.ui.btnStrassen.clicked.connect(self.abrir_strassen)
        self.ui.btnSalir.clicked.connect(self.salir)

    def abrir_listas(self):
        self.ListasMenu = VentanaListas()
        self.ListasMenu.show() 

    def abrir_arboles(self):
        print("Abrir tema de Arboles") 

    def abrir_grafos(self):
        self.GrafosMenu = VentanaGrafos()
        self.GrafosMenu.show() 

    def abrir_Ordenamiento(self):
        self.VentanaOrdenamiento = VentanaOrdenamiento()
        self.VentanaOrdenamiento.show()

    def abrir_hash(self):
        self.hashTables = VentanaHashTables()
        self.hashTables.show()

    def abrir_strassen(self):
        print("Abrir tema de Metodo strassen")  

    def salir(self):
        self.close()