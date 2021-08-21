from models import Materia,Horario,Tema,Subtema,Horario
from controllers.new.serializeController import SerializeController
def testHorario():
    Horario()

def testMateria():
    # modelo=Materia()
    # modelo.recoverJson("temarios/7s/ai.json")
    # print(modelo)
    materia=Materia()
    ctl=SerializeController(materia)
    materia.recoverJson("temarios/8s/redes.json")
    materia.notify_observers()

def testModel():
    testMateria()
