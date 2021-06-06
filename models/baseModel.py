#!/usr/bin/python3
"""Create a Super Class called BaseModel with attributes and methods that
other classes will inherit."""
import models
from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
# import engine
# from engine.dbStorage import DBStorage

Base = declarative_base()


class BaseModel:
    """Class that defines all common attributes/methods
    for other classes will inherit"""

    def __str__(self):
        """String representation of the BaseModel class"""
        Id = 'Id' + self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, eval('self.{}'.format(Id)),
                                         self.__dict__)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["Class"] = self.__class__.__name__
        return new_dict
