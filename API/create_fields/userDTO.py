from typing import Dict, Union

from API.Validators.user_input.gender_valid import gender_validator_func
from API.Validators.user_input.phone_number_valid import phone_number_validator_func
from API.Validators.user_input.email_valid import email_validator_func
from API.Validators.user_input.name_valid import name_validator_func
from API.Validators.user_input.username_valid import username_validate_func
from datetime import datetime

from pydantic import BaseModel, field_validator, Field
from addressDTO import UserAddressDTO


class UserAddDTO(BaseModel):
    """Represents a user's data transfer object. This class is
    used as an argument for the sqlalchemy model.

    Attributes:
        username: (str): The unique username of the user.
        first_name: (str): The first name of the user.
        last_name: (str): The last name of the user.
        email_address: (str): The unique email address of the user.
        main_phone_number: (str): The unique phone number of the user.
        additional_phone_number: (str): The additional phone number of the user (Optional).
        gender: (str): The gender of the user.
        address_id: (int): The address id of the user.

    Methods:
        key_args(): Returns the key arguments from the model.

    Class methods validators:
        validate_username(cls, username: str)
        validate_name(cls, first/last name: str)
        validate_email_address(cls, address: str)
        validate_phone_number(cls, number: str)
        validate_gender(cls, gender: str)
    """
    username: str
    first_name: str
    last_name: str
    email_address: str
    main_phone_number: str
    additional_phone_number: Union[str, None, Field(validate_default=True)] = None
    gender: str
    address_id: int

    @field_validator('username')
    @classmethod
    def validate_username(cls, username: str) -> str:
        """Validates the username.

        :return: The username (str).
        """
        return username_validate_func(username)

    @field_validator('first_name', 'last_name')
    @classmethod
    def validate_name(cls, name: str) -> str:
        """Validates the name.

        :return: The name (str).
        """
        return name_validator_func(name)

    @field_validator('email_address')
    @classmethod
    def validate_email_address(cls, address: str) -> str:
        """Validates the email address.

        :return: The email address (str).
        """
        return email_validator_func(address)



    @field_validator('main_phone_number')
    @classmethod
    def validate_phone_number(cls, number: str) -> str:
        """Validates the phone number.

        :return: The phone number (str).
        """
        return phone_number_validator_func(number)

    @field_validator('additional_phone_number')
    @classmethod
    def validate_phone_number(
            cls, number: Union[str, None]) -> Union[str, None]:
        """Validates the phone number.

        :return: The phone number (str).
        """
        if number is None:
            return None
        return phone_number_validator_func(number)

    @field_validator('gender')
    @classmethod
    def validate_gender(cls, gender: str) -> str:
        """Validates the gender.

        :return: The gender (str).
        """
        return gender_validator_func(gender)

    def key_args(self) -> Dict[str, str]:
        """
        Returns the key arguments from the model.

        Returns:
            Dict: A dictionary containing the key arguments.
        """
        return self.model_dump()

class UserDTO(UserAddDTO):
    """Represents a user class from the sqlalchemy model.

    Attributes:
        id: (int): The primary key for the user.
        username: (str): The unique username of the user.
        first_name: (str): The first name of the user.
        last_name: (str): The last name of the user.
        email_address: (str): The unique email address of the user.
        main_phone_number: (str): The unique phone number of the user.
        additional_phone_number: (str): The additional phone number of the user (Optional).
        gender: (str): The gender of the user.
        address_id: (int): The address id of the user.

    Methods:
        Inherited methods:
            key_args(): Returns the key arguments from the model as a dictionary.

    Class methods validators:
        validate_username(cls, username: str)
        validate_name(cls, first/last name: str)
        validate_email_address(cls, address: str)
        validate_phone_number(cls, number: str)
        validate_gender(cls, gender: str)
    """

    id: int
    registered_at: datetime
    updated_at: datetime


class UserRelationDTO(UserDTO):
    """Represents a relational user class joined with the address table.

    Attributes:
        id: (int): The primary key for the user.
        username: (str): The unique username of the user.
        first_name: (str): The first name of the user.
        last_name: (str): The last name of the user.
        email_address: (str): The unique email address of the user.
        main_phone_number: (str): The unique phone number of the user.
        additional_phone_number: (str): The additional phone number of the user (Optional).
        gender: (str): The gender of the user.
        address_id: (int): The address id of the user.
        address: (UserAddressDTO): The address of the user.

    Methods:
        Inherited methods:
            key_args(): Returns the key arguments from the model as a dictionary.

    Class methods validators:
        validate_username(cls, username: str)
        validate_name(cls, first/last name: str)
        validate_email_address(cls, address: str)
        validate_phone_number(cls, number: str)
    """

    address: "UserAddressDTO"
    # advertisements: List["AdvertisementDTO"]
    # sales_records: List["SalesRecords"]
