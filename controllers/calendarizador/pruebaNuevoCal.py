from connectCalendar import cargarTemario,getCalendarID,apiConnect,eliminarCaledarioCreados
from dataTypes.Materia import Materia
from datetime import datetime, timedelta
from calendarioFI.calendario import calendarioFI
def generarCalendario():
    INICIODECLASES="20-1-2020"
    inicio=datetime.strptime(INICIODECLASES,'%d-%m-%Y')
    day_delta = timedelta(weeks=16)
    fin=inicio+day_delta
    day_delta = timedelta(days=1)
    listaDeDias=[]
    for i in range((fin-inicio).days+1):
        listaDeDias.append(inicio+i*day_delta)
    return listaDeDias

nombre="Clases de septimo"

calendarioID=getCalendarID(nombre)
file="C:/Users/elagabalus/Desktop/compiladores.json"
apiConnect(cargarTemario(file,generarCalendario()),calendarioID)

# eliminarCaledarioCreados(nombre)