#!/usr/bin/python3
""" Create connection using SQLAlchemy with the database"""
from models import baseModel
from models.users import User
from models.books import Book
from models.shared import Shared
import engine
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from decouple import config


class DBStorage:
    """Database Storage"""
    __engine = None
    __session = None

    def __init__(self):
        """DBStorage constructor"""
        password = config('DBPASS')
        self.__engine = create_engine('mysql+mysqldb://root:' + password + '@localhost/readIT_library', pool_size=50, max_overflow=0)

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
                new_dict[key] = obj
        else:
            for clss in classes:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    IdObj = 'Id' + obj.__class__.__name__
                    key = obj.__class__.__name__ + '.' + eval('obj.{}'.format(IdObj))
                    new_dict[key] = obj
        return (new_dict)

    def findEmail(self, Email):
        """ If this returns a user, then the email already exists in database """
        if not self.__session:
            self.reload()

        obj = self.__session.query(User).filter_by(Email=Email).first()
        return (obj)

    def close(self):
        """Close Session"""
        self.__session.remove()

    def findIdUser(self, IdUser):
        """ Returns a User obj from IdUser""" 
        if not self.__session:
            self.reload()

        obj = self.__session.query(User).get(IdUser)
        return (obj)
    
    def findIdBook(self, IdBook):
        """ Returns a User obj from IdUser""" 
        if not self.__session:
            self.reload()

        obj = self.__session.query(Book).get(IdBook)
        return (obj)
    
    def findRequestBook(self, User):
        """ Find requested book for User """
        if not self.__session:
            self.reload()
        allReceiver = []
        S = self.__session.query(Shared)
        for elements in S:
            if elements.to_dict().get('IdGiver') == User.IdUser:
                if elements.to_dict().get('StatusRequest') == "Requested":
                    # acá estoy en la fila que tiene Requested
                    allReceiver.append(elements.to_dict())
        return allReceiver

    def updateStatus(self, IdBook):
        """ Updated status request in table Shared"""
        if not self.__session:
            self.reload()
        S = self.__session.query(Shared)
        for elements in S:
            if elements.to_dict().get('IdBook') == IdBook:
                if elements.to_dict().get('StatusRequest') == "Requested":
                    elements.StatusRequest = "Accepted"
                    self.save()
        book = self.__session.query(Shared).get(IdBook)
        book.Status = "Not Available"
        self.save()
