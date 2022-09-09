# AlarmasABCGrupo31
Se crea el reposiotrio para el proyecto de la elavoracion de las actividades de la materia de arquitectura segundo semestre ciclo 1 de MISO

## Instrucciones

* Crear Entorno Virtual: python -m venv venv
* Activar Entorno Virtual: ./venv/Scripts/activate
* Desactivar Entorno Virtual: deactivate
* Instalar Requerimientos: pip install -r requirements.txt
* Correr redis server para la cola en un terminal linux (en windows se debe en ubuntu): redis-server
1. Servicio Info Temp - Microservicio expone Temperatura: microservicio_1_TempExterna ---> flask run -p 5000
2. Component API - API que agrega a la cola despues de ser ejecutada por app python: flaskr_temp --> flask run -p 5001
3. Servicio Request Temp - App python para requerir esa temperatura: req temp --> python app.py
4. Component Queue - Worker de Cola para extraer y poner en otro lado (temp agrega en un archivo): celery -A tareas worker -l info -P solo
5. Component Consumo Queue Alertador -Servicio Componente Interno: flaskr_temp --> flask run -p 5002
6. Component Observador - App python para monitorear componente Alertador: --> python app.py

![image](https://user-images.githubusercontent.com/98674577/189456084-eab4a6bd-f750-4871-bf3f-cdfd29bd71e2.png)

