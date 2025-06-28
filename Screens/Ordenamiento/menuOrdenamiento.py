from PySide6.QtWidgets import QMainWindow
from Screens.Ordenamiento.Quicksort import VentanaQuickSort
from UIS.Ordenamiento_ui import Ui_MainWindow

class VentanaOrdenamiento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.QUICKSORT.clicked.connect(self.abrir_QuickSort)
        
    def abrir_QuickSort(self):
        self.ventanaQuick = VentanaQuickSort()
        self.ventanaQuick.show()
    