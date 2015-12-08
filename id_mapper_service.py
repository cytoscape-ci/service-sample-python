from flask.ext.restful import Resource, reqparse
from flask import request
from id_mapper import IdMapper as mapper
import json


class IdMapperService(Resource):

    def __init__(self):
        self.__parser = reqparse.RequestParser()

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
        result = mapper.convert(data["ids"], str(data["from"]),str(data["to"]))

        print('----------------- OK')

        return result, 200
