from typing import Callable, Optional


def zip_code_validator_decorator(
        func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the zip code provided to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    def wrapper(zip_code: str) -> str:
        """
        Wrapper function that validates the zip code before calling the input function.

        Args:
            zip_code (str): The zip code to be validated.

        Returns:
            str: The validated zip code.

        The function continues to prompt the user until a valid zip code
        is provided.
        """
        while True:
            if not isinstance(zip_code, str):
                print("Error in zip code validation, please try again")
                zip_code = input('Please enter your zip code: ')
                if len(zip_code) == 5 and zip_code.isdigit():
                    break
            else:
                break
        return func(zip_code)

    return wrapper


def zip_code_validator_func(zip_code: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the zip code.

    Args:
        zip_code (str): The zip code to be validated.

        echo (bool, Optional): Whether to print the success message. Defaults to False.

    Returns:
        str: The validated zip code.

    The function continues to prompt the user until a valid zip code is provided.
    """
    while True:
        if not isinstance(zip_code, str):
            print("Error in zip code validation, please try again")
            zip_code = input('Please enter your zip code: ')
            if len(zip_code) == 5 and zip_code.isdigit():
                break
        else:
            break

    if echo:
        print("Zip code has been saved, validation is successful")

    return zip_code
