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
    # Gets a race
    character_race = requests.get("http://localhost:5001/race")
    string_character_race = character_race.text

    # Gets a class
    character_class = requests.get("http://localhost:5002/class")
    string_character_class = character_class.text
    info = str(character_race.text) + "." + str(character_class.text)

    # Gets a weapon
    weapon = requests.post("http://localhost:5003/weapon", json={"character_race1":character_race.text, "character_class1":character_class.text}, data=info)

    #return render_template('index.html', character_race=string_character_race, character_class=string_character_class, info=info, weapon=weapon.text)

    # Past characters - will work on if I have time at the end

    char=Character.query.order_by(desc("Id")).limit(3).all()
    maxno=Character.query.order_by(Character.Id).first()
    randno=random.randint(1,maxno.Id)
    #randchar=Character.query.filter_by(Id=randno).all()

    new_character= Character(character_class=character_race.text, character_race=character_class.text, weapon=weapon.text)
    db.session.add(new_character)
    db.session.commit()

    return render_template("index.html", character_race=string_character_race, character_class=string_character_class, weapon=weapon.text, char=char)