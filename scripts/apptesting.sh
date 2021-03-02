# Install dependencies
sudo update -y
sudo upgrade -y
sudo apt install -y python3 python3-pip

# cd into service1, install requirements and test it
cd service1
pip3 install -r requirements.txt
python3 -m pytest --cov app

# cd into service2 and test it
cd ../service2
python3 -m pytest --cov app

# cd into service3 and test it
cd ../service3
python3 -m pytest --cov app

# cd into service4 and test it
cd ../service4
python3 -m pytest --cov app

# Return to root
cd ..