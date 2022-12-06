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
        # name = input("Please enter a name (or nothing to stop chatting): ")

        # if name == "":
        #     break

        # hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = name)
        hello_request = greet_pb2.LocationMessage()
        yield hello_request
        time.sleep(1)

def run_grpc_client():
    from app.config import GRPC_SERVER
    # with grpc.insecure_channel('localhost:50051') as channel:
    with grpc.insecure_channel(GRPC_SERVER) as channel:
        stub = greet_pb2_grpc.LocationStub(channel)
        print("1. SayHei - Unary")

        # location_request = greet_pb2.LocationMessage(
        #     person_id = 1, 
        #     person_name = "Bonjour Hoss Al-Nayem", 
        #     longitude = "12.025",
        #     latitude = "3569.263",
        #     creation_time = "2022-01-02 10:00:25",
        # )
        # location_replies = stub.ParrotSaysHi(location_request)

        # for reply in location_replies:
        #     print("\n\n\nParrotSaysHi Response Received:")
        #     print(reply)
        #     global socketio
        #     socketio.emit("location_updates", [{
        #         "person_id": reply.person_id, 
        #         "person_name": reply.person_name, 
        #         "longitude": reply.longitude, 
        #         "latitude": reply.latitude, 
        #         "creation_time": reply.creation_time, 
        #     }], namespace="/npTweet")

        responses = stub.InteractingHi(get_client_stream_requests())

        for reply in responses:
            print("InteractingHi Response Received: ")
            print("\n\n\nParrotSaysHi Response Received:")
            print(reply)
            # global socketio
            # socketio.emit("location_updates", [{
            #     "person_id": reply.person_id, 
            #     "person_name": reply.person_name, 
            #     "longitude": reply.longitude, 
            #     "latitude": reply.latitude, 
            #     "creation_time": reply.creation_time, 
            # }], namespace="/npTweet")

db = SQLAlchemy()

def serializer(message):
    return dumps(message).encode('utf-8')

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect Location Service", version="0.1.0")

    CORS(app, supports_credentials=True)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    from app.config import KAFKA_SERVER

    @app.before_request
    def before_request():
        TOPIC_NAME = 'locations'    
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER],
            api_version=(0,10,2),
            value_serializer=serializer
        )
        # consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER,api_version=(0,10,2),auto_offset_reset='earliest',enable_auto_commit=True,group_id='my-group',value_deserializer=lambda x: loads(x.decode()))
        g.kafka_producer = producer
        # g.kafka_consumer=consumer

    @app.route("/health")
    def health():
        return jsonify("healthy")

    logging.basicConfig()

    b = threading.Thread(name='run_grpc_client', target=run_grpc_client)
    b.daemon = True
    b.start()

    return app

    # # Initializes the gRPC server
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # location_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)

    # print("Server starting on port 5555..")
    # server.add_insecure_port("[::]:5555")
    # server.start()

    # # Keep thread alive
    # try:
    #     while True:
    #         time.sleep(86400)
    # except KeyboardInterrupt:
    #     server.stop(0)
