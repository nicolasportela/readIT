#!/usr/bin/python3
""" Flask Web authlication """
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.users import User
from engine import storage
from flask_login import login_user, logout_user, login_required

# from . import db
# auth = Flask(__name__)
# auth.url_map.strict_slashes = False

auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/index')
def index():
    return render_template('index.html')

"""Get methods for Index"""
@auth.route('/books')
def books():
    return "Books"

@auth.route('/idbook')
def thisBook():
    return "This books"

@auth.route('/available_books')
def availableBooks():
    return "Available books"

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    Email = request.form.get('email')
    FirstName = request.form.get('name')
    Password = request.form.get('password')
    LastName = 'Gularte'
    City = 'New York'
    
    # user = User.query.filter_by(Email=Email).first() # if this returns a user, then the email already exists in database

    user = storage.findEmail(Email)
    print(user)

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))


    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    password = generate_password_hash(Password, method='sha256')
    newDict = {'Email': Email, 'FirstName': FirstName, 'Password': password, 'LastName': LastName, 'City': City}
    new_user = User(**newDict)

    # add the new user to the database
    #db.session.add(new_user)
    #db.session.commit()
    storage.new(new_user)
    storage.save()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    Email = request.form.get('email')
    Password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = storage.findEmail(Email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.Password, Password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('nonAuth.profile'))

@auth.route('/postbook')
@auth.route('/postbook/<newBook>', methods=['POST'])
def NewBook():
    return "New Book"

@auth.route('/about')
def about():
    return "About"

@auth.route('/profile')
def profile():
    return render_template('profile.html')
"""
@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
"""
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('nonAuth.index'))