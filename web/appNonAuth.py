#!/usr/bin/python3
""" Flask Web Application """
from flask import Blueprint, render_template
from engine import storage
# from . import db
# app = Flask(__name__)
# app.url_map.strict_slashes = False

nonAuth = Blueprint('nonAuth', __name__)

@nonAuth.route('/')
def index():
    return render_template('index.html')

"""Get methods for Index"""
@nonAuth.route('/books')
def books():
    return "Books"

@nonAuth.route('/idbook')
def thisBook():
    return "This books"

@nonAuth.route('/available_books')
def availableBooks():
    return "Available books"

@nonAuth.route('/signup')
@nonAuth.route('/signup/<newBook>')
def signup():
    return render_template('singup.html')

@nonAuth.route('/login')
def login():
    return render_template('login.html')

@nonAuth.route('/postbook')
@nonAuth.route('/postbook/<newBook>', methods=['POST'])
def NewBook():
    return "New Book"

@nonAuth.route('/about')
def about():
    return "About"
