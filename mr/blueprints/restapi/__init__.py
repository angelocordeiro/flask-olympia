from flask import Blueprint
from flask_restful import Api

from .resources import OlympiasResource, OlympiaItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(OlympiasResource, "/olympias/")
    api.add_resource(OlympiaItemResource, "/olympia/<num>")
    app.register_blueprint(bp)
