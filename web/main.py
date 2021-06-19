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
    #    <!-- carousel -->
    books = storage.all(Book).values()
    books = sorted(books, key=lambda k: k.Uploaded)
    books.reverse()
    # <!-- carousel-end (sacar el books de los parametros -->
    # return render_template('index.html', books=books[:12])
    booksNotMine = []
    if not current_user.is_anonymous:
        for book in books:
            if getattr(book, 'IdUser') != current_user.IdUser:
                booksNotMine.append(book)
            elif getattr(book, 'Status') == "Not Available":
                booksNotMine.append(book)
        return render_template('index.html', books=booksNotMine[:12])
    else:
        return render_template('index.html', books=books[:12])


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
        Shared.mailConfirmation(receiver.to_dict(),
                                current_user.to_dict(),
                                book.to_dict(),
                                status="confirmed")
        storage.updateStatus(book.to_dict().get('IdBook'))
        return render_template('requested.html', msg="Thanks for  sharing!")


@main.route('/profile/<IdUser>/<IdBook>', methods=['POST'])
@main.route('/profile', methods=['GET'])
@login_required
def profile(IdUser=None, IdBook=None):
    """ Methods for profile """
    if request.method == 'GET':
        return render_template('profile.html', name=current_user.FirstName)
    if request.method == 'POST':
        book = ""
        userGiver = storage.findIdUser(IdUser)
        books = storage.all(Book)
        for Id in books:
            if (getattr(books.get(Id), 'IdBook')) == IdBook:
                book = books.get(Id)
                break
        newShare = {'IdGiver': IdUser,
                    'IdReceiver': current_user.IdUser,
                    'IdBook': book.IdBook,
                    'StatusRequest': 'Requested'}
        newShare = Shared(**newShare)
        storage.new(newShare)
        storage.save()
        Shared.mailRequest(current_user.to_dict(),
                           userGiver.to_dict(),
                           book.Title)
        msg = "Your request has been successfully registered"
        return redirect(url_for('main.requestedBook',
                                msg=msg,
                                name=current_user.FirstName))


@main.route('/requestedBook', methods=['GET'])
@login_required
def requestedBook():
    name = request.args['name']
    msg = request.args['msg']
    return render_template('/requestedBook.html', msg=msg)


@main.route('/postBook', methods=['GET', 'POST'])
@login_required
def postBook():
    if request.method == 'GET':
        return render_template('postBook.html')
    if request.method == 'POST':
        ISBN = request.form.get('ISBN')
        newDict = Book.apiGoogle(ISBN)
        if newDict is None:
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
    booksNotMine = []
    if not current_user.is_anonymous:
        for book in books:
            if getattr(book, 'IdUser') != current_user.IdUser:
                booksNotMine.append(book)
            elif getattr(book, 'Status') == "Not Available":
                booksNotMine.append(book)
        return render_template('books.html', books=booksNotMine)
    else:
        return render_template('books.html', books=books)


@main.route('/idBook')
@main.route('/idBook/<IdBook>')
def thisBook(IdBook=None):
    """Get method for idBook"""
    book = storage.findIdBook(IdBook)
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
    return render_template('availableBooks.html',
                           users=users, book=books.get(idb))
