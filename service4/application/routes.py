#!/usr/bin/python3
#                   Routes.py file

#####   Imports #####
from flask import Flask, Response, requests
import random
from application import app

@app.route('/weapon', methods=['GET', 'POST'])
def weapon():
    info = request.data.decode('utf-8')
    data2 = info.split(".")
    character_race = data2[0]
    character_class = data2[1]

#####   Dwarf weapons   #####

    if character_race == "a Dwarf":
        if character_class == "Barbarian":
            weapon = "a battle axe"
        elif character_class == "Bard":
            weapon = "a light hammer"
        elif character_class == "Cleric":
            weapon = "a warhammer"
        elif character_class == "Druid":
            weapon = "a club"
        elif character_class == "Fighter":
            weapon = "a halberd and shield"
        elif character_class == "Monk":
            weapon = "their bare fists"
        elif character_class == "Paladin":
            weapon = "a battle axe and shield"
        elif character_class == "Ranger":
            weapon = "two maces"
        elif character_class == "Rogue":
            weapon = "a long sword and two hidden daggers"
        elif character_class == "Sorcerer":
            weapon = "two enchanted daggers"
        elif character_class == "Warlock":
            weapon = "eldrich blast"
        elif character_class == "Wizard":
            weapon = "bedazzling illusion spells"

#####   Elf weapons   #####

    elif character_race == "an Elf":
        if character_class == "Barbarian":
            weapon = "a long sword"
        elif character_class == "Bard":
            weapon = "a rapier"
        elif character_class == "Cleric":
            weapon = "a light crossbow"
        elif character_class == "Druid":
            weapon = "a dagger"
        elif character_class == "Fighter":
            weapon = "whips"
        elif character_class == "Monk":
            weapon = "the mystic energy of ki"
        elif character_class == "Paladin":
            weapon = "a great axe and shield"
        elif character_class == "Ranger":
            weapon = "a longbow"
        elif character_class == "Rogue":
            weapon = "a hand crossbow and thieves tools"
        elif character_class == "Sorcerer":
            weapon = "a light crossbow"
        elif character_class == "Warlock":
            weapon = "their book of shadows"
        elif character_class == "Wizard":
            weapon = "elemental magic"

#####   Halfling weapons   #####

    elif character_race == "a Halfling":
        if character_class == "Barbarian":
            weapon = "a club"
        elif character_class == "Bard":
            weapon = "an enchanted lute"
        elif character_class == "Cleric":
            weapon = "a dagger"
        elif character_class == "Druid":
            weapon = "a sling"
        elif character_class == "Fighter":
            weapon = "two short swords"
        elif character_class == "Monk":
            weapon = "kama"
        elif character_class == "Paladin":
            weapon = "a great sword and shield"
        elif character_class == "Ranger":
            weapon = "two daggers"
        elif character_class == "Rogue":
            weapon = "a rapier and a poisoner's kit"
        elif character_class == "Sorcerer":
            weapon = "their wild magic"
        elif character_class == "Warlock":
            weapon = "a spear"
        elif character_class == "Wizard":
            weapon = "transmutation magic"

#####   Human weapons   #####

    elif character_race == "a Human":
        if character_class == "Barbarian":
            weapon = "two hand axes"
        elif character_class == "Bard":
            weapon = "a magical flute"
        elif character_class == "Cleric":
            weapon = "a mace"
        elif character_class == "Druid":
            weapon = "a quarter staff"
        elif character_class == "Fighter":
            weapon = "a great sword and shield"
        elif character_class == "Monk":
            weapon = "a nunchaku"
        elif character_class == "Paladin":
            weapon = "a warhammer and shield"
        elif character_class == "Ranger":
            weapon = "two light hammers"
        elif character_class == "Rogue":
            weapon = "two daggers and a poisoner's kit"
        elif character_class == "Sorcerer":
            weapon = "quarter staff"
        elif character_class == "Warlock":
            weapon = "their pact of the blade to materialise any melee weapon"
        elif character_class == "Wizard":
            weapon = "dark necromancy magic"

#####   Dragonborn weapons   #####

    elif character_race == "a Dragonborn":
        if character_class == "Barbarian":
            weapon = "a glaive"
        elif character_class == "Bard":
            weapon = "a long sword"
        elif character_class == "Cleric":
            weapon = "a spear"
        elif character_class == "Druid":
            weapon = "darts"
        elif character_class == "Fighter":
            weapon = "two scimitars"
        elif character_class == "Monk":
            weapon = "a sling"
        elif character_class == "Paladin":
            weapon = "a heavy crossbow and shield"
        elif character_class == "Ranger":
            weapon = "a great club and dagger"
        elif character_class == "Rogue":
            weapon = "a short sword and two hidden daggers"
        elif character_class == "Sorcerer":
            weapon = "their powerful alchemist's fire"
        elif character_class == "Warlock":
            weapon = "their pact of chain pseudo dragon"
        elif character_class == "Wizard":
            weapon = "their third eye"

#####   Gnome weapons   #####

    elif character_race == "a Gnome":
        if character_class == "Barbarian":
            weapon = "a war pick"
        elif character_class == "Bard":
            weapon = "a dagger"
        elif character_class == "Cleric":
            weapon = "a quarter staff"
        elif character_class == "Druid":
            weapon = "a sickle"
        elif character_class == "Fighter":
            weapon = "a light cross bow"
        elif character_class == "Monk":
            weapon = "a club"
        elif character_class == "Paladin":
            weapon = "a glaive and shield"
        elif character_class == "Ranger":
            weapon = "two short swords"
        elif character_class == "Rogue":
            weapon = "a short sword and thieves tools"
        elif character_class == "Sorcerer":
            weapon = "a lance"
        elif character_class == "Warlock":
            weapon = "their pact of the chain quasit"
        elif character_class == "Wizard":
            weapon = "enchantment spells"

#####   Half-Elf weapons   #####

    elif character_race == "a Half-Elf":
        if character_class == "Barbarian":
            weapon = "a great sword"
        elif character_class == "Bard":
            weapon = "a hypnotising harp"
        elif character_class == "Cleric":
            weapon = "a hand axe"
        elif character_class == "Druid":
            weapon = "a scimitar"
        elif character_class == "Fighter":
            weapon = "a long bow"
        elif character_class == "Monk":
            weapon = "short bow"
        elif character_class == "Paladin":
            weapon = "two rapiers"
        elif character_class == "Ranger":
            weapon = "two sickles"
        elif character_class == "Rogue":
            weapon = "a poisoner's kit and two hidden daggers"
        elif character_class == "Sorcerer":
            weapon = "darts"
        elif character_class == "Warlock":
            weapon = "their pact of the chain sprite"
        elif character_class == "Wizard":
            weapon = "quarter staff"

#####   Half-Orc weapons   #####

    elif character_race == "a Half-Orc":
        if character_class == "Barbarian":
            weapon = "a mace"
        elif character_class == "Bard":
            weapon = "a javelin"
        elif character_class == "Cleric":
            weapon = "a club"
        elif character_class == "Druid":
            weapon = "a spear"
        elif character_class == "Fighter":
            weapon = "two hand axes"
        elif character_class == "Monk":
            weapon = "a short sword"
        elif character_class == "Paladin":
            weapon = "two morning stars"
        elif character_class == "Ranger":
            weapon = "a dagger and spear combo"
        elif character_class == "Rogue":
            weapon = "a long sword and two hidden daggers"
        elif character_class == "Sorcerer":
            weapon = "twin slings"
        elif character_class == "Warlock":
            weapon = "a light crossbow"
        elif character_class == "Wizard":
            weapon = "divination spells"

#####   Tiefling weapons   #####

    elif character_race == "a Tiefling":
        if character_class == "Barbarian":
            weapon = "a great axe"
        elif character_class == "Bard":
            weapon = "a sickle"
        elif character_class == "Cleric":
            weapon = "a javelin"
        elif character_class == "Druid":
            weapon = "a javelin"
        elif character_class == "Fighter":
            weapon = "a morning star"
        elif character_class == "Monk":
            weapon = "a sickle"
        elif character_class == "Paladin":
            weapon = "five javelins"
        elif character_class == "Ranger":
            weapon = "two hand axes"
        elif character_class == "Rogue":
            weapon = "a hand crossbow and thieves tools"
        elif character_class == "Sorcerer":
            weapon = "achient meta magic"
        elif character_class == "Warlock":
            weapon = "the agonising blast cantrip"
        elif character_class == "Wizard":
            weapon = "conjuration magic"
    else:
        return "..... OH! I'm sorry, your character is lost. Try recreating one"

    return Response(weapon, mimetype="text/plain")