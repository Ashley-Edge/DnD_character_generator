from unittest.mock import patch
from flask import url_for
from application import app
from flask_testing import TestCase

from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_weapon(self):
        response = self.client.post(url_for('weapon'), json={"character_race":"a Dwarf", "character_class":"Barbarian"})
        self.assertEqual(b"a battle axe", response.data)