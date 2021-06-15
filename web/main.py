#!/usr/bin/python3
""" Flask Web Application """
from flask import Blueprint, render_template, request, redirect, url_for, flash
from decouple import config
from engine import storage
from flask_login import login_required, current_user
from models.books import Book
from models.users import User
from models.shared import Shared
import requests
main = Blueprint('main', __name__)


@main.route('/index')
@main.route('/')
def index():
    """ Methods for Index """
    return render_template('index.html')

@main.route('/about')
def about():
    """ Methods for about """
    return render_template('about.html')

@main.route('/requested/<IdUser>/<IdBook>', methods=['POST'])
@main.route('/requested/', methods=['GET'])
@login_required
def requested(IdUser=None, IdBook=None):
    """ Methods for Index """
    if request.method == 'GET':
        return render_template('requested.html')
    if request.method == 'POST':
        receiver = storage.findIdUser(IdUser)
        book = storage.findIdBook(IdBook)
        Shared.mailConfirmation(current_user.to_dict(), receiver.to_dict(), book.to_dict(), status="confirmed")
        print(book.to_dict().get('IdBook'))
        storage.updateStatus(book.to_dict().get('IdBook'))
        return render_template('requested.html', msg="Thanks for  sharing!")

@main.route('/profile/<IdUser>/<IdBook>', methods=['POST'])
@main.route('/profile')
@login_required
def profile(IdUser=None, IdBook=None):
    """ Methods for profile """
    if request.method == 'GET':
        return render_template('profile.html', name=current_user.FirstName, requested=current_user.requested)
    if request.method == 'POST':
        giverMail = ""
        book = ""
        giverMail = storage.findIdUser(IdUser)
        books = storage.all(Book)
        for Id in books:
            if (getattr(books.get(Id), 'IdBook')) == IdBook:
                book = books.get(Id)
                break
        newShare = {'IdGiver': IdUser, 'IdReceiver': current_user.IdUser, 'IdBook': book.IdBook, 'StatusRequest': 'Requested'}
        newShare = Shared(**newShare)
        storage.new(newShare)
        storage.save()
        Shared.mailRequest(current_user.to_dict(), giverMail.to_dict(), book.Title)
        
        return render_template('profile.html', msg="Your request has been successfully registered", name=current_user.FirstName)
    
@main.route('/postBook', methods=['GET', 'POST'])
@login_required
def postBook():
    if request.method == 'GET':
        return render_template('postBook.html')
    if request.method == 'POST':
        ISBN = request.form.get('ISBN')
        newDict = apiGoogle(ISBN)
        if newDict == None:
            alert = "Try again or introduce a valid ISBN"
            return render_template('postBook.html', alertIsbn=alert)
        newDict['IdUser'] = current_user.IdUser
        newBook = Book(**newDict)
        storage.new(newBook)
        storage.save()
        successful = "Your book has been successfully registered"
        return render_template('postBook.html', alertIsbnOK=successful)

@main.route('/books')
def books():
    """Get method to show all books"""
    books = storage.all(Book).values()
    books = sorted(books, key=lambda k: k.Title)
    return render_template('books.html', books=books)

@main.route('/idBook')
@main.route('/idBook/<BookId>')
def thisBook(BookId=None):
    """Get method for idBook"""
    IdBook = "Book." + BookId
    books = storage.all(Book)
    book = books.get(IdBook)
    return render_template('idBook.html', book=book)

@main.route('/availableBooks')
@main.route('/availableBooks/<Title>')
def availableBooks(Title=None):
    """Get method for availableBooks"""
    books = storage.all(Book)
    users = []
    for idbook in books:
        if (getattr(books.get(idbook), 'Title')) == Title:
            if (getattr(books.get(idbook), 'IdUser')) != current_user.IdUser:
                keyUser = books.get(idbook).IdUser
                idb = idbook
                users.append(storage.findIdUser(keyUser).to_dict())
            else:
                idb = None
    return render_template('availableBooks.html', users=users, Title=books.get(idb))


def apiGoogle(ISBN):
    """ Get info from Google Books API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url= 'https://www.googleapis.com/books/v1/volumes?q=isbn:{}'
    r = requests.get(url.format(ISBN), allow_redirects=False, headers=header).json()
    if r.get('totalItems') > 0:
        items = r.get('items')
        id = items[0].get('id')
        url2 = 'https://www.googleapis.com/books/v1/volumes/{}'
        r2 = requests.get(url2.format(id), allow_redirects=False, headers=header).json()

        if r2.get('volumeInfo').get('title'):
            Title = r2.get('volumeInfo').get('title')
        else:
            Title = titleOpenL(ISBN)

        if r2.get('volumeInfo').get('authors'):
            authorsList = r2.get('volumeInfo').get('authors')
            Authors = ""
            for name in authorsList:
                if len(authorsList) == 1:
                    Authors = name
                elif len(authorsList) > 1 and name == authorsList[-2]:
                    Authors += '{} '.format(name)
                elif len(authorsList) > 1 and name == authorsList[-1]:
                    Authors += '& {}'.format(name)
                else:
                    Authors += '{}, '.format(name)
        else:
            Authors = authorsOpenL(ISBN)

        if r2.get('volumeInfo').get('description'):
            Description = r2.get('volumeInfo').get('description')
        else:
            Description = descriptionOpenL(ISBN)

        if r2.get('volumeInfo').get('imageLinks'):
            bitlytoken = config('BITLYTOKEN')
            coverLink = r2.get('volumeInfo').get('imageLinks').get('thumbnail')
            headers2 = {'Authorization': 'Bearer ' + bitlytoken,
                        'Content-Type': 'application/json'}
            data = '{ "long_url": "%s"}' % coverLink
            r3 = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers2, data=data)
            Cover = r3.json().get('id')
        else:
            Cover = coverOpenL(ISBN)

        newDict = {'Title': Title, 'Authors': Authors, 'Description': Description, 'Status': 'Available', 'Cover': Cover, "ISBN": ISBN}
        return newDict

    else:
        return apiOpenL(ISBN)

def apiOpenL(ISBN):
    """ Get info from OpenLibrary API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = 'https://openlibrary.org/isbn/{}.json'
    r = requests.get(url.format(ISBN), allow_redirects=True, headers=header)
    if r.status_code == 200:
        Title = titleOpenL(ISBN)
        Authors = authorsOpenL(ISBN)
        Description = descriptionOpenL(ISBN)
        Cover = coverOpenL(ISBN)

        newDict = {'Title': Title, 'Authors': Authors, 'Description': Description, 'Status': 'Available', 'Cover': Cover, "ISBN": ISBN}
        return newDict
    else:
        return None

def titleOpenL(ISBN):
    """ Get title info from OpenLibrary API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = 'https://openlibrary.org/isbn/{}.json'
    r = requests.get(url.format(ISBN), allow_redirects=True, headers=header)
    if r.status_code == 200:
        if r.json().get('title'):
            Title = r.json().get('title')
        else:
            Title = "No title available"
    else:
        Title = "No title available"
    return Title

def authorsOpenL(ISBN):
    """ Get authors info from OpenLibrary API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = 'https://openlibrary.org/isbn/{}.json'
    r = requests.get(url.format(ISBN), allow_redirects=True, headers=header)
    if r.status_code == 200:
        if r.json().get('authors'):
            authorsKey = r.json().get('authors')
            allAuthorsID = []
            for authorEndpoint in authorsKey:
                allAuthorsID.append(authorEndpoint.get('key'))
            url2 = 'https://openlibrary.org{}.json'
            Authors = ""
            for authorID in allAuthorsID:
                r2 = requests.get(url2.format(authorID), headers=header).json()
                if len(allAuthorsID) == 1:
                    Authors += r2.get('name')
                elif len(allAuthorsID) > 1 and authorID == allAuthorsID[-2]:
                    Authors += '{} '.format(r2.get('name'))
                elif len(allAuthorsID) > 1 and authorID == allAuthorsID[-1]:
                    Authors += '& {}'.format(r2.get('name'))
                else:
                    Authors += '{}, '.format(r2.get('name'))
        else:
            Authors = "No authors available"
    else:
        Authors = "No authors available"
    return Authors

def descriptionOpenL(ISBN):
    """ Get description info from OpenLibrary API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = 'https://openlibrary.org/isbn/{}.json'
    r = requests.get(url.format(ISBN), allow_redirects=True, headers=header)
    if r.status_code == 200:
        if r.json().get('description'):
            try:
                Description = r.json().get('description')
            except:
                Description = r.json().get('description').get('value')
        else:
            Description = "No description available"
    else:
        Description = "No description available"
    return Description

def coverOpenL(ISBN):
    """ Get title info from OpenLibrary API """
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    url = 'https://openlibrary.org/isbn/{}.json'
    r = requests.get(url.format(ISBN), allow_redirects=True, headers=header)
    if r.status_code == 200:
        if r.json().get('covers'):
            idCover = r.json().get('covers')[0]
            Cover = 'https://covers.openlibrary.org/b/id/{}.jpg'.format(idCover)
        else:
            Cover = 'https://i.imgur.com/OReLDZt.jpg'
    else:
        Cover = 'https://i.imgur.com/OReLDZt.jpg'
    return Cover

