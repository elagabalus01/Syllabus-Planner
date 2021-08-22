from .ui_sutema_edit_dialog import Ui_subtema_dialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
class SubtemaDialog(QtWidgets.QDialog,Ui_subtema_dialog):
    text=pyqtSignal(str)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def close(self):
        texto=self.edit_subtema.toPlainText()
        self.accept()
        self.text.emit(texto)
