#!/usr/bin/python3
#                   Test_service1 file

#####   Imports #####
import unittest
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_character(self):
        with patch ('request.get') as g:
            g.return_value.text = "a Dwarf"