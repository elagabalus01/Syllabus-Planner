from calendarioFI.calendario import calendarioFI
import calendar
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
def graph(dias):
    objects = ("lunes","martes","miercoles","jueves","viernes","Sabado")
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, dias, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Dias')
    plt.title('Clases')
    plt.show()
def diasDeClase():
    diasDeClase=calendarioFI()
    #0
    lunes=[]
    #1
    martes=[]
    #2
    miercoles=[]
    #3
    jueves=[]
    #4
    viernes=[]
    #
    sabado=[]
    for dia in diasDeClase:
        dia=dia.weekday()
        if dia == 0:
            lunes.append(dia)
        elif dia == 1:
            martes.append(dia)
        elif dia == 2:
            miercoles.append(dia)
        elif dia == 3:
            jueves.append(dia)
        elif dia == 4:
            viernes.append(dia)
        elif dia == 5:
            sabado.append(dia)
    print("lunes","martes","miercoles","jueves","viernes","Sabado",sep='\t')
    print(len(lunes),len(martes),len(miercoles),len(jueves),len(viernes),len(sabado),sep='\t\t')
    dias=[len(lunes),len(martes),len(miercoles),len(jueves),len(viernes),len(sabado)]
    graph(dias)
def main():
    diasDeClase()
if __name__=="__main__":
    main()