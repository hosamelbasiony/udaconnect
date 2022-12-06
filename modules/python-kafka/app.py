import json
import sys 
import os

from kafka import KafkaProducer
from flask import Flask, jsonify, request, g, Response

# KAFKA_SERVER = os.environ["KAFKA_SERVER"]
# DB_PASSWORD = os.environ["DB_PASSWORD"]
# DB_HOST = os.environ["DB_HOST"]
# DB_PORT = os.environ["DB_PORT"]
# DB_NAME = os.environ["DB_NAME"]

####################################################################
####################################################################
from enum import Enum

class Status(Enum):
    Queued = 'Queued'
    Processing = 'Processing'
    Completed = 'Completed'
    Failed = 'Failed'

def create_order(order_data):
    """
    This is a stubbed method of retrieving a resource. It doesn't actually do anything.
    """
    # Turn order_data into a binary string for Kafka
    kafka_data = json.dumps(order_data).encode()
    # Kafka producer has already been set up in Flask context
    kafka_producer = g.kafka_producer
    kafka_producer.send("items", kafka_data)


def retrieve_orders():
    """
    This is a stubbed method of retrieving multiple resources. It doesn't actually do anything.
    """
    return [
        {
            "id": "1",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:31:10.969696",
            "created_by": "USER14",
            "equipment": [
                "KEYBOARD", "MOUSE"
            ]
        },
        {
            "id": "2",
            "status": Status.Queued.value,
            "created_at": "2020-10-16T10:29:10.969696",
            "created_by": "USER15",
            "equipment": [
                "KEYBOARD", "WEBCAM"
            ]
        }
    ]
####################################################################
####################################################################

app = Flask(__name__)

@app.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'items'
    # KAFKA_SERVER = 'localhost:9092'
    KAFKA_SERVER = 'kafka-headless:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        result = create_order(request_body)
        return Response(status=202)
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)