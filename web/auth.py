#!/usr/bin/python3
""" Flask Web authentication """
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.users import User
from engine import storage
from flask_login import login_user, logout_user, login_required
auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Methods for Sign Up"""
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        FirstName = request.form.get('FirstName')
        LastName = request.form.get('LastName')
        Phone = request.form.get('Phone')
        Email = request.form.get('Email')
        City = request.form.get('City')
        Password = request.form.get('Password')
        user = storage.findEmail(Email)
        """ if a user is found, we want to redirect back
        to signup page so user can try again"""
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        password = generate_password_hash(Password, method='sha256')
        newDict = {'Email': Email, 'FirstName': FirstName,
                   'Password': password, 'LastName': LastName,
                   'City': City, 'Phone': Phone}
        new_user = User(**newDict)
        storage.new(new_user)
        storage.save()
        return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Methods for Login"""
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        Email = request.form.get('email')
        Password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = storage.findEmail(Email)
        """ check if the user actually exists
        take the user-supplied password, hash it,
        and compare it to the hashed password in the database"""
        if not user or not check_password_hash(user.Password, Password):
            flash('Please check your login details and try again.')
            # if the user doesn't exist or password is wrong, reload the page
            return redirect(url_for('auth.login'))
        """ If the above check passes,
        then we know the user has the right credentials"""
        login_user(user, remember=remember)
        return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    """Methods for Logout"""
    logout_user()
    return redirect(url_for('main.index'))
