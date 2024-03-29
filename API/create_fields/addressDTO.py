from API.Validators.address_input.address_valid import address_validator_func
from API.Validators.address_input.state_valid import state_validator_func
from API.Validators.address_input.zip_code_valid import zip_code_validator_func
from typing import Dict
from datetime import datetime

from pydantic import BaseModel, field_validator


class UserAddressAddDTO(BaseModel):
    """Represents user's address class as an argument for
    the sqlalchemy model.

    Attributes:
        address: (str): The address of the user.
        address_hash: (str): The address hash of the user.
        city: (str): The city of the user.
        state: (str): The state of the user.
        zip_code: (str): The zip code of the user.
        country: (str): The country of the user.

        Methods:
            key_args(): Returns the key arguments from the model.

        Class method validators:
            validate_address(cls, address: str)
            validate_state(cls, state: str)
            validate_zip_code(cls, zip_code: str)
        """
    address: str
    address_hash: str
    city: str
    state: str
    zip_code: str
    country: str

    @field_validator('address')
    @classmethod
    def validate_address(cls, address: str) -> str:
        """Validates the address of the user.

        :return: The address of the user (str).
        """
        return address_validator_func(address)

    @field_validator('state')
    @classmethod
    def validate_state(cls, state: str) -> str:
        """Validates the state of the user.

        :return: The state of the user (str).
        """
        return state_validator_func(state)

    @field_validator('zip_code')
    @classmethod
    def validate_zip_code(cls, zip_code: str) -> str:
        """Validates the zip code of the user.

        :return: The zip code of the user (str).
        """
        return zip_code_validator_func(zip_code)

    def key_args(self) -> Dict[str, str]:
        """
        Returns the key arguments from the model.

        Returns:
            Dict: A dictionary containing the key arguments.
        """
        return self.model_dump()

class UserAddressDTO(UserAddressAddDTO):
    """Represents a user class from the sqlalchemy model.

    Attributes:
        address_id: (int): The primary key for the address.
        address: (str): The address of the user.
        address_hash: (str): The address hash of the user.
        city: (str): The city of the user.
        state: (str): The state of the user.
        zip_code: (str): The zip code of the user.
        country: (str): The country of the user.
        created_at: (datetime): The creation timestamp.
        updated_at: (datetime): The last update timestamp.

    Methods:
        Inherited methods:
            key_args(): Returns the key arguments from the model as a dictionary.

    Class method validators:
        validate_address(cls, address: str)
        validate_state(cls, state: str)
        validate_zip_code(cls, zip_code: str)
    """

    address_id: int
    created_at: datetime
    updated_at: datetime