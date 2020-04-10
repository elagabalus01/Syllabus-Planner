from .calendarizador.calendarizador import calendarizar
from .topController import TopController
from tkinter import messagebox
class CalendarizadorController(TopController):
    def __init__(self):
        super().__init__()
        self.configurarCalendarizador()
    def configurarCalendarizador(self):
        self.view.menu.menuCalendarizar.add_command(label="Calendarizar",command=self.calendarizarUI)
    def calendarizarUI(self,event=None):
        try:
            calendarizar(self.file,'Prueba calendarizador UI','15-01-2020',16)
        except TypeError:
            messagebox.showinfo(title="Error", message="No se pudo abrir el archivo")




