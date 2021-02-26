#!/urs/bin/python3
#                   Test_service4.py

#####   Imports #####
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

#class TestResponse(TestBase):
#    def test_elf_fighter(self):
#        with patch("requests.get") as g:
#            g.return_value.text = "an Elf"
#            with patch("random.randrange") as p:
#                p.return_value.text = "Fighter"
#                response = self.client.post(url_for("weapon"), data = "an Elf Fighter")
#                self.assertIn(response.data, b"whips")

class TestResponse(TestBase):
    def test_character_race(self):
        character_races = [b"a Dwarf", b"an Elf", b"a Halfling", b"a Human", b"a Dragonborn", b"a Gnome", b"a Half-Elf", b"a Half-Orc", b"a Tiefling"]
        response = self.client.get(url_for("race"))
        self.assertIn(response.data, character_races)

    def test_character_class(self):
        character_classes = [b"Barbarian", b"Bard", b"Cleric", b"Druid", b"Fighter", b"Monk", b"Paladin",b"Ranger", b"Rogue", b"Sorcerer", b"Warlock", b"Wizard"]
        response = self.client.get(url_for("class"))
        self.assertIn(response.data, character_classes)

    def character_weapon(self):
        response = self.client.post(url_for("weapon"), data = "an Elf Fighter", follow_redirects=True)
        self.assertIn(b"whips")
