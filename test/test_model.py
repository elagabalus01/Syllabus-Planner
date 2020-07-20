from models.Horario import Horario as HorarioModelo
from models.Horario import Horario as HorarioControlador
from models.Materia import Materia as MateriaModelo
from models.Materia import Materia as MateriaControlador
def testHorario():
    HorarioModelo()
    HorarioControlador()
def testMateria():
    modelo=MateriaModelo()
    modelo.recoverJson("temarios/7s/ai.json")
    control=MateriaControlador("temarios/7s/ai.json")
    print(modelo)
    # print(control)
def testToJson():
    modelo=MateriaControlador()
    modelo.recoverJson("temarios/7s/ai.json")
    print(modelo.toJson())
def testModel():
    testToJson()
    