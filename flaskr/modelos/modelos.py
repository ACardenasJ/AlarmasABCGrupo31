from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum

db = SQLAlchemy()

class Temperatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Integer)
    tipo = db.Column(db.String(20))
    fecha = db.Column(db.String(50))

class TemperaturaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Temperatura
        include_relationships = True
        load_instance = True