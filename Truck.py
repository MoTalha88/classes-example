class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load

    def display_info(self):
        """Override the parent class method for a Truck."""
        return f"Truck: {self._brand} {self._model}, Max load: {self.max_load} tons ({self._year})"

    def honk(self):
        """Specific implementation for a truck."""
        return "HOOOOONK!"

    def load_cargo(self, weight):
        """
        Simulates loading cargo onto the truck.
        :param weight: Weight of the cargo in tons.
        :return: Message indicating whether the cargo was successfully loaded.
        """
        if weight <= self.max_load:
            return f"Successfully loaded {weight} tons of cargo."
        else:
            return f"Cannot load {weight} tons. Exceeds max load of {self.max_load} tons."

    def calculate_mileage(self, fuel, distance):
        """
        Calculates mileage based on fuel consumption and distance traveled.
        :param fuel: Amount of fuel consumed in liters.
        :param distance: Distance traveled in kilometers.
        :return: Mileage (km/l).
        """
        if fuel > 0:
            mileage = distance / fuel
            return f"The truck's mileage is {mileage:.2f} km/l."
        else:
            return "Fuel consumption must be greater than 0 to calculate mileage."
