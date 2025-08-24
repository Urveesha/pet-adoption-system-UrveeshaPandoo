from .pet import Pet

class Dog(Pet):
    def __init__(self, name, breed, age, description="", status="Available", health_status="Not Vaccinated", pet_id=None):
        super().__init__(name, breed, age, "Dog", status, health_status, pet_id, description)
