from views import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from .menu_controller import MenuController
# from .form_controller import FormController
from .tab_controller import TabController
from .tab_temario_controller import TabTemarioController
from .CalendarizadorDialogController import CalendarizadorDialogController
from models import Materia
from views.widgets.WidTabTemario import WidTabTemario
from views.widgets.CalendarizadorDialog import CalendarizadorDialog

class MainController(QMainWindow,Ui_MainWindow,MenuController):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(900,500)
        self.set_menu_controller()
        self.file_name=None
        self.model=Materia()
        self.tab_widget.clear()
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_controller=TabController()
        self.temario_controller=None
        self.actionCalendarizar.setDisabled(True)

    def close_tab(self,index):
        id=self.tab_widget.widget(index).id
        self.tab_controller.delete_widget(id)
        self.tab_widget.removeTab(index)
        if self.tab_widget.count()==0:
            self.actionCalendarizar.setDisabled(True)

    def calendarizar_dialog(self):
        current_widget_id=self.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        dialog=CalendarizadorDialog()
        ctl_calendarizador_dialog=CalendarizadorDialogController(dialog,current_model)
        ctl_calendarizador_dialog.run()

    def nuevo(self):
        num_tabs=self.tab_widget.count()
        new_tab=WidTabTemario()
        self.tab_controller.addWidget(new_tab,None)
        self.tab_widget.insertTab(num_tabs,new_tab,"Nuevo archivo")
        self.tab_widget.setCurrentIndex(num_tabs)
        if self.tab_widget.count()>0:
            self.actionCalendarizar.setDisabled(False)

    def guardar(self):
        current_widget_id=self.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        if current_model.file:
            current_model.write()
        else:
            self.guardar_como()

    def guardar_como(self):
        current_widget_id=self.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        file_dialog=QFileDialog(self)
        file_name=file_dialog.getSaveFileName(self,"Guardar archivo")[0]
        current_model.file=file_name
        current_model.write()
        index=self.tab_widget.currentIndex()
        self.tab_widget.setTabText(index,file_name.split('/')[-1])


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

        # self.temario_controller=TabTemarioController(new_tab,new_tab.model)

        self.tab_widget.insertTab(num_tabs,new_tab,self.file_name.split('/')[-1])
        self.tab_widget.setCurrentIndex(num_tabs)
        if self.tab_widget.count()>0:
            self.actionCalendarizar.setDisabled(False)

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
