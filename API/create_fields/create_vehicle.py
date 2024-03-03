import abc
from pydantic import BaseModel
from typing import Dict, ClassVar


class AbstractVehicle(BaseModel, abc.ABC):
    """Represents a vehicle abstract class to be inherited
    by other classes
    Attributes:
        maker (str): The manufacturer of the vehicle.
        model (str): The model of the vehicle.

    properties:
        category_id: ClassVar[int]: The category of the vehicle

    Methods:
        key_args(): Returns the key arguments from the model.
    """
    maker: str
    model: str

    @property
    @abc.abstractmethod
    def category_id(self):
        """
        Returns the category of the vehicle.

        Returns:
            Category: The category of the vehicle.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def key_args(self):
        """
        Returns the key arguments from the model.

        Returns:
            Dict: A dictionary containing the key arguments.
        """
        raise NotImplementedError


class Car(AbstractVehicle):
    """Represents a car's manufacturer and model.

    This class inherits from AbstractVehicle and extends its
    category_id property to be set to 1 by default to
    represent a motor car.

    Attributes:
        maker (str): The manufacturer of the car.
        model (str): The model of the car.

    properties:
        category_id: ClassVar[int]: The category of the car

    Methods:
        key_args(): Returns the key arguments from the model.
    """
    category_id: ClassVar[int] = 1

    def key_args(self) -> Dict:
        return self.model_dump()


class Motorcycle(AbstractVehicle):
    """Represents a motorcycle's manufacturer and model.

    This class inherits from AbstractVehicle and extends its
    category_id property to be set to 1 by default to
    represent a motorcycle.

    Attributes:
        maker (str): The manufacturer of the motorcycle.
        model (str): The model of the motorcycle.

    properties:
        category_id: ClassVar[int]: The category of the motorcycle

    Methods:
        key_args(): Returns the key arguments from the model.
        """
    category_id: ClassVar[int] = 2

    def key_args(self) -> Dict:
        return self.model_dump()


class Truck(AbstractVehicle):
    """Represents a truck's manufacturer and model.

    This class inherits from AbstractVehicle and extends its
    category_id property to be set to 1 by default to
    represent a truck.

    Attributes:
        maker (str): The manufacturer of the truck.
        model (str): The model of the truck.

    properties:
        category_id: ClassVar[int]: The category of the truck

    Methods:
        key_args(): Returns the key arguments from the model.
        """
    category_id: ClassVar[int] = 3

    def key_args(self) -> Dict:
        return self.model_dump()


class ElectroCar(AbstractVehicle):
    """Represents an electric car's manufacturer and model.

    This class inherits from AbstractVehicle and extends its
    category_id property to be set to 1 by default to
    represent an electric car.

    Attributes:
        maker (str): The manufacturer of the electric car.
        model (str): The model of the electric car.

    properties:
        category_id: ClassVar[int]: The category of the electric car

    Methods:
        key_args(): Returns the key arguments from the model.
        """
    category_id: ClassVar[int] = 4

    def key_args(self) -> Dict:
        return self.model_dump()
