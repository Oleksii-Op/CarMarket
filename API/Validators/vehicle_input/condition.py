def condition() -> bool:
    """
    This function validates the input used condition
    and returns the used condition if it's a string.
    """
    while True:
        try:
            condition = input('Please enter your used condition: ')
            if condition not in ['New', 'Used']:
                raise ValueError
            return True if condition == 'Used' else False
        except ValueError:
            print("Error in condition validation, please try again")
