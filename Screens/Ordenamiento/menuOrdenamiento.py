from PySide6.QtWidgets import QMainWindow
from Screens.Ordenamiento.Quicksort import VentanaQuickSort
from Screens.Ordenamiento.MergeSort import VentanaMergeSort
from Screens.Ordenamiento.HeapSort import VentanaHeapSort
from Screens.Ordenamiento.CountingSort import VentanaCountingSort
from UIS.Ordenamiento_ui import Ui_MainWindow

class VentanaOrdenamiento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.QUICKSORT.clicked.connect(self.abrir_QuickSort)
        self.ui.MERGESORT.clicked.connect(self.abrir_MergeSort)
        self.ui.HEAPSORT.clicked.connect(self.abrir_HeapSort)
        self.ui.COUNTINGSORT.clicked.connect(self.abrir_Counting)
        self.ui.ATRAS.clicked.connect(self.finish)
       
        
    def abrir_QuickSort(self):
        self.ventanaQuick = VentanaQuickSort()
        self.ventanaQuick.show()

    def abrir_MergeSort(self):
        self.ventanaMerge = VentanaMergeSort()
        self.ventanaMerge.show()

    def abrir_HeapSort(self):
        self.ventanaHeap = VentanaHeapSort()
        self.ventanaHeap.show()
    
    def abrir_Counting(self):
        self.ventanaCount = VentanaCountingSort()
        self.ventanaCount.show()

    def finish(self):
        self.hide()
    