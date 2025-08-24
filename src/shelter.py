import csv
import json
import os
from .dog import Dog
from .cat import Cat
from datetime import datetime

class Shelter:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.pets = []
        self.adoption_log = []
        self.load_from_csv()

    def load_from_csv(self):
        self.pets = []
        try:
            with open(self.csv_file, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    pet_type = row.get("type", "Dog").lower()
                    if pet_type == "dog":
                        pet = Dog(
                            name=row["name"],
                            breed=row["breed"],
                            age=int(row["age"]),
                            description=row.get("description",""),
                            status=row.get("status", "Available"),
                            health_status=row.get("health_status", "Not Vaccinated"),
                            pet_id=row.get("id")
                        )
                    else:
                        pet = Cat(
                            name=row["name"],
                            breed=row["breed"],
                            age=int(row["age"]),
                            description=row.get("description",""),
                            status=row.get("status", "Available"),
                            health_status=row.get("health_status", "Not Vaccinated"),
                            pet_id=row.get("id")
                        )
                    self.pets.append(pet)
        except FileNotFoundError:
            pass

    def save_to_csv(self):
        with open(self.csv_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "name", "type", "breed", "age", "description", "status", "health_status"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for pet in self.pets:
                writer.writerow({
                    "id": pet.id,
                    "name": pet.name,
                    "type": pet.type,
                    "breed": pet.breed,
                    "age": pet.age,
                    "description": pet.description,
                    "status": pet.status,
                    "health_status": pet.health_status
                })

    def add_pet(self, pet):
        self.pets.append(pet)

    def list_pets(self):
        for pet in self.pets:
            print(f"{pet.name} ({pet.type}, {pet.breed}, {pet.age} years old, Status: {pet.status}, Health: {pet.health_status})")

    def search_pets(self, criteria, value):
        results = []
        for pet in self.pets:
            if criteria == "type" and pet.type.lower() == value.lower():
                results.append(pet)
            elif criteria == "breed" and pet.breed.lower() == value.lower():
                results.append(pet)
            elif criteria == "age" and str(pet.age) == str(value):
                results.append(pet)
        return results



    def adopt_pet(self, name):
        for pet in self.pets:
            if pet.name.lower() == name.lower() and pet.status == "Available":
                adopter_name = input("Enter adopter's name: ")
                pet.status = "Adopted"
                adoption_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                adoption_record = {
                    "pet_id": pet.id,
                    "name": pet.name,
                    "adopter": adopter_name,
                    "date": adoption_date
                }
                self.adoption_log.append(adoption_record)
                print(f"{pet.name} adopted by {adopter_name} on {adoption_date}")

                # Save adopter info to adopter.json
                data_folder = os.path.join(os.path.dirname(self.csv_file), "..", "data")
                os.makedirs(data_folder, exist_ok=True)
                adopter_file = os.path.join(data_folder, "adopter.json")
                try:
                    if os.path.exists(adopter_file):
                        with open(adopter_file, "r", encoding="utf-8") as f:
                            adopters = json.load(f)
                    else:
                        adopters = []
                    adopters.append(adoption_record)
                    with open(adopter_file, "w", encoding="utf-8") as f:
                        json.dump(adopters, f, indent=2)
                except Exception as e:
                    print(f"Error saving adopter info: {e}")

                return pet
        print("Pet not available for adoption.")
        return None
