#!/bin/bash

# checking if script is run as root or not
if [ "$EUID" -ne 0 ]; then
        echo "Please run this script as root!!"
        exit
fi

# execute containerA_main 
docker run --network bridge-nw container_a

# receive files from another containerB_main
docker run --network bridge-nw -v `pwd`/xmls:/xmls container_b
