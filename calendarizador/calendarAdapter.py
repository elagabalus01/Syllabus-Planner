from models.Materia import Materia
from .googleCalendarAPI import (crearNuevoCalendario, crearEvento,
    getListaCalendario, eliminarCalendario, getCalendarID)
from .calendario import generarCalendario

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

def apiConnect(materia:Materia,calendarioID:int):
    '''
    Calendarize an Materia object creating a event for
    each class with the themes to teach that day
    '''
    for tema in materia.getTemas():
        for subtema in tema.getSubtemas():
            evento=materia2CalendarTemplate(materia,tema,subtema)
            crearEvento(evento,calendarioID)
            materia.fechasDeClase.remove(subtema.getFechaInicio())
    for dia in materia.fechasDeClase:
        evento=dia2CalendarTemplate(materia,dia)
        crearEvento(evento,calendarioID)

def cargarTemario(jsonPath,calendario):
    ''' Loads a json file into a Materia class as previus stop to calenrize '''
    materia=Materia()
    materia.recoverJson(jsonPath)
    materia.ordenarEnCalendario(calendario)
    return materia

def calendarizarJson(nombreCalendario:str,jsonFile:str,calendario:list):
    '''
    Calendarizes a json file into a gcalendar with a specific name
    with a given calendar (list of datetime objects)
    '''
    calendarioID=getCalendarID(nombreCalendario)
    apiConnect(cargarTemario(jsonFile,calendario),calendarioID)

def calendarizar(filePath,nombreCalendario,fechaInicio,semanasDuracion):
    '''
    Calendarizes a json file into a gcalendar with a specific name
    with a given start date and number of weeks
    '''
    calendarioID=getCalendarID(nombreCalendario)
    apiConnect(cargarTemario(filePath,generarCalendario(fechaInicio,semanasDuracion)),calendarioID)


def calendarizarModelo(modelo,nombreCalendario,fechaInicio,semanasDuracion):
    '''
    Calendarizes a Materia object into a gcalendar with a specific name
    with a given start date and number of weeks
    '''
    calendarioID=getCalendarID(nombreCalendario)
    calendario=generarCalendario(fechaInicio,semanasDuracion)
    modelo.ordenarEnCalendario(calendario)
    apiConnect(modelo,calendarioID)
