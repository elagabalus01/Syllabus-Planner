from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
if __name__=="__main__":
    from datosMateria import FormularioDatos
    from temas import FormularioTemas
    from BarMenu import BarMenu
    from horarios import FormularioHorarios
else:
    from .datosMateria import FormularioDatos
    from .temas import FormularioTemas
    from .BarMenu import BarMenu
    from .horarios import FormularioHorarios

class View(Tk):
    def __init__(self,*args, **kwargs):
        Tk.__init__(self,*args, **kwargs)
        self.__initWindow()
    def __initWindow(self):

        self.formDatos=FormularioDatos(self,"Datos")
        self.formDatos.grid(row=0,column=0,columnspan=2,sticky='news')

        self.formHorarios=FormularioHorarios(self,"Horarios")
        self.formHorarios.grid(row=1,column=0,columnspan=2,sticky='news')
    
        self.formTemas=FormularioTemas(self,"Temas")
        self.formTemas.grid(row=2,column=0,rowspan=2,sticky='news')

        self.guardar=Button(self,text="Guardar")
        self.guardar.grid(row=3,column=1,sticky='e')

        self.grid_columnconfigure(0, weight=11)
        self.grid_columnconfigure(1, weight=1)


        self.menu=BarMenu(self)
        self.config(menu=self.menu)
class EditWindow(Tk):
    def __init__(self,*args, **kwargs):
        Tk.__init__(self,*args, **kwargs)
        self.__initWindow()
    def __initWindow(self):
        self.title("Editar")
        self.geometry("700x200+400+300")
        editFrame=Frame(self,width=200,height=20)
        editFrame.grid(column=0,sticky="nsew")

        self.entrada=scrolledtext.ScrolledText(editFrame,undo=True,width=50,height=9,wrap='none')
        self.entrada.grid(column=0, sticky="nsew")
        # editEntry.insert(END,elemento)
        
        self.grid_columnconfigure(0, weight=1)
        editFrame.grid_columnconfigure(0,weight=1)

        # def replace():
        #     self.listBox.delete(posicion)
        #     self.listBox.insert(posicion,editEntry.get("1.0",END+"-1c"))
        #     editWindow.destroy()
        self.aceptar=Button(editFrame,text="Aceptar")
        self.aceptar.grid(row=1)

def main():
    app=View()
    app.title("Temario")
    app.geometry("546x440+480+150")
    app.mainloop()
    
# def main():
#     app=EditWindow()
#     app.mainloop()

if __name__=="__main__":
    main()