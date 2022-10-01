from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
import json
from sqlalchemy import desc

import re


class VistaValidarPassword(Resource):

    def post(self):
        print("REQUEST LLEGANDO A VALIDAR PASSWORD")
        print(request.json['contrasena'])
        password = request.json['contrasena']
        #validarPassword = re.search("expresion", password)
        validarPassword = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}", password)
        print(validarPassword)
        #status = "True" if validarPassword == password else "False"
        status = "True" if validarPassword is not None else "False"
        #status = "False" if validarPassword == password else "True"
        print(status)
        return {'status': status, 'response': 201}
