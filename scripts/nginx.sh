ssh 10.172.0.12 << EOF
sudo rm -rf qa_project
git clone https://github.com/Ashley-Edge/DnD_character_generator.git
cd DnD_character_generator
cd nginx
docker-compose down --rmi local
docker-compose up -d
EOF