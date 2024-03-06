from typing import Callable, Optional
from string import punctuation, digits


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


def old_name_validator_func(name: str, echo: Optional[bool] = False) -> str:
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
                raise ValueError("Name must be maximum 20 characters")
            if any(p in name for p in punctuation):
                raise ValueError("Name must not contain punctuation")
            if any(p in name for p in digits):
                raise ValueError("Name must not contain digits")

            if echo:
                print('\n\033[1;32;40mName has been saved, validation is successful\033[0m\n')

            return name
        except ValueError as err:
            print(f"\n\033[1;31;40m{err}\033[0m\n")
            name = input('Please enter your name again: ')


def name_validator_func(name: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the first name or last name.

    Args:
        name (str): The first or last name to be validated.

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
            if len(name) > 20:
                raise ValueError("Name must be maximum 20 characters")
            if any(p in name for p in punctuation):
                raise ValueError("Name must not contain punctuation")
            if any(p in name for p in digits):
                raise ValueError("Name must not contain digits")

            if echo:
                print('\n\033[1;32;40mName has been saved, validation is successful\033[0m\n')

            return name
        except ValueError as error:
            print("\n\033[1;31;40mError in first/last name validation, please try again\033[0m\n")
            print("\n\033[1;31;40mError: ", error, "\033[0m\n")

            name = input('Please enter your name again: ')

def name_validator_func_perf(name: str) -> bool:
    # TODO: Docstring
    if not isinstance(name, str):
        return False
    if not name:
        return False
    if len(name) > 20:
        return False
    if any(p in name for p in punctuation):
        return False
    if any(p in name for p in digits):
        return False
    return True
