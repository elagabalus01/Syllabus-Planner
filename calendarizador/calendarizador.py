from .connectCalendar import cargarTemario,getCalendarID,apiConnect,eliminarCaledarioCreados
from models.Materia import Materia
from datetime import datetime, timedelta
#from .calendarioFI.calendario import calendarioFI
def generarCalendario(fechaInicio,semanasDuracion):
    inicio=datetime.strptime(fechaInicio,'%d-%m-%Y')
    day_delta = timedelta(weeks=semanasDuracion)
    fin=inicio+day_delta
    day_delta = timedelta(days=1)
    listaDeDias=[]
    for i in range((fin-inicio).days+1):
        listaDeDias.append(inicio+i*day_delta)
    return listaDeDias

def calendarizar(filePath,nombreCalendario,fechaInicio,semanasDuracion):
    calendarioID=getCalendarID(nombreCalendario)
    apiConnect(cargarTemario(filePath,generarCalendario(fechaInicio,semanasDuracion)),calendarioID)
# Cañemdarizar modelo
def calendarizarModelo(modelo,nombreCalendario,fechaInicio,semanasDuracion):
    calendarioID=getCalendarID(nombreCalendario)
    calendario=generarCalendario(fechaInicio,semanasDuracion)
    modelo.ordenarEnCalendario(calendario)
    apiConnect(modelo,calendarioID)
# eliminarCaledarioCreados(nombre)