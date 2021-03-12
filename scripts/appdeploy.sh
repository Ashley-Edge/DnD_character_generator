# Login dnd-managerz
# ssh 10.172.0.15 << EOF
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@manager << EOF
sudo rm -rf DnD_character_generator
git clone https://github.com/Ashley-Edge/DnD_character_generator.git
cd DnD_character_generator
sudo docker login -u ashley -p PeneloPig1989
sudo docker stack deploy --compose-file docker-compose.yaml dnd
EOF