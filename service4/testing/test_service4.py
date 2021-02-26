#!/urs/bin/python3
#                   Test_service4.py

#####   Imports #####
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

# class TestCharacters(TestBase):
#     def test_character(self):
#         races = [b"a Dwarf", b"an Elf", b"a Halfling", b"a Human", b"a Dragonborn", b"a Gnome", b"a Half-Elf", b"a Half-Orc", b"a Tiefling"]
#         #classes = [b"Barbarian", b"Bard", b"Cleric", b"Druid", b"Fighter", b"Monk", b"Paladin", b"Ranger", b"Rogue", b"Sorcerer", b"Warlock", b"Wizard"]
#         response = self.client.get(url_for("weapon"))
#         self.assertIn(response.data, races)#, classes), b"You will play a Dwarf Barbarian, who fights using a battle axe")

#     def test_dwarf_barbarian(self):
#         response = self.client.post(
#             url_for("weapon"),
#             data = "a Dwarf",
#             follow_redirects=True
#         )
#         self.assertIn(b"a battle axe", response.data)