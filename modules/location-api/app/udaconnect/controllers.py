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

@api.route("/person/locations/<person_id>")
@api.param("person_id", "ID of the persons to list all of his recorded locations", _in="query")
@api.doc(resposes={200: "Success"})
@api.doc(resposes={404: "Query not found"})
class LocationResource(Resource):
    @responds(schema=LocationSchema)
    def get(self, person_id) -> Location:
        location: Location = LocationService.person(person_id)
        return location


# @api.route("/persons")
# class PersonsResource(Resource):
#     @accepts(schema=PersonSchema)
#     @responds(schema=PersonSchema)
#     def post(self) -> Person:
#         payload = request.get_json()
#         new_person: Person = PersonService.create(payload)
#         return new_person

#     @responds(schema=PersonSchema, many=True)
#     def get(self) -> List[Person]:
#         persons: List[Person] = PersonService.retrieve_all()
#         return persons


# @api.route("/persons/<person_id>")
# @api.param("person_id", "Unique ID for a given Person", _in="query")
# class PersonResource(Resource):
#     @responds(schema=PersonSchema)
#     def get(self, person_id) -> Person:
#         person: Person = PersonService.retrieve(person_id)
#         return person


# @api.route("/persons/<person_id>/connection")
# @api.param("start_date", "Lower bound of date range", _in="query")
# @api.param("end_date", "Upper bound of date range", _in="query")
# @api.param("distance", "Proximity to a given user in meters", _in="query")
# class ConnectionDataResource(Resource):
#     @responds(schema=ConnectionSchema, many=True)
#     def get(self, person_id) -> ConnectionSchema:
#         start_date: datetime = datetime.strptime(
#             request.args["start_date"], DATE_FORMAT
#         )
#         end_date: datetime = datetime.strptime(request.args["end_date"], DATE_FORMAT)
#         distance: Optional[int] = request.args.get("distance", 5)

#         results = ConnectionService.find_contacts(
#             person_id=person_id,
#             start_date=start_date,
#             end_date=end_date,
#             meters=distance,
#         )
#         return results
