#!/usr/bin/python3
""" holds class Book"""
from datetime import datetime
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship
from models.shared import Shared
import requests


class Book(BaseModel, Base):
    """Representation of a Book"""
    __tablename__ = 'Books'
    IdBook = Column(String(40), nullable=False, primary_key=True)
    IdUser = Column(String(40), ForeignKey('Users.IdUser'), nullable=False)
    Authors = Column(String(256), nullable=False)
    Title = Column(String(256), nullable=False)
    Description = Column(String(2048), nullable=False)
    ISBN = Column(String(30), nullable=False)
    Status = Column(String(30), nullable=False)
    Uploaded = Column(DateTime, default=datetime.utcnow, nullable=False)
    Cover = Column(String(100))

    def __init__(self, **kwargs):
        """initializes book"""
        self.IdBook = str(uuid4())
        self.IdUser = kwargs.get('IdUser')
        self.Authors = kwargs.get('Authors')
        self.Title = kwargs.get('Title')
        self.Description = kwargs.get('Description')
        self.ISBN = kwargs.get('ISBN')
        self.Status = kwargs.get('Status')
        now = datetime.now()
        self.Uploaded = now.strftime('%Y-%m-%d %H:%M:%S')
        self.Cover = kwargs.get('Cover')

    def apiOpenL(ISBN):
        """ Get info from OpenLibrary API """
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://openlibrary.org/isbn/{}.json'
        r = requests.get(url.format(ISBN),
                         allow_redirects=True,
                         headers=header)
        if r.status_code == 200:
            Title = Book.titleOpenL(ISBN)
            Authors = Book.authorsOpenL(ISBN)
            Description = Book.descriptionOpenL(ISBN)
            Cover = Book.coverOpenL(ISBN)

            newDict = {'Title': Title,
                       'Authors': Authors,
                       'Description': Description,
                       'Status': 'Available',
                       'Cover': Cover,
                       "ISBN": ISBN}
            return newDict
        else:
            return None

    def apiGoogle(ISBN):
        """ Get info from Google Books API """
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'
        r = requests.get(url.format(ISBN),
                         allow_redirects=False,
                         headers=header).json()
        if r.get('totalItems') > 0:
            items = r.get('items')
            id = items[0].get('id')
            url2 = 'https://www.googleapis.com/books/v1/volumes/{}'
            r2 = requests.get(url2.format(id),
                              allow_redirects=False,
                              headers=header).json()

            if r2.get('volumeInfo').get('title'):
                Title = r2.get('volumeInfo').get('title')
            else:
                Title = titleOpenL(ISBN)

            if r2.get('volumeInfo').get('authors'):
                authorsList = r2.get('volumeInfo').get('authors')
                Authors = ""
                for name in authorsList:
                    if len(authorsList) == 1:
                        Authors = name
                    elif len(authorsList) > 1 and name == authorsList[-2]:
                        Authors += '{} '.format(name)
                    elif len(authorsList) > 1 and name == authorsList[-1]:
                        Authors += '& {}'.format(name)
                    else:
                        Authors += '{}, '.format(name)
            else:
                Authors = Book.authorsOpenL(ISBN)

            if r2.get('volumeInfo').get('description'):
                Description = r2.get('volumeInfo').get('description')
            else:
                Description = Book.descriptionOpenL(ISBN)

            if r2.get('volumeInfo').get('imageLinks'):
                Cover = r2.get('volumeInfo').get('imageLinks').get('thumbnail')
            else:
                Cover = Book.coverOpenL(ISBN)

            newDict = {'Title': Title,
                       'Authors': Authors,
                       'Description': Description,
                       'Status': 'Available',
                       'Cover': Cover,
                       "ISBN": ISBN}
            return newDict

        else:
            return Book.apiOpenL(ISBN)


    def titleOpenL(ISBN):
        """ Get title info from OpenLibrary API """
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://openlibrary.org/isbn/{}.json'
        r = requests.get(url.format(ISBN),
                         allow_redirects=True,
                         headers=header)
        if r.status_code == 200:
            if r.json().get('title'):
                Title = r.json().get('title')
            else:
                Title = "No title available"
        else:
            Title = "No title available"
        return Title

    def authorsOpenL(ISBN):
        """ Get authors info from OpenLibrary API """
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://openlibrary.org/isbn/{}.json'
        r = requests.get(url.format(ISBN),
                         allow_redirects=True,
                         headers=header)
        if r.status_code == 200:
            if r.json().get('authors'):
                authorsKey = r.json().get('authors')
                allAuthorsID = []
                for authorEndpoint in authorsKey:
                    allAuthorsID.append(authorEndpoint.get('key'))
                    url2 = 'https://openlibrary.org{}.json'
                    Authors = ""
                for authorID in allAuthorsID:
                    r2 = requests.get(url2.format(authorID),
                                      headers=header).json()
                    if len(allAuthorsID) == 1:
                        Authors += r2.get('name')
                    elif len(allAuthorsID) > 1 and authorID == allAuthorsID[-2]:
                        Authors += '{} '.format(r2.get('name'))
                    elif len(allAuthorsID) > 1 and authorID == allAuthorsID[-1]:
                        Authors += '& {}'.format(r2.get('name'))
                    else:
                        Authors += '{}, '.format(r2.get('name'))
            else:
                Authors = "No authors available"
        else:
            Authors = "No authors available"
            return Authors

    def descriptionOpenL(ISBN):
        """ Get description info from OpenLibrary API """
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://openlibrary.org/isbn/{}.json'
        r = requests.get(url.format(ISBN),
                         allow_redirects=True,
                         headers=header)
        if r.status_code == 200:
            if r.json().get('description'):
                try:
                    Description = r.json().get('description')
                except:
                    Description = r.json().get('description').get('value')
            else:
                Description = "No description available"
        else:
            Description = "No description available"
        return Description

    def coverOpenL(ISBN):
        """ Get title info from OpenLibrary API """
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        url = 'https://openlibrary.org/isbn/{}.json'
        r = requests.get(url.format(ISBN),
                         allow_redirects=True,
                         headers=header)
        if r.status_code == 200:
            if r.json().get('covers'):
                idCover = r.json().get('covers')[0]
                Cover = 'https://covers.openlibrary.org/b/id/{}.jpg'.format(idCover)
            else:
                Cover = 'https://i.imgur.com/OReLDZt.jpg'
        else:
            Cover = 'https://i.imgur.com/OReLDZt.jpg'
        return Cover
