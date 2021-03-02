#!/bin/bash

# Login dnd-manager
ssh 10.172.0.5 << EOF
sudo rm -rf DnD_character_generator
git clone https://github.com/Ashley-Edge/DnD_character_generator.git
cd qa_project
sudo docker login
sudo docker stack deploy --compose-file docker-compose.yaml dnd
EOF