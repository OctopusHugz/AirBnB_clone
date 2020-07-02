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
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(string, out.getvalue().strip())

    def test_BaseModel_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertEqual(str, type(out.getvalue()))

    def test_Review_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertEqual(str, type(out.getvalue()))

    def test_User_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertEqual(str, type(out.getvalue()))

    def test_State_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertEqual(str, type(out.getvalue()))

    def test_City_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertEqual(str, type(out.getvalue()))

    def test_Amenity_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertEqual(str, type(out.getvalue()))

    def test_Place_all(self):
        """test BaseModel all"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertEqual(str, type(out.getvalue()))

if __name__ == "__main__":
    unittest.main()
