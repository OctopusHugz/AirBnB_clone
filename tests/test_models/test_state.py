#!/usr/bin/python3
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Unit Tests for State Class """
    def setUp(self):
        """setup for testing"""
        self.mod1 = State()
        self.mod2 = State()

    def test_setup(self):
        """test insatiation """
        self.assertTrue(hasattr(self.mod1, "name"))
        self.assertTrue(self.mod1.id != self.mod2.id)
        one = self.mod1.created_at
        two = self.mod2.created_at
        self.assertTrue(one != two)

    def test_types(self):
        """test state types"""
        self.assertTrue(type(self.mod1.name) is str)

    def test_save(self):
        """test save"""
        new = self.mod1.updated_at
        self.mod1.save()
        new_saved = self.mod1.updated_at
        self.assertFalse(new == new_saved)

if __name__ == '__main__':
    unittest.main()
