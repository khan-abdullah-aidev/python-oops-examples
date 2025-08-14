class Car: # class is like a blueprint.
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is now running.")

# Creating objects
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

car1.start_engine()
car2.start_engine()
