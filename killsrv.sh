#!/bin/bash

kubectl delete service kubernetes 
kubectl delete service kafka     
kubectl delete service postgres    
kubectl delete service udaconnect-locations-api
kubectl delete service udaconnect-app           
kubectl delete service kafka-zookeeper-headless 
kubectl delete service udaconnect-kafka-consumer
kubectl delete service udaconnect-notifications-service 
kubectl delete service kafka-zookeeper                  
kubectl delete service kafka-headless                   
kubectl delete service udaconnect-api 