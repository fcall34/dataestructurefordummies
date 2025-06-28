from UIS.GrafosAmplitud_ui import Ui_GrafosAmplitud
from PySide6.QtWidgets import QStackedWidget

class VentanaGrafosAmplitud(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GrafosAmplitud()
        self.ui.setupUi(self)

        self.currentIndex()

        self.ui.btnComenzar.clicked.connect(self.avanzar_pagina)
        self.ui.btnNext.clicked.connect(self.avanzar_pagina)

    def avanzar_pagina(self):
        pagina_actual = self.currentIndex()
        total_paginas = self.count()

        if pagina_actual < total_paginas - 1:
            self.setCurrentIndex(pagina_actual + 1)