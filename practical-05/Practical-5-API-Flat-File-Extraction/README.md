# Practical 5 – Extracting Data from APIs and Flat Files Using Python

## Objective

To write a Python program that fetches user data from a public REST API, extracts location information from a flat CSV file, cleans the data, merges both datasets, and saves the final result.

## Technologies Used

- Python
- Pandas
- Requests
- REST API
- CSV / Flat Files

## Data Sources

### REST API

User information is extracted from the JSONPlaceholder REST API:

`https://jsonplaceholder.typicode.com/users`

### Flat CSV File

`locations.csv` contains `id`, `city`, and `country`.

## ETL Process

```text
REST API              CSV File
    │                    │
    ↓                    ↓
Extraction            Extraction
    │                    │
    └──────────┬─────────┘
               ↓
          Data Cleaning
               ↓
          Data Merging
               ↓
        Final DataFrame
               ↓
     cleaned_warehouse_profiles.csv
```

## 1. API Extraction

The `requests` library sends a GET request to the REST API. The JSON response is normalized into a Pandas DataFrame using `pd.json_normalize()`.

## 2. CSV Extraction

Pandas reads the flat file using `pd.read_csv()`.

## 3. Data Cleaning

The program removes missing values using `dropna()` and duplicate records using `drop_duplicates()`.

## 4. Data Transformation

The nested API field `company.name` is renamed to `company`. Only the required API columns are retained.

## 5. Data Merging

The API and CSV datasets are merged using the common `id` column:

```python
pd.merge(api_df, csv_df, on="id", how="inner")
```

## 6. Final Dataset

The final dataset contains `id`, `name`, `email`, `company`, `city`, and `country`.

## 7. Output

The merged data is saved as `cleaned_warehouse_profiles.csv`.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python data_extraction.py
```

## Repository Structure

```text
Practical-5-API-Flat-File-Extraction/
│
├── README.md
├── data_extraction.py
├── requirements.txt
├── locations.csv
└── cleaned_warehouse_profiles.csv   # generated after running
```

## Result

User data was extracted from a REST API and location data was extracted from a CSV flat file. The datasets were cleaned, transformed, and merged using the common `id` field.

## Conclusion

This practical demonstrates how Python can extract data from multiple sources, clean and transform the extracted data, merge datasets using a common key, and save the resulting data for further analysis or use in a data warehouse.
