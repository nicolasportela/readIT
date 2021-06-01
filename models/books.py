#!/usr/bin/python3
""" holds class Book"""
from datetime import datetime
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from uuid import uuid4


class Book(BaseModel, Base):
    """Representation of a Book"""
    __tablename__ = 'Books'
    IdBook = Column(String(40), nullable=False, primary_key=True)
    Authors = Column(String(256), nullable=False)
    Title = Column(String(256), nullable=False)
    Description = Column(String(512), nullable=False)
    ISBN = Column(String(30))
    Status = Column(String(30), nullable=False)
    Uploaded = Column(DateTime, default=datetime.utcnow, nullable=False)


    def __init__(self, *args):
        """initializes book"""
        self.IdBook = str(uuid4())
        if args:
            self.Authors = args[0].get('Authors')
            self.Title = args[0].get('Title')
            self.Description = args[0].get('Description')
            self.ISBN = args[0].get('ISBN')
            self.Status = args[0].get('Status')
            now = datetime.now()
            self.Uploaded = now.strftime('%Y-%m-%d %H:%M:%S')
