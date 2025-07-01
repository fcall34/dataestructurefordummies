from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint, QRect


class PaintableGraphPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.edges = [] # Lista para almacenar las aristas (tuplas de QLabels)

    def set_graph_elements_and_edges(self, ui_labels, edges_data):
        """
        Este método se llama DESPUÉS de que la UI ha sido configurada y los labels existen.
        Toma los labels de la UI original y los hace hijos de esta página,
        y luego configura las aristas.
        """
        # ui_labels debería ser un diccionario o una lista ordenada de tus labels
        # para que puedas accederlos fácilmente. Por ejemplo:
        # { 'label_3': label_3_obj, 'label_4': label_4_obj, ... }

        # Primero, haz que los labels sean hijos de esta PaintableGraphPage
        for label_name, label_obj in ui_labels.items():
            label_obj.setParent(self)
            # Re-aplicar la geometría es importante si no usas layouts en el .ui
            # Si usas layouts, estos se encargarán de posicionarlos cuando cambien de padre
            if not isinstance(label_obj.parent().layout(), QRect): # Check if parent has a layout (simplified)
                 # Si el padre no tiene un layout (es decir, usas setGeometry), re-aplica
                 label_obj.setGeometry(label_obj.geometry())

        # Ahora define las aristas usando las referencias a los objetos QLabel
        # Aquí, 'edges_data' sería una lista de tuplas de los objetos QLabel directamente
        self.edges = edges_data

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor(0, 0, 0)) # Color negro
        pen.setWidth(2)             # Ancho de la línea
        painter.setPen(pen)

        for start_widget, end_widget in self.edges:
            if not start_widget.isVisible() or not end_widget.isVisible():
                continue

            # Las coordenadas de los labels son relativas a SU padre, que es PaintableGraphPage
            start_rect = start_widget.geometry()
            start_center_x = start_rect.x() + start_rect.width() / 2
            start_center_y = start_rect.y() + start_rect.height() / 2
            start_point = QPoint(int(start_center_x), int(start_center_y))

            end_rect = end_widget.geometry()
            end_center_x = end_rect.x() + end_rect.width() / 2
            end_center_y = end_rect.y() + end_rect.height() / 2
            end_point = QPoint(int(end_center_x), int(end_center_y))

            painter.drawLine(start_point, end_point)

        super().paintEvent(event) # Asegúrate de que los hijos (labels) también se dibujen

    def resizeEvent(self, event):
        self.update() # Forzar redibujado de las líneas si el tamaño cambia
        super().resizeEvent(event)