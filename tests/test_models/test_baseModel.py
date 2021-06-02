#!/usr/bin/python3
from models.baseModel import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """test the base model class"""

    def test_to_dict(self):
        """test to_dict method"""
        isDict = BaseModel().to_dict()
        self.assertIsInstance(isDict, dict)

if __name__ == '__main__':
    unittest.main()
