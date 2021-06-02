#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book
from models.shared import Shared

db = DBStorage()
print(db.all())

intercambio = {'IdGiver': '63f3dbe1-c743-40fa-ad96-831be835bb6f', 'IdReceiver': '3f2a0252-fb9d-4eb7-a1c5-15e05a4dec3f', 'IdBook': 'fc90a194-1967-4024-a3da-c5d0b98cd1c8', 'StatusRequest': 'pending'}
prueba = Shared(intercambio)
print(prueba)
db.new(prueba)
db.save()
db.reload()
print(db.all())
