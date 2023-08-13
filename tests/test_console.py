#!/usr/bin/python3
"""
Unittest for the console command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_console(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_console(self):
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_docstrings_in_console(self):
        self.assertTrue(len(console.__doc__) >= 1)

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create User")
            self.typing.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.all()")
            self.assertEqual("[[User]",
                             fake_output.getvalue()[:7])

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", fake_output.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_class_cmd(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.count()")
            self.assertEqual(int, type(eval(fake_output.getvalue())))


if __name__ == "__main__":
    unittest.main()
