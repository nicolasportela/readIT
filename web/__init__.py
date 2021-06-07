#!/usr/bin/python3
"""
Initialize app server
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from engine import storage
from flask_login import LoginManager

# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SECRET_KEY'] = 'firstaccess'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Hbtn.2021*+@localhost/readIT_library'

    # db.init_app(app)
    # storage.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'appAuth.login'
    login_manager.init_app(app)

    from models.users import User

    @login_manager.user_loader
    def load_user(IdUser):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        # return User.query.get(IdUser)
        
        # obj = self.__session.query(User).filter_by(IdUser=IdUser)
        obj = storage.findIdUser(IdUser)
        return (obj)

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
