
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "students.bin"

students = [
    {"id": 1, "name": "Alice", "course": "Data Science", "marks": 85},
    {"id": 2, "name": "Bob", "course": "Data Science", "marks": 78},
    {"id": 3, "name": "Charlie", "course": "Computer Science", "marks": 92},
]

with open(FILE_PATH, "wb") as file:
    pickle.dump(students, file)

print("Binary file written successfully.")

with open(FILE_PATH, "rb") as file:
    loaded_students = pickle.load(file)

print("\nData read from binary file:")
for student in loaded_students:
    print(student)
