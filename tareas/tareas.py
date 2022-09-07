from celery import Celery
import requests

celery = Celery(__name__, broker='redis://localhost:6379/0')

@celery.task(name="registrar_temp")
def registrar_temp(temp_json):
    with open('log_registrar_temp.txt','a+') as file:
        file.write('{}\n'.format(temp_json))
    
    if(temp_json['temperatura'] is not None and temp_json['tipo'] is not None and temp_json['now'] is not None):
        requests.post('http://localhost:5002/temperatura', json=temp_json)
    