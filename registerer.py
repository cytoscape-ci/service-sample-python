import json
import requests
import logging

from requests.exceptions import ConnectionError

logging.basicConfig(level=logging.DEBUG)

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
        service_location = location + ":" + str(port)

        reg = {
            "name": name,
            "capacity": capacity,
            "location": service_location,
            "version": version
        }

        # Try registering this service to Submit Agent
        try:
            res = requests.post(
                service_url,
                data=json.dumps([reg]),
                headers=HEADERS)
            status = res.status_code

            logging.info("Registered: " + str(status))

        except ConnectionError as ce:
            logging.warning("Could not register this service to Submit Agent.")
            logging.warning("Caused by: ")
            logging.warning(ce)
            logging.warning("Running as an independent service at: " + str(service_location))
