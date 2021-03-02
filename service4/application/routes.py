#!/usr/bin/python3
#           Routes.py file

from application import app
from flask import request, Response

@app.route('/weapon', methods=["POST"])
def weapon():
    weapons = {
        "a Dwarf" : {
            "Barbarian" : "a battle axe", 
            "Cleric" : "a warhammer", 
            "Fighter": "a halberd and shield", 
            "Paladin": "a battle axe and shield", 
            "Wizard": "bedazzling illusion spells"
        },
        "an Elf" : {
            "Barbarian" : "a long sword",
            "Cleric" : "a light crossbow",
            "Fighter" : "whips", 
            "Paladin" : "a great axe and shield", 
            "Wizard" : "elemental magic"
        },
        "a Halfling" : {
            "Barbarian" : "a club",
            "Cleric" : "a dagger",
            "Fighter": "two short swords", 
            "Paladin": "a great sword and shield", 
            "Warlock": "a spear", "Wizard": "transmutation magic"
        },
        "a Human": {
            "Barbarian": "two hand axes", 
            "Cleric": "a mace",
            "Fighter": "a great sword and shield", 
            "Paladin": "a warhammer and shield", 
            "Wizard": "dark necromancy magic"
        },
    }
    info = request.json 
    return Response(weapons[info["character_race"]][info["character_class"]], mimetype='text/plain')