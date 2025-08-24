class Pet:
    id_counter = {"Dog": 0, "Cat": 0}

    def __init__(self, name, breed, age, pet_type, status="Available", health_status="Not Vaccinated", pet_id=None, description=""):
        self._name = name
        self._breed = breed
        self._age = age
        self._type = pet_type
        self.status = status
        self.health_status = health_status
        self.description = description

        # Pet ID generation
        if pet_id:
            self.id = pet_id
        else:
            Pet.id_counter[pet_type] += 1
            self.id = f"{pet_type[:3].upper()}{Pet.id_counter[pet_type]:03d}"

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

    @property
    def age(self):
        return self._age

    @property
    def type(self):
        return self._type

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        print(f"Health: {self.health_status}")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "breed": self.breed,
            "age": self.age,
            "description": self.description,
            "status": self.status,
            "health_status": self.health_status
        }
