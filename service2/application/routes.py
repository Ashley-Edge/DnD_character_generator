#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, Response, request
import random
from application import app

#####    Race route #####

@app.route('/race', methods=['GET'])
def character_race():
    character_races = ["a Dwarf", "an Elf", "a Halfling", "a Human", "a Dragonborn", "a Gnome", "a Half-Elf", "a Half-Orc", "a Tiefling"]
    return Response(random.choices(character_races), mimetype="text/plain")
