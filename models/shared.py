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


    def	mailRequest(userReceiver, userGiver, book):
        """send automatic email to confirm request or book already shared"""
        PASSWORD = config('PASSWORD')
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg = MIMEMultipart()
        msg2 = MIMEMultipart()
        fromx = 'readit.uy@gmail.com'
        to  = userReceiver.get('Email')
        to2 = userGiver.get('Email')
        msg = MIMEText('Hello, {}!\n\nWe\'ve received your request of "{}".\nYou\'ll receive within 24hrs an e-mail confirmation to contact {}.\n\nThanks for being part of this book lovers community!\n\nreadIT Team'.format(userReceiver.get('FirstName'), book, userGiver.get('FirstName')))
        msg['Subject'] = 'New book request'
        msg['From'] = fromx
        msg['To'] = to
        msg2 = MIMEText('Hello, {}!\n\nYour book "{}" has been requested.\nPlease, check your notification area within 24hrs to confirm it and contact {} or it will be automatically cancelled otherwise.\n\nThanks for being part of this book lovers community!\n\nreadIT Team'.format(userGiver.get('FirstName'), book, userReceiver.get('FirstName')))
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

    def mailConfirmation(userReceiver, userGiver, book, status):
        """send automatic email to confirm request or book already shared"""
        PASSWORD = config('PASSWORD')
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg = MIMEMultipart()
        msg2 = MIMEMultipart()
        fromx = 'readit.uy@gmail.com'
        to  = userReceiver.get('Email')
        to2 = userGiver.get('Email')

        if status == 'confirmed':
            if userGiver.get('Phone'):
                msg = MIMEText('Hello, {}!\n\nYour request of "{}" has been confirmed.\nPlease, contact {} to read it:\nPhone: {}\nE-mail: {}\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userReceiver.get('FirstName'), book.get('Title'), userGiver.get('FirstName'), userGiver.get('Phone'), userGiver.get('Email')))
            else:
                msg = MIMEText('Hello, {}!\n\nYour request of "{}" has been confirmed.\nPlease, contact {} to read it:\nE-mail: {}\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userReceiver.get('FirstName'), book.get('Title'), userGiver.get('FirstName'), userGiver.get('Email')))
            msg['Subject'] = 'Book request confirmed'
            msg['From'] = fromx
            msg['To'] = to
            if userReceiver.get('Phone'):
                msg2 = MIMEText('Hello, {}!\n\nYou have confirmed a request of your book "{}".\nPlease, contact {} to spread the culture:\nPhone: {}\nE-mail: {}\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userGiver.get('FirstName'), book.get('Title'), userReceiver.get('FirstName'), userReceiver.get('Phone'), userReceiver.get('Email')))
            else:
                msg2 = MIMEText('Hello, {}!\n\nYou have confirmed a request of your book "{}".\nPlease, contact {} to spread the culture:\nE-mail: {}\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userGiver.get('FirstName'), book.get('Title'), userReceiver.get('FirstName'), userReceiver.get('Email')))
            msg2['Subject'] = 'Book request confirmed'
            msg2['From'] = fromx
            msg2['To'] = to2

        else:
            msg = MIMEText('Hello, {}!\n\nYour request of "{}" to {} has not been confirmed.\nPlease, make another request.\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userReceiver.get('FirstName'), book.get('Title'), userGiver.get('FirstName')))
            msg['Subject'] = 'Book request not confirmed'
            msg['From'] = fromx
            msg['To'] = to
            msg2 = MIMEText('Hello, {}!\n\nYou haven\'t confirmed a request of your book "{}" from {} within the past 24hrs and it has been automatically cancelled.\n\nThanks for being part of this book lovers community!\nreadIT Team'.format(userGiver.get('FirstName'), book.get('Title'), userReceiver.get('FirstName')))
            msg2['Subject'] = 'Book request not confirmed'
            msg2['From'] = fromx
            msg2['To'] = to2

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login('readit.uy@gmail.com', PASSWORD)
        server.sendmail(fromx, to, msg.as_string())
        server.sendmail(fromx, to2, msg2.as_string())
        server.quit()

