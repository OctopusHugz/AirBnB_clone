#!/usr/bin/python3
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """test empty line from console"""

    @classmethod
    def setUp(self):
        """setup for json file"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        """teardown json file"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_prompt(self):
        """ test prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """ test empty line"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertEqual("", out.getvalue().strip())

    def test_quit(self):
        """ test quit function"""
        with patch("sys.stdout", new=StringIO) as out:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_all(self):
        """ test all function"""
        string = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("all Model"))
            self.assertEqual(string, out.getvalue().strip())

    def test_help_quit(self):
        """ test quit from help function"""
        string = "Quit command to exit the console"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(string, out.getvalue().strip())

    def test_help_EOF(self):
        """ test EOF from help"""
        string = "EOF command to exit the console"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(string, out.getvalue().strip())

    def test_show(self):
        """ test show from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(string, out.getvalue().strip())

    def test_update(self):
        """ test update from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(string, out.getvalue().strip())

    def test_destroy(self):
        """ test destroy from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(string, out.getvalue().strip())

    def test_create(self):
        """test create from console"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
