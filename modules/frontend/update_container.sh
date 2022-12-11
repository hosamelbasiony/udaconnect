#!/bin/bash

docker rmi udaconnect-app
docker build -t udaconnect-app .
docker tag udaconnect-app hosamelbasiony/udaconnect-app:"$1"
docker push hosamelbasiony/udaconnect-app:"$1"

echo "First arg: $1"
