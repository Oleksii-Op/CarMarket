from typing import Optional, List
from datetime import datetime
from sqlalchemy import (create_engine, Integer, String, DateTime,
                        ForeignKey, Float, Boolean)

from sqlalchemy.orm import (relationship, Mapped,
                            validates, mapped_column, DeclarativeBase, Session)

from sqlalchemy.ext.declarative import AbstractConcreteBase

from aux_annotations.annotations import created_at, updated_at
from Validators.user_input.gender_valid import gender_validator_func
from Validators.user_input.phone_number_valid import phone_number_validator_func
from Validators.user_input.email_valid import email_validator_func
from Validators.user_input.name_valid import name_validator_func
from Validators.user_input.username_valid import username_validate_func
from Validators.address_input.address_valid import address_validator_func
from Validators.address_input.state_valid import state_validator_func
from Validators.address_input.zip_code_valid import zip_code_validator_func
from conn_to_database import select_database
from config import settings


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    user_property: Mapped[str] = mapped_column(String(1), default='r')
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=True)
    email_address: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    main_phone_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    additional_phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    gender: Mapped[str] = mapped_column(String(7), nullable=False)
    registered_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    @validates('gender')
    def validate(self, key, gender):
        return gender_validator_func(gender)

    @validates('phone_number')
    def validate_phone_number(self, key, number):
        return phone_number_validator_func(number)

    @validates('email_address')
    def validate_email_address(self, key, address):
        return email_validator_func(address)

    @validates('username')
    def validate_username(self, key, username):
        return username_validate_func(username)

    @validates('name')
    def validate_name(self, key, name):
        return name_validator_func(name)

    # trucks: Mapped[List["Trucks"]] = relationship(
    #     back_populates='user', cascade='all, delete-orphan')
    #
    # motorcycles: Mapped[List["Motorcycles"]] = relationship(
    #     back_populates='user', cascade='all, delete-orphan')
    #
    # motor_cars: Mapped[List["MotorCars"]] = relationship(
    #     back_populates='user', cascade='all, delete-orphan')
    #
    # electro_cars: Mapped[List["ElectroCars"]] = relationship(
    #     back_populates='user', cascade='all, delete-orphan')

    address: Mapped[List["Address"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    users_vehicles: Mapped[List["UsersVehicles"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')

    sales_records: Mapped[List["SalesRecords"]] = relationship(
        back_populates='user', cascade='all, delete-orphan')



    def __repr__(self) -> str:
        return (f"User(username={self.username},"
                f"name={self.name}, email_address={self.email_address},"
                f"phone_number={self.phone_number}, gender={self.gender}")


class Address(Base):
    __tablename__ = 'addresses'

    address_id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(40), nullable=False)
    state: Mapped[str] = mapped_column(String(40), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(5), nullable=False)
    country: Mapped[str] = mapped_column(String(40), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='address')

    @validates('zip_code')
    def validate_zip_code(self, key, zip_code):
        return zip_code_validator_func(zip_code)

    @validates('address')
    def validate_address(self, key, address):
        return address_validator_func(address)

    @validates('state')
    def validate_state(self, key, state):
        return state_validator_func(state)

    def __repr__(self) -> str:
        return (f"Address(address_id={self.address_id},"
                f" address={self.address}, city={self.city},"
                f" state={self.state}, zip_code={self.zip_code},"
                f" country={self.country})")

class SalesRecords(Base):
    __tablename__ = 'sales_records'

    record_id: Mapped[int] = mapped_column(primary_key=True)
    seller_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    buyer_id: Mapped[Optional["User"]] = mapped_column(ForeignKey('users.user_id'), default=None)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('users_vehicles.vehicle_id'))
    sale_date: Mapped[created_at]

    user: Mapped["User"] = relationship(back_populates='sales_records')
    vehicle: Mapped["UserVehicle"] = relationship(back_populates='sales_records')


class Category(Base):
    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return (f"Category(category_id={self.category_id},"
                f" category_name={self.category_name},"
                f" description={self.description})")


class UserVehicle(Base):
    __tablename__ = 'users_vehicles'

    vehicle_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.category_id'))

    def __repr__(self) -> str:
        return (f"UserVehicle(vehicle_id={self.vehicle_id},"
                f" user_id={self.user_id},"
                f" category_id={self.category_id})")
    

class Vehicle(AbstractConcreteBase, Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    discontinued: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    maker: Mapped[str] = mapped_column(String(20), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    condition_type: Mapped[str] = mapped_column(String(50), nullable=False)
    fuel: Mapped[str] = mapped_column(String(20), nullable=False)
    power_output: Mapped[int] = mapped_column(Integer, nullable=False)
    gearbox: Mapped[str] = mapped_column(String(20), nullable=False)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False)
    used: Mapped[bool] = mapped_column(Boolean, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)
    primary_registration: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    manufactured_date: Mapped[datetime] = mapped_column(
        DateTime, nullable=False)

    engine_volume: Mapped[float] = mapped_column(
        Float, nullable=False)

    average_consumption: Mapped[float] = mapped_column(
        Float, nullable=True)

    vin_number: Mapped[str] = mapped_column(
        String(40), nullable=False, unique=True)

    body_type: Mapped[Optional[str]]
    wheel_drive: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    interior: Mapped[Optional[str]]
    audio_video_system: Mapped[Optional[str]]
    wheels_discs: Mapped[Optional[str]]
    safety_equip: Mapped[Optional[str]]
    lights: Mapped[Optional[str]]
    comfort_equip: Mapped[Optional[str]]

    # Miscellaneous equpment
    miscell_equip: Mapped[Optional[str]]

    # Miscellaneous information
    miscell_info: Mapped[Optional[str]]
    number_of_seats: Mapped[Optional[str]]
    number_of_doors: Mapped[Optional[str]]
    empty_weight: Mapped[Optional[str]]
    max_weight: Mapped[Optional[str]]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


    __mapper_args__ = {
        'polymorphic_identity': 'vehicle',
        'concrete': True
    }


class Trucks(Vehicle):
    __tablename__ = 'trucks'
    __mapper_args__ = {
        'polymorphic_identity': 'trucks',
        'concrete': True
    }

    # user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    # user: Mapped["User"] = relationship(back_populates='trucks')

    user_vehicle_id: Mapped[int] = mapped_column(ForeignKey('users_vehicles.vehicle_id'))
    user_vehicle: Mapped["UserVehicle"] = relationship(back_populates='vehicle')

class ElectroCars(Vehicle):
    __tablename__ = "electro_cars"
    __mapper_args__ = {
        'polymorphic_identity': 'electro_cars',
        'concrete': True
    }

    hybrid: Mapped[bool] = mapped_column(Boolean, nullable=False)
    battery_capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    # user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    # user: Mapped["User"] = relationship(back_populates='electro_cars')

    user_vehicle_id: Mapped[int] = mapped_column(ForeignKey('users_vehicles.vehicle_id'))
    user_vehicle: Mapped["UserVehicle"] = relationship(back_populates='vehicle')

class Motorcycles(Vehicle):
    __tablename__ = 'motorcycles'
    __mapper_args__ = {
        'polymorphic_identity': 'motorcycles',
        'concrete': True
    }
    #
    # user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    # user: Mapped["User"] = relationship(back_populates='motorcycles')

    user_vehicle_id: Mapped[int] = mapped_column(ForeignKey('users_vehicles.vehicle_id'))
    user_vehicle: Mapped["UserVehicle"] = relationship(back_populates='vehicle')

class MotorCars(Vehicle):
    __tablename__ = "motorcars"
    __mapper_args__ = {
        'polymorphic_identity': 'motorcars',
        'concrete': True
    }

    # user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    # user: Mapped["User"] = relationship(back_populates='motorcars')

    user_vehicle_id: Mapped[int] = mapped_column(ForeignKey('users_vehicles.vehicle_id'))
    user_vehicle: Mapped["UserVehicle"] = relationship(back_populates='vehicle')
    
def create():
    engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)
    Base.metadata.create_all(engine)

create()