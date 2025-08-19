# pillars_of_oop/inheritance.py

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving."

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def charge(self):
        return f"{self.brand} {self.model} is charging. Battery: {self.battery_size} kWh"

# demo
if __name__ == "__main__":
    my_tesla = ElectricCar("Tesla", "Model S", 100)
    print(my_tesla.model)        # Model S
    print(my_tesla.drive())      # Tesla Model S is driving.
    print(my_tesla.charge())     # Tesla Model S is charging. Battery: 100 kWh
