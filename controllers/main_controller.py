from views import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from .menu_controller import MenuController
from .catalog_controller import CatalogController
from .form_controller import FormController
from models import Materia

class MainController(QMainWindow,Ui_MainWindow,MenuController,CatalogController,
    FormController):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_menu_controller()
        self.set_catalog()
        self.model=Materia()

    def abrir(self):
        file_dialog=QFileDialog(self,"Abrir archivo","~","CSV file (*.csv,*.py)")
        file_name=file_dialog.getOpenFileName(self,"Abrir archivo","~","Temarios (*.json)")[0]
        print(f"File {file_name}")
        self.model.recoverJson(file_name)
        print(self.model)
        self.set_form()

    def cerrar(self):
        print("Cerrando")

    def salir(self):
        print("Salir")
