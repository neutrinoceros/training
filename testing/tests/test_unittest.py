# imports to build tests
import os
from tempfile import mkstemp
from unittest import TestCase

from src.algebra import add
from src.greetings import greet

# import API to be tested


class TestAddition(TestCase):
    def test_simple_additon(self):
        self.assertEqual(add(1, 1), 2)

    def test_broken(self):
        self.assertEqual(add(1, 1), 3)


class TestGreetings(TestCase):
    def setUp(self):
        self.tempfile, self.path = mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_greet_to_file(self):
        greet("Heisenberg", self.tempfile)
        with open(self.path) as fi:
            content = fi.read()
        self.assertEqual(content, "Hello Heisenberg !")
