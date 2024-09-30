class Vehicle:
    def __init__(self, make, model, year, color, wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.wheels = wheels

    def description(self):
        return f"This {self.year} {self.color} {self.make} {self.model} has {self.wheels} wheels."

    def honk(self):
        return "Honk honk!"

class Car(Vehicle):
    def __init__(self, make, model, year, color, wheels, doors, transmission):
        super().__init__(make, model, year, color, wheels)
        self.doors = doors
        self.transmission = transmission

    def car_description(self):
        return f"This car is a {self.description()} with {self.doors} doors and a {self.transmission} transmission."

    def start_engine(self):
        return "Vroom! The engine is started."

class ElectricCar(Car):
    def __init__(self, make, model, year, color, wheels, doors, transmission, battery_capacity):
        super().__init__(make, model, year, color, wheels, doors, transmission)
        self.battery_capacity = battery_capacity

    def electric_car_description(self):
        return f"This electric car is a {self.car_description()} with a {self.battery_capacity} kWh battery."

    def charge_battery(self):
        return "The battery is charging..."

class GasolineCar(Car):
    def __init__(self, make, model, year, color, wheels, doors, transmission, fuel_capacity):
        super().__init__(make, model, year, color, wheels, doors, transmission)
        self.fuel_capacity = fuel_capacity

    def gasoline_car_description(self):
        return f"This gasoline car is a {self.car_description()} with a {self.fuel_capacity} liter fuel tank."

    def fill_gas(self):
        return "The gas tank is full!"

# Create instances of the classes
my_tesla = ElectricCar("Tesla", "Model S", 2022, "silver", 4, 4, "automatic", 75)
my_camry = GasolineCar("Toyota", "Camry", 2020, "blue", 4, 4, "automatic", 60)

# Call methods on the instances
print(my_tesla.electric_car_description())
print(my_tesla.honk())
print(my_tesla.start_engine())
print(my_tesla.charge_battery())

print(my_camry.gasoline_car_description())
print(my_camry.honk())
print(my_camry.start_engine())
print(my_camry.fill_gas())