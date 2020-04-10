from re import findall
from datetime import time
class Horario(object):
    dicDias={"Lu":0,"Ma":1,"Mi":2,"Ju":3,"Vi":4,"Sa":5,"Do":6}
    def __init__(self,dia,horaInicio,horaFin):
        self.dia=self.dicDias[dia]
        str2time=lambda hora:time(int(hora.split(":")[0]),int(hora.split(":")[1]))
        self.horaInicio=str2time(horaInicio)
        self.horaFin=str2time(horaFin)
    def __str__(self):
        aux=f"Dia: {self.dia}\nHoras: {self.horaInicio} - {self.horaFin}\n"
        return aux
    def setDia(self,_dia):
        self.dia=_dia
    def setHoraIncio(self,_inicio):
        self.horaInicio=_inicio
    def setHoraFin(self,_horaFin):
        self.horaFin
    def getDia(self):
        return self.dia
    def getHoraInicio(self):
        return self.horaInicio
    def getHoraFin(self):
        return self.horaFin
if __name__=="__main__":
    h=Horario("Ma","15:00","16:00")
    print(h.__dict__)
