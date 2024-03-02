def __init__(self,
             fuel: Mapped[str], power_output: Mapped[int],
             gearbox: Mapped[str], mileage: Mapped[int],
             used: Mapped[bool], color: Mapped[str],
             description: Mapped[Optional[str]],
             primary_registration: Mapped[datetime],
             body_type: Mapped[str], wheel_drive: Mapped[str],
             interior: Mapped[str],
             audio_video_system: Mapped[str],
             wheels_discs: Mapped[str],
             safety_equp: Mapped[str],
             lights: Mapped[str],
             comfort_equip: Mapped[str],
             miscell_equip: Mapped[str],
             miscell_info: Mapped[str],
             number_of_seats: Mapped[int],
             number_of_doors: Mapped[int],
             empty_weight: Mapped[int],
             max_weight: Mapped[int],
             manufactured_date: Mapped[datetime],
             engine_volume: Mapped[float],
             average_consump: Mapped[float],
             vin_number: Mapped[str]) -> None:
    self.maker, self.model = validate_maker()
    self.price = validate_price()
    self.condition = condition()
    self.fuel = fuel_type()
    self.power_output = power_output
    self.gearbox = gearbox
    self.mileage = mileage
    self.used = used
    self.color = color
    self.description = description
    self.primary_registration = primary_registration
    self.body_type = body_type
    self.wheel_drive = wheel_drive
    self.interior = interior
    self.audio_video_system = audio_video_system
    self.wheels_discs = wheels_discs
    self.safety_equp = safety_equp
    self.lights = lights



    def __init__(self,
                 address: Mapped[str],
                 city: Mapped[str],
                 state: Mapped[str],
                 zip_code: Mapped[str],
                 country: Mapped[str]) -> None:
        """
        Initialize the address with the provided details.
        Args:
        address (str): The address of the user.
        city (str): The city of the user.
        state (str): The state of the user.
        zip_code (str): The zip code of the user.
        country (str): The country of the user.
        Returns:
        None
        """
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country