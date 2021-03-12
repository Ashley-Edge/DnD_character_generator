# Remove any previous locally built images 
docker-compose down --rmi local
sudo chmod 666 /var/run/docker.sock
docker-compose build   
sudo docker login 
# sudo docker-compose push