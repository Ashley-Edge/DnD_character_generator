#!/usr/bin/python3
#                   Test_service1 file

#####   Imports #####
import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
#from os import getenv
#import requests_mock

from app import app, db
from application.models import character

#####   Test version 1    #####

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_page(self):
        with patch("requests.get") as x:
            with patch("requests.post") as y:
                x.return_value.text = "Dwarf"
                y.return_value.text = "Barbarian"
                response = self.client.get(url_for("index"))
                self.assertIn(b"You will play a Dwarf Barbarian, who fights using an axe.", response.data)

#####   Test version 2   #####

#class TestBase(TestCase):
#    def create_app(self):
#        app,config.update(SQLALCHEMY_DATABASE_URI=getenv("DnD_db"),
#                DEBUG=True, WTF_CSRF_ENABLED=False)
#        return app

#    def setUp(self):
#        db.create_all()
#        test_character=character(character_race="a Dwarf", character_class="Barbarian", weopan="axe")
#        db.session.add(test_character)
#        db.session.commit()

#    def tearDown(self):
#        db.session.remove()
#        db.drop_all()

#class TestCreate(Testbase):
#    def test_character1(self):
#        with requests_mock() as x:
#            x.get("http://service2:5000/character_race", text="a Dwarf")
#            x.get("http://service3:5000/character_class",test="Barbarian")
#            x.get("http://service4:5000/weopan", test="axe")
#            response=self.client.get(url_for("index"))
#            self.assertEqual(response.status_code,200)
#            self.assertIn(b'You will play a Dwarf Barbarian, who fights using an axe.', response.data)
