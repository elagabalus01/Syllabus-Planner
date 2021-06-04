from models import Materia
class TabController():
    def __init__(self):
        # [(WidTabTemario,Materia)]
        self.tabs=[]
    def addWidget(self,new_WidTabTemario,file):
        model=Materia()
        model.recoverJson(file)
        new_WidTabTemario.set_model(model)
        new_WidTabTemario.set_form()
        self.tabs.append((new_WidTabTemario,model))

    def find_widget_index(self,id)->int:
        i=0
        for tab in self.tabs:
            if tab[0].id==id:
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
