# Login dnd-managerz
# ssh 10.172.0.15 << EOF
ssh -i ~/etc/ssh/ssh_host_rsa_key 10.172.0.15 << EOF
sudo rm -rf DnD_character_generator
git clone https://github.com/Ashley-Edge/DnD_character_generator.git
cd DnD_character_generator
sudo docker login -u ashley -p PeneloPig1989
sudo docker stack deploy --compose-file docker-compose.yaml dnd
EOF