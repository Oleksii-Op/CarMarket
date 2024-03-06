def validate_price() -> int:
    """
        This function validates the input price in
        euro and returns the price if it's a positive integer.
        """
    while True:
        try:
            price = int(input('Please enter your price in euro: '))
            if price < 0:
                raise ValueError
            return price
        except ValueError:
            print("Error in price validation, please try again")
