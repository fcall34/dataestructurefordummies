import sys
from PySide6.QtWidgets import QApplication
from Screens.menu import MenuPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec())
