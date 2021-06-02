#!/usr/bin/python3
""" holds class User"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String
from uuid import uuid4
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user """
    __tablename__ = 'Users'
    IdUser = Column(String(40), nullable=False, primary_key=True)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    Phone = Column(String(30), nullable=False)
    Mail = Column(String(50), nullable=True)
    Password = Column(String(50), nullable=False)
    City = Column(String(50), nullable=False)

    def __init__(self, **kwargs):
        """initializes user"""
        self.IdUser = str(uuid4())
        self.FirstName = kwargs.get('FirstName')
        self.LastName = kwargs.get('LastName')
        self.Phone = kwargs.get('Phone')
        self.Mail = kwargs.get('Mail')
        self.Password = kwargs.get('Password')
        self.City = kwargs.get('City')
