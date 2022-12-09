## gRPC documentation of the endpoint and how to make a sample request:
<hr><br>

### The following is the protobuf message structure used to pass <b><i>Location CheckIn Message</i></b> from Locations microservice and Kafka consumer service

<br>

```
syntax = "proto3";

message LocationMessage {   
	int32 person_id = 1;
	string person_name = 2;
	string longitude = 3;
	string latitude = 4;
	string creation_time = 5;
}

message Empty {

}

message LocationMessageList {
	repeated LocationMessage locations = 1;
}

service LocationService {
	rpc Create(LocationMessage) returns (LocationMessage);
	rpc Get(Empty) returns (LocationMessageList);
}
```
<br>

### How to make requests:

1. Clone https://github.com/hosamelbasiony/udaconnect

2. cd into ./modules/notifications-service/demo

3. Run 

```
python -m venv venv
source venv/Scripts/activate => windows
source venv/bin/activate => linux
pip install -r requirements.txt
```

4. Run server.py

5. Run client.py

6. You should see a sample location message passed and logged to the terminal