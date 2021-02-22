#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, render_template, request
import requests
from application import app, db
from application.models import Character

#####   Routes  #####

@app.route('/', methods=['GET','POST'])
def index():
    # Gets a race
    character_race = requests.get("http://service2:5001/character_race")
    # Gets a class
    character_class = requests.get("http://service3:5002/character_class")
    info = str(character_race.text) + " " + str(character_class.text)
    # Gets a weapon
    weapon = requests.post("http://service4:5003/weapon")
    #description = requests.post("http://service4:5003/description")        might add later

    return render_template('index.html', character_race=character_race.text, character_class=character_class.text, weapon=weapon.text, info=info)
