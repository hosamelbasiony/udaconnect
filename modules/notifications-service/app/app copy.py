
from flask import Flask
from flask_socketio import SocketIO
import json
import grpc
import greet_pb2 as greet_pb2
import greet_pb2_grpc as greet_pb2_grpc
import time
import threading

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
    with grpc.insecure_channel('localhost:50051') as channel:
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
            global socketio
            socketio.emit("location_updates", [{
                "person_id": reply.person_id, 
                "person_name": reply.person_name, 
                "longitude": reply.longitude, 
                "latitude": reply.latitude, 
                "creation_time": reply.creation_time, 
            }], namespace="/npTweet")


app = Flask(__name__)

app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")

def root():
    return app.send_static_file("index.html")

@socketio.on("connect", namespace="/npTweet")
def connectServer():
    print("Client connected")
    socketio.emit("connected", namespace="/npTweet")


@socketio.on("startTweets", namespace="/npTweet")
def tweetStreaming():
    print("Start streaming tweets...")
    socketio.emit("streamTweets", {"stream_result": "test"}, namespace="/npTweet")

@socketio.on("location_updates", namespace="/npTweet")
def tweetStreaming():
    print("Start streaming locations...")
    socketio.emit("location_updates",  [{
        "person_id": 1, 
        "longitude": "30.605240974982205", 
        "latitude": "32.29687938288871",
        "creation_time": "2022-08-18 10:37:06.000000"
    }], namespace="/npTweet")


if __name__ == "__main__":
    
    b = threading.Thread(name='run_grpc_client', target=run_grpc_client)
    b.daemon = True
    b.start()

    socketio.run(app, debug=True, host="0.0.0.0", port=5005)