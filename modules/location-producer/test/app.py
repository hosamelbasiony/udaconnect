from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from kafka import KafkaProducer,KafkaConsumer
from json import dumps, loads
import logging
import os
import time
from concurrent import futures
import grpc
import threading

import greet_pb2 as greet_pb2
import greet_pb2_grpc as greet_pb2_grpc

def get_client_stream_requests():
    while True:
        hello_request = greet_pb2.LocationMessage()
        yield hello_request
        time.sleep(1)

def run_grpc_client():
    # from app.config import GRPC_SERVER
    GRPC_SERVER = "10.43.128.9:30005"
    
    print("***********************************************")
    print("\n\nTRYING TO CONNECT TO GRPC_SERVER AT: " + GRPC_SERVER + "\n\n")
    print("***********************************************")

    # with grpc.insecure_channel(GRPC_SERVER) as channel:
    with grpc.insecure_channel(GRPC_SERVER) as channel:        
        print("1. SayHei - Unary")
        stub = greet_pb2_grpc.LocationStub(channel)

        responses = stub.InteractingHi(get_client_stream_requests())

        for reply in responses:
            print("InteractingHi Response Received: ")
            print("\n\n\nParrotSaysHi Response Received:")
            print(reply)

run_grpc_client()
