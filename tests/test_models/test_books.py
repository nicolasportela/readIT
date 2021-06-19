#!/usr/bin/python3
""" Contains the Test Book class """
from datetime import datetime
from models.books import Book
from models.baseModel import BaseModel
import unittest


class TestBook(unittest.TestCase):
    """Test the Book class"""
    def test_is_subclass(self):
        """Test that Book is a subclass of BaseModel"""
        book = Book()
        self.assertIsInstance(book, BaseModel)

    def test_init_(self):
        book = Book()
        self.assertTrue(hasattr(book, "IdBook"))
        self.assertTrue(hasattr(book, "Authors"))
        self.assertTrue(hasattr(book, "Title"))
        self.assertTrue(hasattr(book, "Description"))
        self.assertTrue(hasattr(book, "ISBN"))
        self.assertTrue(hasattr(book, "Status"))
        self.assertTrue(hasattr(book, "Uploaded"))

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S"
        book1984 = {'Authors': 'George Orwell',
                    'Title': '1984',
                    'Description': 'Love this novel!',
                    'ISBN': '0102030405061',
                    'Status': 'Requested'}
        b = Book(**book1984)
        new_d = b.to_dict()
        self.assertEqual(new_d["Class"], "Book")
        self.assertEqual(type(new_d["IdBook"]), str)
        self.assertEqual(type(new_d["Authors"]), str)
        self.assertEqual(type(new_d["Title"]), str)
        self.assertEqual(type(new_d["Description"]), str)
        self.assertEqual(type(new_d["ISBN"]), str)
        self.assertEqual(type(new_d["Status"]), str)
        self.assertEqual(type(new_d["Uploaded"]), str)

    def test_str(self):
        """test that the str method has the correct output"""
        book = Book()
        string = "[Book] ({}) {}".format(book.IdBook, book.__dict__)
        self.assertEqual(string, str(book))
