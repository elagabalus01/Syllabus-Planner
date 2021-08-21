dicDias={0:"lu",1:"ma",2:"mi",3:"ma",4:"ju",5:"vi",6:"sa"}
def num_dia_to_dia():
    listaDias=[0,1,2]
    diaStr=lambda numDia: dicDias[numDia].title()
    listaHorarios=[diaStr(dia) for dia in listaDias]
    print(listaHorarios)
def dia_to_num_dia():
    diaNum=lambda dia:list(dicDias.values()).index(dia.lower())
    # list(my_dict.keys())[list(my_dict.values()).index(112)]
    print(diaNum('lu'))
def nomasUnaLista():
    dias=["lu","ma","mi","ma","ju","vi","sa"]
    dia2Str=lambda numDia: dias[numDia].title()
    dia2Num=lambda dia:dias.index(dia.lower())
    print(dia2Str(6))
    print(dia2Num("Mi"))

def loop():
    nomasUnaLista()
    