
from flask import Flask
from flask_socketio import SocketIO
import json
import grpc
import greet_pb2 as greet_pb2
import greet_pb2_grpc as greet_pb2_grpc
import time
import random
import threading
from concurrent import futures

class LocationServicer(greet_pb2_grpc.LocationServicer):
    def SayHi(self, request, context):
        print("SayHi LocationServicer Request Made:")
        print(request)
        reply = greet_pb2.LocationMessage()
        reply.person_name = "Wedny eheheheh eeeeehhh"

        return reply
    
    def ParrotSaysHi(self, request, context):
        print("ParrotSaysHi Request Made:")
        print(request)

        for i in range(3):
            reply = greet_pb2.LocationMessage()
            reply.person_name = "Wedny eheheheh eeeeehhh paroooot la moaakhzahh"
            yield reply
            time.sleep(3)
    
    def InteractingHi(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHi Request Made:")
            print(request)

            reply = greet_pb2.LocationMessage()
            reply.person_name = "Wedny eheheheh eeeeehhh paroooot la moaakhzahhhhh"
            reply.person_id = 1
            reply.longitude = "1236.56"
            reply.latitude = "1236.56"
            reply.latitude = "2022-01-02 10:00:" + str(random.randint(0, 59))

            global socketio
            socketio.emit("location_updates", [{
                "person_id": reply.person_id, 
                "person_name": reply.person_name, 
                "longitude": reply.longitude, 
                "latitude": reply.latitude, 
                "creation_time": reply.creation_time,
            }], namespace="/npTweet")

            yield reply

def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_LocationServicer_to_server(LocationServicer(), server)
    server.add_insecure_port("[::]:30050")
    print("Server starting on port 30050..")
    server.start()
    server.wait_for_termination()

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
    
    b = threading.Thread(name='serve_grpc', target=serve_grpc)
    b.daemon = True
    b.start()

    socketio.run(app, debug=True, host="0.0.0.0", port=5005, allow_unsafe_werkzeug=True)