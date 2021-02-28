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

class TestCreate(TestBase):
    def test_character_race(self):
        response=self.client.get(url_for('character_race'))
        self.assertEqual(response.status_code,200)
        self.assertIn(response.data, [b'a Dwarf', b'an Elf', b'a Halfling', b'a Human'])
