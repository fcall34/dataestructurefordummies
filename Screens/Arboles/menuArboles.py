from PySide6.QtWidgets import QMainWindow
from UIS.menuArboles_ui import Ui_MainWindow
from Screens.Arboles.arbolBusqueda import VentanaArbolesBusqueda
from Screens.Arboles.arbolesAuto import VentanaArbolesAuto

class VentanaArboles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ATRAS.clicked.connect(self.finish)
        self.ui.ARBOLESBINARIOS.clicked.connect(self.abrir_busqueda)
        self.ui.ARBOLESAUTOBALANCEADOS.clicked.connect(self.abrir_auto)

    def finish(self):
        self.hide()

    def abrir_busqueda(self):
        self.ventanaBusqueda = VentanaArbolesBusqueda()
        self.ventanaBusqueda.show()

    def abrir_auto(self):
        self.ventanaAuto = VentanaArbolesAuto()
        self.ventanaAuto.show()