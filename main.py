# from controllers.mainController import MainController
# def main():
#     MainController().run()
import sys
from PyQt5.QtWidgets import QApplication
from controllers.new.MainController import MainController

if __name__=="__main__":
    # main()
    app = QApplication(sys.argv)
    win=MainController()
    win.run()
    sys.exit(app.exec())
