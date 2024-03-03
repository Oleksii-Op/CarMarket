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
        try:
            if not isinstance(zip_code, str):
                raise ValueError("Zip code must be a string")
            if not zip_code:
                raise ValueError("Zip code cannot be empty")
            if len(zip_code) != 5 or not zip_code.isdigit():
                raise ValueError("Zip code must be a 5-digit number")

            if echo:
                print("\n\033[1;32;40mZip code has been saved, validation is successful\033[0m\n")

            return zip_code
        except ValueError as error:
            print("\n\033[1;31;40mError in zip code validation, please try again\033[0m\n")
            print("\n\033[1;31;40mError: ", error, "\033[0m\n")
            zip_code = input('Please enter valid zip code: ')
