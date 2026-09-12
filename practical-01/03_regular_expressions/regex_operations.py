
import re

text = """
Contact us at alice@example.com or bob@test.org.
Call +91-9876543210 or 9876543210.
Important dates: 12-09-2026 and 25/12/2026.
Python is powerful. Python is beginner-friendly.
"""

emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print("--- EMAIL SEARCH ---")
print(emails)

phones = re.findall(r"(?:\+91[- ]?)?\d{10}", text)
print("\n--- PHONE SEARCH ---")
print(phones)

dates = re.findall(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b", text)
print("\n--- DATE SEARCH ---")
print(dates)

sentences = re.split(r"[.!?]\s*", text.strip())
sentences = [sentence for sentence in sentences if sentence]
print("\n--- SPLIT ---")
print(sentences)

updated_text = re.sub(r"\bPython\b", "Programming", text)
print("\n--- REPLACE ---")
print(updated_text)
