def fuel_type() -> str:
    while True:
        try:
            fuel_type = input('Please enter your fuel type: ')
            if fuel_type not in ['Petrol', 'Diesel']:
                raise ValueError
            return fuel_type
        except ValueError:
            print("Error in fuel type validation, please try again")