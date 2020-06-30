#!/usr/bin/python3
"""Test console module """
import sys
import unittest
from test import support
from unittest.mock import create_autospec
from console import HBNBCommand
from io import StringIO
from test.support import captured_stdout, captured_stderr


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

    def test_create_error(self):
        """test do_create method"""
        c = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            expected = "** class name missing **\n"
            self.assertFalse(c.onecmd("create"))
            self.assertEqual(expected, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            expected = "** class doesn't exist **\n"
            self.assertFalse(c.onecmd("create Random"))
            self.assertEqual(expected, stdout.getvalue())

    def test_all_error(self):
        """test do_all method"""
        c = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("all Random"))
            self.assertEqual(TestConsole.no_cl, stdout.getvalue())

    def test_update_error(self):
        """test do_update method"""
        c = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("update"))
            self.assertEqual(TestConsole.missing_cl, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("update Random"))
            self.assertEqual(TestConsole.no_cl, stdout.getvalue())

    def test_empty(self):
        """test empty line method"""
        c = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd('\n'))
            self.assertEqual("", stdout.getvalue())

    def test_show_error(self):
        """test do_show method"""
        c = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("show"))
            self.assertEqual(TestConsole.missing_cl, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("show Random"))
            self.assertEqual(TestConsole.no_cl, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("show BaseModel Z"))
            self.assertEqual(TestConsole.no_ins, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("show BaseModel"))
            self.assertEqual(TestConsole.missing_id, stdout.getvalue())

    def test_destroy_error(self):
        """test do_destroy method"""
        c = self.create()
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("destroy"))
            self.assertEqual(TestConsole.missing_cl, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("destroy Random"))
            self.assertEqual(TestConsole.no_cl, stdout.getvalue())
        with captured_stdout() as stdout, captured_stderr() as stderr:
            self.assertFalse(c.onecmd("destroy BaseModel"))
            self.assertEqual(TestConsole.missing_id, stdout.getvalue())
