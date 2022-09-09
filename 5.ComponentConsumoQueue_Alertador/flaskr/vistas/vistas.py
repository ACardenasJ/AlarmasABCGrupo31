from flask_restful import Resource
from flask import request
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import requests
import json
from sqlalchemy import desc

from ..modelos import db, Temperatura, TemperaturaSchema

temp_schema = TemperaturaSchema()

class VistaTemperaturas(Resource):
    def get(self):
        #temperaturas = Temperatura.query.all()
        temperaturas = Temperatura.query.order_by(desc(Temperatura.id)).all()
        return temp_schema.dump(temperaturas, many=True), 200

    def post(self):
        temp_json = request.get_json()
        temp = Temperatura(temperatura=temp_json['temperatura'], tipo=temp_json['tipo'], fecha=temp_json['now'])
        db.session.add(temp)
        db.session.commit()
        return temp_schema.dump(temp), 201

class VistaHealthCheck(Resource):
    def get(self):
        return {"status": "ok"}, 200