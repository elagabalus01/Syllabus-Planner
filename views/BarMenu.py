from tkinter import *
from tkinter.ttk import *
class MenuArchivo(Menu):
    def __init__(self,master,**options):
        super().__init__(master,**options)
        self.__initWindow()
    def __initWindow(self):
        pass
        # self.add_command(label="abrir")
        # self.add_command(label="guardar como")
        # self.add_command(label="cerrar")
        # self.add_command(label="salir")
class BarMenu(Menu):
    def __init__(self,master,**options):
        super().__init__(master,**options)
        self.__initWindow(master)
    def __initWindow(self,master):
        self.menuArchivo=MenuArchivo(master,tearoff=0)
        self.add_cascade(label="Archivo", menu=self.menuArchivo)

        self.menuCalendarizar=Menu(master,tearoff=0)
        self.add_cascade(label="Calendarizar",menu=self.menuCalendarizar)