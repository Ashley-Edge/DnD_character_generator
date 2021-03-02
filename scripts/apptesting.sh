# Install dependencies
sudo apt update
sudo apt upgrade 
sudo apt install -y python3 python3-pip
sudo pip3 install --upgrade pip

# cd into service1, install requirements and test it
cd service1
pip3 install -r requirements.txt
python3 create.py
pytest --cov=application

# cd into service2 and test it
cd ../service2
python3 -m pytest --cov=application

# cd into service3 and test it
cd ../service3
python3 -m pytest --cov=application

# cd into service4 and test it
cd ../service4
pytest --cov=application

# Return to root
cd ..