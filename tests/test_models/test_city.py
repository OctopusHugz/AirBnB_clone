#!/usr/bin/python3
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ Unit Tests for City Class """
    def setUp(self):
        """setup for testing"""
        self.mod1 = City()
        self.mod2 = City()

    def test_setup(self):
        """test insatiation """
        self.assertTrue(hasattr(self.mod1, "state_id"))
        self.assertTrue(hasattr(self.mod1, "name"))
        self.assertTrue(self.mod1.id != self.mod2.id)
        one = self.mod1.created_at
        two = self.mod2.created_at
        self.assertTrue(one != two)

    def test_types(self):
        """test city types"""
        self.assertTrue(type(self.mod1.state_id) is str)
        self.assertTrue(type(self.mod1.name) is str)

    def test_save(self):
        """test save"""
        new = self.mod1.updated_at
        self.mod1.save()
        new_saved = self.mod1.updated_at
        self.assertFalse(new == new_saved)

if __name__ == '__main__':
    unittest.main()
