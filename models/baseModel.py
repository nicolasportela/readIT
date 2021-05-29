#!/usr/bin/python3
"""Create a Super Class called BaseModel with attributes and methods that
other classes will inherit."""

import models
from uuid import uuid4

class BaseModel:
    """Class that defines all common attributes/methods
    for other classes will inherit"""

    def __init__(self):
        """Initialization of the base model"""
        self.id = str(uuid4())

    # ¿revisar cómo visualizaremos los objetos?
    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    # ¿cómo actúa esto en los métodos de storage?
    def save(self):
        """Create new register in the db"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
