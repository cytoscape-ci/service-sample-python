import json

from flask import request
from flask.ext.restful import Resource, reqparse

from services.id_mapper import IdMapper as mapper


class IdMapperService(Resource):

    def get(self):

        summary = {
            'serviceName': 'uniprot-id-mapper',
            'description': "Simple ID mapper using Uniprot API."
        }

        return summary

    def post(self):
        dataBytes = request.stream.read()
        data = json.loads(dataBytes.decode("utf-8"))

        # Call actual mapper
        result = mapper.convert(data["ids"], data["from"], data["to"])

        return result, 200
