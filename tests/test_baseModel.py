#!/usr/bin/python3
from models.baseModel import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """test the base model class"""

    def test_base_model_id_format(self):
        """test if UUID is a string"""
        id_nbr = BaseModel()
        self.assertIsInstance(id_nbr.id, str)

    def test_str(self):
        """test if the str method has the correct output"""
        instance = BaseModel()
        string = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(string, str(instance))

    def test_to_dict(self):
        """test to_dict method"""
        isDict = BaseModel().to_dict()
        self.assertIsInstance(isDict, dict)

if __name__ == '__main__':
    unittest.main()