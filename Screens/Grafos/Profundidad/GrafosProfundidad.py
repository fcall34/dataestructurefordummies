from PySide6.QtWidgets import QStackedWidget, QWidget, QLabel
from PySide6.QtGui import QPainter, QPen, QColor, QPixmap
from PySide6.QtCore import Qt, QPoint, QRect
from UIS.GrafosProfundidad_ui import Ui_VistaProfundiad
from .PaintableGraphPage import PaintableGraphPage

class VentanaGrafosProfundidad(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VistaProfundiad()
        self.ui.setupUi(self)

        original_page = self.ui.page
        ui_elements_to_transfer_map = {
            "label": self.ui.label,         # Título "Recorrido En Profundidad"
            "label_2": self.ui.label_2,     # Descripción
            "label_3": self.ui.label_3,     # Montaña Rusa (Imagen)
            "label_4": self.ui.label_4,     # Tesoro (Imagen)
            "label_5": self.ui.label_5,     # Trencito (Imagen)
            "label_6": self.ui.label_6,     # Entrada (Imagen)
            "label_7": self.ui.label_7,     # Chocones (Imagen)
            "label_8": self.ui.label_8,     # Ruleta (Imagen)
            "label_9": self.ui.label_9,     # Entrada
            "pushButton": self.ui.btnNext # botón "Siguiente"
        }

        self.graph_display_page = PaintableGraphPage(self)

        # --- Actualizado: Mover TODOS los elementos a la nueva página pintable ---
        for element_name, element_obj in ui_elements_to_transfer_map.items():
            element_obj.setParent(self.graph_display_page)
            # Asegurarse de que la geometría se re-aplique si no hay layouts
            # Esto es crucial para widgets posicionados con setGeometry
            element_obj.setGeometry(element_obj.geometry())
        # --- FIN ACTUALIZACIÓN ---

        # Define las aristas (usando las referencias a los QLabels originales que ahora son hijos de graph_display_page)
        edges_to_draw = [
            (self.ui.label_3, self.ui.label_5),
            (self.ui.label_5, self.ui.label_4),
            (self.ui.label_3, self.ui.label_6),
            (self.ui.label_7, self.ui.label_6),
            (self.ui.label_8, self.ui.label_6),
            (self.ui.label_5, self.ui.label_6)
        ]
        self.graph_display_page.set_graph_elements_and_edges(ui_elements_to_transfer_map, edges_to_draw)


        page_index = self.indexOf(original_page)
        if page_index != -1:
            self.removeWidget(original_page)
            self.insertWidget(page_index, self.graph_display_page)
            self.setCurrentIndex(page_index)
        else:
            print("Advertencia: La página 'self.page' no se encontró en el QStackedWidget. Añadiendo directamente.")
            self.addWidget(self.graph_display_page)
            self.setCurrentWidget(self.graph_display_page)

        # El botón ya está conectado arriba, así que esta línea podría duplicarse si no se maneja bien
        self.ui.btnNext.clicked.connect(self.on_siguiente_clicked)
        self.ui.btnNext_2.clicked.connect(self.on_siguiente_clicked)
        self.ui.btnNext_3.clicked.connect(self.on_siguiente_clicked)
        self.ui.btnNext_4.clicked.connect(self.on_siguiente_clicked)
        self.ui.btnNext_5.clicked.connect(self.on_siguiente_clicked)
        self.ui.btnTerminar.clicked.connect(self.teminar)
        # La línea anterior en el __init__ de VentanaGrafosProfundidad es suficiente.

    def on_siguiente_clicked(self):
        current_page_index = self.currentIndex()
        total_pages = self.count()

        if current_page_index < total_pages - 1:
            self.setCurrentIndex(current_page_index + 1)

    def teminar(self):
        self.hide()