#!/usr/bin/python3
from models.shared import Shared
from models.users import User
from models.books import Book

eva = {'FirstName':'Eva', 'LastName':'DaughterOfGod', 'Email':'2278@holbertonschool.com', 'Phone':None, 'Password':'Hola', 'City':'Paradise'}
adan = {'FirstName':'Adan', 'LastName':'Son ff God', 'Email':'2330@holbertonschool.com', 'Phone':'099111222', 'Password':'Hola', 'City':'Paradise'}
book1984 = {'Authors':'George Orwell', 'Title':'1984', 'Description':'Love this novel!', 'Status':'confirmed'}

u1 = User(**eva)
u2 = User(**adan)
b = Book(**book1984)
# u1 = '2103@holbertonschool.com'
# u2 = '2278@holbertonschool.com'

Shared.mailRequest(u1.to_dict(), u2.to_dict(), b.to_dict())
Shared.mailConfirmation(u1.to_dict(), u2.to_dict(), b.to_dict(), 'available')