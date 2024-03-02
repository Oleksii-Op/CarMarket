from typing import Optional, List
from datetime import datetime
import psycopg2
from phone_validator import is_valid_number, InvalidNumberError
from email_validator import is_valid_email, InvalidEmailError

from sqlalchemy import (create_engine, Integer, String, DateTime,
                        ForeignKey, Column, Float, Boolean)
from sqlalchemy.orm import (relationship, Mapped,
                            validates, mapped_column, declarative_base)
from sqlalchemy.ext.declarative import ConcreteBase


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)
    email_address: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    gender: Mapped[str] = mapped_column(String(6), nullable=False)
    registered_on = Column(DateTime, default=datetime.now)
    updated_info_on = Column(DateTime,
                             default=datetime.now,
                             onupdate=datetime.now)

    tracks: Mapped[List["Tracks"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    motorcycles: Mapped[List["Motorcycles"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    motor_cars: Mapped[List["MotorCars"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    electro_cars: Mapped[List["ElectroCars"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    address: Mapped[List["Address"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    @validates('gender')
    def validate(self, key, gender):
        try:
            if not isinstance(gender, str):
                raise ValueError
            if not gender:
                raise ValueError
            if gender not in ['male', 'female', 'other', 'unknown']:
                raise ValueError
            return gender
        except (ValueError, AttributeError):
            while True:
                print("Error in gender validation, please try again")
                print("Choose from: male, female, other, unknown")
                gender = input('Please enter your gender: ')
                if gender in ['male', 'female', 'other', 'unknown']:
                    break
            return gender

    @validates('phone_number')
    def validate_phone_number(self, key, number):
        try:
            if not number or not isinstance(number, str):
                raise ValueError
            if not is_valid_number(number):
                raise InvalidNumberError
            return number
        except (ValueError, AttributeError, InvalidNumberError):
            while True:
                print("Error in phone number validation, please try again")
                number = input('Please enter your phone number: ')
                if is_valid_number(number):
                    break
            return number

    @validates('email_address')
    def validate_email_address(self, key, address):
        try:
            if not address or not isinstance(address, str):
                raise ValueError
            if not is_valid_email(address):
                raise InvalidEmailError
            return address
        except (ValueError, AttributeError, InvalidEmailError):
            while True:
                print("Error in email address validation, please try again")
                address = input('Please enter your email address: ')
                if is_valid_email(address):
                    break
            return address

    @validates('username')
    def validate_username(self, key, username):
        try:
            # if len(username) < 6:
            #     raise ValueError("Username must be at least 6 characters")
            if len(username) > 20:
                raise ValueError("Username must be maximum 20 characters")
            return username
        except (ValueError, AttributeError) as error:
            while True:
                print(error)
                print("Error in username validation, please try again")
                username = input('Please enter your username: ')
                if 6 <= len(username) <= 20:
                    break
            return username

    @validates('name')
    def validate_name(self, key, name):
        try:
            if not isinstance(name, str):
                raise ValueError
            if not name:
                raise ValueError("Name cannot be empty")
            if len(name) > 40:
                raise ValueError("Name must be maximum 40 characters")
            return name
        except (ValueError, AttributeError):
            while True:
                print("Error in name validation, please try again")
                name = input('Please enter your name: ')
                if len(name) <= 40:
                    break
            return name

    def __init__(self,
                 username: str,
                 name: str,
                 email_address: str,
                 phone_number: str,
                 gender: str = 'Unknown') -> None:
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
        self.username = username
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
        self.gender = gender

    def __repr__(self) -> str:
        return (f"User(username={self.username},"
                f"name={self.name}, email_address={self.email_address},"
                f"phone_number={self.phone_number}, gender={self.gender},"
                f" registered_on={self.registered_on},"
                f" updated_info_on={self.updated_info_on})")


class Address(Base):
    __tablename__ = 'addresses'

    address_id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(40), nullable=False)
    state: Mapped[str] = mapped_column(String(40), nullable=False)
    zip_code: Mapped[str] = mapped_column(Integer, nullable=False)
    country: Mapped[str] = mapped_column(String(40), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='address')

    @validates('zip_code')
    def validate_zip_code(self, key, zip_code):
        try:
            if not isinstance(zip_code, str):
                raise ValueError
            if not zip_code:
                raise ValueError
            if len(zip_code) != 5 or not zip_code.isdigit():
                raise ValueError
            return zip_code
        except (ValueError, AttributeError):
            while True:
                print("Error in zip code validation, please try again")
                zip_code = input('Please enter your zip code: ')
                if len(zip_code) == 5 and zip_code.isdigit():
                    break
            return zip_code

    @validates('address')
    def validate_address(self, key, address):
        try:
            if not isinstance(address, str):
                raise ValueError
            if not address:
                raise ValueError
            if len(address) > 255:
                raise ValueError
            return address
        except (ValueError, AttributeError):
            while True:
                print("Error in address validation, please try again")
                address = input('Please enter your address: ')
                if len(address) <= 255:
                    break
            return address

    @validates('state')
    def validate_state(self, key, state):
        try:
            if not isinstance(state, str):
                raise ValueError
            if not state:
                raise ValueError
            if len(state) > 40:
                raise ValueError
            return state
        except (ValueError, AttributeError):
            while True:
                print("Error in state validation, please try again")
                state = input('Please enter your state: ')
                if len(state) <= 40:
                    break
            return state

    def __init__(self,
                 address: Mapped[str],
                 city: Mapped[str],
                 state: Mapped[str],
                 zip_code: Mapped[str],
                 country: Mapped[str]) -> None:
        """
        Initialize the address with the provided details.
        Args:
        address (str): The address of the user.
        city (str): The city of the user.
        state (str): The state of the user.
        zip_code (str): The zip code of the user.
        country (str): The country of the user.
        Returns:
        None
        """
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

    def __repr__(self) -> str:
        return (f"Address(address_id={self.address_id},"
                f" address={self.address}, city={self.city},"
                f" state={self.state}, zip_code={self.zip_code},"
                f" country={self.country})")


class Vehicle(ConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    maker: Mapped[str] = mapped_column(String(20), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    condition: Mapped[str] = mapped_column(String(20), nullable=False)
    fuel: Mapped[str] = mapped_column(String(20), nullable=False)
    power_output: Mapped[int] = mapped_column(Integer, nullable=False)
    gearbox: Mapped[str] = mapped_column(String(20), nullable=False)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=False)
    primary_registration: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    body_type: Mapped[str] = mapped_column(String(20), nullable=False)
    wheel_drive: Mapped[str] = mapped_column(String(20), nullable=False)

    interior: Mapped[str] = mapped_column(String(255))
    audio_video_system: Mapped[str] = mapped_column(String(255))
    wheels_discs: Mapped[str] = mapped_column(String(255))
    safety_equp: Mapped[str] = mapped_column(String(255))
    lights: Mapped[str] = mapped_column(String(255))
    comfort_equip: Mapped[str] = mapped_column(String(255))
    # Miscellaneous equpment
    miscell_equip: Mapped[str] = mapped_column(String(255))
    # Miscellaneous information
    miscell_info: Mapped[str] = mapped_column(String(255))
    number_of_seats: Mapped[int] = mapped_column(Integer)
    number_of_doors: Mapped[int] = mapped_column(Integer)
    empty_weight: Mapped[int] = mapped_column(Integer)
    max_weight: Mapped[int] = mapped_column(Integer)

    manufactured_date: Mapped[datetime] = mapped_column(DateTime,
                                                        nullable=False)
    engine_volume: Mapped[float] = mapped_column(Float,
                                                 nullable=False)

    average_consump: Mapped[float] = mapped_column(Float,
                                                   nullable=False)

    vin_number: Mapped[str] = mapped_column(String(40),
                                            nullable=False, unique=True)

    uploaded_on: Mapped[datetime] = mapped_column(DateTime, nullable=False,
                                                  default=datetime.now)

    updated_on: Mapped[datetime] = mapped_column(DateTime,
                                                 nullable=False, default=datetime.now,
                                                 onupdate=datetime.now)


class Tracks(Vehicle):
    __tablename__ = 'tracks'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='tracks')


class ElectroCars(Vehicle):
    __tablename__ = "electro_cars"

    hybrid: Mapped[bool] = mapped_column(Boolean, nullable=False)
    battery_capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='electro_cars')


class Motorcycles(Vehicle):
    __tablename__ = 'motorcycles_sales'

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='motorcycles')


class MotorCars(Vehicle):
    __tablename__ = "motorcars_sales"

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='motor_cars')


engine = create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)

user = User(username='J7i', name='Jade',
            email_address='utEeMFTeli@yahoo.com',
            phone_number='+37067673346', gender='male')
