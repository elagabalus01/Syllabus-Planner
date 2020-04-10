from json import load
from datetime import datetime,date
try:
    from .Tema import Tema
    from .Subtema import Subtema
    from .Horario import Horario
except (ModuleNotFoundError,ImportError):
    from Tema import Tema
    from Subtema import Subtema
    from Horario import Horario
class Materia(object):
    ''' Contructor a partir json '''
    dicDias={"Lu":0,"Ma":1,"Mi":2,"Ju":3,"Vi":4,"Sa":5,"Do":6}
    def __init__(self,jsonFile):
        with open(jsonFile,'r',encoding="UTF-8") as file:
            dic=load(file)
            self.nombre=dic["materia"]
            self.salon=dic["salon"]
            self.color=dic["color"]
            self.horarios=[]
            dicHorarios=dic["horarios"]
            for horario in dicHorarios:
                self.horarios.append(Horario(horario["dia"],horario["horaInicio"],horario["horaFin"]))
            self.temas=[]
            for tema in dic["temas"]:
                t=Tema()
                t.setNumero(tema["numero"])
                t.setNombre(tema["tema"])
                t.setHoras(tema["duracion"])
                subtemas=[]
                for subtema in tema["subtemas"]:
                    s=Subtema()
                    s.setNombre(subtema)
                    subtemas.append(s)
                t.setSubtemas(subtemas)
                self.temas.append(t)
            self.duracionPromedio=0
            for i in self.horarios:
                self.duracionPromedio+=(datetime.combine(date.min,i.getHoraFin())-datetime.combine(date.min,i.getHoraInicio())).seconds/3600
            self.duracionPromedio/=len(self.horarios)

    ''' setters '''
    def setNombre(self,_nombre):
        self.nombre=_nombre
    def setSalon(self,_salon):
        self.salon=_salon
    def setTemas(self,_temas):
        self.temas=_temas
    def setColor(self,_color):
        self.color=_color
    ''' getters '''
    def getNombre(self):
        return self.nombre
    def getSalon(self):
        return self.salon
    def getTemas(self):
        return self.temas
    def getColor(self):
        return self.color
    ''' Método string '''
    def __str__(self):
        aux=""
        for tema in self.temas:
            aux+=str(tema)+'\n'
        return aux
    ''' ordenar En Calendario calendario es el calendario completo '''
    def ordenarEnCalendario(self,calendario):
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

    ''' imprimir objeto completo '''
    def printFullObject(self):
        print(f"{self.nombre} en el salon {self.salon}")
        for clase in self.clases:
            print(clase)
        print(self.__str__())

def main():
    materia=Materia("C:/Users/elagabalus/3D Objects/programming/python/calendarizador/dataTypes/quim.json")
    materia.printFullObject()
if __name__=="__main__":
    main()