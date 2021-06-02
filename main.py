#!/usr/bin/python3
from engine.dbStorage import DBStorage
from models.baseModel import BaseModel
from models.users import User
from models.books import Book

print("Create test dictonaries...")
eva = {'FirstName':'Eva', 'LastName':'DaughterOfGod', 'Mail':'evacontacto@readIT', 'Phone':'099111222', 'Password':'Hola', 'City':'Paradise'}
adan = {'FirstName':'Adan', 'LastName':'Son ff God', 'Mail':'adancontacto@readIT', 'Phone':'099111222', 'Password':'Hola', 'City':'Paradise'} 
1984 = {'Authors':'George Orwell', 'Title':'1984', 'Description':'Love this novel!', 'Status':'Requested'}

Print("Create instants User...")
user1 = User(eva)
user2 = User(adan)

print("Create instants Book...")
book1 = Book(1984)

print("Show representations...")

print(user1)
print(user2)
print(book1)

Print("Adding to mysql...")
db = DBStorage()
db.reload()
db.new(prueba1)
db.new(prueba2)
db.save()
db.reload()
print("Printing all objects...")
db.all()
