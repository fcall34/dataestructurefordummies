from UIS.menuTemas_ui import Ui_MenuTemas
from PySide6.QtWidgets import QMainWindow

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

    def abrir_listas(self):
        print("Abrir tema de listas") 

    def abrir_arboles(self):
        print("Abrir tema de Arboles") 

    def abrir_grafos(self):
        print("Abrir tema de Grafos") 

    def abrir_Ordenamiento(self):
        print("Abrir tema de Ordenamiento") 

    def abrir_hash(self):
        print("Abrir tema de Hash tables")

    def abrir_strassen(self):
        print("Abrir tema de Metodo strassen")  