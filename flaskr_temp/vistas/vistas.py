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
        content = requests.get('http://localhost:5000/temperatura')
        if content.status_code == 404:
            return {'error': 'Temperatura no disponible'}, 404
        else:
            temperatura = content.json()
            args = (temperatura,)
            registrar_temp.apply_async(args=args)
        return json.dumps(temperatura), 200



