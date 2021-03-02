#!/usr/bin/python3
#                   __init__.py file

#####   Imports #####
from flask import Flask

app = Flask(__name__)

from application import routes
