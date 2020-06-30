#!/usr/bin/python3
import os
import json
from datetime import datetime
from models.base_model import BaseModel
import models
import unittest
from models.engine.file_storage import FileStorage
from models.user import User


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

    def test_save(self):
        """test file save"""
        b = BaseModel()
        u = User()
        models.storage.new(b)
        models.storage.new(u)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + b.id, save_text)
            self.assertIn("User." + u.id, save_text)

if __name__ == "__main__":
    unittest.main()
