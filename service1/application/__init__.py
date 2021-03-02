#!/usr/bin/python3
#                   __init__.py file

#####   Imports #####
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import getenv

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@database/character_db'
app.config['SECRET_KEY'] = 'ashleysecrret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
