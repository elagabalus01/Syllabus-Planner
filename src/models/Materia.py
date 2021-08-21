import json
import copy
from datetime import datetime,date,time
try:
    from .Tema import Tema
    from .Subtema import Subtema
    from .Horario import Horario
except (ModuleNotFoundError,ImportError):
    from Tema import Tema
    from Subtema import Subtema
    from Horario import Horario
from models.infrastructure.observable import Observable
class Materia(Observable):
    # Constructor
    def __init__(self):
        super().__init__()
        self.materia = None
        self.salon = None
        self.color=None
        self.horarios = []
        self.temas = []
        self.file=None

    # Se abre un archivo json
    def recoverJson(self,jsonFile):
        self.file=jsonFile
        with open(jsonFile,'r',encoding="utf-8") as file:
            dic=json.load(file)
            self.materia=dic["materia"]
            self.salon=dic["salon"]
            dicHorarios=dic["horarios"]
            for horario in dicHorarios:
                h=Horario(horario["dia"],horario["horaInicio"],horario["horaFin"])
                self.horarios.append(h)
            self.color=dic["color"]
            temas=[]
            dicTemas=dic["temas"]
            for tema in dicTemas:
                t=Tema()
                t.numero=(tema["numero"])
                t.tema=(tema["tema"])
                t.duracion=(tema["duracion"])
                dicSubtemas=tema["subtemas"]
                subtemas=[]
                for subtema in dicSubtemas:
                    s=Subtema()
                    s.setNombre(subtema)
                    subtemas.append(s)
                t.subtemas=(subtemas)
                temas.append(t)
            self.temas=temas
        self.duracionPromedio=0

    def write(self):
        with open(self.file,'w',encoding="utf-8") as file:
            file.write(self.toJson())

    def delete_tema(self,id):
        tema=self.getTemaById(id)
        if tema:
            self.temas.remove(tema)

    def getTemaById(self,id):
        for tema in self.temas:
            if tema.numero==id:
                return tema
        return False

    def agregar_tema(self,nuevo_tema):
        ''' Si encuentra un tema con el mismo id regresa falso
        pero debería actualizar el tema
        si logra insertarlo regresa verdadero
        '''
        for tema in self.temas:
            if nuevo_tema.numero == tema.numero:
                return False
        self.temas.append(nuevo_tema)
        return True


    def toJson(self):
        self.temas.sort(key=lambda x:x.numero )
        return json.dumps(self,default=json_decoder,indent=4,ensure_ascii=False)
    ''' setters '''
    def setNombre(self,_nombre):
        self.materia=_nombre
    def setSalon(self,_salon):
        self.salon=_salon
    def setTemas(self,_temas):
        self.temas=_temas
    def setColor(self,_color):
        self.color=_color
    ''' getters '''
    def getNombre(self):
        return self.materia
    def getSalon(self):
        return self.salon
    def getTemas(self):
        return self.temas
    def getColor(self):
        return self.color

    def __str__(self):
        ''' Método string '''
        aux=""
        for tema in self.temas:
            aux+=str(tema)+'\n'
        return aux

    def ordenarEnCalendario(self,calendario):
        ''' ordenar En Calendario calendario es el calendario completo '''
        for i in self.horarios:
            self.duracionPromedio+=(datetime.combine(date.min,i.getHoraFin())-datetime.combine(date.min,i.getHoraInicio())).seconds/3600
        try:
            self.duracionPromedio/=len(self.horarios)
        except ZeroDivisionError as e:
            pass
        timeOut=[]
        fechasDeClase=[x for x in calendario if x.weekday() in [x.dia for x in self.horarios]]
        self.fechasDeClase=fechasDeClase
        diasDeClase=len(fechasDeClase)
        inicio=0
        for tema in self.temas:
            intervalo=round(tema.getHoras()/self.duracionPromedio)
            if inicio < diasDeClase-1:
                tema.setFechaInicio(fechasDeClase[inicio])
                if inicio+intervalo < diasDeClase-1:
                    tema.setFechaFin(fechasDeClase[inicio+intervalo])
                    tema.ordenarEnCalendario(fechasDeClase[inicio:inicio+intervalo],self.duracionPromedio)
                else:
                    tema.setFechaFin(fechasDeClase[diasDeClase-1])
                    tema.ordenarEnCalendario(fechasDeClase[inicio:diasDeClase-1],self.duracionPromedio)
            else:
                timeOut.append(tema)
            inicio+=intervalo
        for tema in timeOut:
            print(f"El tema {tema.getNombre()} no de podra tomar")
            self.temas.remove(tema)

    def printFullObject(self):
        ''' imprimir objeto completo '''
        print(f"{self.materia} en el salon {self.salon}")
        for horario in self.horarios:
            print(horario)
        print(self.__str__())

def json_decoder(objeto):
    if isinstance(objeto,time):
        return f"{objeto.hour:02}:{objeto.minute:02}"
    if isinstance(objeto,Materia):
        return {
            "materia":objeto.materia,
            "salon":objeto.salon,
            "color":objeto.color,
            "horarios":objeto.horarios,
            "temas":objeto.temas
        }
    if isinstance(objeto,Tema):
        return {
            "numero":objeto.numero,
            "tema":objeto.tema,
            "duracion":objeto.duracion,
            "subtemas":objeto.subtemas

        }
    if isinstance(objeto,Subtema):
        return objeto.nombre
    else:
        return objeto.__dict__

def main():
    materia=Materia()
    materia.recoverJson("C:/Users/elagabalus/3D Objects/temarios/7s/diseño.json")
    # materia.printFullObject()
    print(materia.toJson())
if __name__=="__main__":
    main()
