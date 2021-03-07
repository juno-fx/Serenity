import unittest

import dotenv
import flask

import serenity

dotenv.load_dotenv()


class TestSerenity(unittest.TestCase):
    def test_create_app(self):
        self.assertIsInstance(serenity.create_app(), flask.Flask)
