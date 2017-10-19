#!/bin/bash

PORT=9999
MEMORY=100 #in MB

docker rm -f crypto500
docker run --name crypto500 -m ${MEMORY}m -p $PORT:9999 -d ugractf_crypto500:latest
