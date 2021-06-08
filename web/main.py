#!/usr/bin/python3
""" Flask Web Application """
from flask import Blueprint, render_template
from engine import storage
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
        return render_template('profile.html', name=current_user.FirstName)

"""Get methods for Index"""
@main.route('/books')
def books():
    return "Books"

@main.route('/idbook')
def thisBook():
    return "This books"

@main.route('/available_books')
def availableBooks():
    return "Available books"

@main.route('/postbook')
@main.route('/postbook/<newBook>', methods=['POST'])
def NewBook():
    return "New Book"

@main.route('/about')
def about():
    return "About"


