#!/usr/bin/python3
""" holds class User"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String
from uuid import uuid4
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(UserMixin, BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'Users'
    IdUser = Column(String(40), nullable=False, primary_key=True)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Phone = Column(String(30), nullable=False)
    Email = Column(String(50), nullable=True)
    Password = Column(String(512), nullable=False)
    City = Column(String(50), nullable=False)

    def __init__(self, **kwargs):
        """initializes user"""
        self.IdUser = str(uuid4())
        self.FirstName = kwargs.get('FirstName')
        self.LastName = kwargs.get('LastName')
        self.Phone = kwargs.get('Phone')
        self.Email = kwargs.get('Email')
        self.Password = kwargs.get('Password')
        self.City = kwargs.get('City')

    def get_id(self):
        return (self.IdUser)

    @property
    def requested(self):
        """ Load all book requested """
        from engine import storage
        allRequested = []
        requested = storage.findRequestBook(self)
        for elements in requested:
            IdReceiver = elements.get('IdReceiver')
            receiver = storage.findIdUser(IdReceiver)
            IdBook = elements.get('IdBook')
            book = storage.findIdBook(IdBook)
            newDict = {'Receiver': receiver, 'Book': book}
            allRequested.append(newDict)
        return allRequested
