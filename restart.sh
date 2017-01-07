#/bin/bash
# Stop currently running containers
docker-compose stop

# Remove unused containers
docker rmi $(docker images -a | grep '^<none>' | awk '{print $3}')

docker-compose rm -f --all

# Start the containers with a rebuild.
docker-compose up -d --force-recreate --build --remove-orphans
