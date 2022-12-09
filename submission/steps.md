# Analysis:
## What to refactor with strangler pattern

- ### Location route and location service are more decoupled from the rest of the application

- ### Further the location route will be refactored to accomodate message queueing to Kafka logs aggregator later on

### This is a good candidate for refactoring
<br />

![alt text](images/image1.png)
<br /><br />
# Messaging passing strategies used
- ### For the front-end facing routes REST APIs are used
- ### Websocket microservice is added to notify the connected users with potential realtime connections
- ### Message queueing with Kafka logs aggregator is implemented to receive the <b>posted locations</b> from the loations rest endpoit (Kafka producer) and mediates the events to the locations service which will persist the data and notify the websocker microservice
- ### gRPC prtocol is used to carry the messages from the Kafka consumer in the locations microservice to the websocket microservice
<br />

![alt text](images/image2.png)
<br /><br />

# Rationale for using various message passing protocols:
## REST APIs
- ### REST APIs are the most suitable for endpoints intefacing with the users because it is flexible, easy to implement, and provides stateless client-server relationship
- ### REST APIs are the most popular choice in this context and we have no reason to adopt any other protocol

## gRPC
- ### gRPC is used where typing is essential for inter-microservice messaging
- ### gRPC provide standard messaging system even if we decide later on to implement other technologies or recruit other teams in the futures

## Message Queues
- ### Message queueing is used where enormous amount of data is expected (in the locations <b>POST</b> route) to accomodate the events in a way that prevents data loss