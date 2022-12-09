import threading
import grpc
import logging
from datetime import datetime, timedelta
from typing import Dict, List

from flask import g

from app import db
from app.udaconnect.models import Connection, Location, Person
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api")

class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
            .filter(Location.id == location_id)
            .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def person(person_id) -> List[Location]:
        return db.session.query(Location).filter(
            Location.person_id == person_id
        ).all()

    @staticmethod
    def retrieve_all() -> List[Location]:
        return db.session.query(Location).all()

