from typing import Callable, Optional


def gender_validator_decorator(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the gender provided to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    def wrapper(gender: str) -> str:
        """
        Wrapper function that validates the gender before calling the input function.

        Args:
            gender (str): The gender to be validated.

        Returns:
            str: The validated gender.

        The function continues to prompt the user until a valid gender is provided.
        """
        while True:
            try:
                if not isinstance(gender, str):
                    raise ValueError
                if not gender:
                    raise ValueError
                if gender not in ['male', 'female', 'other', 'unknown']:
                    raise ValueError
                return func(gender)
            except (ValueError, AttributeError):
                print("Error in gender validation, please try again")
                print("Choose from: male, female, other, unknown")
                gender = input('Please enter your gender: ')

    return wrapper


def gender_validator_func(gender: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the gender.

    Args:
        gender (str): The gender to be validated.

        echo (bool, optional): Whether to print the validation result. Defaults to False.

    Returns:
        str: The validated gender.

    The function continues to prompt the user until a valid gender is provided.
    """
    while True:
        try:
            if not isinstance(gender, str):
                raise ValueError
            if not gender:
                raise ValueError
            if gender not in ['male', 'female', 'other', 'unknown']:
                raise ValueError
            if echo:
                print("\n\033[1;32;40mGender has been saved, validation is successful\033[0m\n")
            return gender
        except (ValueError, AttributeError) as error:
            print("\n\033[1;31;40mError in gender validation, please try again\033[0m\n")
            print("\n\033[1;31;40mError: ", error, "\033[0m\n")
            print("Choose from: male, female, other, unknown")

            gender = input('Please enter your gender: ')

def gender_validator_func_perf(gender: str) -> bool:
    # TODO: Docstring
    if not isinstance(gender, str):
        return False
    if not gender:
        return False
    if gender not in ['male', 'female', 'other', 'unknown']:
        return False
    return True