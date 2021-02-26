#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, render_template, request
import requests, random
from application import app, db
from application.models import Character
from sqlalchemy import desc

#####   Routes  #####

@app.route('/', methods=['GET','POST'])
def index():
    character_race_response = requests.get("http://localhost:5001/race")
    character_class_response = requests.get("http://localhost:5002/class")
    weapon_response = requests.post("http://localhost:5003/weapon", json={"character_race":character_race_response.text, "character_class":character_class_response.text})

    new_character= Character(character_race=character_race_response.text,character_class=character_class_response.text,weapon=weapon_response.text)
    db.session.add(new_character)
    db.session.commit()

    old_characters = Character.query.order_by(desc("Id")).limit(3).all()

    return render_template("index.html", character_race=character_race_response.text, character_class=character_class_response.text, weapon=weapon_response.text, old_characters=old_characters)