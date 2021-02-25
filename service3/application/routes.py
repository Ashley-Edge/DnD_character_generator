#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, Response, request
import random
from application import app

#####   Classes #####

@app.route('/class', methods=['GET'])
def team():

    character_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    character_class = random.choices(character_classes)
    #character_race = character_races[random.randrange(0,9)]
    return Response(str(character_race), mimetype="text/plain")
    #return Response(character_class, mimetype="text/plain")

