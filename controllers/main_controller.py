from views import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from .menu_controller import MenuController
# from .form_controller import FormController
from .tab_controller import TabController
from models import Materia
from views.widgets.WidTabTemario import WidTabTemario

class MainController(QMainWindow,Ui_MainWindow,MenuController):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_menu_controller()
        self.file_name=None
        self.model=Materia()
        self.tab_widget.clear()
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_controller=TabController()

    def close_tab(self,index):
        id=self.tab_widget.widget(index).id
        self.tab_controller.delete_widget(id)
        self.tab_widget.removeTab(index)

    def abrir(self):
        if self.file_name:
            # self.clear_form()
            self.model=Materia()
        file_dialog=QFileDialog(self,"Abrir archivo","~","CSV file (*.csv,*.py)")
        self.file_name=file_dialog.getOpenFileName(self,"Abrir archivo","~","Temarios (*.json)")[0]
        # self.model.recoverJson(self.file_name)
        num_tabs=self.tab_widget.count()
        print(f"Number of tabs {num_tabs}")

        new_tab=WidTabTemario()
        self.tab_controller.addWidget(new_tab,self.file_name)
        self.tab_widget.insertTab(num_tabs,new_tab,self.file_name.split('/')[-1])
        self.tab_widget.setCurrentIndex(num_tabs)

        # self.set_form()

    def cerrar(self):
        if self.tab_widget.count()>0:
            self.close_tab(self.tab_widget.currentIndex())
        # if self.file_name:
        #     self.file_name=None
        #     self.clear_form()
        #     print("Cerrando")


    def salir(self):
        self.close()
        print("Salir")
