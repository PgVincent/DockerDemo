#!/bin/bash
docker-compose stop
docker-machine rm default -y
docker-machine create --driver virtualbox default
eval "$(docker-machine env default)"
docker-compose rm -f --all
docker-compose build
docker-compose up -d
