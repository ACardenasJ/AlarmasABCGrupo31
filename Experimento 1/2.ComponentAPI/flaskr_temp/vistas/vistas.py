from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import requests
import json
from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task(name='registrar_temp')
def registrar_temp(temp_json):
    pass

class VistaTemperatura(Resource):
    def get(self):
        try:
            content = requests.get('http://localhost:5000/temperatura')
            if content.status_code == 404:
                return {'error': 'Servicio InfoTemp - Temperatura no disponible'}, 404
            else:
                temperatura = content.json()
                args = (temperatura,)
                #AGREGA A LA COLA DE TAREAS
                registrar_temp.apply_async(args=args)
            return json.dumps(temperatura), 200
        except ConnectionError as e:
            return {'error': 'Servicio InfoTemp offline -- Connection'}, 404
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            return {'error': 'Servicio InfoTemp offline -- Timeout'}, 404
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            return {'error': 'Servicio InfoTemp offline -- ManyRedirects'}, 404
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            return {'error': 'Servicio InfoTemp offline -- Request'}, 404
        except Exception as e:
            return {'error': 'Servicio InfoTemp - Error desconocido -' + str(e)}, 404



