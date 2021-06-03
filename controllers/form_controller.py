from .utils import dias,dia2Num, dia2Str
from PyQt5.QtCore import QTime
# dias=["lu","ma","mi","ma","ju","vi","sa"]
# dia2Str=lambda numDia: dias[numDia].title()
# dia2Num=lambda dia:dias.index(dia.lower())
class FormController:
    def form_bind_signals(self):
        self.horario_box.currentIndexChanged.connect(self.set_current_horario)
        self.tema_box.currentIndexChanged.connect(self.set_current_tema)

    def set_form(self):
        self.form_bind_signals()

        self.materia_in.insert(self.model.materia)
        self.materia_in.setCursorPosition(0)
        self.materia_in.setToolTip(self.model.materia)
        print(self.materia_in.toolTip)
        self.salon_in.insert(self.model.salon)
        # self.color_in.setCurrentText(self.model.color)

        self.color_box.setCurrentIndex(self.model.color)
        i=0
        for horario in self.model.horarios:
            self.horario_box.insertItem(i,dia2Str(horario.dia))
            i=i+1
        self.set_current_horario(0)
        i=0
        for tema in self.model.temas:
            self.tema_box.insertItem(i,str(tema.numero))
            i=i+1
        self.set_current_tema(0)

    def set_current_horario(self,index):
        current_horario=self.model.horarios[index]
        self.dia_box.setCurrentIndex(current_horario.dia)
        self.hora_inicio_in.setTime(QTime(current_horario.horaInicio))
        self.hora_fin_in.setTime(QTime(current_horario.horaFin))

    def set_current_tema(self,index):
        print(f"Current tema changed?{index}")
        current_tema=self.model.temas[index]
        self.subtemas_list.clear()
        self.nombre_tema_in.clear()
        self.num_tema_in.setValue(current_tema.numero)
        self.duracion_tema_in.setValue(current_tema.duracion)
        self.nombre_tema_in.insert(current_tema.tema)
        self.nombre_tema_in.setCursorPosition(0)
        subtemas=[subtema.nombre for subtema in current_tema.subtemas]
        self.subtemas_list.addItems(subtemas)
