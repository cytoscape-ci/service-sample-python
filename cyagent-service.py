from flask import Flask
from flask_restful import Api

from id_mapper_service import IdMapperService
from registerer import ServiceRegisterer
from service_status import ServiceStatus

app = Flask(__name__)
api = Api(app)

# Routing
api.add_resource(ServiceStatus, '/')
api.add_resource(IdMapperService, '/idmapping')


if __name__ == '__main__':

    # Register this API server as a service
    ServiceRegisterer.register()

    # Start the App
    app.run(debug=True, port=3333, use_reloader=False)
