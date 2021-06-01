#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book
from models.shared import Shared

db = DBStorage()
print(db.all())

intercambio = {'IdGiver': '02f87f75-1a2e-479c-8f97-24ded7d15045', 'IdReceiver': '3924aaa9-d7f0-4d18-94dd-d43dee975e60', 'IdBook': '6027b4f2-3dc0-4579-b70e-c8d04d825812', 'StatusRequest': 'pending'}
prueba = Shared(intercambio)
print(prueba)
db.new(prueba)
db.save()
db.reload()
print(db.all())
