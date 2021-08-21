from models.infrastructure.observer import Observer
from PyQt5.QtWidgets import QFileDialog
class SerializeController(Observer):
    def __init__(self,observable,view):
        super().__init__(observable)
        self.view=view

    def notify(self, observable, *args, **kwargs):
        if kwargs['msg']=="SAVE":
            self.write_file(observable)

    def write_file(self,model):
        if model.file:
            print("Guardando")
            model.write()
        else:
            self.write_as(model)

    def write_as(self,model):
        print("Guardando como...")
        file_name=QFileDialog.getSaveFileName(self.view,"Guardar archivo")[0]
        model.file=file_name
        model.write()
        index=self.view.main_win.tab_widget.currentIndex()
        self.view.main_win.tab_widget.setTabText(index,file_name.split('/')[-1])
