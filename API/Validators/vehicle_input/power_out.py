def power_output() -> int:
    """
    This function validates the input power output
    and returns the power output if it's a positive integer.
    """
    while True:
        try:
            power_output = int(input('Please enter your power output in kW: '))
            if power_output < 0:
                raise ValueError
            return power_output
        except ValueError:
            print("Error in power output validation, please try again")