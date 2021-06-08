#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book
from models.shared import Shared

db = DBStorage()
print(db.all())

intercambio = {'IdGiver': '967236f1-63d0-46a3-bf26-6446ddac2486', 'IdReceiver': 'ef29c5db-fdab-4a99-830b-0b6fa29206bd', 'IdBook': 'b5e12629-1098-4ca5-a565-66f7b516c93b', 'StatusRequest': 'pending'}
prueba = Shared(**intercambio)
print(prueba)
db.new(prueba)
db.save()
db.reload()
print(db.all())
