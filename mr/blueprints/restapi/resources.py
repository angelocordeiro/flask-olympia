from flask import abort, jsonify
from flask_restful import Resource

from mr.models import Mrdata


class OlympiasResource(Resource):
    def get(self):
        olympias = Mrdata.query.all() or abort(204)
        return jsonify(
            {"olympias": [olympia.to_dict() for olympia in olympias]}
        )


class OlympiaItemResource(Resource):
    def get(self, num):
        olympia = Mrdata.query.filter_by(num=num).first() or abort(404)
        print(olympia)
        return jsonify(olympia.to_dict())
    