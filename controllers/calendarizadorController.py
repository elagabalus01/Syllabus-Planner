from .calendarizador.calendarizador import calendarizar
from .topController import TopController
from tkinter import messagebox
class CalendarizadorController(TopController):
    def __init__(self):
        super().__init__()
        self.configurarCalendarizador()
    def configurarCalendarizador(self):
        self.view.menu.menuCalendarizar.add_command(label="Calendarizar",command=self.calendarizarUI)
        self.view.menu.menuCalendarizar.add_command(label="Configurar",command=self.configurarCalendario)
    def calendarizarUI(self,event=None):
        try:
            calendarizar(self.file,'VACACIONES INTENSIVAS  2020-2','03-06-2020',16)
        except TypeError:
            messagebox.showinfo(title="Error", message="No se pudo abrir el archivo")
    def configurarCalendario(self,event=None):
        print("Se va a configurar esa cosa")




