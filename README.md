# 🐾 Pet Shelter System 🐾

Welcome to the **Pet Shelter System**, a Python-based command-line application designed to manage pets in a shelter. This project showcases object-oriented design (OOP), CSV data management, and enhanced user experience with a clean CLI interface.

---

## 🌟 Features

### Core Features (Assignment Requirements)
- **List all pets**: View all pets with detailed information.
- **Add a new pet**: Add dogs or cats with attributes like name, breed, age, description, status, and health status.
- **Search pets**: Search by type, breed, or age.
- **Adopt a pet**: Mark pets as adopted and record adopter details.
- **Display pet details**: View complete information for a selected pet.
- **Save and load data**: Store and retrieve shelter data in/from a CSV file.

### 🏆 Bonuses Implemented
- **Pet ID Generation System**: Unique auto-generated IDs for each pet (e.g., `DOG001`, `CAT023`).
- **Adoption Log**: Keeps a log of adopted pets, including adopter name and adoption date.
- **Bonus functions on menu**: When clicking on "Display pet details", pet status (Available or Adopted) and health_status (Vaccinated, Not Vaccinated or neuteured) is also displayed for additional pet information.
- **Enhanced CLI with ASCII Art & Styling**:
  - Friendly pet icons 🐶 and 🐱
  - Text borders and headings for a clean interface
  - Numbered menu with custom bullet points for better readability
    
- **Unit Testing**:
  - Full coverage of `Pet` and `Shelter` classes
  - Tests for loading, saving, adding pets, searching, and adoption log

---

## 🐕🐈 Pet Attributes

Each pet has the following attributes:
- **ID**: Unique identifier auto-generated for each pet
- **Name**: Pet's name
- **Type**: Dog or Cat
- **Breed**: Pet breed
- **Age**: Age in years
- **Description**: Short description of the pet
- **Status**: Available or Adopted
- **Health Status**: Vaccinated, Not Vaccinated, Neutered, etc.

---

## 💻 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Urveesha/pet-adoption-system-UrveeshaPandoo-22402581
cd pet_shelter_system
```

## Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

## Install dependencies
pip install -r requirements.txt


## 🏃 Running the Application

Run the CLI app:
python -m src.main

You will see a friendly menu as such:

================= 🐶 Welcome to the Pet Shelter System 🐱 =================

🐾 Please choose an option:

════════════════════════════

➊ List all pets

➋ Add a new pet

➌ Search for a pet

➍ Adopt a pet

➎ Display pet details

➏ Save shelter data

➐ Load shelter data

➑ View adoption log

➒ Exit

════════════════════════════

👉 Enter your choice (1-9):

## 📦 Running Unit Tests
All features are fully tested using Python’s unittest.

To run the tests:
# Test Pet class
python -m unittest tests/test_pet.py -v

# Test Shelter class and adoption log
python -m unittest tests/test_shelter.py -v

## 📝 CSV Data

The app uses data/pets.csv to store and load pet information.
Example:
id,name,type,breed,age,description,status,health_status
DOG001,Buddy,Dog,Golden Retriever,3,Friendly and energetic,Adopted,Vaccinated
CAT001,Whiskers,Cat,Siamese,2,Calm and affectionate,Adopted,Not Vaccinated

## 💡 Notes

-Adoption log records each adoption with the adopter's name and date.

-Pet IDs are auto-generated for easy tracking.

-CLI styling makes navigation easier and more visually appealing.

-Designed using OOP principles for easy scalability.

## 🐾 Author

Urveesha Pandoo
Project completed as part of a Python programming assignment.






