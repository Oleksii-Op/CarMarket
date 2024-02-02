from sqlalchemy import (create_engine, Integer, String, DateTime,
                        ForeignKey, Column)
from sqlalchemy.orm import sessionmaker, relationship, backref, validates
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///database.db')

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    name = Column(String(40), nullable=False)
    email_address = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    gender = Column(String(6), nullable=False)
    registered_on = Column(DateTime, default=datetime.now)
    updated_info_on = Column(DateTime,
                        default=datetime.now,
                        onupdate=datetime.now)

    @validates('email_address')
    def validate_email_address(self, key, address):
        if "@" not in address:
            raise ValueError("Invalid email address")
        if len(address) < 6:
            raise ValueError(f"Email address is too short -> {len(address)}")
        return address


    def __init__(self,
                 username: str,
                 name: str,
                 email_address: str,
                 phone_number: str,
                 gender: str) -> None:
        """
        Initialize the user with the provided details.
        Args:
        username (str): The username of the user.
        name (str): The name of the user.
        email_address (str): The email address of the user.
        phone_number (str): The phone number of the user.
        gender (str): The gender of the user.
        Returns:
        None
        """
        self._username = username
        self._name = name
        self._email_address = email_address
        self._phone_number = phone_number
        self._gender = gender

    def __repr__(self):
        return (f"User(username={self.username},"
                f"name={self.name}, email_address={self.email_address},"
                f"phone_number={self.phone_number}, gender={self.gender},"
                f" registered_on={self.registered_on},"
                f" updated_info_on={self.updated_info_on})")


class Address(Base):
    __tablename__ = 'addresses'

    address_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)

    relationship('User', backref=backref('addresses', order_by=address_id))