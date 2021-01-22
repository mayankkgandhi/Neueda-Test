#!/bin/bash

if [ "$EUID" -ne 0 ]; then 
	echo "Please run this script as root!!"
  	exit
fi

#Creating a Docker Network - bridge type
docker network create -d bridge bridge-nw

# build containerA_main docker image
docker build -t container_a container_a

# build containerB_main docker image
docker build -t container_b container_b/

# Run RabbitMQ Container in network created above
docker run -d --restart always --hostname rabbitqueue --name rabbitqueue --network bridge-nw rabbitmq:management
