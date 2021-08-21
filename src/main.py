import sys
from PyQt5.QtWidgets import QApplication
from controllers.new.MainController import MainController

if __name__=="__main__":
    app = QApplication(sys.argv)
    win=MainController(app.clipboard())
    win.run()
    sys.exit(app.exec())
