import datetime,pickle,os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleCalendarAPI
import pkg_resources
credentials=pkg_resources.resource_filename(googleCalendarAPI.__name__,"credentials.json")
storageToken=pkg_resources.resource_filename(googleCalendarAPI.__name__,"token.pickle")
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
''' prueba lista de calendario '''
def getListaCalendario():
    service=crearServicio()
    calendar_list = service.calendarList().list().execute()['items']
    return calendar_list
''' crea un nuevo calendario '''
def crearNuevoCalendario(nombre):
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
''' elimina el nuevo calendario '''
def eliminarCalendario(id):
    service=crearServicio()
    valorEliminado=service.calendars().delete(calendarId=id).execute()
''' FUNCION AÑADIR EVENTO '''
def crearEvento(evento,calendarID):
    service=crearServicio()
    event = service.events().insert(calendarId=calendarID, body=evento).execute()

''' función principal '''
def main():
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
