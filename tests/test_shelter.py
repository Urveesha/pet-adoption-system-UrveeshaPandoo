import unittest
import tempfile
import os
import csv
from src.shelter import Shelter
from src.dog import Dog
from src.cat import Cat
from datetime import datetime

class TestShelter(unittest.TestCase):

    def setUp(self):
        
        self.temp_csv = tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='', encoding='utf-8')
        writer = csv.DictWriter(self.temp_csv, fieldnames=["id","name","type","breed","age","description","status","health_status"])
        writer.writeheader()
        writer.writerow({"id":"DOG001","name":"Buddy","type":"Dog","breed":"Golden Retriever","age":3,"description":"Friendly","status":"Available","health_status":"Vaccinated"})
        writer.writerow({"id":"CAT001","name":"Whiskers","type":"Cat","breed":"Siamese","age":2,"description":"Calm","status":"Available","health_status":"Not Vaccinated"})
        self.temp_csv.close()
        self.shelter = Shelter(self.temp_csv.name)

    def tearDown(self):
        os.unlink(self.temp_csv.name)

    def test_load_from_csv(self):
        self.assertEqual(len(self.shelter.pets), 2)
        self.assertEqual(self.shelter.pets[0].name, "Buddy")
        self.assertEqual(self.shelter.pets[1].type, "Cat")

    def test_add_pet(self):
        dog = Dog("Max", "Labrador", 5, "Playful")
        self.shelter.add_pet(dog)
        self.assertIn(dog, self.shelter.pets)

    def test_search_pets(self):
        results = self.shelter.search_pets("type", "Dog")
        self.assertEqual(len(results), 1)
        results_breed = self.shelter.search_pets("breed", "Siamese")
        self.assertEqual(results_breed[0].name, "Whiskers")

    def test_adopt_pet(self):
        # simulate input for adopter name
        import builtins
        builtins.input = lambda _: "Alice"
        pet = self.shelter.adopt_pet("Buddy")
        self.assertEqual(pet.status, "Adopted")
        # Verify adoption log
        self.assertEqual(len(self.shelter.adoption_log), 1)
        log_entry = self.shelter.adoption_log[0]
        self.assertEqual(log_entry["pet_id"], pet.id)
        self.assertEqual(log_entry["name"], pet.name)
        self.assertEqual(log_entry["adopter"], "Alice")
        
        datetime.strptime(log_entry["date"], "%Y-%m-%d %H:%M")
        builtins.input = input  

    def test_save_and_reload_csv(self):
        dog = Dog("Max", "Labrador", 5, "Playful")
        self.shelter.add_pet(dog)
        self.shelter.save_to_csv()
        new_shelter = Shelter(self.temp_csv.name)
        self.assertTrue(any(p.name == "Max" for p in new_shelter.pets))


if __name__ == "__main__":
    unittest.main()
