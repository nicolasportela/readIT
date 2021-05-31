#!/usr/bin/python3
from models.baseModel import BaseModel
from models.users import User
from engine.dbStorage import DBStorage
"""
prueba_dict = {'FirstName':'Eva', 'lastName':'DaughterOfGod', 'Mail':'contacto@readIT'} 
prueba = User(prueba_dict)
print(prueba)
print(prueba.to_dict())
"""
primera_prueba_all = DBStorage()
x = primera_prueba_all.all(User)
print(x)

