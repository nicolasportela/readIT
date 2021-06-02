#!/usr/bin/python3
""" holds class Shared"""
from datetime import datetime
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


class Shared(BaseModel, Base):
    """Representation of a Shared"""
    __tablename__ = 'Shared'
    IdShared = Column(String(40), nullable=False, primary_key=True)
    IdGiver = Column(String(40), ForeignKey('Users.IdUser'), nullable=False)
    IdReceiver = Column(String(40), ForeignKey('Users.IdUser'), nullable=False)
    IdBook = Column(String(40), ForeignKey('Books.IdBook'), nullable=False)
    Datashared = Column(DateTime, default=datetime.utcnow, nullable=False)
    StatusRequest = Column(String(30), nullable=False)

    IdGivers = relationship('User', foreign_keys=[IdGiver])
    IdReceivers = relationship('User', foreign_keys=[IdReceiver])
    IdBooks = relationship('Book', foreign_keys=[IdBook])

    def __init__(self, **kwargs):
        """initializes Shared"""
        self.IdShared = str(uuid4())
        self.IdGiver = kwargs.get('IdGiver')
        self.IdReceiver = kwargs.get('IdReceiver')
        self.IdBook = kwargs.get('IdBook')
        now = datetime.now()
        self.Datashared = now.strftime('%Y-%m-%d %H:%M:%S')
        self.StatusRequest = kwargs.get('StatusRequest')
