from .ui_tab_temario import Ui_tab_temario
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime
from controllers.new.utils import dias,dia2Num, dia2Str
import uuid
class WidTabTemario(QtWidgets.QWidget,Ui_tab_temario):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.set_catalog()
        self.bind_signals()
        self.id=str(uuid.uuid4())
        self.model=None

    def set_model(self,model):
        self.model=model

    def set_catalog(self):
        self.color_box.addItems(["Rojo","Verde","Azul","Amarillo"])
        self.dia_box.addItems(["Lu","Ma","Mi","Ju","Vi","Sa"])

    def bind_signals(self):
        self.horario_box.currentIndexChanged.connect(self.set_current_horario)
        self.tema_box.currentIndexChanged.connect(self.set_current_tema)
        self.btn_guardar.pressed.connect(self.read_temario)

    def set_form(self):
        self.materia_in.insert(self.model.materia)
        self.materia_in.setCursorPosition(0)
        self.materia_in.setToolTip(self.model.materia)
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
        try:
            current_horario=self.model.horarios[index]
        except IndexError:
            if index!=0:
                print("ERROR")
            return
        self.dia_box.setCurrentIndex(current_horario.dia)
        self.hora_inicio_in.setTime(QTime(current_horario.horaInicio))
        self.hora_fin_in.setTime(QTime(current_horario.horaFin))

    def set_current_tema(self,index):
        print(f"Current tema changed?{index}")
        try:
            current_tema=self.model.temas[index]
        except IndexError:
            if index!=0:
                print("Error")
            return

        self.subtemas_list.clear()
        self.nombre_tema_in.clear()
        self.num_tema_in.setValue(current_tema.numero)
        self.duracion_tema_in.setValue(current_tema.duracion)
        self.nombre_tema_in.insert(current_tema.tema)
        self.nombre_tema_in.setCursorPosition(0)
        subtemas=[subtema.nombre for subtema in current_tema.subtemas]
        self.subtemas_list.addItems(subtemas)

    def read_temario(self):
        self.model.materia=self.materia_in.text()
        self.model.salon=self.salon_in.text()
        self.model.color=self.color_box.currentIndex()



    def clear_form(self):
        self.clear_header()
        self.clear_horario()
        self.clear_temas()

    def clear_header(self):
        self.materia_in.clear()
        self.salon_in.clear()
        self.color_box.setCurrentIndex(0)

    def clear_horario(self):
        self.horario_box.clear()
        self.dia_box.setCurrentIndex(0)
        self.hora_inicio_in.setTime(QTime(0,0))
        self.hora_fin_in.setTime(QTime(0,0))

    def clear_temas(self):
        self.tema_box.clear()
        self.subtemas_list.clear()
        self.num_tema_in.setValue(0)
        self.duracion_tema_in.setValue(0)
        self.nombre_tema_in.clear()
