from flask import Flask
from flask_restful import Api

from registerer import ServiceRegisterer
from services.service_id_mapper import IdMapperService
from services.service_status import ServiceStatus

PORT_NUMBER = 3333

app = Flask(__name__)
api = Api(app)

# Routing
api.add_resource(ServiceStatus, '/') # Simply returns version of API
api.add_resource(IdMapperService, '/map') # ID Mapping service


if __name__ == '__main__':

    """
    Sample REST API Server registering itself to CytoAgent.
    """

    # Register this API server as a service
    ServiceRegisterer.register("idmapping", port=PORT_NUMBER, capacity=4)

    # Start the App
    app.run(debug=True, port=PORT_NUMBER, use_reloader=False)
