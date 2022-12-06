from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from kafka import KafkaProducer,KafkaConsumer
from json import dumps, loads
import logging
import os
from config import KAFKA_SERVER

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

    # @app.before_request
    # def before_request():
    TOPIC_NAME = 'locations'    
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_SERVER],
        api_version=(0,10,2),
        value_serializer=serializer
    )
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,api_version=(0,10,2))
    # consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER,api_version=(0,10,2),auto_offset_reset='earliest',enable_auto_commit=True,group_id='my-group',value_deserializer=lambda x: loads(x.decode()))
    g.kafka_producer = producer
    # g.kafka_consumer=consumer

    @app.route("/health")
    def health():
        return jsonify("healthy")

    logging.basicConfig()

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
