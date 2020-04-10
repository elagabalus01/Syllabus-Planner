from tkinter import *
from tkinter.ttk import *

class FormularioTemas(Frame):
    def __init__(self,master,_nombre,**options):
        self.nombreWitget=_nombre
        super().__init__(master,**options)
        self.__initWindow()
    def __initWindow(self):
        self.formularioTema=Frame(self)
        self.formularioTema.grid(row=1,column=0,columnspan=3,sticky='w')
        
        Label(self.formularioTema,text="Número").grid(row=0,column=0,sticky='w')
        self.numero=Entry(self.formularioTema,width=5)
        self.numero.grid(row=0,column=1,sticky='w')

        Label(self.formularioTema,text="Duracion").grid(row=1,column=0,sticky='w')
        self.duracion=Entry(self.formularioTema,width=5)
        self.duracion.grid(row=1,column=1,sticky='w')

        Label(self.formularioTema,text="Nombre").grid(row=2,column=0,sticky='w')
        self.titulo=Entry(self.formularioTema,width=60)
        self.titulo.grid(row=2,column=1,sticky='w')

        self.entradaSubtema=Entry(self,width=35)
        self.entradaSubtema.grid(row=2,column=0,columnspan=3,sticky="nsew")

        self.subtemas=Listbox(self,font=("Helvetica",11))
        self.subtemas.grid(row=3,column=0,columnspan=3,sticky="nsew")

        self.eliminar=Button(self,text="Eliminar")
        self.eliminar.grid(row=4,column=0)

        self.limpiar=Button(self,text="Limpiar")
        self.limpiar.grid(row=4,column=1)

        self.agregar=Button(self,text="Agregar")
        self.agregar.grid(row=4,column=2)

        self.temaMenu=Frame(self)
        self.temaMenu.grid(row=0,column=0,sticky='w')

        Label(self.temaMenu,text="Tema: ").grid(row=0,column=0,sticky='w')
        self.currentTema=StringVar()
        self.temas=OptionMenu(self.temaMenu,self.currentTema,None)
        self.temas.grid(row=0,column=1,sticky='w')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)