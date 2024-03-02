import re
from typing import Callable, Optional


class InvalidEmailError(Exception):
    """Custom exception raised when an email address is invalid"""
    pass


def is_valid_email(email: str) -> bool:
    """
       Check if the input string is a valid email address.
       Args:
           email (str): The input email address to be validated.
       Returns:
           bool: True if the email address is valid, False otherwise.
       """
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
    return bool(match)


def email_validator_decorator(
        func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the email address provided
    to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    def wrapper(address: str) -> str:
        """
        Wrapper function that validates the email address before calling the input function.

        Args:
            email address (str): The name to be validated.

        Returns:
            str: The validated email address.

        The function continues to prompt the user until a valid email
        address is provided.
        """
        while True:
            try:
                if not address or not isinstance(address, str):
                    raise ValueError
                if not is_valid_email(address):
                    raise InvalidEmailError
                return func(address)
            except (ValueError, AttributeError, InvalidEmailError):
                print("Error in email address validation, please try again")
                address = input('Please enter your email address: ')

    return wrapper


def email_validator_func(address: str, echo: Optional[bool] = False) -> str:
    """
        Function that validates the email address.

        Args:
            email address (str): The email address to be validated.

            echo (bool, optional): Whether to print the validation result. Defaults to False.

        Returns:
            str: The validated email address.

        The function continues to prompt the user until a valid email address is provided.
        """
    while True:
        try:
            if not address or not isinstance(address, str):
                raise ValueError
            if not is_valid_email(address):
                raise InvalidEmailError
            if echo:
                print('\n\033[1;32;40mEmail address has been saved, validation is successful\033[0m\n')
            return address
        except (ValueError, AttributeError, InvalidEmailError):
            print("\n\033[1;31;40mError in email address validation, please try again\033[0m\n")
            address = input('Please enter your email address: ')

# @email_validator_decorator
# def validate_email_address(address):
#     return address
#
# Test the decorated function
