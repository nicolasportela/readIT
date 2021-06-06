#!/usr/bin/python3
""" Create connection using SQLAlchemy with the database"""
from models import baseModel
from models.users import User
from models.books import Book
from models.shared import Shared
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage constructor"""
        # password = environ('READITDBPASS')
        self.__engine = create_engine('mysql+mysqldb://root:root@localhost/readIT_library')

    def reload(self):
        """Load objects from database"""
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        baseModel.Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Creates a new object in database"""
        self.__session.add(obj)

    def save(self):
        """Commit current changes in database"""
        self.__session.commit()

    def all(self, cls=None):
        """Return a dictionary with all objects depending on class name"""
        classes = {"Users": User, "Books": Book, "Shared": Shared}
        if not self.__session:
            self.reload()
        new_dict = {}
        if cls:
            IdObj = 'Id' + cls.__name__
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + eval('obj.{}'.format(IdObj))
                new_dict[key] = obj.__str__()
        else:
            for clss in classes:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    IdObj = 'Id' + obj.__class__.__name__
                    key = obj.__class__.__name__ + '.' + eval('obj.{}'.format(IdObj))
                    new_dict[key] = obj.__str__()
        return (new_dict)

    def close(self):
        """Close Session"""
        self.__session.remove()
