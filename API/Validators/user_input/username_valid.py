from typing import Callable, Optional


def username_validate_decorator(func: Callable[[str], str]) -> Callable[[str], str]:
    """
        Decorator function to validate the username provided to the decorated function.

        Args:
            func (Callable): The function to be decorated.

        Returns:
            Callable: The decorated function.
        """

    def wrapper(username: str) -> str:
        """
        Wrapper function that validates the username before calling the input function.

        Args:
            username (str): The username to be validated.


        Returns:
            str: The validated username.

        The function continues to prompt the user until a valid username
        is provided.
        """
        while True:
            try:
                if len(username) < 6:
                    raise ValueError("Username must be at least 6 characters")
                elif len(username) > 20:
                    raise ValueError("Username must be maximum 20 characters")
                return func(username)
            except ValueError:
                print("Error in username validation, please try again")
                username = input('Please enter your username: ')

    return wrapper


def username_validate_func(username: str, echo: Optional[bool] = False) -> str:
    """
        Function that validates the username.

        Args:
            username (str): The username to be validated.

            echo (bool, optional): Whether to print the validation result. Defaults to False.

        Returns:
            str: The validated username.

        The function continues to prompt the user until a valid username
        is provided.
        """
    while True:
        try:
            if len(username) < 6:
                raise ValueError("Username must be at least 6 characters")
            elif len(username) > 20:
                raise ValueError("Username must be maximum 20 characters")
            if echo:
                print("\n\033[1;32;40mUsername has been saved, validation is successful\033[0m\n")
            return username
        except ValueError:
            print("\n\033[1;31;40mError in username validation, please try again\033[0m\n")
            username = input('Please enter your username: ')