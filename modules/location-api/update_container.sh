#!/bin/bash

docker rmi udaconnect-location-api
docker build -t udaconnect-location-api .
docker tag udaconnect-location-api hosamelbasiony/udaconnect-location-api:"$1"
docker push hosamelbasiony/udaconnect-location-api:"$1"

echo "First arg: $1"
