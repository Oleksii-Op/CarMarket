from typing import Optional, List
from datetime import datetime
from sqlalchemy import (create_engine, Integer, String, DateTime,
                        ForeignKey, Float, Boolean, UniqueConstraint,
                        CheckConstraint, Index)

from sqlalchemy.orm import (relationship, Mapped,
                            validates, mapped_column, DeclarativeBase)

from aux_annotations.annotations import created_at, updated_at
from API.Validators.user_input.gender_valid import gender_validator_func
from Validators.user_input.phone_number_valid import phone_number_validator_func
from Validators.user_input.email_valid import email_validator_func
from Validators.user_input.name_valid import name_validator_func
from Validators.user_input.username_valid import username_validate_func
from Validators.address_input.address_valid import address_validator_func
from Validators.address_input.state_valid import state_validator_func
from Validators.address_input.zip_code_valid import zip_code_validator_func
from conn_to_database import select_database
from config import settings
import enum


# str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""

    # type_annotations_map = {
    #     str_256: String(256)
    # }
    def __repr__(self):
        # cols = [repr(getattr(self, c.name)) for c in self.__table__.columns]
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self, col)}")
            return f"{self.__class__.__name__} {",".join(cols)}"


class Address(Base):
    """Model representing address details.

        Attributes:
            address_id (int): The primary key for the address.
            address (str): The street address.
            city (str): The city.
            state (str): The state.
            zip_code (str): The postal code.
            country (str): The country.
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The last update timestamp.
        """

    __tablename__ = 'addresses'

    address_id: Mapped[int] = mapped_column(primary_key=True)
    address_hash: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(40), nullable=False)
    state: Mapped[str] = mapped_column(String(40), nullable=True)
    zip_code: Mapped[str] = mapped_column(String(5), nullable=False)
    country: Mapped[str] = mapped_column(String(40), nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped["User"] = relationship(back_populates='addresses')

    def __repr__(self) -> str:
        return (f"Address(address_id={self.address_id},"
                f" address={self.address}, city={self.city},"
                f" state={self.state}, zip_code={self.zip_code},"
                f" country={self.country})")


class User(Base):
    """Model representing user details.

        Attributes:
            user_id (int): The primary key for the user.
            address_id (int): The foreign key referencing the address.
            username (str): The username.
            user_property (str): The user property.
            first_name (str): The first name.
            last_name (str): The last name.
            email_address (str): The email address.
            main_phone_number (str): The main phone number.
            additional_phone_number (str): The additional phone number.
            gender (str): The gender.
            registered_at (datetime): The registration timestamp.
            updated_at (datetime): The last update timestamp.
            address (Address): The related address.
            advertisements (list of Advertisement): The related advertisements.
            sales_records (list of SalesRecords): The related sales records.
        """

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

    address_id: Mapped["Address"] = mapped_column(ForeignKey('addresses.address_id'), unique=True)
    addresses: Mapped["Address"] = relationship(
        back_populates='user', uselist=False)

    advertisements: Mapped[List["Advertisement"]] = relationship(
        back_populates='user')

    # : Mapped[List["SalesRecords"]] = relationship(
    #     back_populates='user')

    sales_as_seller: Mapped["SalesRecords"] = relationship(
        back_populates="seller", foreign_keys="[SalesRecord.seller_id]"
    )

    sales_as_buyer: Mapped["SalesRecords"] = relationship(
        back_populates="buyer", foreign_keys="[SalesRecords.buyer_id]"
    )

    __table_args__ = (
        UniqueConstraint('address_id'),
        # Index('title_index', 'title'),
        # CheckConstraint('gender IN ("male", "female", "other", "unknown")'),
        # CheckConstraint('user_property IN ("r", "b")'),
    )

    def __repr__(self) -> str:
        return (f"User(user_id={self.user_id}, username={self.username}, "
                f"user_property={self.user_property}, first_name={self.first_name}, "
                f"last_name={self.last_name}, email_address={self.email_address}, "
                f"main_phone_number={self.main_phone_number}, "
                f"additional_phone_number={self.additional_phone_number}, "
                f"gender={self.gender}, registered_at={self.registered_at}, "
                f"updated_at={self.updated_at})")


class SalesRecords(Base):
    """Model representing sales records.

        Attributes:
            record_id (int): The primary key for the sales record.
            sale_date (datetime): The sale date.
            seller_id (int): The seller's user ID.
            buyer_id (int): The buyer's user ID.
            seller (User): The related user.
            buyer (User): The related
            advertisement (Advertisement): The related advertisement.
        """

    __tablename__ = 'sales_records'

    record_id: Mapped[int] = mapped_column(primary_key=True)
    sale_date: Mapped[created_at]

    seller_id: Mapped["User"] = mapped_column(ForeignKey('users.user_id'))
    buyer_id: Mapped[Optional["User"]] = mapped_column(ForeignKey('users.user_id'))
    ad_id: Mapped[int] = mapped_column(ForeignKey('advertisements.ad_id'))

    seller: Mapped["User"] = relationship("User", foreign_keys=seller_id, uselist=False)
    buyer: Mapped["User"] = relationship("User", foreign_keys=buyer_id, uselist=False)

    advertisement: Mapped["Advertisement"] = relationship(back_populates='sales_records')

    def __repr__(self) -> str:
        return (f"SalesRecords(record_id={self.record_id},"
                f" sale_date={self.sale_date},"
                f" seller_id={self.seller_id},"
                f" buyer_id={self.buyer_id},"
                f" ad_id={self.ad_id})")


class Category(Base):
    """Model representing vehicle's categories.

        Attributes:
            category_id (int): The primary key for the category.
            category_name (str): The category name.
            description (str): The category description.
        """

    __tablename__ = 'categories'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)

    vehicles: Mapped[List["Vehicle"]] = relationship(back_populates='category')

    def __repr__(self) -> str:
        return (f"Category(category_id={self.category_id},"
                f" category_name={self.category_name},"
                f" description={self.description})")


class Advertisement(Base):
    """Model representing advertisements.

        Attributes:
            ad_id (int): The primary key for the advertisement.
            discontinued (bool): Indicates if the advertisement is discontinued.
            price (int): The price of the advertisement.
            condition_type (str): The condition type of the advertisement.
            fuel (str): The fuel type.
            power_output (int): The power output.
            gearbox (str): The gearbox type.
            mileage (int): The mileage.
            used (bool): Indicates if the advertisement is used.
            color (str): The color.
            primary_registration (datetime): The primary registration date.
            manufactured_date (datetime): The manufactured date.
            engine_volume (float): The engine volume.
            average_consumption (float): The average consumption.
            vin_number (str): The VIN number.
            body_type (str, optional): The body type.
            wheel_drive (str, optional): The wheel drive type.
            description (str, optional): The description.
            interior (str, optional): The interior.
            audio_video_system (str, optional): The audio/video system.
            wheels_discs (str, optional): The wheels discs.
            safety_equip (str, optional): The safety equipment.
            lights (str, optional): The lights.
            comfort_equip (str, optional): The comfort equipment.
            miscell_equip (str, optional): The miscellaneous equipment.
            miscell_info (str, optional): The miscellaneous information.
            number_of_seats (str, optional): The number of seats.
            number_of_doors (str, optional): The number of doors.
            empty_weight (str, optional): The empty weight.
            max_weight (str, optional): The maximum weight.
            created_at (datetime): The creation timestamp.
            updated_at (datetime): The last update timestamp.
            user (User): The related user.
            vehicle (Vehicle): The related vehicle.
        """

    __tablename__ = 'advertisements'

    ad_id: Mapped[int] = mapped_column(primary_key=True)

    discontinued: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
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

    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped["User"] = relationship(back_populates='advertisements')

    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicles.vehicle_id'))
    vehicle: Mapped["Vehicle"] = relationship(back_populates='advertisements', uselist=False)

    sales_record: Mapped["SalesRecords"] = relationship(
        back_populates="advertisements"
    )

    # __table_args__ = (
    #     CheckConstraint(price > 0),
    #     CheckConstraint(mileage > 0),
    #     CheckConstraint(power_output > 0),
    #     CheckConstraint(engine_volume > 0),
    #     CheckConstraint(average_consumption > 0),
    # )

    def __repr__(self) -> str:
        return (f"Advertisement(ad_id={self.ad_id},"
                f" discontinued={self.discontinued},"
                f" price={self.price},"
                f" condition_type={self.condition_type},"
                f" fuel={self.fuel},"
                f" power_output={self.power_output},"
                f" gearbox={self.gearbox},"
                f" mileage={self.mileage},"
                f" used={self.used},"
                f" color={self.color},"
                f" primary_registration={self.primary_registration},"
                f" manufactured_date={self.manufactured_date},"
                f" engine_volume={self.engine_volume},"
                f" average_consumption={self.average_consumption},"
                f" vin_number={self.vin_number},"
                f" body_type={self.body_type},"
                f" wheel_drive={self.wheel_drive},"
                f" description={self.description},"
                f" interior={self.interior},"
                f" audio_video_system={self.audio_video_system},"
                f" wheels_discs={self.wheels_discs},"
                f" safety_equip={self.safety_equip},"
                f" lights={self.lights},"
                f" comfort_equip={self.comfort_equip},"
                f" miscell_equip={self.miscell_equip},"
                f" miscell_info={self.miscell_info},"
                f" number_of_seats={self.number_of_seats},"
                f" number_of_doors={self.number_of_doors},"
                f" empty_weight={self.empty_weight},"
                f" max_weight={self.max_weight},"
                f" created_at={self.created_at},"
                f" updated_at={self.updated_at})")


class Vehicle(Base):
    """Model representing vehicles.

       Attributes:
           vehicle_id (int): The primary key for the vehicle.
           maker (str): The maker of the vehicle.
           model (str): The model of the vehicle.
           category_id (int): The foreign key referencing the category.
           category (Category): The related category.
       """

    __tablename__ = 'vehicles'

    vehicle_id: Mapped[int] = mapped_column(primary_key=True)

    maker: Mapped[str] = mapped_column(String(20), nullable=False)
    model: Mapped[str] = mapped_column(String(20), nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.category_id'))
    category: Mapped["Category"] = relationship(back_populates='vehicles', uselist=False)

    advertisements: Mapped["Advertisement"] = relationship(back_populates='vehicles')

    def __repr__(self) -> str:
        return (f"Vehicle(vehicle_id={self.vehicle_id},"
                f" maker={self.maker},"
                f" model={self.model},"
                f" category_id={self.category_id})")


class AdvertisementReplied(Base):
    pass
    # __tablename__ = 'advertisement_replied'


if __name__ == "__main__":
    # By default, the engine is created using the environment variables
    # from .env file.
    # use select_database() to change the engine to use a different database
    # example: engine = create_engine(select_database(), echo=True)
    engine = create_engine(settings.DATABASE_URL_psycopg, echo=True)
    Base.metadata.create_all(engine)


class UserType(enum.Enum):
    regular_user = 'regular_user'
    business_user = 'business_user'
