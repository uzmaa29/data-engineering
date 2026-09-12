
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "students.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    course TEXT NOT NULL,
    marks REAL CHECK(marks >= 0 AND marks <= 100)
)
""")
connection.commit()

cursor.execute("DELETE FROM students")
connection.commit()

students = [
    ("Alice", "alice@example.com", "Data Science", 85),
    ("Bob", "bob@example.com", "Data Science", 78),
    ("Charlie", "charlie@example.com", "Computer Science", 92),
    ("Diana", "diana@example.com", "Data Science", 88)
]

cursor.executemany("""
INSERT INTO students (name, email, course, marks)
VALUES (?, ?, ?, ?)
""", students)
connection.commit()

print("--- CREATE / INSERT ---")
print("Student records inserted successfully.")

print("\n--- READ ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
UPDATE students
SET marks = ?
WHERE name = ?
""", (91, "Bob"))
connection.commit()

print("\n--- UPDATE ---")
print("Bob's marks updated to 91.")

cursor.execute("SELECT * FROM students WHERE name = ?", ("Bob",))
print(cursor.fetchone())

cursor.execute("""
DELETE FROM students
WHERE name = ?
""", ("Diana",))
connection.commit()

print("\n--- DELETE ---")
print("Diana's record deleted.")

print("\n--- FINAL TABLE ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

connection.close()
print("\nDatabase connection closed.")
