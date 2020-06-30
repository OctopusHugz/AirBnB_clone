#!/usr/bin/python3
import sys
import unittest
from test import support
from unittest.mock import create_autospec
from console import HBNBCommand
from io import StringIO
from test.support import captured_stdout, captured_stderr
import pep8


class TestConsole(unittest.TestCase):
    """Test console class"""
    missing_cl = "** class name missing **\n"
    missing_id = "** instance id missing **\n"
    no_ins = "** no instance found **\n"
    no_cl = "** class doesn't exist **\n"

    def setUp(self):
        """setup for test"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.mock_stderr = create_autospec(sys.stderr)

    def create(self, server=None):
        """helper function for test class"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """test exit command"""
        c = self.create()
        self.assertTrue(c.onecmd("quit"))

    def test_EOF(self):
        """test EOF command"""
        c = self.create()
        self.assertTrue(c.onecmd("EOF"))

    def test_pep8_conformance(self):
        """load_from_file Docstring Test"""
        print("test_test_pep8_conformance")
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
