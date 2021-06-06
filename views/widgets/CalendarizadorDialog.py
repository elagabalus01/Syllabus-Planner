from .ui_calendarizador_dialog import Ui_CalendarizadorDialog
from PyQt5 import QtWidgets
class CalendarizadorDialog(QtWidgets.QDialog,Ui_CalendarizadorDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
