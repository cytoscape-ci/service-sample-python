import json
import requests


DEFAULT_PORT = 3333
DEFAULT_LOCATION = "localhost"
DEFAULT_VERSION = "v1"

HEADERS = {'Content-Type': 'application/json'}

AGENT_ENDPOINT = "http://localhost:8080/register"


class ServiceRegisterer:

    @staticmethod
    def register(name, capacity=1, location=DEFAULT_LOCATION,
                 port=DEFAULT_PORT, version=DEFAULT_VERSION, service_url=AGENT_ENDPOINT):

        # Basic info about this service
        reg = {
            "name": name,
            "capacity": capacity,
            "location": location + ":" + str(port),
            "version": version
        }

        res = requests.post(
            service_url,
            data=json.dumps([reg]),
            headers=HEADERS)

        print(res.status_code)
        print("\n ### Service registered ###")
