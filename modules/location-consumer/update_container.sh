#!/bin/bash

docker rmi udaconnect-location-consumer
docker build -t udaconnect-location-consumer .
docker tag udaconnect-location-consumer hosamelbasiony/udaconnect-location-consumer:"$1"
docker push hosamelbasiony/udaconnect-location-consumer:"$1"

echo "First arg: $1"
