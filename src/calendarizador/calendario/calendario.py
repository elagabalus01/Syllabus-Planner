from datetime import datetime, timedelta

def filtrarDesdeArchivo(file:str)->list:
    ''' Filtra fechas desde un archivo'''
    listaFeriados=[]
    with open(file,'r',encoding='utf-8') as archivo:
        for fecha in archivo:
            feriado=datetime.strptime(fecha[:-1],'%d-%m-%Y')
            listaFeriados.append(feriado)
    return listaFeriados

def filtrarDesdeCadena(cadena:str)->list:
    ''' Filtra fechas desde cadena'''
    listaFeriados=[]
    archivo=file.split('\n')
    for fecha in archivo:
        try:
            feriado=datetime.strptime(fecha.rstrip(),'%d-%m-%Y')
            listaFeriados.append(feriado)
        except ValueError as e:
            print(f"No se pudo agregar la fecha por que {e}")
    return listaFeriados

def generarCalendario(fechaInicio:str,semanasDuracion:int)->list:
    '''
    :param fechaInicio: The start day of the calendar with the following formar
    '%d-%m-%Y'
    :param semanasDuracion: Number of week of the calendar
    :return: list of the dates with type datetime
    '''
    inicio=datetime.strptime(fechaInicio,'%d-%m-%Y')
    day_delta = timedelta(weeks=semanasDuracion)
    fin=inicio+day_delta
    day_delta = timedelta(days=1)
    listaDeDias=[]
    for i in range((fin-inicio).days+1):
        listaDeDias.append(inicio+i*day_delta)
    return listaDeDias

def main():
    for dia in generarCalendario('10-5-2021',3):
        print(dia)

if __name__=="__main__":
    main()
