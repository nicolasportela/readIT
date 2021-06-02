#!/usr/bin/python3
""" Contains the Test Shared class """
from datetime import datetime
from models.shared import Shared
from models.baseModel import BaseModel
import unittest


class TestBook(unittest.TestCase):
    """Test the Shared class"""
    def test_is_subclass(self):
        """Test that Shared is a subclass of BaseModel"""
        shared = Shared()
        self.assertIsInstance(shared, BaseModel)

    def test_init_(self):
        shared = Shared()
        self.assertTrue(hasattr(shared, "IdShared"))
        self.assertTrue(hasattr(shared, "IdGiver"))
        self.assertTrue(hasattr(shared, "IdReceiver"))
        self.assertTrue(hasattr(shared, "IdBook"))
        self.assertTrue(hasattr(shared, "Datashared"))
        self.assertTrue(hasattr(shared, "StatusRequest"))

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S"
        sharedAndTaken = {'IdGiver': '02f87f75-1a2e-479c-8f97-24ded7d15045', 'IdReceiver': '3924aaa9-d7f0-4d18-94dd-d43dee975e60', 'IdBook': '6027b4f2-3dc0-4579-b70e-c8d04d825812', 'StatusRequest': 'pending'}
        s = Shared(**sharedAndTaken)
        new_d = s.to_dict()
        self.assertEqual(new_d["Class"], "Shared")
        self.assertEqual(type(new_d["IdGiver"]), str)
        self.assertEqual(type(new_d["IdReceiver"]), str)
        self.assertEqual(type(new_d["IdBook"]), str)
        self.assertEqual(type(new_d["Datashared"]), str)
        self.assertEqual(type(new_d["StatusRequest"]), str)

    def test_str(self):
        """test that the str method has the correct output"""
        shared = Shared()
        string = "[Shared] ({}) {}".format(shared.IdShared, shared.__dict__)
        self.assertEqual(string, str(shared))
