#!/usr/bin/python3
"""Create a Super Class called BaseModel with attributes and methods that
other classes will inherit."""
import models
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from engine.dbStorage import DBStorage

Base = declarative_base()

class BaseModel:
    """Class that defines all common attributes/methods
    for other classes will inherit"""

    """
    In memorium our first user:
    
    self.FirstName = "Adan"
    self.LastName = "Son of God"
    self.Mail = "contactos@readit.uy"
    self.Password = "ABC1234"
    self.City = "Paradise"
    """

    def __str__(self):
        """String representation of the BaseModel class"""
        Id = 'Id' + self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, eval('self.{}'.format(Id)),
                                         self.__dict__)
    def save(self):
        """Create new register in the db"""
        DBStorage.new(self)
        DBStorage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["Class"] = self.__class__.__name__
        return new_dict
