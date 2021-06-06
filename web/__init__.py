#!/usr/bin/python3
"""
Initialize app server
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from engine import storage


# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SECRET_KEY'] = 'firstaccess'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Hbtn.2021*+@localhost/readIT_library'

    # db.init_app(app)

    # blueprint for auth routes in our app
    from .appAuth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint) # app_auth.py

    # blueprint for non-auth parts of app
    from .appNonAuth import nonAuth as nonAuth_blueprint
    app.register_blueprint(nonAuth_blueprint) # app.py

    return app
    
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
