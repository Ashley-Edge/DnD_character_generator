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
    character_race = requests.get("http://localhost:5001/race")
    string_character_race = character_race.text

    # Gets a class
    character_class = requests.get("http://localhost:5002/class")
    string_character_class = character_class.text

    info = str(character_race.text) + "." + str(character_class.text)
    # Gets a weapon
    weapon = requests.post("http://localhost:5003/weapon", data=info)

    return render_template('index.html', character_race=string_character_race, character_class=string_character_class, info=info, weapon=weapon.text)
