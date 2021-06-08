from models import Materia
from .TabController import TabController

class TabListController():
    def __init__(self,view):
        # [(WidTabTemario,Materia)]
        self.tabs=[]
        self.view=view

    def addWidget(self,new_WidTabTemario,file):
        model=Materia()

        if file:
            model.recoverJson(file)
            new_WidTabTemario.set_model(model)
        ctrl=TabController(new_WidTabTemario,model)
        self.tabs.append(ctrl)
        if ctrl.model.file:
            ctrl.set_form()


    def get_model_by_id(self,id):
        i=0
        for tab in self.tabs:
            if tab.id==id:
                return tab.model
            else:
                i=i+1
        print("No se encontro el widget con ese ID")
        return -1

    def find_widget_index(self,id)->int:
        i=0
        for tab in self.tabs:
            if tab.id==id:
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

    def close_tab(self,index):
        id=self.view.tab_widget.widget(index).id
        self.delete_widget(id)
        self.view.tab_widget.removeTab(index)
        if self.view.tab_widget.count()==0:
            self.view.actionCalendarizar.setDisabled(True)
