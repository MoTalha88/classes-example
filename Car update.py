class Car(Vehicle):
    def __init__(self, brand, model, year, seats, fuel_type):
        super().__init__(brand, model, year)
        self.seats = seats  # Number of seats in the car
        self.fuel_type = fuel_type  # Type of fuel (e.g., petrol, diesel, electric)

    def display_info(self):
        """Override the parent class method for a Car."""
        return f"Car: {self._brand} {self._model} ({self._year}), Seats: {self.seats}, Fuel: {self.fuel_type}"

    def play_music(self):
        """Simulates playing music in the car."""
        return "Playing your favorite music playlist!"

    def activate_air_conditioner(self):
        """Simulates turning on the air conditioner."""
        return "Air conditioner activated. Enjoy your ride!"

    def check_fuel(self):
        """Checks the fuel type and returns a message."""
        if self.fuel_type.lower() == "electric":
            return "The car is fully charged."
        else:
            return f"Fuel type: {self.fuel_type}. Please ensure the tank is full."
