from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore
from views.qt_view.MainWindow import MainWindow
from models import Materia

from .MenuController import MenuController
# from .form_controller import FormController
from .TabListController import TabListController
from .tab_temario_controller import TabTemarioController
from .CalendarizadorDialogController import CalendarizadorDialogController
from views.widgets.WidTabTemario import WidTabTemario
from views.widgets.CalendarizadorDialog import CalendarizadorDialog

class MainController(MenuController):
    def __init__(self):
        self.file_name=None
        self.view=MainWindow()
        self.model=Materia()
        self.set_menu_controller()
        self.view.tab_widget.clear()
        self.view.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.tab_controller=TabListController()
        self.view.temario_controller=None
        self.view.actionCalendarizar.setDisabled(True)

    def close_tab(self,index):
        id=self.view.tab_widget.widget(index).id
        self.tab_controller.delete_widget(id)
        self.view.tab_widget.removeTab(index)
        if self.view.tab_widget.count()==0:
            self.view.actionCalendarizar.setDisabled(True)

    def calendarizar_dialog(self):
        current_widget_id=self.view.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        dialog=CalendarizadorDialog()
        ctl_calendarizador_dialog=CalendarizadorDialogController(dialog,current_model)
        ctl_calendarizador_dialog.run()

    def nuevo(self):
        num_tabs=self.view.tab_widget.count()
        new_tab=WidTabTemario()
        self.tab_controller.addWidget(new_tab,None)
        self.view.tab_widget.insertTab(num_tabs,new_tab,"Nuevo archivo")
        self.view.tab_widget.setCurrentIndex(num_tabs)
        if self.view.tab_widget.count()>0:
            self.view.actionCalendarizar.setDisabled(False)

    def guardar(self):
        current_widget_id=self.view.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        if current_model.file:
            current_model.write()
        else:
            self.guardar_como()

    def guardar_como(self):
        current_widget_id=self.view.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        # file_dialog=(self,QFileDialog.DontUseNativeDialog)
        file_name=QFileDialog.getSaveFileName(self,"Guardar archivo",'.','','',QFileDialog.DontUseNativeDialog)[0]
        current_model.file=file_name
        current_model.write()
        index=self.view.tab_widget.currentIndex()
        self.view.tab_widget.setTabText(index,file_name.split('/')[-1])


    def abrir(self):
        if self.file_name:
            # self.clear_form()
            self.model=Materia()
        self.file_name=QFileDialog.getOpenFileName(self.view,
        "Abrir archivo","~","Temarios (*.json)")[0]
        # self.model.recoverJson(self.file_name)
        num_tabs=self.view.tab_widget.count()

        print(f"Number of tabs {num_tabs}")

        new_tab=WidTabTemario()
        self.tab_controller.addWidget(new_tab,self.file_name)

        # self.temario_controller=TabTemarioController(new_tab,new_tab.model)

        self.view.tab_widget.insertTab(num_tabs,new_tab,self.file_name.split('/')[-1])
        self.view.tab_widget.setCurrentIndex(num_tabs)
        if self.view.tab_widget.count()>0:
            self.view.actionCalendarizar.setDisabled(False)

        # self.set_form()

    def cerrar(self):
        if self.view.tab_widget.count()>0:
            self.view.close_tab(self.view.tab_widget.currentIndex())
        # if self.file_name:
        #     self.file_name=None
        #     self.clear_form()
        #     print("Cerrando")


    def salir(self):
        self.close()
        print("Salir")

    def run(self):
        self.view.show()
