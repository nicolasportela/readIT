#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book

prueba_user = {'FirstName':'Eva', 'LastName':'DaughterOfGod', 'Mail':'contacto@readIT', 'Phone':'099111222', 'Password':'Hola', 'City':'Paradise'} 
prueba_book = {'Authors':'George Orwell', 'Title':'1984', 'Description':'Love this novel!', 'Status':'Requested'}
prueba1 = User(prueba_user)
prueba2 = Book(prueba_book)
print(prueba1)
print(prueba2)

db = DBStorage()
db.reload()
db.new(prueba1)
db.new(prueba2)
db.save()
db.reload()
db.all()
