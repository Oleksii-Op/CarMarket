from typing import Callable, Optional


def state_validator_decorator(
        func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator function to validate the state provided to the decorated function.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """

    def wrapper(state: str) -> str:
        """
        Wrapper function that validates the state before calling the input function.

        Args:
            state (str): The state to be validated.

        Returns:
            str: The validated state.

        The function continues to prompt the user until a valid state
        is provided.
        """
        while True:
            try:
                if not isinstance(state, str):
                    raise ValueError
                if not state:
                    raise ValueError
                if len(state) > 40:
                    raise ValueError
                return func(state)
            except ValueError as err:
                print(err)
                state = input('Please enter your state again: ')

    return wrapper


def state_validator_func(state: str, echo: Optional[bool] = False) -> str:
    """
    Function that validates the state.

    Args:
        state (str): The state to be validated.

        echo (bool, Optional): Whether to print the success message. Defaults to False.

    Returns:
        str: The validated state.

    The function continues to prompt the user until a valid state is provided.
    """
    while True:
        try:
            if not isinstance(state, str):
                raise ValueError
            if not state:
                raise ValueError
            if len(state) > 40:
                raise ValueError
            if echo:
                print("State has been saved, validation is successful")
            return state
        except ValueError as err:
            print(err)
            state = input('Please enter your state again: ')
