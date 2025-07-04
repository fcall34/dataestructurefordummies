from UIS.grafosMenu import Ui_GrafosWindow
from Screens.Grafos.Amplitud.GrafosAmplitud import VentanaGrafosAmplitud
from Screens.Grafos.Profundidad.GrafosProfundidad import VentanaGrafosProfundidad
from Screens.Grafos.Dijkstra.Dijkstra import VentanDijkstra
from PySide6.QtWidgets import QMainWindow
from Screens.Grafos.Profundidad.PaintableGraphPage import PaintableGraphPage

class VentanaGrafos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GrafosWindow()
        self.ui.setupUi(self)

        # Crear la capa de dibujo
        self.graph_overlay = PaintableGraphPage(self.ui.centralwidget)
        self.graph_overlay.setGeometry(self.ui.centralwidget.rect())
        self.graph_overlay.lower()  # Asegúrate de que esté debajo de los botones

        self.configurar_grafo_visual()

        # Botones conectados a funciones
        self.ui.btnAmplitud.clicked.connect(self.abrir_Amplitud)
        self.ui.btnProfundida.clicked.connect(self.abrir_Profundidad)
        self.ui.btndijkstra.clicked.connect(self.abrir_dijkstra)

    def configurar_grafo_visual(self):
        # Diccionario de labels
        nodos = {
            'amplitud': self.ui.btnAmplitud,
            'profundidad': self.ui.btnProfundida,
            'kruskal': self.ui.btnKruskal,
            'floyd': self.ui.btnFloyd,
            'prim': self.ui.btnPrim,
            'bellman': self.ui.btnBellman,
            'dijkstra': self.ui.btndijkstra,
            'ford': self.ui.btnFord,
            'aestrella': self.ui.btnAestrella,
        }

        # Definir aristas como conexiones entre botones
        edges = [
            (nodos['amplitud'], nodos['profundidad']),
            (nodos['profundidad'], nodos['amplitud']),
            (nodos['kruskal'], nodos['bellman']),
            (nodos['bellman'], nodos['aestrella']),
            (nodos['kruskal'], nodos['floyd']),
            (nodos['amplitud'], nodos['aestrella']),
            (nodos['floyd'], nodos['profundidad']),
            (nodos['profundidad'], nodos['ford']),
            (nodos['ford'], nodos['prim']),
            (nodos['prim'], nodos['dijkstra']),
            (nodos['dijkstra'], nodos['profundidad'])
        ]

        self.graph_overlay.set_graph_elements_and_edges(nodos, edges)
        self.graph_overlay.raise_()  # Lo ponemos encima para que pinte sobre fondo pero debajo de botones

    def resizeEvent(self, event):
        self.graph_overlay.setGeometry(self.ui.centralwidget.rect())
        super().resizeEvent(event)

    def abrir_Amplitud(self):
        self.Amplitud = VentanaGrafosAmplitud()
        self.Amplitud.show()

    def abrir_Profundidad(self):
        self.Profundidad = VentanaGrafosProfundidad()
        self.Profundidad.show()

    def abrir_dijkstra(self):
        self.dijkstra = VentanDijkstra()
        self.dijkstra.show()