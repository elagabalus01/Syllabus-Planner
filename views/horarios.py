from tkinter import *
from tkinter.ttk import *

class FormularioHorarios(Frame):
    def __init__(self,master,_nombre,**options):
        self.nombreWitget=_nombre
        super().__init__(master,**options)
        self.__initWindow()
    def __initWindow(self):
        self.currentHorario=StringVar()
        self.horarios=OptionMenu(self,self.currentHorario,None)
        self.horarios.grid(row=0,column=0,sticky='w')
        
        self.diaLabel=LabelFrame(self,text="Dia",height=100,width=100)
        self.diaLabel.grid(row=0,column=1)
        self.dia=Entry(self.diaLabel)
        self.dia.grid(row=0,column=0)

        self.horaInicioLabel=LabelFrame(self,text="Hora de inicio",height=100,width=200)
        self.horaInicioLabel.grid(row=0,column=2)
        self.horaInicio=Entry(self.horaInicioLabel)
        self.horaInicio.grid(row=0,column=0)

        self.horaFinLabel=LabelFrame(self,text="Hora de finalizacion",height=100,width=200)
        self.horaFinLabel.grid(row=0,column=3)
        self.horaFin=Entry(self.horaFinLabel)
        self.horaFin.grid(row=0,column=0)

        self.agregarHorario=Button(self,text="Agregar horario")
        self.agregarHorario.grid(row=0,column=5)
        
if __name__=="__main__":
    root=Tk()
    horarios=FormularioHorarios(root,"horarios")
    horarios.grid(row=0,column=0)
    root.mainloop()

