import json
try:
    from Tema import Tema
    from Horario import Horario
except Exception as e:
    from .Tema import Tema
    from .Horario import Horario
class Materia(object):
    def __init__(self):
        self.materia = None
        self.salon = None
        self.color=None
        self.horarios = []
        self.temas = []
    def toJson(self):
        return json.dumps(self.__dict__,default=lambda o: o.__dict__,indent=4,ensure_ascii=False)
    def recoverJson(self,jsonFile):
        with open(jsonFile,'r',encoding="utf-8") as file:
            dic=json.load(file)
            self.materia=dic["materia"]
            self.salon=dic["salon"]
            dicHorarios=dic["horarios"]
            for horario in dicHorarios:
                h=Horario()
                h.horaInicio=horario["horaInicio"]
                h.horaFin=horario["horaFin"]
                h.dia=horario["dia"]
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
                    subtemas.append(subtema)
                t.subtemas=(subtemas)
                temas.append(t)
            self.temas=temas
if __name__=='__main__':
    file='C:/Users/elagabalus/3D Objects/programming/python/calendarizador/dataTypes/quim.json'
    m=Materia()
    m.recoverJson(file)
    print(m.toJson())
