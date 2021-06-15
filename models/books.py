#!/usr/bin/python3
""" holds class Book"""
from datetime import datetime
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship
from models.shared import Shared


class Book(BaseModel, Base):
    """Representation of a Book"""
    __tablename__ = 'Books'
    IdBook = Column(String(40), nullable=False, primary_key=True)
    IdUser = Column(String(40), ForeignKey('Users.IdUser'), nullable=False) 
    Authors = Column(String(256), nullable=False)
    Title = Column(String(256), nullable=False)
    Description = Column(String(2048), nullable=False)
    ISBN = Column(String(30), nullable=False)
    Status = Column(String(30), nullable=False)
    Uploaded = Column(DateTime, default=datetime.utcnow, nullable=False)
    Cover = Column(String(100))
    
    def __init__(self, **kwargs):
        """initializes book"""
        self.IdBook = str(uuid4())
        self.IdUser = kwargs.get('IdUser')
        self.Authors = kwargs.get('Authors')
        self.Title = kwargs.get('Title')
        self.Description = kwargs.get('Description')
        self.ISBN = kwargs.get('ISBN')
        self.Status = kwargs.get('Status')
        now = datetime.now()
        self.Uploaded = now.strftime('%Y-%m-%d %H:%M:%S')
        self.Cover = kwargs.get('Cover')
