from .HorarioController import HorarioController
from .TemaController import TemaController
from controllers.new.utils import dias,dia2Num, dia2Str
class TabController():
    def __init__(self,view,model):
        self.model=model
        self.view=view
        self.id=self.view.id
        self.tema_ctrl=TemaController(self.view,self.model)
        self.horario_ctrl=HorarioController(self.view,self.model)

    def set_form(self):
        self.view.materia_in.insert(self.model.materia)
        self.view.materia_in.setCursorPosition(0)
        self.view.materia_in.setToolTip(self.model.materia)
        self.view.salon_in.insert(self.model.salon)
        # self.color_in.setCurrentText(self.model.color)
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
        self.tema_ctrl.set_current_tema(0)
