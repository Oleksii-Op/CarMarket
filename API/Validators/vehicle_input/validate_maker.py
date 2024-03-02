import json

def validate_maker(maker: str):
    with open('Validators/vehicle_input/Data/cars.json') as cars:
        data = json.load(cars)

        for id, brand in enumerate(data ,start=1):
            print(f"{id}. {brand['brand']}")





validate_maker('BMW')