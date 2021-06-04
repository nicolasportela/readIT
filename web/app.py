#!/usr/bin/python3
""" Flask Web Application """
from engine import storage
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/')
def index():
    return "Index"

"""Get methods for Index"""
@app.route('/books')
def books():
    return "Books"

@app.route('/idbook')
def thisBook():
    return "This books"

@app.route('/available_books')
def availableBooks():
    return "Available books"

@app.route('/signup/<newBook>')
@app.route('/signup')
def signup():
    return "Sign Up"

@app.route('/login')
def login():
    return "Login"

@app.route('/postbook')
@app.route('/postbook/<newBook>', methods=['POST'])
def NewBook():
    return "New Book"

@app.route('/about')
def about():
    return "About"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
