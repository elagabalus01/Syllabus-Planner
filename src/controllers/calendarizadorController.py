from calendarizador import calendarizar,calendarizarModelo
from controllers.topController import TopController
from tkinter import messagebox,END
from views.configureCalendar import CalendarConfig
class CalendarizadorController(TopController):
    def __init__(self):
        super().__init__()
        # self.cal_conf_view=CalendarConfig()
        self.configurarCalendarizador()

    def configurarCalendarizador(self):
        self.view.menu.menuCalendarizar.add_command(label="Calendarizar",command=self.calendarizarUI)
        self.view.menu.menuCalendarizar.add_command(label="Configurar",command=self.configurarCalendario)
        # self.cal_conf_view.boton.configure(command=self.calendarizar)

    def _read_calendar_config(self):
        win=self.cal_conf_view
        cal,fecha_inicio,num_sem=win.calendario.get(),win.fecha_inicio.get(),int(win.semanas.get())
        win.calendario.delete(0,END)
        win.fecha_inicio.delete(0,END)
        win.semanas.delete(0,END)
        return cal,fecha_inicio,num_sem
    def calendarizar(self,event=None):
        win=self.cal_conf_view
        cal,fecha_inicio,num_sem=self._read_calendar_config()
        calendarizarModelo(self.model,cal,fecha_inicio,num_sem)
        messagebox.showinfo(title="Hecho", message="Este temario fue calendarizado exitosamente")
        win.destroy()

    def calendarizarUI(self,event=None):
        self.cal_conf_view=CalendarConfig()
        self.cal_conf_view.boton.configure(command=self.calendarizar)
        self.cal_conf_view.mainloop()
        # calendarizarModelo(self.model,'Refactoring horario','29-06-2020',16)
        # messagebox.showinfo(title="Hecho", message="Este temario fue calendarizado exitosamente")
    def configurarCalendario(self,event=None):
        print("Se va a configurar esa cosa")
