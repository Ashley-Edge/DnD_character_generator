#!/usr/bin/python3
#		            Test_service3.py file

#####	Imports	#####
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app
        
class TestCreate(TestBase):
    def test_character_class(self):
        response=self.client.get(url_for('character_class'))
        self.assertEqual(response.status_code,200)
        self.assertIn(response.data, [b"Barbarian", b"Cleric", b"Fighter", b"Paladin", b"Wizard"])
            