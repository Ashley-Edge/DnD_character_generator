#!/usr/bin/python3
#		Test_service3.py file

#####	Imports	#####
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        return app

#####   Test version 2  #####

class TestCreate(Testbase):
    def test_char(self):
        for _ in range(11):
            response=self.client.get(url_for("character_class"))
            self.assertEqual(response.status_code,200)
            self.assertIn(response.data, [b"Barbarian",b"Bard", b"Cleric", b"Druid", b"Fighter", b"Monk", b"Paladin", b"Ranger", b"Rogue", b"Sorcerer", b"Warlock", b"Wizard"])

#####   Test version 1  #####
#class TestResponse(TestBase):

#    def test_barbarian_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 0
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Barbarian', response.data)

#    def test_bard_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 1
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Bard', response.data)

#    def test_cleric_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 2
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Cleric', response.data)

#    def test_druid_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 3
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Druid', response.data)

#    def test_fighter_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 4
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Fighter', response.data)

#    def test_monk_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 5
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Monk', response.data)

#    def test_paladin_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 6
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Paladin', response.data)

#    def test_ranger_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 7
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Ranger', response.data)

#    def test_rogue_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 8
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Rogue', response.data)

#    def test_sorcerer_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 9
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Sorcerer', response.data)

#    def test_warlock_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 10
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Warlock', response.data)

#    def test_wizard_class(self):
#        with patch('random.randrange') as r:
#            r.return_value = 11
#            response = self.client.get(url_for('team'))
#            self.assertIn(b'Wizard', response.data)
