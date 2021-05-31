#!/usr/bin/python3
""" holds class User"""
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String


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
               
    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.IdUser,
                                         self.__dict__)
