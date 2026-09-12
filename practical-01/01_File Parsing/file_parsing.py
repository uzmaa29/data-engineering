
import csv
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).parent


def parse_txt():
    path = BASE_DIR / "sample.txt"
    print("\n--- TXT FILE ---")
    lines = path.read_text(encoding="utf-8").splitlines()

    for line in lines[1:]:
        if line.strip():
            print(line)


def parse_csv():
    path = BASE_DIR / "sample.csv"
    print("\n--- CSV FILE ---")

    with open(path, newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    print("Records:")
    for row in rows:
        print(row)

    missing = []
    for i, row in enumerate(rows, start=2):
        for column, value in row.items():
            if value == "":
                missing.append(f"Row {i}: missing {column}")

    seen = set()
    duplicates = []
    for i, row in enumerate(rows, start=2):
        key = tuple(row.items())
        if key in seen:
            duplicates.append(f"Row {i}: duplicate record")
        seen.add(key)

    invalid_marks = []
    for i, row in enumerate(rows, start=2):
        if row["marks"]:
            marks = float(row["marks"])
            if not 0 <= marks <= 100:
                invalid_marks.append(f"Row {i}: marks={marks}")

    print("\nAnomaly Check:")
    print("Missing values:", missing or "None")
    print("Duplicate records:", duplicates or "None")
    print("Invalid marks:", invalid_marks or "None")


def parse_html():
    path = BASE_DIR / "sample.html"
    print("\n--- HTML FILE ---")
    text = path.read_text(encoding="utf-8")

    rows = re.findall(r"<tr>(.*?)</tr>", text, re.DOTALL)
    for row in rows[1:]:
        cells = re.findall(r"<td>(.*?)</td>", row)
        print(cells)


def parse_xml():
    path = BASE_DIR / "sample.xml"
    print("\n--- XML FILE ---")
    root = ET.parse(path).getroot()

    for student in root.findall("student"):
        print({
            "id": student.get("id"),
            "name": student.findtext("name"),
            "course": student.findtext("course"),
            "marks": student.findtext("marks")
        })


def parse_json():
    path = BASE_DIR / "sample.json"
    print("\n--- JSON FILE ---")

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for student in data["students"]:
        print(student)

    missing = [
        student["name"]
        for student in data["students"]
        if student.get("marks") is None
    ]
    print("Students with missing marks:", missing or "None")


if __name__ == "__main__":
    parse_txt()
    parse_csv()
    parse_html()
    parse_xml()
    parse_json()
