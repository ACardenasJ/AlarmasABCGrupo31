# AlarmasABCGrupo31
Se crea el reposiotrio para el proyecto de la elavoracion de las actividades de la materia de arquitectura segundo semestre ciclo 1 de MISO

## Instrucciones

* Crear Entorno Virtual: python -m venv venv
* Activar Entorno Virtual: ./venv/Scripts/activate
* Desactivar Entorno Virtual: deactivate
* Instalar Requerimientos: pip install -r requirements.txt
* Correr redis server para la cola en un terminal linux (en windows se debe en ubuntu): redis-server
* Microservicio expone Temperatura: microservicio_1_TempExterna ---> flask run -p 5000
* API que agrega a la cola despues de ser ejecutada por app python: flaskr_temp --> flask run -p 5001
* App python para requerir esa temperatura: req temp --> python app.py
* Worker de Cola para extraer y poner en otro lado (temp agrega en un archivo): celery -A tareas worker -l info -P solo
* Servicio Componente Interno: flaskr_temp --> flask run -p 5002


![image](https://user-images.githubusercontent.com/98674577/188791161-77b8f1aa-3e4d-4b9b-ac08-fcf06891ebcb.png)
