class Tema(object):
    def __init__(self,numero=-1,tema=None,duracion=0,
        fechaInicio=-1,fechaFin=-1,subtemas=[]):
        self.numero=numero
        self.tema=tema
        self.duracion=duracion
        self.fechaInicio=fechaInicio
        self.fechaFin=fechaFin
        self.subtemas=subtemas
    ''' Setters '''
    def setNumero(self,_numero):
        self.numero=_numero
    def setNombre(self,_nombre):
        self.tema=_nombre
    def setHoras(self,_horas):
        self.duracion=_horas
    def setFechaInicio(self,_fechaInicio):
        self.fechaInicio=_fechaInicio
    def setFechaFin(self,_fechaFin):
        self.fechaFin=_fechaFin
    def setSubtemas(self,_subtemas):
        self.subtemas=_subtemas
    ''' getters '''
    def getNumero(self):
        return self.numero
    def getNombre(self):
        return self.tema
    def getHoras(self):
        return self.duracion
    def getFechaInicio(self):
        return self.fechaInicio
    def getFechaFin(self):
        return self.fechaFin
    def getSubtemas(self):
        return self.subtemas
    ''' metodo string '''
    def __str__(self):
        aux=""
        for subtema in self.subtemas:
            aux+='\t'+str(subtema)+'\n'
        return self.tema+'\n'+aux
    def __repr__(self):
        return self.tema
    ''' genera el inicio y final de cada tema '''
    def getInicioFInNombre(self):
        i=self.fechaInicio.strftime("%d-%B")
        f=self.fechaFin.strftime("%d-%B")
        return (f"\n{self.tema}: {i} - {f}")
    ''' ordena cada tema en '''
    def ordenarEnCalendario(self,dias,duracion):
        numeroDeDias=len(dias)
        numeroDeHoras=numeroDeDias*duracion
        subtemas=self.subtemas
        numeroTemas=len(subtemas)
        span=numeroDeHoras/numeroTemas
        acumulado=0
        nuevaListaSubtemas=[]
        fecha=dias.pop(0)
        while acumulado < duracion and len(subtemas)>0:
            subtemaActualizado=subtemas.pop(0)
            subtemaActualizado.setFechaInicio(fecha)
            nuevaListaSubtemas.append(subtemaActualizado)
            acumulado+=span
            if acumulado >= duracion and len(subtemas)>0:
                fecha=dias.pop(0)
                acumulado-=duracion
            if acumulado >= duracion and len(subtemas)>0:
                acumulado-=(span)/duracion
                dias.pop(0)
        self.subtemas=nuevaListaSubtemas
        self.reduce()
    ''' REDUCE LOS TEMAS QUE TIENEN LA MISMA FECHA'''
    def reduce(self):
        l=[str(x.getFechaInicio()) for x in self.subtemas]
        repetidos=[x for x in l if l.count(x) > 1]
        final=[]
        for repetido in repetidos:
            if repetido not in final:
                final.append(repetido)
        for repetido in final:
            l=[str(x.getFechaInicio()) for x in self.subtemas]
            indices=[i for i,x in enumerate(l) if x==repetido]
            original=self.subtemas[indices[0]]
            indices=indices[1:]
            aux=""
            contEliminados=0
            for index in indices:
                index-=contEliminados
                aux+=self.subtemas[index].getNombre()+'\n'
                self.subtemas.remove(self.subtemas[index])
                contEliminados+=1
            if aux[len(aux)-1]=='\n':
                aux=aux[:-1]
            original.setNombre(original.getNombre()+'\n'+aux)

if __name__=="__main__":
    print("Hola mudno")
