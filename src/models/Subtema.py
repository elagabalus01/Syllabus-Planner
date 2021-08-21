class Subtema(object):
    def __init__(self,_nombre=None,_fechaInicio=-1):
        self.nombre = _nombre
        self.fechaInicio = _fechaInicio
    ''' setter '''
    def setNombre(self,_nombre):
        self.nombre=_nombre
    def setFechaInicio(self,_fechaInicio):
        self.fechaInicio=_fechaInicio
    ''' getter '''
    def getNombre(self):
        return self.nombre
    def getFechaInicio(self):
        return self.fechaInicio
    ''' other overwrited methods '''
    def __str__(self):
        return self.nombre
    def __repr__(self):
        return self.__str__()
