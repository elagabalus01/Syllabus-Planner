from os import listdir
from os.path import isfile, join
from calendarioFI.calendario import calendarioFI
from connectCalendar import calendarizarJson,eliminarCaledarioCreados,generarCalendario
def calendarizar(nombreCalendario,myPath,calendario):
    files = [myPath+'/'+f for f in listdir(myPath) if isfile(join(myPath,f))]
    for file in files:
        calendarizarJson(nombreCalendario,file,calendario)
def calendarizarRepasos():
    nombre='Repasos 2020-1'
    calendarizar(nombre,'./repaso5s',generarCalendario("5-8-2019",16))
    # eliminarCaledarioCreados(nombre)
def calendarizarClases(nombre,folder):
    calendarizar(nombre,folder,calendarioFI())
    # eliminarCaledarioCreados(nombre)
def main():
    calendarizarClases('Clases 2020-2','C:/Users/ikaru/3D Objects/programming/python/temarios/')

if __name__=='__main__':
    main()