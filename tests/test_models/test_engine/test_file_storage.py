#!/usr/bin/python3
"""
Unittest for File Storage class
"""
import unittest
import json
import os
import pep8
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "A1"
        cls.rev1.user_id = "CA"
        cls.rev1.text = "HL"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        who = User()
        who.id = 350
        who.name = "donno"
        m_storage.new(who)
        key = who.__class__.__name__ + "." + str(who.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
