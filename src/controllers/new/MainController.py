# from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from views.qt_view.MainWindow import MainWindow
from models import Materia

from .MenuController import MenuController
from .TabListController import TabListController

from .CalendarizadorDialogController import CalendarizadorDialogController

from views.widgets.CalendarizadorDialog import CalendarizadorDialog

class MainController():
    def __init__(self,clipboard):
        self.clipboard=clipboard
        self.view=MainWindow()
        self.model=Materia()
        self.view.tab_widget.clear()
        self.tab_controller=TabListController(self.view,clipboard)
        self.menuFileController=MenuController(self.model,self.view,self.tab_controller)
        self.view.actionCalendarizar.setDisabled(True)
        self.view.tab_widget.tabCloseRequested.connect(self.tab_controller.close_tab)
        self.view.actionCalendarizar.triggered.connect(self.calendarizar_dialog)

    def calendarizar_dialog(self):
        current_widget_id=self.view.tab_widget.currentWidget().id
        current_model=self.tab_controller.get_model_by_id(current_widget_id)
        dialog=CalendarizadorDialog()
        ctl_calendarizador_dialog=CalendarizadorDialogController(dialog,current_model)
        ctl_calendarizador_dialog.run()

    def run(self):
        self.view.show()
