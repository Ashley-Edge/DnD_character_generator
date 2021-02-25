#!/usr/bin/python3
#                   Create.py file

#####   Imports #####
from application import db
from application.models import Character

db.drop_all()
db.create_all()
Character1=Character(character_race="a Dwarf", character_class="Fighter", weapon="whips")
db.session.add(Character1)
#db.create_all()
db.session.commit()
