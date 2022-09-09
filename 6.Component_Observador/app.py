import requests
import json
import random
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import threading


def printit():
    threading.Timer(3.0, printit).start()
    try:
        content = requests.get('http://localhost:5002/healthcheck')
        if content.status_code == 404:
            print('SERVICIO Alertador OFFLINE------')
        else:
            #print('recibido: ', content.json())
            print('SERVICIO Alertador ONLINE')
    except ConnectionError as e:
        print('SERVICIO Alertador OFFLINE')
    except requests.exceptions.Timeout:
    # Maybe set up for a retry, or continue in a retry loop
        print('SERVICIO Alertador OFFLINE --- TIMEOUT')
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print('SERVICIO Alertador OFFLINE --- REDIRECT')
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print('SERVICIO Alertador OFFLINE --- REQUEST')
    except Exception as e:
        print('error' + str(e))

printit()