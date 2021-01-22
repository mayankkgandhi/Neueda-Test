#!/bin/bash

# checking if script is run as root or not
if [ "$EUID" -ne 0 ]; then
        echo "Please run this script as root!!"
        exit
fi

# removing containers with bridge-nw
docker rm -f $(docker ps -aq -f network=bridge-nw)

# removing other containers used for the process
docker rmi container_a:latest
docker rmi container_b:latest
docker rmi rabbitmq:management

# removing network bridge
docker network rm bridge-nw
