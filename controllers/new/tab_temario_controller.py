from models import Horario
from .utils  import dia2Str
from PyQt5.QtCore import pyqtSlot,QObject

class TabTemarioController(QObject):
    def __init__(self,tab,model):
        super().__init__()
        self.view=tab
        self.model=model
        self.bind_slots()

    def bind_slots(self):
        print("Binding")
        self.view.btn_agregar_horario.pressed.connect(self.agregar_horario)
        self.view.btn_eliminar_horario.pressed.connect(self.eliminar_horario)

    @pyqtSlot()
    def eliminar_horario(self):
        print("Eliminando horario")
        index=self.view.horario_box.currentIndex()
        self.view.horario_box.removeItem(index)
        #REMOVING FROM MODEL NOT SECURE
        del self.model.horarios[index]
        self.model.write()

    @pyqtSlot()
    def agregar_horario(self):
        print("Agregando horario")
        num_dia=self.view.dia_box.currentIndex()
        print(f"Num dia{num_dia}")
        qtime2str=lambda hora:f"{hora.hour()}:{hora.minute()}"
        str_hora_inicio=qtime2str(self.view.hora_inicio_in.time())
        str_hora_fin=qtime2str(self.view.hora_fin_in.time())
        new_horario=Horario(num_dia,str_hora_inicio,str_hora_fin)
        self.model.horarios.append(new_horario)
        num_horarios=self.view.horario_box.count()
        self.view.horario_box.insertItem(num_horarios,dia2Str(num_dia))
        self.model.write()
