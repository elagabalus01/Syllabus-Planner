import datetime,pickle,os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
'''
Facade for google calendar REST API
'''
credentials="credentials.json"
storageToken="token.pickle"
SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDARIOESCUELA="Calendario escuela 2020-1"

''' crear servicio '''
def crearServicio():
    creds = None
    if os.path.exists(storageToken):
        with open(storageToken, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials, SCOPES)
            creds = flow.run_local_server(
            	authorization_prompt_message='Please visit this \
            	URL to authorize this application: {url}',
            	success_message='The authentication flow has completed,\
            	you may close this window.'
            	)
        with open(storageToken, 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3',credentials=creds)
    return service

def getListaCalendario()->list:
    ''' prueba lista de calendario '''
    service=crearServicio()
    calendar_list = service.calendarList().list().execute()['items']
    return calendar_list

def crearNuevoCalendario(nombre:str):
    ''' crea un nuevo calendario '''
    service=crearServicio()
    calendar={
      "kind": "calendar#calendar",
      "colorId":"15",
      "summary":nombre,
      "description": "Calendario creado para ordenar los temas de las materias",
      "timeZone":"America/Mexico_City"
    }
    calendarioTemas = service.calendars().insert(body=calendar).execute()
    return calendarioTemas['id']

def eliminarCalendario(id:int):
    ''' elimina el nuevo calendario '''
    service=crearServicio()
    valorEliminado=service.calendars().delete(calendarId=id).execute()

def crearEvento(evento,calendarID:int):
    ''' FUNCION AÑADIR EVENTO '''
    service=crearServicio()
    event = service.events().insert(calendarId=calendarID, body=evento).execute()

def getCalendarID(nombre:str)->int:
    '''
    Returns the id of the calendar of the given name
    '''
    calendarioID=None
    listaDeCalendarios=getListaCalendario()
    listaDeCalendarioID=[x['id'] for x in listaDeCalendarios if x['summary']==nombre]
    if len(listaDeCalendarioID)==0:
        calendarioID=crearNuevoCalendario(nombre)
    else:
        calendarioID=listaDeCalendarioID[0]
    return calendarioID

def delete_calendar(nombre:str)->bool:
    listaDeCalendario=getListaCalendario()
    listaDeCalendarioID=[x['id'] for x in listaDeCalendario if x['summary']==nombre]
    for id in listaDeCalendarioID:
        eliminarCalendario(id)
    return True


def main():
    ''' función principal '''
    service=crearServicio()
    colors = service.colors().get().execute()
    # Print available calendarListEntry colors.
    for id, color in colors['calendar'].items():
        print(f"colorId {id}")
        print(f"Background {color['background']}")
        print(f"Foreground {color['foreground']}")
    print("Para eventos")
    for id, color in colors['event'].items():
        print(f"colorId {id}")
        print(f"Background {color['background']}")
        print(f"Foreground {color['foreground']}")

if __name__ == '__main__':
    main()
