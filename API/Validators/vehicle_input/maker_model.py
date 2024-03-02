import json
from typing import Tuple, Union


def validate_maker() -> Union[str, Tuple[str, str]]:
    """
       Validates the user input for choosing a car brand and model from the
       provided JSON data. Returns the chosen brand and model as a tuple, or
       just the chosen brand if 'Exit' is entered as the model choice.
       Returns:
           str | Tuple[str, str]: The chosen brand and model, or just the chosen
           brand if 'Exit' is entered as the model choice to exit.
       """
    with open('Data/cars.json', encoding='utf-8') as cars:
        data = json.load(cars)

        brands_dict = {brand['brand']: brand.get('models', [])
                       for brand in data}

        print("Available brands:")
        for index, brand in enumerate(brands_dict.keys()):
            print(f"{index}. {brand}")

        maker = input("\nPlease choose one of the following"
                      " brands (Type in name as shown above in the list): ")
        while maker not in brands_dict.keys():
            print("\nWrong input. Try again.")
            maker = input("Your choice (Type in exactly name as shown): ")

        print(f"Available models for {maker}:")
        for index, model in enumerate(brands_dict[maker]):
            # if model.get('title', None) is None:
            print(f"{index}. {model.get('title', 'Unknown')}")

        print("\nIf no model is available, please type 'Exit'")
        model_choice = input(
            "Please choose one of the following models "
            "(Type in name as shown above in the list): ")

        while model_choice not in [model.get('title', '')
                                   for model in brands_dict[maker]]:
            if model_choice.lower() == 'exit':
                return maker, "Unknown"
            print("\nWrong input. Try again.")
            model_choice = input(
                "Your choice (Type in exactly name as shown): ")

        return maker, model_choice