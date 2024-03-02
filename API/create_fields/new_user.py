from typing import Dict

from API.Validators.user_input.gender_valid import gender_validator_func
from API.Validators.user_input.phone_number_valid import phone_number_validator_func
from API.Validators.user_input.email_valid import email_validator_func
from API.Validators.user_input.name_valid import name_validator_func
from API.Validators.user_input.username_valid import username_validate_func

from pydantic import BaseModel, field_validator


class NewUser(BaseModel):
    """Represents a new user class as an argument for
    the sqlalchemy model.

    Attributes:
        username: (str): The unique username of the user.
        name: (str): The name of the user.
        email_address: (str): The unique email address of the user.
        phone_number: (str): The unique phone number of the user.
        gender: (str): The gender of the user.

    Methods:
        key_args(): Returns the key arguments from the model.

    Class methods validators:
        validate_username(cls, username: str)
        validate_name(cls, name: str)
        validate_email_address(cls, address: str)
        validate_phone_number(cls, number: str)
        validate_gender(cls, gender: str)
    """
    username: str
    name: str
    email_address: str
    phone_number: str
    gender: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, username: str) -> str:
        """Validates the username.

        :return: The username (str).
        """
        return username_validate_func(username, echo=True)

    @field_validator('name')
    @classmethod
    def validate_name(cls, name: str) -> str:
        """Validates the name.

        :return: The name (str).
        """
        return name_validator_func(name, echo=True)

    @field_validator('email_address')
    @classmethod
    def validate_email_address(cls, address: str) -> str:
        """Validates the email address.

        :return: The email address (str).
        """
        return email_validator_func(address, echo=True)

    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, number: str) -> str:
        """Validates the phone number.

        :return: The phone number (str).
        """
        return phone_number_validator_func(number, echo=True)

    @field_validator('gender')
    @classmethod
    def validate_gender(cls, gender: str) -> str:
        """Validates the gender.

        :return: The gender (str).
        """
        return gender_validator_func(gender, echo=True)

    def key_args(self) -> Dict[str, str]:
        """
        Returns the key arguments from the model.

        Returns:
            Dict: A dictionary containing the key arguments.
        """
        return self.model_dump()

    # def __repr__(self):
    #     return (f"NewUser(username={self.username},"
    #             f"name={self.name}, email_address={self.email_address},"
    #             f"phone_number={self.phone_number}, gender={self.gender}")

    # def key_args(self):
    #     return {
    #         'username': self.username,
    #         'name': self.name,
    #         'email_address': self.email_address,
    #         'phone_number': self.phone_number,
    #         'gender': self.gender
    #     }

    # @classmethod
    # @field_validator('username')
    # def username_valid(cls, value):
    #     if any(p in value for p in string.punctuation):
    #         raise ValueError("Username must not contain punctuation")


# new_user = NewUser.model_validate({
#     'username': 'newuser',
#     'name': 'newuser',
#     'email_address': 'newuser@gmail.com',
#     'phone_number': '+3800502741543',
#     'gender': 'unknown'
# })
#
# print(new_user)
