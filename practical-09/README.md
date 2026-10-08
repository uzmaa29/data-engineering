# Practical 9 – End-to-End E-Commerce ETL Pipeline

## Objective

Build an end-to-end ETL pipeline that extracts e-commerce data from CSV files, cleans and transforms it using Python/Pandas, loads it into a SQL Server database, and generates a report. The practical also demonstrates handling historical data and newly arriving records.

## Requirements Covered

1. CSV → Python/Pandas → Data Cleaning → SQL Database → Report
2. E-commerce ETL for customers, orders, products, and payments
3. Historical + newly arriving data using incremental loading

## Technologies

- Python
- Pandas
- SQL Server
- SQLAlchemy
- PyODBC
- Excel/CSV reporting

## Structure

```text
Practical-9-End-to-End-ECommerce-ETL/
├── README.md
├── requirements.txt
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── payments.csv
│   └── new_orders.csv
├── scripts/
│   ├── etl_pipeline.py
│   └── incremental_pipeline.py
├── sql/
│   └── database_setup.sql
└── reports/
    └── (generated after running the pipeline)
```

## Setup

Install packages:

```bash
pip install -r requirements.txt
```

Run `sql/database_setup.sql` in SQL Server Management Studio.

The Python scripts assume:

```text
Server: localhost
Database: Practical9_ECommerce
Driver: ODBC Driver 17 for SQL Server
```

Change the connection settings if your SQL Server configuration is different.

## ETL Process

```text
CSV Files
   ↓
Extraction
   ↓
Data Cleaning
   ↓
Transformation
   ↓
SQL Server
   ↓
Report
```

### Extraction

The pipeline reads four source files:

- Customers
- Products
- Orders
- Payments

### Cleaning

The pipeline:

- Removes duplicate IDs
- Removes required-field nulls
- Standardizes text fields
- Removes invalid quantities
- Removes negative prices/payment amounts

### Transformation

Orders are joined with products, customers, and payments. A calculated `line_total` is created:

```text
line_total = quantity × unit_price
```

### Loading

The transformed data is stored in SQL Server tables:

- `Customers`
- `Products`
- `Orders`
- `Payments`
- `Sales_Report`

### Reporting

The pipeline generates:

- `reports/ecommerce_report.xlsx`
- `reports/category_sales.csv`

The Excel report contains sales detail, category sales, and city sales.

## Historical and New Data

`incremental_pipeline.py` demonstrates incremental loading.

Historical orders come from `orders.csv`. Newly arriving records come from `new_orders.csv`.

The pipeline combines them and removes duplicate `order_id` values instead of rebuilding the dataset from scratch.

Run:

```bash
python scripts/incremental_pipeline.py
```

Then run it again after adding new records to `new_orders.csv`. Existing orders will not be duplicated.

## Run the Complete ETL

```bash
python scripts/etl_pipeline.py
```

Then run the incremental pipeline:

```bash
python scripts/incremental_pipeline.py
```

## Expected Result

The final pipeline produces a cleaned and transformed sales dataset in SQL Server and an Excel/CSV report summarizing sales performance.

## Conclusion

This practical demonstrates a complete real-world ETL workflow: extracting multiple related datasets, cleaning and validating them, transforming and joining the data, loading it into a relational database, generating reports, and handling newly arriving data through incremental loading.
