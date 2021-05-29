#!/usr/bin/python3
""" Create connection using SQLAlchemy with the database"""
from os import environ
from models.baseModel import Base
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
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Creates a new object in database"""
        self.__session.add(obj)

    def save(self):
        """Commit current changes in database"""
        self.__session.commit()
