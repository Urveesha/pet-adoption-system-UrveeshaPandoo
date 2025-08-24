import unittest
from src.pet import Pet
from src.dog import Dog
from src.cat import Cat


class TestPet(unittest.TestCase):

    def setUp(self):
        self.pet = Pet("Buddy", "Golden Retriever", 3, "Dog", description="Friendly dog", status="Available", health_status="Vaccinated")

        self.dog = Dog("Max", "Labrador", 5, "Playful", status="Available", health_status="Not Vaccinated")
        self.cat = Cat("Whiskers", "Siamese", 2, "Calm", status="Available", health_status="Vaccinated")

    def test_pet_attributes(self):
        self.assertEqual(self.pet.name, "Buddy")
        self.assertEqual(self.pet.type, "Dog")
        self.assertEqual(self.pet.breed, "Golden Retriever")
        self.assertEqual(self.pet.age, 3)
        self.assertEqual(self.pet.status, "Available")
        self.assertEqual(self.pet.health_status, "Vaccinated")

    def test_dog_cat_subclasses(self):
        self.assertEqual(self.dog.type, "Dog")
        self.assertEqual(self.cat.type, "Cat")

    def test_to_dict(self):
        data = self.pet.to_dict()
        self.assertEqual(data["name"], "Buddy")
        self.assertEqual(data["type"], "Dog")
        self.assertEqual(data["breed"], "Golden Retriever")
        self.assertEqual(data["age"], 3)
        self.assertEqual(data["status"], "Available")
        self.assertEqual(data["health_status"], "Vaccinated")


if __name__ == "__main__":
    unittest.main()
