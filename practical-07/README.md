# Practical 8 – ETL Pipeline Design and Implementation

## Objective
Design and implement ETL pipelines using Python, Pandas, CSV/JSON files, and SQL Server.

## Requirements Covered
1. CSV → clean → transform → SQL Server
2. Multiple CSV files → combine → SQL Server
3. JSON → transform selected fields → relational database
4. Identify and remove invalid records
5. Validate data before loading
6. Incremental data loading

## Technologies
- Python
- Pandas
- SQL Server
- SQLAlchemy
- PyODBC
- CSV
- JSON

## Project Structure
```text
Practical-8-ETL-Pipelines/
├── README.md
├── requirements.txt
├── data/
│   ├── customers_1.csv
│   ├── customers_2.csv
│   ├── sales.json
│   ├── invalid_records.csv
│   └── incremental_sales.csv
├── scripts/
│   ├── csv_to_database.py
│   ├── multiple_csv_etl.py
│   ├── json_to_database.py
│   ├── invalid_record_etl.py
│   ├── validation_pipeline.py
│   └── incremental_load.py
└── sql/
    └── database_setup.sql
```

## Setup
```bash
pip install -r requirements.txt
```
Run `sql/database_setup.sql` in SQL Server Management Studio.

The scripts use Windows Trusted Authentication with `localhost`, database `Practical8_ETL`, and `ODBC Driver 17 for SQL Server`. Change these values if your SQL Server setup differs.

## ETL Flow
```text
CSV / JSON Sources
        ↓
     Extraction
        ↓
       Cleaning
        ↓
     Validation
        ↓
    Transformation
        ↓
      Loading
        ↓
   SQL Server Database
```

## 1. CSV to Database
`csv_to_database.py` extracts `customers_1.csv`, cleans text fields, removes missing/duplicate records, and loads the result into `Customers_CSV`.

```bash
python scripts/csv_to_database.py
```

## 2. Multiple CSV Files
`multiple_csv_etl.py` reads all `customers_*.csv` files, combines them, removes duplicates/incomplete records, and loads the combined dataset into `Customers_Combined`.

```bash
python scripts/multiple_csv_etl.py
```

## 3. JSON to Relational Database
`json_to_database.py` reads sales JSON, transforms product names to uppercase, calculates `total_amount`, and loads the result into `Sales_JSON`.

```bash
python scripts/json_to_database.py
```

## 4. Invalid Record Removal
`invalid_record_etl.py` identifies missing names, invalid emails, and invalid ages. It creates `invalid_records_found.csv` and `valid_records.csv`.

```bash
python scripts/invalid_record_etl.py
```

## 5. Data Validation
`validation_pipeline.py` checks for missing IDs, duplicate IDs, missing emails, and invalid email formats before data is considered ready for loading.

```bash
python scripts/validation_pipeline.py
```

## 6. Incremental Loading
`incremental_load.py` checks the latest `LastUpdated` value in the target table and loads only records newer than that value. The first run performs the initial full load.

```bash
python scripts/incremental_load.py
```

### Full Load vs Incremental Load
| Full Load | Incremental Load |
|---|---|
| Loads all records | Loads only new/changed records |
| More processing | Less processing |
| Useful for initial load | Useful for regular updates |

## Conclusion
This practical demonstrates extraction from multiple file formats, cleaning, validation, transformation, combining sources, loading into SQL Server, invalid-record handling, and incremental ETL.
