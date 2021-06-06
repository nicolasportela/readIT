#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book
from models.shared import Shared

db = DBStorage()
print(db.all())

intercambio = {'IdGiver': '150eb59e-dbc4-4622-a52e-8f035e54c119', 'IdReceiver': '03b24e9a-2dfa-450c-b488-71649f3160d1', 'IdBook': '22625294-cc88-47d1-a935-d515c5b39879', 'StatusRequest': 'pending'}
prueba = Shared(intercambio)
print(prueba)
db.new(prueba)
db.save()
db.reload()
print(db.all())
