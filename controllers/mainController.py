import sys
sys.path.append("..")
from tkinter import BOTH, END, LEFT,filedialog
from tkinter import messagebox
from views.view import View,EditWindow
from models.Materia import Materia
from models.Tema import Tema
from models.Horario import Horario
from .calendarizadorController import CalendarizadorController

def limpiarCadena(string):
    string=string.capitalize()
    string=string.replace('\n','')
    string=string.replace('\t','')
    string=string.replace('\r','')
    return string
def validarEntero(valor):
    if not valor:
        return True
    if valor.isdigit():
        return True
    else:
        messagebox.showinfo(title="Prueba", message="No es un número")
        return False
def validarFlotante(valor):
    if not valor:
        return True
    try:
        float(valor)
        return True
    except Exception:
        messagebox.showinfo(title="Prueba", message="No es un número flotante")
        return False
def validarLista(valor):
    if not valor:
        return True
    valor=valor[-1:]
    if valor.isdigit() or valor == ',':
        return True
    else:
        print(valor)
        messagebox.showinfo(title="Prueba", message="No es un número")
        return False
class MainController(CalendarizadorController):
    """docstring for MainController"""
    def __init__(self):
        super().__init__()
        # self.model.recoverJson('C:/Users/elagabalus/3D Objects/prueba.json')
        ''' PRUEBAS '''
        self.configurarComandos()
        # self.setForm()
        ''' PRUEBAS '''
    def configurarComandos(self):
        self.view.guardar.configure(command=self.guardar)
        
        self.view.formHorarios.agregarHorario.configure(command=self.agregarHorario)

        self.view.formTemas.eliminar.configure(command=self.eliminarTema)
        self.view.formTemas.limpiar.configure(command=self.vaciarTema)
        self.view.formTemas.agregar.configure(command=self.agregarTema)

        self.view.formTemas.titulo.bind('<Return>',self.agregarTema)
        self.view.formTemas.entradaSubtema.bind('<Return>',self.agregarSubtema)
        self.view.formTemas.subtemas.bind('<Double-Button-1>',self.editarSubtema)
        self.view.formTemas.subtemas.bind('<Delete>',self.eliminarSubtema)

        self.view.menu.menuArchivo.add_command(label="Abrir",command=self.abrir)
        self.view.menu.menuArchivo.add_command(label="Guardar como",command=self.guardarComo)
        self.view.menu.menuArchivo.add_command(label="Cerrar",command=self.cerrar)

        self.view.bind('<Control-q>',self.cerrar)
        self.view.bind('<Control-o>',self.abrir)
        self.view.bind('<Control-w>',self.cerrar)
        self.view.bind('<Control-s>',self.guardar)

        self.validaciones()

    def validaciones(self):
        # entry['validatecommand'] = (entry.register(testVal),'%P','%d')
        vE = self.view.register(validarEntero)
        vF = self.view.register(validarFlotante)
        self.view.formDatos.color.configure(validate="key",validatecommand=(vE,'%P'))
        self.view.formTemas.numero.configure(validate="key",validatecommand=(vE,'%P'))
        self.view.formTemas.duracion.configure(validate="key",validatecommand=(vF,'%P'))

    def quitarValidaciones(self):
        self.view.formDatos.color.configure(validatecommand=None)
        self.view.formTemas.numero.configure(validatecommand=None)
        self.view.formTemas.duracion.configure(validatecommand=None)
    
    def abrir(self,event=None):
        try:
            ftypes = [('json files', '*.json'), ('All files', '*')]
            filePath = filedialog.askopenfilename(filetypes=ftypes,initialdir="~/Documents")
            self.file=filePath
            self.view.title(self.file)
            self.model=Materia()
            self.model.recoverJson(filePath)
            self.setForm()
            self.updateTemas()
            self.updateHorarios()
        except FileNotFoundError:
            print("Se canceló")
        except:
            messagebox.showinfo(title="Error", message="No se pudo abrir el archivo")
   
    def guardar(self,event=None):
        self.readForm()
        if self.file:
            with open(self.file,'w',encoding="utf8") as file:
                file.write(self.model.toJson())
        else:
            self.guardarComo()

    def guardarComo(self):
        try:
            file=filedialog.asksaveasfile(mode='w',
                defaultextension=".json",initialdir="~/Documents",filetypes=(("json file", ".json"),("todo", "*")))
            self.file=file.name
            with open(self.file,'w') as file:
                file.write(self.model.toJson())
            self.updateViewNombre()
        except AttributeError:
            print("No se selecciono nombre para el archivo")
    
    def cerrar(self,event=None) :
        self.model=Materia()
        self.view.title('Nuevo')
        self.file=None
        self.view.formTemas.temas["menu"].delete(0, "end")
        self.view.formTemas.currentTema.set('--')
        self.quitarValidaciones()
        self.vaciarFomrulario()
        self.vaciarHorario()
        self.vaciarTema()
        self.validaciones()

    def updateViewNombre(self):
        self.view.title(self.file)

    def setForm(self):
        self.view.formDatos.materia.insert(0,self.model.materia)
        self.view.formDatos.salon.insert(0,self.model.salon)
        self.view.formDatos.color.insert(0,self.model.color)
    
    def readForm(self):
        try:
            self.model.materia=limpiarCadena(self.view.formDatos.materia.get())
            if not len(self.model.materia)>0:
                raise Exception
            try:
                self.model.salon=self.view.formDatos.salon.get()
                if not len(self.model.salon)>0:
                    raise Exception
                try:
                    self.model.color=int(self.view.formDatos.color.get())
                except ValueError as e:
                    messagebox.showinfo(title="Prueba", message="Es necesario escribir el número del color")
            except Exception as e:
                messagebox.showinfo(title="Prueba", message="Es necesario escribir el nombre del salon")
        except Exception as e:
            messagebox.showinfo(title="Prueba", message="Es necesario escribir el nombre de la materia")
    
    def vaciarFomrulario(self):
        self.view.formDatos.materia.delete(0,END)
        self.view.formDatos.salon.delete(0,END)
        self.view.formDatos.color.delete(0,END)
    
    ''' CONTRUYENTO HORARIOS '''
    def readHorario(self):
        listaHorarios=[horario.dia for horario in self.model.horarios]
        dia=self.view.formHorarios.dia.get()
        horaInicio=self.view.formHorarios.horaInicio.get()
        horaFin=self.view.formHorarios.horaFin.get()
        if dia not in listaHorarios:
            print("Aun no existia el horario")
            nuevoHorario=Horario()
            nuevoHorario.dia=dia
            nuevoHorario.horaInicio=horaInicio
            nuevoHorario.horaFin=horaFin
            self.model.horarios.append(nuevoHorario)
            self.view.formHorarios.horarios["menu"].add_command(label=nuevoHorario.dia,command=lambda value=nuevoHorario.dia: self.setHorario(value))
        else:
            for horario in self.model.horarios:
                if dia == horario.dia:
                    horario.dia=dia
                    horario.horaInicio=horaInicio
                    horario.horaFin=horaFin
        self.view.formTemas.currentTema.set('--')

    def vaciarHorario(self):
        self.view.formHorarios.dia.delete(0,END)
        self.view.formHorarios.horaInicio.delete(0,END)
        self.view.formHorarios.horaFin.delete(0,END)
    
    def agregarHorario(self,event=None):
        self.readHorario()
        self.vaciarHorario()
        self.guardar()

    def setHorario(self,dia):
        for horario in self.model.horarios:
            if horario.dia==dia:
                self.view.formHorarios.currentHorario.set(horario.dia)
                
                self.view.formHorarios.dia.delete(0,END)
                self.view.formHorarios.dia.insert(0,horario.dia)

                self.view.formHorarios.horaInicio.delete(0,END)
                self.view.formHorarios.horaInicio.insert(0,horario.horaInicio)

                self.view.formHorarios.horaFin.delete(0,END)
                self.view.formHorarios.horaFin.insert(0,horario.horaFin)
    
    def updateHorarios(self):
        listaHorarios=[horario.dia for horario in self.model.horarios]
        self.view.formHorarios.horarios["menu"].delete(0, "end")
        self.view.formHorarios.currentHorario.set('--')
        for string in listaHorarios:
            self.view.formHorarios.horarios["menu"].add_command(label=string,command=lambda value=string: self.setHorario(value))
    ''' CONTRUYENTO HORARIOS '''


    def setTema(self,numTema):
        for tema in self.model.temas:
            if tema.numero==numTema:
                self.view.formTemas.currentTema.set(tema.numero)

                self.view.formTemas.numero.delete(0,END)
                self.view.formTemas.numero.insert(0,tema.numero)

                self.view.formTemas.titulo.delete(0,END)
                self.view.formTemas.titulo.insert(0,tema.tema)

                self.view.formTemas.duracion.delete(0,END)
                self.view.formTemas.duracion.insert(0,tema.duracion)

                self.view.formTemas.subtemas.delete(0,END)
                for subtema in tema.subtemas:
                    self.view.formTemas.subtemas.insert(END,subtema)
    
    def readTema(self):
        listaTemas=[tema.numero for tema in self.model.temas]
        try:
            numero=int(self.view.formTemas.numero.get())
            try:
                duracion=float(self.view.formTemas.duracion.get())
                try:
                    nombre=limpiarCadena(self.view.formTemas.titulo.get())
                    if not len(nombre)>0:
                        raise Exception
                    subtemas=list(self.view.formTemas.subtemas.get(0,END))
                    if numero not in listaTemas:
                        print("Aun no existia")
                        nuevoTema=Tema()
                        nuevoTema.numero=numero
                        nuevoTema.duracion=duracion
                        nuevoTema.tema=nombre
                        nuevoTema.subtemas=subtemas
                        self.model.temas.append(nuevoTema)
                        self.view.formTemas.temas["menu"].add_command(label=nuevoTema.numero,command=lambda value=nuevoTema.numero: self.setTema(value))
                    else:
                        for tema in self.model.temas:
                            if numero == tema.numero:
                                tema.numero=numero
                                tema.duracion=duracion
                                tema.tema=nombre
                                tema.subtemas=subtemas
                    self.view.formTemas.currentTema.set('--')
                except Exception as e:
                    messagebox.showinfo(title="Prueba", message="El nombre debe ser mayor")
            except ValueError:
                messagebox.showinfo(title="Prueba", message="Aún no se define la duracion")
        except ValueError as e:
            messagebox.showinfo(title="Prueba", message="Aún no se define el numero del tema")
    
    def agregarTema(self,event=None):
        self.readTema()
        self.vaciarTema()
        self.guardar()

    def updateTemas(self):
        listaTemas=[x.numero for x in self.model.temas]
        self.view.formTemas.temas["menu"].delete(0, "end")
        self.view.formTemas.currentTema.set('--')
        for string in listaTemas:
            self.view.formTemas.temas["menu"].add_command(label=string,command=lambda value=string: self.setTema(value))
    
    def agregarSubtema(self,x):
        self.view.formTemas.subtemas.insert(END,self.view.formTemas.entradaSubtema.get())
        self.view.formTemas.entradaSubtema.delete(0,END)
        self.readTema()
        self.guardar()

    def vaciarTema(self):
        self.view.formTemas.numero.delete(0,END)
        self.view.formTemas.duracion.delete(0,END)
        self.view.formTemas.titulo.delete(0,END)
        self.view.formTemas.subtemas.delete(0,END)
    
    def eliminarSubtema(self,x):
        posicion=self.view.formTemas.subtemas.curselection()[0]
        self.view.formTemas.subtemas.delete(posicion)

    def editarSubtema(self,x):
        posicion=self.view.formTemas.subtemas.curselection()[0]
        ventanaEdicion=EditWindow()
        ventanaEdicion.entrada.insert(END,self.view.formTemas.subtemas.get(posicion))
        def aceptarEdicionSubtema():
            self.view.formTemas.subtemas.delete(posicion)
            self.view.formTemas.subtemas.insert(posicion,ventanaEdicion.entrada.get("1.0",END+"-1c"))
            self.readTema()
            self.guardar()
            ventanaEdicion.destroy()
        ventanaEdicion.aceptar.configure(command=aceptarEdicionSubtema)

    
    def eliminarTema(self):
        try:
            numero=int(self.view.formTemas.numero.get())
            for tema in self.model.temas:
                if numero == tema.numero:
                    self.model.temas.remove(tema)
                    self.updateTemas()
                    self.guardar()
        except ValueError:
            print("No se selecciono un tema")
        self.vaciarTema()
    
    def run(self):
        self.view.mainloop()
def main():
    MainController().run()
if __name__=="__main__":
    main()
