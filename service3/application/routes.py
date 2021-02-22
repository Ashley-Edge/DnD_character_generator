#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, Response, request
import random
from application import app

#####   Classes #####

@app.route('/class', methods=['GEiT'])
def team():

    character_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
#    character_classe = character_classes[random.randrange(0,11)]
#    return Response(team, mimetype="text/plain")
    return Response(random.choices(character_classes), mimetype="text/plain")
