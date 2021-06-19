#!/usr/bin/python3
""" Contains the Test User class """
from models.users import User
from models.baseModel import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_init_(self):
        user = User()
        self.assertTrue(hasattr(user, "IdUser"))
        self.assertTrue(hasattr(user, "FirstName"))
        self.assertTrue(hasattr(user, "LastName"))
        self.assertTrue(hasattr(user, "Phone"))
        self.assertTrue(hasattr(user, "Mail"))
        self.assertTrue(hasattr(user, "Password"))
        self.assertTrue(hasattr(user, "City"))

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        eva = {'FirstName': 'Eva',
               'LastName': 'DaughterOfGod',
               'Mail': 'evacontacto@readIT',
               'Password': 'Hola',
               'Phone': '59899101010',
               'City': 'Paradise'}
        u = User(**eva)
        new_d = u.to_dict()
        self.assertEqual(new_d["Class"], "User")
        self.assertEqual(type(new_d["IdUser"]), str)
        self.assertEqual(type(new_d["FirstName"]), str)
        self.assertEqual(type(new_d["LastName"]), str)
        self.assertEqual(type(new_d["Phone"]), str)
        self.assertEqual(type(new_d["Mail"]), str)
        self.assertEqual(type(new_d["Password"]), str)
        self.assertEqual(type(new_d["City"]), str)

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.IdUser, user.__dict__)
        self.assertEqual(string, str(user))
