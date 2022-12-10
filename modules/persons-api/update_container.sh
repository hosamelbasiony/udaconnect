#!/bin/bash

docker rmi udaconnect-persons-api
docker build -t udaconnect-persons-api .
docker tag udaconnect-persons-api hosamelbasiony/udaconnect-persons-api:"$1"
docker push hosamelbasiony/udaconnect-persons-api:"$1"

echo "First arg: $1"
