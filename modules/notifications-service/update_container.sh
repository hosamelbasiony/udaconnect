#!/bin/bash

docker rmi udaconnect-notifications-service
docker build -t udaconnect-notifications-service .
docker tag udaconnect-notifications-service hosamelbasiony/udaconnect-notifications-service:"$1"
docker push hosamelbasiony/udaconnect-notifications-service:"$1"

echo "First arg: $1"
