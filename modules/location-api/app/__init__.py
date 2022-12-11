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

db = SQLAlchemy()

def serializer(message):
    return dumps(message).encode('utf-8')

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "test"])
    api = Api(app, title="UdaConnect Location Service", version="0.1.0")

    #################################################################
    ################################################################
    ## TRACING #####################################################
    ################################################################    
    import logging  
    from jaeger_client import Config
    from flask_opentracing import FlaskTracing  
    config = Config(
    config={
            'sampler':
            {'type': 'const',
            'param': 1},
                            'logging': True,
                            'reporter_batch_size': 1,}, 
                            service_name="udaconnect-service")
    jaeger_tracer = config.initialize_tracer()
    tracing = FlaskTracing(jaeger_tracer, True, app)
    with jaeger_tracer.start_span("locations-api-span") as span:
        span.set_tag("locations-api-tag", "100")
    ################################################################
    ################################################################

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

    return app
