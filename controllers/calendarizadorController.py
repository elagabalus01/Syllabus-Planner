from .calendarizador.calendarizador import calendarizar
from .topController import TopController
class CalendarizadorController(TopController):
    def __init__(self):
        super().__init__()
        self.configurarCalendarizador()
    def configurarCalendarizador(self):
        self.view.menu.menuCalendarizar.add_command(label="Calendarizas",command=self.calendarizarUI)
    def calendarizarUI(self,event=None):
        calendarizar(self.file,'Prueba calendarizador UI','15-01-2020',16)



