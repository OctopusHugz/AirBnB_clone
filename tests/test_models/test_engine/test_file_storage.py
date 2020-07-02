#!/usr/bin/python3
"""This module tests the FileStorage instance"""
import os
import json
from datetime import datetime
from models.base_model import BaseModel
import models
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Test FileStorage instantiation"""

    def test_FileStorage_no_args(self):
        """ test storage with no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_arg(self):
        """test file storage with one argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_str(self):
        """test storage str"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_dict(self):
        """test storage dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_type(self):
        """ test filestorage type"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """test for FileStorage methods"""

    def test_all(self):
        """test all from storage"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with(self):
        """test with one argument"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_no_file(self):
        """test reload with no file"""
        self.assertRaises(FileNotFoundError, models.storage.reload())

    def test_reload_arg(self):
        """test reload with argument"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save(self):
        """test file save"""
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + b.id, save_text)
            self.assertIn("User." + u.id, save_text)
            self.assertIn("State." + s.id, save_text)
            self.assertIn("Place." + p.id, save_text)
            self.assertIn("City." + c.id, save_text)
            self.assertIn("Amenity." + a.id, save_text)
            self.assertIn("Review." + r.id, save_text)

    def test_reload(self):
        """test reload"""
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage().all()
        self.assertIn("BaseModel." + b.id, objs)
        self.assertIn("User." + u.id, objs)
        self.assertIn("State." + s.id, objs)
        self.assertIn("Place." + p.id, objs)
        self.assertIn("City." + c.id, objs)
        self.assertIn("Amenity." + a.id, objs)
        self.assertIn("Review." + r.id, objs)

    def test_new(self):
        """test new"""
        b = BaseModel()
        u = User()
        s = State()
        p = Place()
        c = City()
        a = Amenity()
        r = Review()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.new(s)
        models.storage.new(p)
        models.storage.new(c)
        models.storage.new(a)
        models.storage.new(r)
        models.storage.save()
        objs = FileStorage().all()
        self.assertIn("BaseModel." + b.id, objs)
        self.assertIn("User." + u.id, objs)
        self.assertIn("State." + s.id, objs)
        self.assertIn("Place." + p.id, objs)
        self.assertIn("City." + c.id, objs)
        self.assertIn("Amenity." + a.id, objs)
        self.assertIn("Review." + r.id, objs)

    def test__file_path(self):
        """test file path"""
        dic = FileStorage._FileStorage__file_path
        self.assertEqual("file.json", dic)

    # def test__objects(self):
    #    """test objects"""
    #    pass


if __name__ == '__main__':
    unittest.main()
