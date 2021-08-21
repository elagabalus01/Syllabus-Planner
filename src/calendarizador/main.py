from os import listdir
from os.path import isfile, join
from datetime import datetime
from .calendarAdapter import calendarizar
def main():
    current_date=datetime.now().strftime('%d-%m-%Y')
    file_path='/home/elagabalus/archivos/programming/python/calendarizadorui/temarios/7s/ai.json'
    calendarizar(file_path,'Prueba refactoring 2021',current_date,16)

if __name__=='__main__':
    main()
