#!/usr/bin/python3
#                   Test_service1 file

#####   Imports #####
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_character(self):
        with patch("requests.get") as g:
            with patch("requests.post") as r:
                g.return_value.text = "an Elf"
                r.return_value.text = "whips"

                response = self.client.get(url_for("index"))
                self.assertIn(b"You will play an Elf an Elf, who fights using whips", response.data)

# I wanted to test with adding the class Fighter, but it kept throwing up AssertIn Errors