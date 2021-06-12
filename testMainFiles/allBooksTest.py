#!/usr/bin/python3

from models.books import Book
from engine import storage

books = storage.all(Book)

print(books)
