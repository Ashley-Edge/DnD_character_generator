#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, Response, request
import random
from application import app

#####   Classes #####

@app.route('/class', methods=['GET'])
def character_class():

    character_classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
    character_class = random.choices(character_classes)
    return Response(str(character_class[0]), mimetype="text/plain")
    