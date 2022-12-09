import location_pb2
import location_pb2_grpc
from concurrent import futures

import grpc
import os
import time

def get_client_stream_requests(location):
    location_request = location_pb2.LocationMessage(
        person_id = location["person_id"], 
        person_name = "in grpc service - " + location["person_name"], 
        longitude = location["longitude"],
        latitude = location["latitude"],
        creation_time = location["creation_time"],
    )    
    yield location_request

def run():
    GRPC_SERVER = "127.0.0.1:30050" #os.environ["GRPC_SERVER"]

    print(GRPC_SERVER)
    
    print("***********************************************")
    print("\n\nTRYING TO CONNECT TO GRPC_SERVER AT: " + GRPC_SERVER + "\n\n")
    print("LOCATION:\n")
    print("***********************************************")

    with grpc.insecure_channel(GRPC_SERVER) as channel:
        stub = location_pb2_grpc.LocationStub(channel)
        print("run_grpc_client ... running")

        responses = stub.LocationCheckIn(get_client_stream_requests({
            "person_id": 10,
            "person_name": "Some Name",
            "latitude": "2022-08-18T10:37:06",
            "longitude": "31.2968793828787",
            "creation_time": "2022-08-18T10:37:06"
        }))

        for reply in responses:
            print("LocationCheckIn Response Received: ")
            print("\n\n\nParrotSaysHi Response Received:")
            print(reply)

if __name__ == "__main__":
    run()