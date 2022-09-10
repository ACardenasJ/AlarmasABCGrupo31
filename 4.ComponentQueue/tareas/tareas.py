from celery import Celery
import requests

celery = Celery(__name__, broker='redis://localhost:6379/0')

def reintegrar_cola(temp_json):
    args = (temp_json,)
    #AGREGA A LA COLA DE TAREAS
    registrar_temp.apply_async(args=args)

def servicio_2(temp_json):
    try:
        content = requests.get('http://localhost:5003/healthcheck')
        if content.status_code == 404:
            print('SERVICIO Alertador 5003 OFFLINE------')
            reintegrar_cola(temp_json)
        else:
            #print('recibido: ', content.json())
            print('SERVICIO Alertador 5003 ONLINE')
            requests.post('http://localhost:5003/temperatura', json=temp_json)
            with open('log_registrar_temp.txt','a+') as file:
                file.write('{}\n'.format(temp_json))
    except ConnectionError as e:
        print('SERVICIO Alertador 5003 OFFLINE')
        reintegrar_cola(temp_json)
    except requests.exceptions.Timeout:
    # Maybe set up for a retry, or continue in a retry loop
        print('SERVICIO Alertador 5003 OFFLINE --- TIMEOUT')
        reintegrar_cola(temp_json)
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print('SERVICIO Alertador 5003 OFFLINE --- REDIRECT')
        reintegrar_cola(temp_json)
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print('SERVICIO Alertador 5003 OFFLINE --- REQUEST')
        reintegrar_cola(temp_json)
    except Exception as e:
        print('error' + str(e))
        reintegrar_cola(temp_json)    

@celery.task(name="registrar_temp")
def registrar_temp(temp_json):
    
    if(temp_json['temperatura'] is not None and temp_json['tipo'] is not None and temp_json['now'] is not None):
        try:
            content = requests.get('http://localhost:5002/healthcheck')
            if content.status_code == 404:
                print('SERVICIO Alertador 5002 OFFLINE------')
                #reintegrar_cola(temp_json)
                servicio_2(temp_json)
            else:
                #print('recibido: ', content.json())
                print('SERVICIO Alertador 5002 ONLINE')
                requests.post('http://localhost:5002/temperatura', json=temp_json)
                with open('log_registrar_temp.txt','a+') as file:
                    file.write('{}\n'.format(temp_json))
        except ConnectionError as e:
            print('SERVICIO Alertador 5002 OFFLINE')
            servicio_2(temp_json)
        except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
            print('SERVICIO Alertador 5002 OFFLINE --- TIMEOUT')
            servicio_2(temp_json)
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print('SERVICIO Alertador 5002 OFFLINE --- REDIRECT')
            servicio_2(temp_json)
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            print('SERVICIO Alertador 5002 OFFLINE --- REQUEST')
            servicio_2(temp_json)
        except Exception as e:
            print('error' + str(e))
        
    