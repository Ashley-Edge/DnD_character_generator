#!/usr/bin/python3
#           Routes.py file

from application import app
from flask import request, Response

@app.route('/weapon', methods=["POST"])
def weapon():
    weapons = {
        "a Dwarf" : {
            "Barbarian" : "a battle axe", 
            "Bard" : "a light hammer", 
            "Cleric" : "a warhammer", 
            "Druid": "a club", 
            "Fighter": "a halberd and shield", 
            "Monk": "their bare fists", 
            "Paladin": "a battle axe and shield", 
            "Ranger": "two maces", 
            "Rogue": "a long sword and two hidden daggers", 
            "Sorcerer": "two enchanted daggers", 
            "Warlock": "eldrich blast", 
            "Wizard": "bedazzling illusion spells"
        },
        "an Elf" : {
            "Barbarian" : "a long sword", 
            "Bard" : "a rapier", 
            "Cleric" : "a light crossbow", 
            "Druid" : "a dagger", 
            "Fighter" : "whips", 
            "Monk" : "the mystic energy of ki", 
            "Paladin" : "a great axe and shield", 
            "Ranger" : "a longbow", 
            "Rogue" : "a hand crossbow and thieves tools", 
            "Sorcerer" : "a light crossbow", 
            "Warlock" : "their book of shadows", 
            "Wizard" : "elemental magic"
        },
        "a Halfling" : {
            "Barbarian" : "a club", 
            "Bard" : "an enchanted lute", 
            "Cleric" : "a dagger", 
            "Druid": "a sling", 
            "Fighter": "two short swords", 
            "Monk": "kama", 
            "Paladin": "a great sword and shield", 
            "Ranger": "two daggers", 
            "Rogue": "a rapier and a poisoner's kit", 
            "Sorcerer": "their wild magic", 
            "Warlock": "a spear", "Wizard": "transmutation magic"
        },
        "a Human": {
            "Barbarian": "two hand axes", 
            "Bard": "a magical flute", 
            "Cleric": "a mace", 
            "Druid": "a quarter staff", 
            "Fighter": "a great sword and shield", 
            "Monk": "a nunchaku", 
            "Paladin": "a warhammer and shield", 
            "Ranger": "two light hammers", 
            "Rogue": "two daggers and a poisoner's kit", 
            "Sorcerer": "quarter staff", 
            "Warlock": "their pact of the blade to materialise any melee weapon", 
            "Wizard": "dark necromancy magic"
        },
        "a Dragonborn": {
            "Barbarian": "a glaive", 
            "Bard": "a long sword", 
            "Cleric": "a spear", 
            "Druid": "darts", 
            "Fighter": "two scimitars", 
            "Monk": "a sling", 
            "Paladin": "a heavy crossbow and shield", 
            "Ranger": "a great club and dagger", 
            "Rogue": "a short sword and two hidden daggers", 
            "Sorcerer": "their powerful alchemist's fire", 
            "Warlock": "their pact of chain pseudo dragon", 
            "Wizard": "their third eye"
        },
        "a Gnome": {
            "Barbarian": "a war pick", 
            "Bard": "a dagger", 
            "Cleric": "a quarter staff", 
            "Druid": "a sickle", 
            "Fighter": "a light cross bow", 
            "Monk": "a club", 
            "Paladin": "a glaive and shield", 
            "Ranger": "two short swords", 
            "Rogue": "a short sword and thieves tools", 
            "Sorcerer": "a lance", 
            "Warlock": "their pact of the chain quasit", 
            "Wizard": "enchantment spells"
        },
        "a Half-Elf": {
            "Barbarian": "a great sword", 
            "Bard": "a hypnotising harp", 
            "Cleric": "a hand axe", 
            "Druid": "a scimitar", 
            "Fighter": "a long bow", 
            "Monk": "short bow", 
            "Paladin": "two rapiers", 
            "Ranger": "two sickles", 
            "Rogue": "a poisoner's kit and two hidden daggers", 
            "Sorcerer": "darts", 
            "Warlock": "their pact of the chain sprite", 
            "Wizard": "quarter staff"
        },
        "a Half-Orc": {
            "Barbarian": "a mace", 
            "Bard": "a javelin", 
            "Cleric": "a club", 
            "Druid": "a spear", 
            "Fighter": "two hand axes", 
            "Monk": "a short sword", 
            "Paladin": "two morning stars", 
            "Ranger": "a dagger and spear combo", 
            "Rogue": "a long sword and two hidden daggers", 
            "Sorcerer": "twin slings", 
            "Warlock": "a light crossbow", 
            "Wizard": "divination spells"
        },
        "a Tiefling": {
            "Barbarian": "a great axe", 
            "Bard": "a sickle", 
            "Cleric": "a javelin", 
            "Druid": "a javelin", 
            "Fighter": "a morning star", 
            "Monk": "a sickle", 
            "Paladin": "five javelins", 
            "Ranger": "two hand axes", 
            "Rogue": "a hand crossbow and thieves tools", 
            "Sorcerer": "achient meta magic", 
            "Warlock": "the agonising blast cantrip", 
            "Wizard": "conjuration magic"
        }
    }
    info = request.json 
    return Response(weapons[info["character_race"]][info["character_class"]], mimetype='text/plain')