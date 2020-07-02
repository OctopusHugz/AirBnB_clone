#!/usr/bin/python3
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """ Unit Tests for User Class """

    def setUp(self):
        """setup for testing"""
        self.mod1 = User()
        self.mod2 = User()

    def test_setup(self):
        """test insatiation """
        self.assertTrue(hasattr(self.mod1, "email"))
        self.assertTrue(hasattr(self.mod1, "password"))
        self.assertTrue(hasattr(self.mod1, "last_name"))
        self.assertTrue(hasattr(self.mod1, "first_name"))
        self.assertTrue(self.mod1.id != self.mod2.id)
        one = self.mod1.created_at
        two = self.mod2.created_at
        self.assertTrue(one is not two)

    def test_types(self):
        """test user types"""
        self.assertTrue(type(self.mod1.email) is str)
        self.assertTrue(type(self.mod1.password) is str)
        self.assertTrue(type(self.mod1.last_name) is str)
        self.assertTrue(type(self.mod1.first_name) is str)

    def test_save(self):
        """test save"""
        new = self.mod1.updated_at
        self.mod1.save()
        new_saved = self.mod1.updated_at
        self.assertFalse(new == new_saved)


if __name__ == '__main__':
    unittest.main()
