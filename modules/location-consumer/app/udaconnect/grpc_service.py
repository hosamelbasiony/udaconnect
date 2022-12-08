import threading
import grpc
import logging
from datetime import datetime, timedelta
from typing import Dict, List
import os

import location_pb2 as location_pb2
import location_pb2_grpc as location_pb2_grpc

def get_client_stream_requests(location):
    location_request = location_pb2.LocationMessage(
        person_id = location["person_id"], 
        person_name = "in grpc service - " + location["person_name"], 
        longitude = location["longitude"],
        latitude = location["latitude"],
        creation_time = location["creation_time"],
    )    
    yield location_request

def run_grpc_client(location):
    
    GRPC_SERVER = os.environ["GRPC_SERVER"]

    
    print("***********************************************")
    print("\n\nTRYING TO CONNECT TO GRPC_SERVER AT: " + GRPC_SERVER + "\n\n")
    print("LOCATION:\n")
    print(location)
    print("***********************************************")

    with grpc.insecure_channel(GRPC_SERVER) as channel:
        stub = location_pb2_grpc.LocationStub(channel)
        print("run_grpc_client ... running")

        responses = stub.LocationCheckIn(get_client_stream_requests(location))

        for reply in responses:
            print("LocationCheckIn Response Received: ")
            print("\n\n\nParrotSaysHi Response Received:")
            print(reply)


