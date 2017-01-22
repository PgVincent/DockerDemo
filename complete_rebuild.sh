#!/bin/bash
docker-compose stop
docker-machine rm -fy default
docker rmi $(docker images -a | grep '^<none>' | awk '{print $3}')
docker-machine create --driver virtualbox default
eval "$(docker-machine env default)"
docker-compose rm -f
docker-compose build
docker-compose up -d
docker exec -ti d2_web_1 python manage.py migrate
docker exec -ti d2_web_1 python manage.py collectstatic --noinput