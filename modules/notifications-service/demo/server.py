
import grpc
import location_pb2 as location_pb2
import location_pb2_grpc as location_pb2_grpc
from concurrent import futures

class LocationServicer(location_pb2_grpc.LocationServicer):    
    def LocationCheckIn(self, request_iterator, context):
        for request in request_iterator:
            print(request)
            print("Interacting gRPC Request Made")
            print("**************************************\n")

            reply = location_pb2.LocationMessage()
            reply.person_name = request.person_name 
            reply.person_id = request.person_id #1
            reply.longitude = request.longitude #"1236.56"
            reply.latitude = request.latitude #"1236.56"
            reply.latitude = request.latitude #"2022-01-02 10:00:" + str(random.randint(0, 59))


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
location_pb2_grpc.add_LocationServicer_to_server(LocationServicer(), server)
server.add_insecure_port("[::]:30050")
print("Server starting on port 30050..")
server.start()
server.wait_for_termination()