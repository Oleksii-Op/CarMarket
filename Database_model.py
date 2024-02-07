from typing import Optional, List
from datetime import datetime
import psycopg2
from conn_to_database import select_database

from sqlalchemy import (create_engine, Integer, String, DateTime,
                        ForeignKey, Column, Float, Boolean)
from sqlalchemy.orm import (relationship, Mapped,
                            validates, mapped_column)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


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

    tracks_sales: Mapped[List["Tracks_Sales"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    motorcycles_sales: Mapped[List["Motorcycles_Sales"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    motorcycles_sales: Mapped[List["MotorCars"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    motorcycles_sales: Mapped[List["ElectroCars"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    motorcycles_sales: Mapped[List["Address"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    @validates('gender')
    def validate(self, key, gender):
        if not isinstance(gender, str):
            raise TypeError(
                f'str object expected, '
                f'got {gender.__class__.__name__} insted'
            )

        if not gender:
            raise ValueError('Gender cannot be empty')

        if gender.lower() not in ['male', 'female', 'other', 'unknown']:
            raise ValueError('Wrong selection')

    @validates('phone_number')
    def validate_phone_number(self, key, number):
        if not isinstance(number, str):
            raise TypeError(
                f'str object expected, '
                f'got {number.__class__.__name__} insted')
        elif len(number) > 20:
            raise ValueError('Wrong number format')

    @validates('email_address')
    def validate_email_address(self, key, address):
        if "@" not in address:
            raise ValueError("Invalid email address")
        if len(address) < 6:
            raise ValueError(f"Email address is too short -> {len(address)}")
        return address

    @validates('username')
    def validate_username(self, key, username):
        if len(username) < 6:
            raise ValueError("Username can be at least 6 characters")
        elif len(username) > 20:
            raise ValueError("Username can be maximum 20 characters")
        return username

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        if len(name) > 40:
            raise ValueError("Name can be maximum 40 characters")

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
    zip_code: Mapped[int] = mapped_column(Integer, nullable=False)
    country: Mapped[str] = mapped_column(String(40), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='addresses')

    def __repr__(self) -> str:
        return (f"Address(address_id={self.address_id},"
                f" address={self.address}, city={self.city},"
                f" state={self.state}, zip_code={self.zip_code},"
                f" country={self.country})")


class TracksSales(Base):
    __tablename__ = 'tracks_sales'

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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='tracks_sales')


class ElectroCars(Base):
    __tablename__ = "electro_cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    maker: Mapped[str] = mapped_column(String(20), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    condition: Mapped[str] = mapped_column(String(20), nullable=False)
    fuel: Mapped[str] = mapped_column(String(20), nullable=False)
    hybrid: Mapped[bool] = mapped_column(Boolean, nullable=False)
    power_output: Mapped[int] = mapped_column(Integer, nullable=False)
    gearbox: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=False)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)
    primary_registration: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    body_type: Mapped[str] = mapped_column(String(20), nullable=False)
    wheel_drive: Mapped[str] = mapped_column(String(20), nullable=False)
    battery_capacity: Mapped[int] = mapped_column(Integer, nullable=False)

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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='electro_cars')


class Motorcycles(Base):
    __tablename__ = 'motorcycles_sales'

    id: Mapped[int] = mapped_column(primary_key=True)
    maker: Mapped[str] = mapped_column(String(20), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    condition: Mapped[str] = mapped_column(String(20), nullable=False)
    fuel: Mapped[str] = mapped_column(String(20), nullable=False)
    power_output: Mapped[int] = mapped_column(Integer, nullable=False)
    gearbox: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=False)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)
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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='motorcycles_sales')

class MotorCars(Base):
    __tablename__ = "motorcars_sales"

    id: Mapped[int] = mapped_column(primary_key=True)
    maker: Mapped[str] = mapped_column(String(20), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    condition: Mapped[str] = mapped_column(String(20), nullable=False)
    fuel: Mapped[str] = mapped_column(String(20), nullable=False)
    power_output: Mapped[int] = mapped_column(Integer, nullable=False)
    gearbox: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255), nullable=False)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)
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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='motorcars_sales')



# engine = create_engine(select_database(), echo=True)
# Base.metadata.create_all(engine)