#!/usr/bin/python3
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_empty_prompt(unittest.TestCase):
    """test empty line from console"""

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty(self):
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertEqual("", out.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
