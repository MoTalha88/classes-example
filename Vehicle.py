class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    def display_info(self):
        """Abstract method to display vehicle info."""
        return f"{self._brand} {self._model} ({self._year})"
    
    def honk(self):
        """A general honk sound for all vehicles."""
        return "Beep beep!"
    
    def fuel_up(self):
        """Simulates fueling the vehicle."""
        return "Full tank"

    def windshield_fluid(self):
        return "Windshield fluid empty."
    
    def brake(self):
        """Simulates braking."""
        return "Braking the vehicle."
    
    def mileage(self):
        """Provides general information about mileage."""
        return "High mileage!"
