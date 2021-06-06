#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book
from models.shared import Shared

db = DBStorage()
print(db.all())

intercambio = {'IdGiver': '5d1fc5a6-98f2-4ca4-979a-bd5ef55fc668', 'IdReceiver': '8f835f5e-1fe2-4ffe-bb6c-f7ba289785e9', 'IdBook': '991a07af-0f9e-4ad9-b765-84136058f4bf', 'StatusRequest': 'pending'}
prueba = Shared(**intercambio)
print(prueba)
db.new(prueba)
db.save()
db.reload()
print(db.all())
