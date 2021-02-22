#!/usr/bin/python3
#                   Test_service2.py file

#####   Imports #####
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

#####   Short test  #####
#class TestCreate(Testbase):
#    def test_character_race(self):
#        for i in range(9):
#            response=self.client.get(url_for('character_race'))
#            self.assertEqual(response.status_code,200)
#            self.assertIn(response.data, [b'a Dwarf', b'an Elf', b'a Halfling', b'a Human', b'a Dragonborn', b'a Gnome', b'a Half-Elf', b'a Half-Orc', b'a Tiefling'])

#####   Long test   #####
class TestResponse(TestBase):

    def test_dwarf_race(self):
        with patch('random.randrange') as x:
            x.return_value = 0
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Dwarf', response.data)

    def test_elf_race(self):
        with patch('random.randrange') as x:
            x.return_value = 1
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'an Elf', response.data)

    def test_halfling_race(self):
        with patch('random.randrange') as x:
            x.return_value = 2
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Halfling', response.data)

    def test_human_race(self):
        with patch('random.randrange') as x:
            x.return_value = 3
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Human', response.data)

    def test_dragonborn_race(self):
        with patch('random.randrange') as x:
            x.return_value = 4
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Dragonborn', response.data)

    def test_gnome_race(self):
        with patch('random.randrange') as x:
            x.return_value = 5
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Gnome', response.data)

    def test_halfelf_race(self):
        with patch('random.randrange') as x:
            x.return_value = 6
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Half-Elf', response.data)

    def test_halforc_race(self):
        with patch('random.randrange') as x:
            x.return_value = 7
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Half-Orc', response.data)

    def test_tiefling_race(self):
        with patch('random.randrange') as x:
            x.return_value = 8
            response = self.client.get(url_for('character_race'))
            self.assertIn(b'a Tiefling', response.data)
