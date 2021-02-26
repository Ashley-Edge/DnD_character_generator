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
    def test_elf_fighter(self):
        with patch("requests.get") as g:
            g.return_value.text = "an Elf"
            with patch("random.randrange") as p:
                p.return_value.text = "Fighter"
                response = self.client.post(url_for("weapon"), data = "an Elf Fighter")
                self.assertIn(b"whips", response.data)