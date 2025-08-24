import os
import platform
from .shelter import Shelter
from .dog import Dog
from .cat import Cat
import json


DATA_PATH = "data/pets.csv"

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def main():
    shelter = Shelter(DATA_PATH)

    while True:
        clear_console()
        print("\n" + "="*60)
        print("🐶 Welcome to the Pet Shelter System 🐱".center(60))
        print("="*60 + "\n")
        print("\n🐾 Please choose an option:")
        print("════════════════════════════")
        print("1. List all pets")
        print("2. Add a new pet")
        print("3. Search for a pet")
        print("4. Adopt a pet")
        print("5. Display pet details")
        print("6. Save shelter data")
        print("7. Load shelter data")
        print("8. View adoption log")
        print("9. Exit")
        print("════════════════════════════")


        choice = input("👉 Enter your choice (1-9): ")

        if choice == "1":
            print("\n=== All Pets in the Shelter ===")
            shelter.list_pets()
            input("\nPress Enter to return to the main menu.")

        elif choice == "2":
            pet_type = input("\nEnter pet type (dog/cat): ").lower()
            name = input("Enter name: ")
            breed = input("Enter breed: ")
            age = int(input("Enter age: "))
            description = input("Enter description: ")
            health_status = input("Enter health status (Vaccinated/Not Vaccinated): ")
            if pet_type == "dog":
                pet = Dog(name, breed, age, description, status="Available", health_status=health_status)
            else:
                pet = Cat(name, breed, age, description, status="Available", health_status=health_status)
            shelter.add_pet(pet)
            shelter.save_to_csv()  # auto-save
            print(f"\n{name} added to shelter and saved to CSV.")
            input("Press Enter to return to the main menu.")

        elif choice == "3":
            print("\nSearch by: 1. Type 2. Breed 3. Age")
            c = input("Enter choice (1-3): ")
            if c == "1":
                value = input("Enter type (dog/cat): ")
                results = shelter.search_pets("type", value)
            elif c == "2":
                value = input("Enter breed: ")
                results = shelter.search_pets("breed", value)
            elif c == "3":
                value = input("Enter age: ")
                results = shelter.search_pets("age", value)
            else:
                results = []

            print("\n=== Search Results ===")
            if results:
                for idx, pet in enumerate(results, 1):
                    print(f"{idx}. {pet.name} ({pet.breed}, {pet.age} years old, Status: {pet.status}, Health: {pet.health_status})")
            else:
                print("No pets found.")
            input("\nPress Enter to return to the main menu.")

        elif choice == "4":
            name = input("\nEnter the name of the pet to adopt: ")
            adopted_pet = shelter.adopt_pet(name)
            if adopted_pet:
                shelter.save_to_csv()  # auto-save after adoption
            input("\nPress Enter to return to the main menu.")

        elif choice == "5":
            name = input("\nEnter pet's name: ")
            found = False
            for pet in shelter.pets:
                if pet.name.lower() == name.lower():
                    print("\n=== Pet Details ===")
                    pet.display_info()  # prints all info
                    found = True
                    break
            if not found:
                print("Pet not found.")
            input("\nPress Enter to return to the main menu.")

        elif choice == "6":
            shelter.save_to_csv()
            print("\nShelter data saved successfully.")
            input("\nPress Enter to return to the main menu.")

        elif choice == "7":
            shelter.load_from_csv()
            print("\nShelter data loaded successfully.")
            input("\nPress Enter to return to the main menu.")

 


        elif choice == "8":
            print("\n=== Adoption Log ===")
            adopter_file = os.path.join(os.path.dirname(DATA_PATH), "adopter.json")
            try:
                if os.path.exists(adopter_file) and os.path.getsize(adopter_file) > 0:
                    with open(adopter_file, "r", encoding="utf-8") as f:
                        adoption_log = json.load(f)
                    if adoption_log:
                        for entry in adoption_log:
                            print(f"{entry['pet_id']} - {entry['name']} adopted by {entry['adopter']} on {entry['date']}")
                    else:
                        print("No adoptions yet.")
                else:
                    print("No adoptions yet.")
            except Exception as e:
                print(f"Error reading adoption log: {e}")
            input("\nPress Enter to return to the main menu.")

        elif choice == "9":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Try again.")
            input("\nPress Enter to return to the main menu.")

if __name__ == "__main__":
    main()
