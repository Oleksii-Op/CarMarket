from typing import Callable, Optional


def address_validator_decorator(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the address provided to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    def wrapper(address: str) -> str:
        """
        Wrapper function that validates the address before calling the input function.

        Args:
            address (str): The address to be validated.

        Returns:
            str: The validated address.

        The function continues to prompt the user until a valid address
        is provided.
        """
        while True:
            try:
                if not isinstance(address, str):
                    raise ValueError
                if not address:
                    raise ValueError
                if len(address) > 255:
                    raise ValueError
                return func(address)
            except (ValueError, AttributeError):
                print("Error in address validation, please try again")
                address = input('Please enter your address: ')

    return wrapper


def address_validator_func(address: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the address.

    Args:
        address (str): The address to be validated.

        echo (bool, Optional): Whether to print the success message. Defaults to False.

    Returns:
        str: The validated address.

    The function continues to prompt the user until a valid address is provided.
    """
    while True:
        try:
            if not isinstance(address, str):
                raise ValueError
            if not address:
                raise ValueError
            if len(address) > 255:
                raise ValueError
            if echo:
                print("Address has been saved, validation is successful")
            return address
        except (ValueError, AttributeError):
            print("Error in address validation, please try again")
            address = input('Please enter your address: ')
