from datetime import datetime
from typing import Optional, Dict
from abc import abstractmethod
from pydantic import BaseModel


class AbstractVehicle(BaseModel):
    """Represents a vehicle abstract class to be inherited
    by other classes

    Attributes:
        user_id (int): The unique ID of the user
            who created the advertisement.
        maker (str): The manufacturer of the truck.
        model (str): The model of the truck.
        price (int): The price of the truck.
        condition (str): The condition of the truck
            (e.g., after an accident, broken).
        fuel (str): The type of fuel the truck uses.
        power_output (int): The power output of the truck in kilowatts.
        gearbox (str): The type of gearbox the truck has.
        mileage (int): The mileage of the truck.
        used (bool): Indicates if the truck is used or not.
        color (str): The color of the truck.
        primary_registration (datetime): The date of primary
            registration for the truck.
        manufactured_date (datetime): The manufacturing date
            of the truck.
        engine_volume (float): The engine volume of the truck.
        average_consumption (float): The average consumption
            of fuel by the truck.
        vin_number (str): The VIN (Vehicle Identification Number)
            of the truck.
        body_type (Optional[str]): The body type of the truck
            (default is "Not provided").
        wheel_drive (Optional[str]): The type of wheel drive of the
            truck (default is "Not provided").
        interior (Optional[str]): Description of the interior of the
            truck (default is "Not provided").
        audio_video_system (Optional[str]): Details of the audio/video
            system in the truck (default is "Not provided").
        wheels_discs (Optional[str]): Information about the
            wheels/discs of the truck (default is "Not provided").
        safety_equip (Optional[str]): Safety equipment installed
            in the truck (default is "Not provided").
        lights (Optional[str]): Details of the lights in the truck
            (default is "Not provided").
        comfort_equip (Optional[str]): Comfort equipment in the truck
            (default is "Not provided").
        miscell_equip (Optional[str]): Miscellaneous equipment in the
            truck (default is "Not provided").
        miscell_info (Optional[str]): Miscellaneous information about
            the truck (default is "Not provided").
        number_of_seats (Optional[str]): Number of seats in the truck
            (default is "Not provided").
        number_of_doors (Optional[str]): Number of doors in the truck
            (default is "Not provided").
        empty_weight (Optional[str]): The empty weight of the truck
            (default is "Not provided").
        max_weight (Optional[str]): The maximum weight the truck can
            carry (default is "Not provided").

    Methods:
        key_args(): Returns the key arguments from the model.
    """
    user_id: int
    maker: str
    model: str
    price: int
    condition: str
    fuel: str
    power_output: int
    gearbox: str
    mileage: int
    used: bool
    color: str
    primary_registration: datetime

    manufactured_date: datetime
    engine_volume: float
    average_consumption: float
    vin_number: str

    body_type: Optional[str] = "Not provided"
    wheel_drive: Optional[str] = "Not provided"
    interior: Optional[str] = "Not provided"
    audio_video_system: Optional[str] = "Not provided"
    wheels_discs: Optional[str] = "Not provided"
    safety_equip: Optional[str] = "Not provided"
    lights: Optional[str] = "Not provided"
    comfort_equip: Optional[str] = "Not provided"
    miscell_equip: Optional[str] = "Not provided"
    miscell_info: Optional[str] = "Not provided"
    number_of_seats: Optional[str] = "Not provided"
    number_of_doors: Optional[str] = "Not provided"
    empty_weight: Optional[str] = "Not provided"
    max_weight: Optional[str] = "Not provided"

    @abstractmethod
    def key_args(self):
        """
        Returns the key arguments from the model.

        Returns:
            Dict: A dictionary containing the key arguments.
        """
        raise NotImplementedError


class TruckAd(AbstractVehicle):
    """Represents an advertisement for a truck.

    This class inherits from AbstractVehicle and extends it to
    represent truck advertisements.

    Attributes:
        Attributes similar to AbstractVehicle class

    Methods:
        key_args(): Returns the key arguments from the model.
    """

    def key_args(self) -> Dict:
        return self.model_dump()


class ElectroCarAd(AbstractVehicle):
    """Represents an advertisement for an electric car.

    This class inherits from AbstractVehicle and extends it to
    represent specific attributes and functionalities related
    to electric car advertisements.

    Attributes:
        Attributes similar to AbstractVehicle class
        hybrid (bool): Indicates if the car is hybrid or not.
        battery_capacity (int): The battery capacity of the car.

    Methods:
        key_args(): Returns the key arguments from the model.
       """
    hybrid: bool
    battery_capacity: int

    def key_args(self) -> Dict:
        return self.model_dump()


class MotorcycleAd(AbstractVehicle):
    """Represents an advertisement for a motorcycle.

    This class inherits from AbstractVehicle and extends it to
    represent motorcycle advertisements.

    Attributes:
        Attributes similar to AbstractVehicle class

    Methods:
        key_args(): Returns the key arguments from the model.
    """

    def key_args(self) -> Dict:
        return self.model_dump()


class MotorCarAd(AbstractVehicle):
    """Represents an advertisement for a car driven by only
     combustion engines.

    This class inherits from AbstractVehicle and extends it to
    represent motor car advertisements.

    Attributes:
        Attributes similar to AbstractVehicle class

    Methods:
        key_args(): Returns the key arguments from the model.
    """

    def key_args(self) -> Dict:
        return self.model_dump()
