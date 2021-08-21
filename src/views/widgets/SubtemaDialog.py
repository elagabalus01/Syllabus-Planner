from .ui_sutema_edit_dialog import Ui_subtema_dialog
from PyQt5 import QtWidgets

class SubtemaDialog(QtWidgets.QDialog,Ui_subtema_dialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
