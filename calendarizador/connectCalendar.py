from models.Materia import Materia
from .googleCalendarAPI.CreadorCalendario import crearNuevoCalendario,\
crearEvento,getListaCalendario,eliminarCalendario
from datetime import timedelta,datetime

def materia2CalendarTemplate(materia,tema,subtema):
    horario=None
    for clase in materia.horarios:
        if clase.dia==subtema.getFechaInicio().weekday():
            horario=clase
            break
    dayFormat=lambda time:str(time.strftime("%Y-%m-%d"))
    hI=str(horario.getHoraInicio())
    hF=str(horario.getHoraFin())
    try:
        start=dayFormat(subtema.getFechaInicio())+'T'+hI
        end=dayFormat(subtema.getFechaInicio())+'T'+hF
    except:
        print(f"Error {subtema.getNombre()} {subtema.getFechaInicio()}")
    evento={
      "kind": "calendar#event",
      "summary":f"{materia.getSalon()} {materia.getNombre()}. T:{tema.getNumero()} {tema.getNombre()}",
      "description": subtema.getNombre(),
      "colorId":materia.getColor(),
      "start": {
        "dateTime":start,
        "timeZone":"America/Mexico_City"
      },
      "end": {
        "dateTime":end,
        "timeZone":"America/Mexico_City"
      }
    }
    return evento

def dia2CalendarTemplate(materia,dia):
    horario=None
    for clase in materia.horarios:
        if clase.dia==dia.weekday():
            horario=clase
            break
    dayFormat=lambda time:str(time.strftime("%Y-%m-%d"))
    hI=str(horario.getHoraInicio())
    hF=str(horario.getHoraFin())
    try:
        start=dayFormat(dia)+'T'+hI
        end=dayFormat(dia)+'T'+hF
    except:
        print("Error dia sin tema nuevo")
    evento={
      "kind": "calendar#event",
      "summary": f"{materia.getSalon()} {materia.getNombre()}",
      "description":"Continua tema anterior",
      "colorId":materia.getColor(),
      "start": {
        "dateTime":start,
        "timeZone":"America/Mexico_City"
      },
      "end": {
        "dateTime":end,
        "timeZone":"America/Mexico_City"
      }
    }
    return evento

def apiConnect(materia,calendarioID):
    for tema in materia.getTemas():
        for subtema in tema.getSubtemas():
            evento=materia2CalendarTemplate(materia,tema,subtema)
            crearEvento(evento,calendarioID)
            materia.fechasDeClase.remove(subtema.getFechaInicio())
    for dia in materia.fechasDeClase:
        evento=dia2CalendarTemplate(materia,dia)
        crearEvento(evento,calendarioID)

def eliminarCaledarioCreados(nombre):
    listaDeCalendario=getListaCalendario()
    listaDeCalendarioID=[x['id'] for x in listaDeCalendario if x['summary']==nombre]
    for id in listaDeCalendarioID:
        eliminarCalendario(id)

def getCalendarID(nombre):
    calendarioID=None
    listaDeCalendarios=getListaCalendario()
    listaDeCalendarioID=[x['id'] for x in listaDeCalendarios if x['summary']==nombre]
    if len(listaDeCalendarioID)==0:
        calendarioID=crearNuevoCalendario(nombre)
    else:
        calendarioID=listaDeCalendarioID[0]
    return calendarioID

def generarCalendario(inicio,semanas):
    inicio=datetime.strptime(inicio,'%d-%m-%Y')
    day_delta = timedelta(weeks=semanas)
    fin=inicio+day_delta
    day_delta = timedelta(days=1)
    listaDeDias=[]
    for i in range((fin-inicio).days+1):
        listaDeDias.append(inicio+i*day_delta)
    return listaDeDias

def calendarizarJson(nombreCalendario,jsonFile,calendario):
  calendarioID=getCalendarID(nombreCalendario)
  apiConnect(cargarTemario(jsonFile,calendario),calendarioID)

def cargarTemario(jsonPath,calendario):
    materia=Materia()
    materia.recoverJson(jsonPath)
    materia.ordenarEnCalendario(calendario)
    return materia