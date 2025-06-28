from UIS.GrafosAmplitud_ui import Ui_GrafosAmplitud
from PySide6.QtWidgets import QStackedWidget, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem, QLabel
from PySide6.QtGui import QBrush, QPen, QFont, QColor
from PySide6.QtCore import Qt, QTimer
import math
from collections import deque

class VentanaGrafosAmplitud(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GrafosAmplitud()
        self.ui.setupUi(self)

        # Configuración del temporizador para la animación del BFS
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animate_bfs_step) # Conecta el timeout a la función que avanza la animación

        # Variables para el algoritmo BFS y el estado de la animación
        self.bfs_queue = deque()      # Cola para nodos a visitar (FIFO)
        self.visited_nodes = set()    # Conjunto para nodos ya visitados (evitar repeticiones)
        self.bfs_path = []            # Lista para almacenar el orden del recorrido
        self.current_animation_step = 0 # Paso actual de la animación (opcional, útil para depuración)

        # Diccionarios para guardar referencias a los elementos gráficos de nodos y aristas
        # Esto nos permite cambiar sus propiedades (color, etc.) durante la animación
        self.node_graphics_items = {}
        self.edge_graphics_items = {}

        # Conexiones de los botones de navegación
        self.ui.btnComenzar.clicked.connect(self.avanzar_pagina)
        self.ui.btnNext.clicked.connect(self.avanzar_pagina)
        self.ui.btnNext_2.clicked.connect(self.avanzar_pagina)
        
        # Ojo: Asegúrate de que 'btnNext_2' exista en tu archivo UI si lo estás usando.
        # Si no existe, esta línea causará un error. Si no lo necesitas, puedes borrarla.
        # self.ui.btnNext_2.clicked.connect(self.avanzar_pagina)

        # Conexión del botón de reiniciar la animación
        # Asegúrate de que 'btnReiniciar' esté en tu archivo UI.
        self.ui.btnReiniciar.clicked.connect(self.reiniciar_animacion)

        # Ocultar el mensaje de "Recorrido Terminado" al inicio de la aplicación
        self.ui.lblRecorridoTerminado.hide()

    def avanzar_pagina(self):
        """
        Avanza a la siguiente página del QStackedWidget.
        Si se llega a la página de animación (la tercera), inicializa el grafo y el BFS.
        """
        current_page_index = self.currentIndex()
        total_pages = self.count()

        # Solo avanzamos si no estamos en la última página
        if current_page_index < total_pages - 1:
            self.setCurrentIndex(current_page_index + 1)

            # Si la página actual es la TERCERA (índice 2), mostramos el grafo y comenzamos la animación
            # La corrección importante: el índice 2 corresponde a la TERCERA página.
            if self.currentIndex() == 2:
                self.mostrar_grafo()
                self.start_bfs_animation()
                # Asegurarse de que el mensaje de "Recorrido Terminado" esté oculto al iniciar la animación
                self.ui.lblRecorridoTerminado.hide()
        # Si ya estamos en la última página y se presiona un botón de "Siguiente",
        # no hacemos nada (o podrías agregar otra lógica aquí si la necesitas).

    def reiniciar_animacion(self):
        """
        Reinicia el estado de la animación del BFS, restableciendo colores y datos.
        """
        # Detener el temporizador de la animación si está en curso
        self.animation_timer.stop()

        # Limpiar las estructuras de datos del algoritmo BFS
        self.bfs_queue.clear()
        self.visited_nodes.clear()
        self.bfs_path = []
        self.current_animation_step = 0

        # Restablecer los colores y propiedades de todos los nodos a su estado inicial
        for node_id, (circle, text) in self.node_graphics_items.items():
            circle.setBrush(QBrush(Qt.white))
            circle.setPen(QPen(Qt.black, 2))
            text.setDefaultTextColor(Qt.black)
            text.setFont(QFont("Arial", 14, QFont.Bold)) # Restablecer el tamaño de la fuente original

        # Restablecer los colores de todas las aristas a su estado inicial
        for edge_id, edge_item in self.edge_graphics_items.items():
            edge_item.setPen(QPen(Qt.black, 2))
        
        # Ocultar el mensaje de "Recorrido Terminado" si estaba visible
        self.ui.lblRecorridoTerminado.hide()
        
        # Volver a iniciar la animación desde el nodo 0
        self.start_bfs_animation()

    def mostrar_grafo(self):
        """
        Dibuja el grafo en el QGraphicsView.
        """
        # Limpiar la escena si ya existe para evitar duplicados al redibujar
        if self.ui.vistaGrafo.scene():
            self.ui.vistaGrafo.scene().clear()

        scene = QGraphicsScene()
        self.ui.vistaGrafo.setScene(scene)
        self.ui.vistaGrafo.setStyleSheet("background-color: white;") # Fondo blanco para la vista del grafo

        # Definición de las posiciones manuales de los nodos en la escena
        self.positions = {
            0: (50, 150), 1: (150, 50), 2: (200, 180),
            3: (300, 150), 4: (350, 50), 5: (380, 180),
            6: (450, 100)
        }

        # Inicializar diccionarios para guardar centros y objetos gráficos de nodos y aristas
        self.node_items_center = {}
        self.node_graphics_items = {}
        self.edge_graphics_items = {}

        # Dibujar cada nodo (círculo y texto) y guardar sus referencias
        for nodo, (x, y) in self.positions.items():
            circle = QGraphicsEllipseItem(x, y, 50, 50)
            circle.setBrush(QBrush(Qt.white))
            circle.setPen(QPen(Qt.black, 2))
            scene.addItem(circle)

            text = QGraphicsTextItem(str(nodo))
            text.setDefaultTextColor(Qt.black)
            font = QFont()
            font.setPointSize(14)
            font.setBold(True)
            text.setFont(font)
            text.setPos(x + 17, y + 10) # Posicionar el texto en el centro del círculo
            scene.addItem(text)

            self.node_items_center[nodo] = (x + 20, y + 20)  # Centro del nodo (para dibujar aristas)
            self.node_graphics_items[nodo] = (circle, text) # Guardamos el objeto círculo y texto

        # Definición de las aristas del grafo (dirigidas: de 'inicio' a 'fin')
        self.edges = [
            (0, 1), (0, 2),
            (1, 2), (1, 4),
            (2, 1),
            (3, 2), (3, 5), (3, 6),
            (4, 5),
            (5, 2),
            (6, 4)
        ]

        radio = 25 # Radio de los nodos para ajustar los extremos de las aristas

        # Dibujar cada arista y guardar sus referencias
        for inicio, fin in self.edges:
            x1, y1 = self.node_items_center[inicio]
            x2, y2 = self.node_items_center[fin]

            dx = x2 - x1
            dy = y2 - y1
            distancia = math.hypot(dx, dy) # Calcular la distancia entre los centros

            if distancia == 0:
                continue # Evitar división por cero si los nodos están en la misma posición

            # Calcular los puntos de inicio y fin de la línea, ajustados por el radio del nodo
            x1a = x1 + radio * dx / distancia
            y1a = y1 + radio * dy / distancia
            x2a = x2 - radio * dx / distancia
            y2a = y2 - radio * dy / distancia

            line = QGraphicsLineItem(x1a, y1a, x2a, y2a)
            line.setPen(QPen(Qt.black, 2)) # Color y grosor de la línea
            scene.addItem(line)
            self.edge_graphics_items[(inicio, fin)] = line # Guardamos el objeto línea

        # Ajustar el tamaño de la escena para que se adapte al tamaño actual del QGraphicsView
        scene.setSceneRect(0, 0, self.ui.vistaGrafo.width(), self.ui.vistaGrafo.height())
        self.ui.vistaGrafo.viewport().update() # Forzar la actualización visual

    def start_bfs_animation(self):
        """
        Prepara e inicia el proceso de animación del BFS desde el nodo inicial.
        """
        # Limpiar todas las estructuras de datos de la animación para un nuevo inicio
        self.bfs_queue.clear()
        self.visited_nodes.clear()
        self.bfs_path = []
        self.current_animation_step = 0

        # Ocultar el mensaje de "Recorrido Terminado" al iniciar una nueva animación
        self.ui.lblRecorridoTerminado.hide()

        # Restablecer el color y la fuente de todos los nodos a su estado predeterminado
        for node_id, (circle, text) in self.node_graphics_items.items():
            circle.setBrush(QBrush(Qt.white))
            circle.setPen(QPen(Qt.black, 2))
            text.setDefaultTextColor(Qt.black)
            text.setFont(QFont("Arial", 14, QFont.Bold)) # Restablecer el tamaño de la fuente

        # Restablecer el color de todas las aristas a su estado predeterminado
        for edge_id, line in self.edge_graphics_items.items():
            line.setPen(QPen(Qt.black, 2))

        # Definir el nodo de inicio del recorrido (en este caso, el nodo 0)
        start_node = 0
        
        # Asegurarse de que el nodo de inicio exista en el grafo
        if start_node in self.node_graphics_items:
            # Añadir el nodo de inicio a la cola y marcarlo como visitado
            self.bfs_queue.append(start_node)
            self.visited_nodes.add(start_node)
            self.bfs_path.append(start_node) # Registrar el nodo en el camino del BFS

            # Iniciar el temporizador para que 'animate_bfs_step' se llame repetidamente
            self.animation_timer.start(800) # El valor (en ms) controla la velocidad de la animación
        else:
            print(f"Error: El nodo inicial {start_node} no se encuentra en el grafo.")


    def animate_bfs_step(self):
        """
        Ejecuta un único paso del algoritmo BFS y actualiza la visualización.
        Esta función es llamada repetidamente por el QTimer.
        """
        # Si la cola está vacía, el recorrido BFS ha terminado
        if not self.bfs_queue:
            self.animation_timer.stop() # Detener el temporizador
            print("Recorrido BFS completado.")
            # Mostrar el mensaje de "Recorrido Terminado"
            self.ui.lblRecorridoTerminado.show()
            return

        # Obtener el siguiente nodo de la cola (FIFO)
        current_node = self.bfs_queue.popleft()

        # Resaltar visualmente el nodo que se está procesando actualmente
        circle, text = self.node_graphics_items[current_node]
        circle.setBrush(QBrush(QColor("#FFD700")))  # Color oro para el nodo actual
        circle.setPen(QPen(Qt.red, 3))               # Borde rojo más grueso
        text.setDefaultTextColor(Qt.blue)            # Texto azul
        text.setFont(QFont("Arial", 16, QFont.Bold)) # Aumentar ligeramente el tamaño del texto para resaltarlo

        # Encontrar los vecinos del nodo actual
        neighbors = []
        # Iterar sobre todas las aristas para encontrar las que salen del nodo actual
        for u, v in self.edges:
            if u == current_node:
                neighbors.append(v)

        # Procesar cada vecino del nodo actual
        for neighbor in neighbors:
            # Si el vecino no ha sido visitado aún
            if neighbor not in self.visited_nodes:
                self.visited_nodes.add(neighbor)  # Marcarlo como visitado
                self.bfs_queue.append(neighbor)   # Añadirlo a la cola para futuras visitas
                self.bfs_path.append(neighbor)    # Registrarlo en el camino del BFS

                # Resaltar la arista que conecta el nodo actual con el nuevo vecino
                edge_item = self.edge_graphics_items.get((current_node, neighbor))
                if edge_item:
                    edge_item.setPen(QPen(Qt.red, 3)) # Hacer la arista roja y más gruesa

                # Marcar visualmente el nodo vecino (está en la cola para ser visitado pronto)
                neighbor_circle, neighbor_text = self.node_graphics_items[neighbor]
                neighbor_circle.setBrush(QBrush(QColor("#ADD8E6")))  # Azul claro
                neighbor_circle.setPen(QPen(Qt.blue, 2))              # Borde azul
                neighbor_text.setDefaultTextColor(Qt.darkBlue)        # Texto azul oscuro
                neighbor_text.setFont(QFont("Arial", 14, QFont.Bold)) # Mantener el tamaño de fuente original

        # Forzar el redibujado del QGraphicsView para mostrar los cambios
        self.ui.vistaGrafo.viewport().update()