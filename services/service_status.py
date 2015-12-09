from flask_restful import Resource


class ServiceStatus(Resource):

    """
    Sample service for server status check.
    """

    def get(self):

        summary = {
            'apiVersion': '0.1',
            'services': [
                "id_mapper"
            ]
        }

        return summary
