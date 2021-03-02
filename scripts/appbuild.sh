# Remove current containers
docker-compose down --rmi all
# Re-build the containers again
docker-compose build
# login to DockerHub
sudo docker login
# Push new images to the DockerHub
sudo docker-compose push