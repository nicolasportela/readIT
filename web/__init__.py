#!/usr/bin/python3
"""
Initialize app server
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from engine import storage
from flask_login import LoginManager
import os


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    mysql = 'mysql://root:Hbtn.2021*+@localhost/readIT_library'
    app.config['SECRET_KEY'] = 'firstaccess'
    app.config['SQLALCHEMY_DATABASE_URI'] = mysql

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(IdUser):
        obj = storage.findIdUser(IdUser)
        return (obj)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
