#!usr/bin/python3
#                   Models.py file

#####   Imports ####
from application import db
from wtforms import StringField, SubmitField, IntergerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length

#####   Table   #####

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_race = db.Column(db.String(20), nullable=False)
    character_class = db.Column(db.String(20), nullable=False)
    weapon =  db.Column(db.String(20), nullable=False)
    #description = db.Column(db.String(250o), nullable=False)