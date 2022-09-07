from microservicio_1_TempExterna import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
import random
from datetime import datetime


app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

class VistaTemp(Resource):
    def get(self):
        n = random.randint(-20,55)
        now = datetime.now()
        return {'temperatura': n,'tipo':'C','now':str(now)}, 200
        

api.add_resource(VistaTemp, '/temperatura')