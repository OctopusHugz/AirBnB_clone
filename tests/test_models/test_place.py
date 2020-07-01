#!/usr/bin/python3
import unittest
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """ Unit Tests for User Place """
    def setUp(self):
        """setup for testing"""
        self.mod1 = Place()
        self.mod2 = Place()

    def test_setup(self):
        """test insatiation """
        self.assertTrue(hasattr(self.mod1, "city_id"))
        self.assertTrue(hasattr(self.mod1, "user_id"))
        self.assertTrue(hasattr(self.mod1, "description"))
        self.assertTrue(hasattr(self.mod1, "number_rooms"))
        self.assertTrue(hasattr(self.mod1, "number_bathrooms"))
        self.assertTrue(hasattr(self.mod1, "max_guest"))
        self.assertTrue(hasattr(self.mod1, "price_by_night"))
        self.assertTrue(hasattr(self.mod1, "latitude"))
        self.assertTrue(hasattr(self.mod1, "longitude"))
        self.assertTrue(hasattr(self.mod1, "amenity_ids"))
        self.assertTrue(self.mod1.id != self.mod2.id)
        one = self.mod1.created_at
        two = self.mod2.created_at
        self.assertTrue(one != two)

    def test_types(self):
        """test place types"""
        self.assertTrue(type(self.mod1.city_id) is str)
        self.assertTrue(type(self.mod1.user_id) is str)
        self.assertTrue(type(self.mod1.name) is str)
        self.assertTrue(type(self.mod1.description) is str)
        self.assertTrue(type(self.mod1.number_rooms) is int)
        self.assertTrue(type(self.mod1.number_bathrooms) is int)
        self.assertTrue(type(self.mod1.max_guest) is int)
        self.assertTrue(type(self.mod1.price_by_night) is int)
        self.assertTrue(type(self.mod1.latitude) is float)
        self.assertTrue(type(self.mod1.longitude) is float)
        self.assertTrue(type(self.mod1.amenity_ids) is list)

    def test_save(self):
        """test save"""
        new = self.mod1.updated_at
        self.mod1.save()
        new_saved = self.mod1.updated_at
        self.assertFalse(new == new_saved)

if __name__ == '__main__':
    unittest.main()
