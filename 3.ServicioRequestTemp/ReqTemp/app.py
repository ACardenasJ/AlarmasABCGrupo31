
import requests
import json
import random
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import threading


def printit():
    threading.Timer(3.0, printit).start()
    try:
        content = requests.get('http://localhost:5001/temperatura')
        if content.status_code == 404:
            print('Servicio API Temp - temperatura no encontrada')
        else:
            #print('recibido: ', content.json())
            #temp_json = content.json()
            res = json.loads(content.json())
            temp = str(res['temperatura'])
            tipo = str(res['tipo'])
            fecha = str(res['now'])
            #print(temp_json)
            print('T: ' + temp + ' - ' + tipo + ' - ' + fecha)

    except ConnectionError as e:
            print('Servicio API Temp - OFFLINE')
    except requests.exceptions.Timeout:
    # Maybe set up for a retry, or continue in a retry loop
        print('Servicio API Temp --- TIMEOUT')
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print('Servicio API Temp --- REDIRECT')
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print('Servicio API Temp --- REQUEST')
    except Exception as e:
        print('Servicio API Temp - error' + str(e))

printit()