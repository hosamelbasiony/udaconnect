import json
import sys 
import os
import threading

from dotenv import load_dotenv

from kafka import KafkaProducer, KafkaConsumer
from flask import Flask, jsonify, request, g, Response

load_dotenv()

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
    kafka_data = order_data
    # Kafka producer has already been set up in Flask context
    g.kafka_producer.send("first_kafka_topic", kafka_data)


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
KAFKA_SERVER = os.environ["KAFKA_SERVER"]

def background():
    consumer = KafkaConsumer(
        # 'first_kafka_topic',
        'first_kafka_topic',
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest'
    )

    for message in consumer:
        print("\n\n\n\n\n")
        print(json.loads(message.value))

def serializer(message):
    return json.dumps(message).encode('utf-8')

app = Flask(__name__)

@app.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'first_kafka_topic'
    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_SERVER],
        value_serializer=serializer
    )
    g.kafka_producer = producer


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['GET', 'POST'])
def computers():
    if request.method == 'GET':
        msg = {
                "created_at": "2020-10-16T10:31:10.969696",
                "created_by": "USER14",
                "equipment": [
                "KEYBOARD",
                "MOUSE"
                ],
                "id": "1",
                "status": "Queued"
            }
        result = create_order(json.dumps(msg))
        return jsonify(retrieve_orders())
    elif request.method == 'POST':
        request_body = request.json
        result = create_order(request_body)
        return Response(status=202)
    else:
        raise Exception('Unsupported HTTP request type.')



if __name__ == '__main__':
    b = threading.Thread(name='background', target=background)
    b.daemon = True
    b.start()
    app.run(debug=True, host="0.0.0.0", port=5001)