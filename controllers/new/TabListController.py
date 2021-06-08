from models import Materia
from .tab_temario_controller import TabTemarioController
from .TemaController import TemaController
class TabListController():
    def __init__(self):
        # [(WidTabTemario,Materia)]
        self.tabs=[]

    def addWidget(self,new_WidTabTemario,file):
        model=Materia()
        if file:
            model.recoverJson(file)
            new_WidTabTemario.set_model(model)
            new_WidTabTemario.set_form()
        ctrl=TabTemarioController(new_WidTabTemario,model)
        tema_ctl=TemaController(new_WidTabTemario,model)
        self.tabs.append(tema_ctl)
        self.tabs.append(ctrl)

    def get_model_by_id(self,id):
        i=0
        for tab in self.tabs:
            if tab.view.id==id:
                return tab.model
            else:
                i=i+1
        print("No se encontro el widget con ese ID")
        return -1

    def find_widget_index(self,id)->int:
        i=0
        for tab in self.tabs:
            if tab.view.id==id:
                return i
            else:
                i=i+1
        print("No se encontro el widget con ese ID")
        return -1

    def delete_widget(self,id:str):
        index=self.find_widget_index(id)
        if index!=-1:
            del self.tabs[index]
        else:
            print("No se encontrol el widget a eliminar")
