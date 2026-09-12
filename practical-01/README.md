# Practical 1 – File Handling, Regular Expressions and SQL

## Objective

To understand file handling, document parsing, binary file operations,
regular expressions, and relational database operations using Python and SQL.

## Exercises

### Exercise 1 – File Parsing and Data Validation

The program parses:

- TXT
- CSV
- HTML
- XML
- JSON

It also checks the CSV and JSON data for simple anomalies such as:

- Missing values
- Duplicate records
- Invalid marks

**File:** `01_file_parsing/file_parsing.py`

### Exercise 2 – Binary File Handling

The program demonstrates:

- Writing Python data to a binary file
- Reading data from a binary file
- Using Python's `pickle` module

**File:** `02_binary_files/binary_files.py`

### Exercise 3 – Regular Expressions

The program demonstrates:

- Searching for email addresses
- Searching for phone numbers
- Searching for dates
- Splitting strings
- Replacing text

**File:** `03_regular_expressions/regex_operations.py`

### Exercise 4 – Relational Database and SQL CRUD

A Student Management System is created using SQLite.

The database demonstrates:

- CREATE TABLE
- INSERT
- SELECT
- UPDATE
- DELETE

**File:** `04_sql_crud/database.py`

The SQLite database file `students.db` is generated automatically when
the program is executed.

## Technologies Used

- Python
- SQL
- SQLite
- Regular Expressions
- TXT
- CSV
- HTML
- XML
- JSON
- Pickle

## Requirements

Python 3.x is sufficient. No external Python packages are required.

## How to Run

Open the repository in VS Code or a terminal.

### Exercise 1

```bash
cd 01_file_parsing
python file_parsing.py
```

### Exercise 2

```bash
cd 02_binary_files
python binary_files.py
```

This creates `students.bin`.

### Exercise 3

```bash
cd 03_regular_expressions
python regex_operations.py
```

### Exercise 4

```bash
cd 04_sql_crud
python database.py
```

This creates `students.db`.

## Sample Output

The programs print the extracted data and the results of the
anomaly checks / CRUD operations directly in the terminal.

## Conclusion

This practical demonstrates basic Python file handling, parsing of
different document formats, binary file operations, pattern matching
using regular expressions, and CRUD operations on a relational database.
