from models import Materia,Horario,Tema,Subtema,Horario

def testHorario():
    Horario()

def testMateria():
    modelo=Materia()
    modelo.recoverJson("temarios/7s/ai.json")
    print(modelo)

def testModel():
    testMateria()
