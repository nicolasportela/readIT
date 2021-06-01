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

    def __init__(self, *args):
        """initializes user"""
        self.IdUser = str(uuid4())
        if args:
            self.FirstName = args[0].get('FirstName')
            self.LastName = args[0].get('LastName')
            self.Phone = args[0].get('Phone')
            self.Mail = args[0].get('Mail')
            self.Password = args[0].get('Password')
            self.City = args[0].get('City')
