import json
import requests

HEADERS = {'Content-Type': 'application/json'}
AGENT_ENDPOINT = "http://localhost:8080/register"


class ServiceRegisterer:

    @staticmethod
    def register(service_url=AGENT_ENDPOINT):

        # Basic info about this service
        reg = {
            "name": "id-mapping-service",
            "capacity": 4,
            "location": "127.0.0.1:3333",
            "version": "v1"
        }

        res = requests.post(
            service_url,
            data=json.dumps([reg]),
            headers=HEADERS)

        print("Got response from agent: ")
        print(res.content)
        print("\n ### Service registered ###")
