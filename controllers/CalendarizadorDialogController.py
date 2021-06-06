from calendarizador import calendarizarModelo
class CalendarizadorDialogController():
    def __init__(self,view,model):
        self.view=view
        self.model=model
        self.bind_commands()

    def bind_commands(self):
        self.view.btn_calendarizar.pressed.connect(self.calendarizar)

    def calendarizar(self):
        # modelo,nombreCalendario,fechaInicio,semanasDuracion):
        nombre=self.view.cal_in.text()
        fecha_inicio=self.view.fecha_in.date().toString('dd-MM-yyyy')
        print(f"Inicio: {fecha_inicio}")
        num_semanas=self.view.semanas_in.value()
        calendarizarModelo(self.model,nombre,fecha_inicio,num_semanas)

    def run(self):
        self.view.exec()
