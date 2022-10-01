from API import create_app
from markupsafe import escape
from flask_restful import Api
from API.vistas.vistas import VistaAPIGateway

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)


api.add_resource(VistaAPIGateway, '/registrar')
