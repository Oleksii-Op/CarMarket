from typing import Callable, Optional
import phonenumbers

class InvalidNumberError(Exception):
    """Custom exception raised when a phone number is invalid"""
    pass


def is_valid_number(number: str) -> bool:
    """
        Check if the given number is a valid phone number.
        Args:
            number (str): The input phone number as a string.
        Returns:
            bool: True if the number is a valid phone number, False otherwise.
        """
    p_number = phonenumbers.parse(number)
    return phonenumbers.is_possible_number(p_number)


def phone_number_validator_decorator(
        func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the phone number provided to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    def wrapper(number: str) -> str:
        """
        Wrapper function that validates the phone number before calling the input function.

        Args:
            phone number (str): The phone number to be validated.

        Returns:
            str: The validated phone number.

        The function continues to prompt the user until a valid phone number
        is provided.
        """
        while True:
            try:
                if not number or not isinstance(number, str):
                    raise ValueError
                if not is_valid_number(number):
                    raise InvalidNumberError
                return func(number)
            except (ValueError, AttributeError, InvalidNumberError):
                print("Error in phone number validation, please try again")
                number = input('Please enter your phone number: ')

    return wrapper


def phone_number_validator_func(number: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the phone number.

    Args:
        number (str): The phone number to be validated.

        echo (bool, optional): Whether to print the validation result. Defaults to False.

    Returns:
        str: The validated phone number.

    The function continues to prompt the user until a valid phone number
    is provided.
    """
    while True:
        try:
            if not number or not isinstance(number, str):
                raise ValueError
            if not is_valid_number(number):
                raise InvalidNumberError

            if echo:
                print("\n\033[1;32;40mPhone number has been saved, validation is successful\033[0m\n")

            return number
        except (ValueError, AttributeError, InvalidNumberError) as error:
            print("\n\033[1;31;40mError in phone number validation, please try again\033[0m\n")
            print("\n\033[1;31;40mError: ", error, "\033[0m\n")

            number = input('Please enter your valid phone number: ')

