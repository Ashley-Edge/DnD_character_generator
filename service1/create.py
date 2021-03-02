#!/usr/bin/python3
#                   Create.py file

#####   Imports #####
from application import db
from application.models import Character

db.drop_all()
db.create_all()

#   Adding a Dummy character to check on my database
Character1=Character(character_race="a Dwarf", character_class="Fighter", weapon="whips")
db.session.add(Character1)
db.session.commit()
