#!/usr/bin/python3
""" holds class Shared"""
from datetime import datetime
from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship
from decouple import config


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

    def mailRequestConfirmation(userReceiver, userGiver, book):
        """send automatic email to confirm request or book already shared"""
        PASSWORD = config('PASSWORD')
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg = MIMEMultipart()
        msg2 = MIMEMultipart()
        fromx = 'readit.uy@gmail.com'
        to  = userReceiver.get('Mail')
        to2 = userGiver.get('Mail')
        msg = MIMEText('Hello {}!\n\nWe\'ve received your request of "{}".\nYou\'ll receive within 24hrs an e-mail confirmation to contact {}.\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userReceiver.get('FirstName'), book.get('Title'), userGiver.get('FirstName')))
        msg['Subject'] = 'New book request'
        msg['From'] = fromx
        msg['To'] = to
        msg2 = MIMEText('Hello {}!\n\nYour book "{}" has been requested.\nPlease check your notification area within 24hrs.\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userGiver.get('FirstName'), book.get('Title')))
        msg2['Subject'] = 'New book request'
        msg2['From'] = fromx
        msg2['To'] = to2

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login('readit.uy@gmail.com', PASSWORD)
        server.sendmail(fromx, to, msg.as_string())
        server.sendmail(fromx, to2, msg2.as_string())
        server.quit()
