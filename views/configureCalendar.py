from tkinter import *
from tkinter.ttk import *

class CalendarConfig(Toplevel):
    def __init__(self,*args, **kwargs):
        Toplevel.__init__(self,*args, **kwargs)
        self.__initWindow()
    def __initWindow(self):
        self.title("Configuracion del calendario")
        self.geometry("500x100+400+300")
        
        Label(self,text='Nombre del calendario').grid(column=0,row=0)
        
        self.calendario=Entry(self,width=60)
        self.calendario.grid(column=1,row=0)
        self.grid_columnconfigure(0, weight=0)
        
        Label(self,text='Desde el dia').grid(column=0,row=1)
        self.fecha_inicio=Entry(self,width=30)
        self.fecha_inicio.grid(column=1,row=1,stick='w')
        
        Label(self,text='N° de semanas').grid(column=0,row=2)
        self.semanas=Spinbox(self,width=3,from_=0, to=100)
        self.semanas.grid(column=1,row=2,stick='w')
        
        self.boton=Button(self,text="Calendarizar!")
        self.boton.grid(column=0,row=3,columnspan=2)

if __name__=='__main__':
    CalendarConfig().mainloop()
