#!/usr/bin/python3
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Unit Tests for Review Class """
    def setUp(self):
        """setup for testing"""
        self.mod1 = Review()
        self.mod2 = Review()

    def test_setup(self):
        """test insatiation """
        self.assertTrue(hasattr(self.mod1, "place_id"))
        self.assertTrue(hasattr(self.mod1, "user_id"))
        self.assertTrue(hasattr(self.mod1, "text"))
        self.assertTrue(self.mod1.id != self.mod2.id)
        one = self.mod1.created_at
        two = self.mod2.created_at
        self.assertTrue(one != two)

    def test_types(self):
        """test state types"""
        self.assertTrue(type(self.mod1.place_id) is str)
        self.assertTrue(type(self.mod1.user_id) is str)
        self.assertTrue(type(self.mod1.text) is str)

    def test_save(self):
        """test save"""
        new = self.mod1.updated_at
        self.mod1.save()
        new_saved = self.mod1.updated_at
        self.assertFalse(new == new_saved)

if __name__ == '__main__':
    unittest.main()
