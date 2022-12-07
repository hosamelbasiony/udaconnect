#!/bin/bash

docker rmi udaconnect-location-producer
docker build -t udaconnect-location-producer .
docker tag udaconnect-location-producer hosamelbasiony/udaconnect-location-producer:"$1"
docker push hosamelbasiony/udaconnect-location-producer:"$1"

echo "First arg: $1"
