import threading
import grpc
import logging
from datetime import datetime, timedelta
from typing import Dict, List

import greet_pb2 as greet_pb2
import greet_pb2_grpc as greet_pb2_grpc

def get_client_stream_requests(location):
    location_request = greet_pb2.LocationMessage(
        person_id = location.person_id, 
        person_name = "in grpc service - " + location.person_name, 
        longitude = location.longitude,
        latitude = location.latitude,
        creation_time = location.creation_time,
    )    
    yield location_request

def run_grpc_client(location):
    from app.config import GRPC_SERVER
    
    print("***********************************************")
    print("\n\nTRYING TO CONNECT TO GRPC_SERVER AT: " + GRPC_SERVER + "\n\n")
    print("LOCATION:\n")
    print(location)
    print("***********************************************")

    with grpc.insecure_channel(GRPC_SERVER) as channel:
        stub = greet_pb2_grpc.LocationStub(channel)
        print("run_grpc_client ... running")

        responses = stub.InteractingHi(get_client_stream_requests(location))

        for reply in responses:
            print("InteractingHi Response Received: ")
            print("\n\n\nParrotSaysHi Response Received:")
            print(reply)

