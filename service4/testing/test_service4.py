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

class TestResponse(TestBase):

    def test_dwarf_barbarian(self):
        with patch('requests.get') as g:
            g.return_value.text = "a Dwarf"
            with patch('random.randrange') as h:
                    h.return_value = "Barbarian"
                    response = self.client.post(url_for('weapon'), data = "a Dwarf Barbarian")
                    self.assertIn(b"a battle axe", response.data)