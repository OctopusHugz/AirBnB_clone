#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
import models


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel class"""
    def setUp(self):
        """set up some testing objects"""
        self.test_model1 = BaseModel()
        self.test_model2 = BaseModel()

    def test_no_args(self):
        """test comapares with no arguments"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """test to make sure id is str"""
        self.assertEqual(str, type(BaseModel().id))

    def test_basic_setup(self):
        """test for to_dict method of BaseModel class """
        self.assertTrue(hasattr(self.test_model1, "id"))
        self.assertTrue(hasattr(self.test_model1, "__class__"))
        self.assertTrue(hasattr(self.test_model1, "created_at"))
        self.assertTrue(hasattr(self.test_model1, "updated_at"))
        self.assertTrue(self.test_model1.id != self.test_model2.id)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        self.assertTrue(m1c != m2c)

    def test_types(self):
        """test to make sure types are correct"""
        self.assertTrue(type(self.test_model1.id) is str)
        self.assertTrue(type(self.test_model1.__class__) is type)
        m1c = self.test_model1.created_at
        m2c = self.test_model2.created_at
        m1u = self.test_model1.updated_at
        m2u = self.test_model2.updated_at
        self.assertTrue(type(m1c) is datetime.datetime)
        self.assertTrue(type(m2c) is datetime.datetime)
        self.assertTrue(type(m1u) is datetime.datetime)
        self.assertTrue(type(m2u) is datetime.datetime)

    def test_save(self):
        """testing whether save updates time"""
        m1u = self.test_model1.updated_at
        self.test_model1.save()
        m1u_saved = self.test_model1.updated_at
        self.assertFalse(m1u == m1u_saved)

    def test_to_dict(self):
        """test to_dict more advanced"""
        m1_dict = self.test_model1.to_dict()
        m2_dict = self.test_model2.to_dict()
        self.assertTrue(hasattr(m1_dict, "__class__"))
        self.assertTrue(m1_dict != self.test_model1.__dict__)
        self.assertEqual(m1_dict["id"], self.test_model1.__dict__["id"])
        self.assertNotEqual(m1_dict["created_at"],
                            self.test_model1.__dict__["created_at"])
        self.assertNotEqual(type(m1_dict["created_at"]),
                            type(self.test_model1.__dict__["created_at"]))
        self.assertNotEqual(m1_dict, m2_dict)

if __name__ == '__main__':
    unittest.main()
