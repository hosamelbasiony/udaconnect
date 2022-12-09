from datetime import datetime
import time

from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import (
    ConnectionSchema,
    LocationSchema,
    PersonSchema,
)
from app.udaconnect.services import LocationService
from flask import request, g
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa

# TODO: This needs better exception handling

@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    # @responds(schema=LocationSchema)
    def post(self):
        request.get_json()        
        # location: Location = LocationService.create(request.get_json())        
        location = request.get_json();

        location = {
            "person_id": location["person_id"],
            "person_name": "Yet to get- Name",
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "creation_time": location["creation_time"]
        }
        producer = g.kafka_producer
        producer.send("location", location)
        producer.flush()

        time_stamp = time.time()
        print(time_stamp)
        return {
            "payload": "added to queue at " + str(time_stamp)
        }

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location

@api.route("/person/locations")
@api.route("/person/locations/<person_id>")
@api.param("person_id", "ID of the persons to list all of his recorded locations", _in="query")
@api.doc(resposes={200: "Success"})
@api.doc(resposes={404: "Query not found"})
class LocationResource(Resource):
    @responds(schema=LocationSchema)
    def get(self, person_id) ->List[Location]:
        return LocationService.person(person_id)

    @responds(schema=LocationSchema)
    def get(self) ->List[Location]:
        return LocationService.retrieve_all()