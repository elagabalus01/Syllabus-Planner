from tkinter import *
from tkinter.ttk import *

class FormularioDatos(Frame):
    def __init__(self,master,_nombre,**options):
        self.nombreWitget=_nombre
        super().__init__(master,**options)
        self.__initWindow()
    def __initWindow(self):
        self.materiaLabel=LabelFrame(self,text="Materia",height=100,width=200)
        self.materiaLabel.grid(row=0,column=0)
        self.materia=Entry(self.materiaLabel)
        self.materia.grid(row=0,column=0)

        self.salonLabel=LabelFrame(self,text="Salon",height=100,width=200)
        self.salonLabel.grid(row=0,column=1)
        self.salon=Entry(self.salonLabel)
        self.salon.grid(row=0,column=0)
        
        self.colorLabel=LabelFrame(self,text="Color",height=100,width=200)
        self.colorLabel.grid(row=0,column=2)
        self.color=Entry(self.colorLabel)
        self.color.grid(row=0,column=0)