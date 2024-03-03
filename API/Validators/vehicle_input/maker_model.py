import json
from typing import Tuple, Union


def input_maker_model() -> Union[str, Tuple[str, str]]:
    """
       Prompt the user to choose a specific car brand and model.
       Forbids the user from typing non-existing car brands and models.
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
        for maker_index, brand in enumerate(brands_dict.keys()):
            print(f"{maker_index}. {brand}")

        maker = input("\nPlease choose one of the following"
                      " brands (Type in name as shown above in the list): ")

        while maker not in brands_dict.keys():
            print("\nWrong input. Try again.")
            maker = input("Your choice (Type in exactly name as shown): ")

        print(f"Available models for {maker}:")

        models = brands_dict.get(maker, [])
        model_names = [model.get('title', 'Unknown') for model in models]
        for model_index, model in enumerate(models):
            print(f"{model_index}. {model.get('title', 'Unknown')}")

        print("\nIf no model is available, please type 'Exit'")
        model_choice = input(
            "Please choose one of the following models "
            "(Type in name as shown above in the list): ")

        if model_choice.lower() == 'exit':
            return maker

        while model_choice not in model_names:
            print("\nWrong input. Try again.")
            model_choice = input(
                "Your choice (Type in exactly name as shown): ")

        model_index = [index for index, model in enumerate(models)
                       if model['title'] == model_choice]
        types = models[model_index[0]].get('types', [])

        if types:
            print(f"Available types for {model_choice}:")

            for type_index, type_model in enumerate(types):
                print(f"{type_index}. {type_model}")

            type_choice = input(
                "Please choose one of the following types "
                "(Type in name as shown above in the list): ")

            while type_choice not in list(types):
                print("\nWrong input. Try again.")
                type_choice = input(
                    "Your choice (Type in exactly name as shown): ")

            model_choice = model_choice + " " + type_choice

        return maker, model_choice

