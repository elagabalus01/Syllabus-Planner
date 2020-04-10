from datetime import datetime, timedelta
try:
    import calendarioFI
    from pkg_resources import resource_string
    FERIADOS=resource_string(calendarioFI.__name__,"/feriados.txt").decode("utf-8")[:-1]
except ModuleNotFoundError:
    print("Ejecutando main")
    FERIADOS=open("feriados.txt",'r',encoding="utf-8").read()

''' Vairables globales'''
INICIODECLASES="27-1-2020"
FINDECLASES="23-5-2020"

''' Filtra fechas desde un archivo'''
def filtrarDesdeArchivo(file):
    listaFeriados=[]
    with open(file,'r',encoding='utf-8') as archivo:
        for fecha in archivo:
            feriado=datetime.strptime(fecha[:-1],'%d-%m-%Y')
            listaFeriados.append(feriado)
    return listaFeriados
''' Filtra fechas desde cadena'''
def filtrarDesdeCadena(file):
    listaFeriados=[]
    archivo=file.split('\n')
    for fecha in archivo:
        try:
            feriado=datetime.strptime(fecha.rstrip(),'%d-%m-%Y')
            listaFeriados.append(feriado)
        except ValueError as e:
            print(f"No se pudo agregar la fecha por que {e}")
    return listaFeriados

''' Generar calendarioUNAM '''
def calendarioFI():
    inicio=datetime.strptime(INICIODECLASES,'%d-%m-%Y')
    fin=datetime.strptime(FINDECLASES,'%d-%m-%Y')
    day_delta = timedelta(days=1)
    listaDeDias=[]
    feriados=filtrarDesdeCadena(FERIADOS)
    for i in range((fin-inicio).days+1):
        dia=inicio+i*day_delta
        if dia.weekday() !=6 and dia not in feriados:
            listaDeDias.append(inicio+i*day_delta)
    return listaDeDias

''' generar calendario sin restricciones '''
def semestre():
    inicio=datetime.strptime(INICIODECLASES,'%d-%m-%Y')
    fin=datetime.strptime(FINDECLASES,'%d-%m-%Y')
    day_delta = timedelta(days=1)
    listaDeDias=[]
    for i in range((fin-inicio).days+1):
        dia=inicio+i*day_delta
        listaDeDias.append(inicio+i*day_delta)
    return listaDeDias
def main():
    # for dia in semestre():
    #     print(dia)
    for dia in calendarioFI():
        print(dia)
if __name__=="__main__":
    main()