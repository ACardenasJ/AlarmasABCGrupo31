
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
            print('temperatura no encontrada')
        else:
            print('recibido: ', content.json())
    except Exception as e:
        print('error' + str(e))

printit()