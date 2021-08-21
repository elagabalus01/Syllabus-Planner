from PyQt5.QtGui import QKeySequence
from PyQt5 import QtCore
from .HorarioController import HorarioController
from .TemaController import TemaController
from .serializeController import SerializeController
from .StateController import StateController
from controllers.new.utils import dias,dia2Num, dia2Str

class TabController():
    def __init__(self,view,model,clipboard):
        self.clipboard=clipboard
        self.model=model
        self.view=view
        self.id=self.view.id
        self.tema_ctrl=TemaController(self.view,self.model,clipboard)
        self.horario_ctrl=HorarioController(self.view,self.model)
        self.bind()
        self.serializer=SerializeController(self.model,self.view)
        self.stater=StateController(self.model)
        self.stater.add_state(self.model)
        self.state=0

    def bind(self):
        self.view.btn_guardar.pressed.connect(self.read_form)
        self.view.materia_in.editingFinished.connect(self.set_materia)
        self.view.salon_in.editingFinished.connect(self.set_salon)
        self.view.color_box.currentIndexChanged.connect(self.set_color)

        # self.view.btn_guardar.pressed.connect(self.read_form)
        self.view.keyPressEvent=self.test_method

    def test_method(self,event):

        if event.modifiers()==QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Z:
            print("Regresando estado")
            state=self.stater.get_previus_state()
            if state:
                print(id(state))
                self.model=state
                self.clear_form()
                self.set_form()

            # self.set_state(self.state)
        elif event.modifiers()==QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_Y:
            self.state=self.state+1
            # self.set_state(self.state)


    def set_form(self):
        self.view.materia_in.insert(self.model.materia)
        self.view.materia_in.setCursorPosition(0)
        self.view.materia_in.setToolTip(self.model.materia)
        self.view.salon_in.insert(self.model.salon)
        if self.model.color:
            self.view.color_box.setCurrentIndex(self.model.color)
        i=0
        for horario in self.model.horarios:
            self.view.horario_box.insertItem(i,dia2Str(horario.dia))
            i=i+1
        self.horario_ctrl.set_current_horario(0)
        i=0
        for tema in self.model.temas:
            self.view.tema_box.insertItem(i,str(tema.numero))
            i=i+1
        if len(self.model.temas)>0:
            self.tema_ctrl.set_current_tema(0)

    def set_materia(self):
        self.model.materia=self.view.materia_in.text()
        self.model.notify_observers(msg="ADD_STATE")

    def set_salon(self):
        self.model.salon=self.view.salon_in.text()
        self.model.notify_observers(msg="ADD_STATE")

    def set_color(self,index):
        self.model.color=index
        self.model.notify_observers(msg="ADD_STATE")

    def read_form(self):
        self.set_materia()
        self.set_salon()
        self.set_color(self.view.color_box.currentIndex())
        self.model.notify_observers(msg="SAVE")

    def clear_form(self):
        self.clear_header()
        self.clear_horario()
        self.clear_temas()

    def clear_header(self):
        self.view.materia_in.clear()
        self.view.salon_in.clear()
        self.view.color_box.setCurrentIndex(0)

    def clear_horario(self):
        self.view.horario_box.clear()
        self.view.dia_box.setCurrentIndex(0)
        self.view.hora_inicio_in.setTime(QtCore.QTime(0,0))
        self.view.hora_fin_in.setTime(QtCore.QTime(0,0))

    def clear_temas(self):
        self.view.tema_box.clear()
        self.view.subtemas_list.clear()
        self.view.num_tema_in.setValue(0)
        self.view.duracion_tema_in.setValue(0)
        self.view.nombre_tema_in.clear()
