#!/usr/bin/python3
from models.baseModel import BaseModel
from models.users import User
from engine.dbStorage import DBStorage

prueba_dict = {'FirstName':'Eva', 'LastName':'DaughterOfGod', 'Mail':'contacto@readIT', 'Phone':'099111222', 'Password':'Hola', 'City':'Paradise'} 
prueba = User(prueba_dict)
print(prueba)

# primera_prueba_all = DBStorage()
# x = primera_prueba_all.all(User)
# print(x)
