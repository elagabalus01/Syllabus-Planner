from .ui_MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.resize(900,500)
