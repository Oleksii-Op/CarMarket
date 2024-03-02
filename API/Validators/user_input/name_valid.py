from typing import Callable, Optional


def name_validator_decorator(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the name provided to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    def wrapper(name: str) -> str:
        """
        Wrapper function that validates the name before calling the input function.

        Args:
            name (str): The name to be validated.

        Returns:
            str: The validated name.

        The function continues to prompt the user until a valid name
        is provided.
        """
        while True:
            try:
                if not isinstance(name, str):
                    raise ValueError("Name must be a string")
                if not name:
                    raise ValueError("Name cannot be empty")
                if len(name) > 40:
                    raise ValueError("Name must be maximum 40 characters")
                return func(name)
            except ValueError as err:
                print(err)
                name = input('Please enter your name again: ')

    return wrapper


def name_validator_func(name: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the name.

    Args:
        name (str): The name to be validated.

        echo (bool, optional): Whether to print the validation result. Defaults to False.

    Returns:
        str: The validated name.

    The function continues to prompt the user until a valid name is provided.
    """
    while True:
        try:
            if not isinstance(name, str):
                raise ValueError("Name must be a string")
            if not name:
                raise ValueError("Name cannot be empty")
            if len(name) > 40:
                raise ValueError("Name must be maximum 40 characters")
            if echo:
                print('\n\033[1;32;40mName has been saved, validation is successful\033[0m\n')
            return name
        except ValueError as err:
            print(f"\n\033[1;31;40m{err}\033[0m\n")
            name = input('Please enter your name again: ')


# Usage example
# @name_validator_decorator
# def process_name(name: str) -> str:
#     """
#     Example function that requires a validated name.
#     """
#     return f"Hello, {name}!"
#
#
# # Test the decorated function
# processed_name = process_name("John Doe")
# print(processed_name)
