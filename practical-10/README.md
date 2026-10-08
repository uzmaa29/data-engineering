# Practical 10 – End-to-End Data Engineering Mini Project

## Objective

Design and implement an end-to-end data engineering solution covering data ingestion, cleaning, transformation, storage, data warehouse design and reporting.

## Architecture

```text
CSV Sources
   |
   v
Data Ingestion
   |
   v
Data Cleaning
   |
   v
Transformation + Joins
   |
   +------> Clean/Transformed Data
   |
   v
SQL Server Data Warehouse
   |
   v
Reporting
```

## Technologies

- Python
- Pandas
- SQL Server
- SQLAlchemy / PyODBC
- Excel
- CSV

## Project Structure

```text
Practical-10-End-to-End-Data-Engineering/
├── README.md
├── requirements.txt
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── payments.csv
├── ingestion/
│   └── ingest_data.py
├── cleaning/
│   └── clean_data.py
├── transformation/
│   └── transform_data.py
├── warehouse/
│   ├── create_database.sql
│   ├── create_dimensions.sql
│   └── create_fact_tables.sql
├── pipeline/
│   └── run_pipeline.py
├── reporting/
│   ├── generate_report.py
│   └── reports/
└── docs/
    └── data_warehouse_design.md
```

## 1. Data Ingestion

The ingestion module reads customer, product, order and payment CSV files using Pandas.

Run:

```bash
python ingestion/ingest_data.py
```

## 2. Data Cleaning

The cleaning stage:

- Removes duplicate customers and orders.
- Standardizes email values.
- Converts dates to datetime.
- Converts numeric fields to numeric types.
- Removes invalid negative quantities/prices.
- Writes cleaned datasets to `data/cleaned/`.

Run:

```bash
python cleaning/clean_data.py
```

## 3. Data Transformation

The transformation stage:

- Calculates `TotalAmount = Quantity × UnitPrice`.
- Extracts year/month from order dates.
- Joins orders with customers, products and payments.
- Creates the fact sales dataset.
- Creates customer, product and date dimensions.

Run:

```bash
python transformation/transform_data.py
```

## 4. Data Warehouse

The SQL Server warehouse follows a star schema:

```text
              Dim_Customer
                    |
                    |
Dim_Date ---- Fact_Sales ---- Dim_Product
```

Run the SQL files in SQL Server Management Studio in this order:

1. `warehouse/create_database.sql`
2. `warehouse/create_dimensions.sql`
3. `warehouse/create_fact_tables.sql`

## 5. Reporting

The reporting script generates:

- Overall sales summary
- Revenue by category
- Monthly revenue
- Excel workbook containing all reports
- CSV report files

Run:

```bash
python reporting/generate_report.py
```

Reports are created under `reporting/reports/`.

## 6. Run the Complete Python Pipeline

```bash
python pipeline/run_pipeline.py
```

This runs cleaning followed by transformation.

## Business Metrics

The project can answer questions such as:

- What is total revenue?
- How many orders were placed?
- Which product categories generate the most revenue?
- How does revenue change by month?
- How many units were sold?
- Which customers and products are associated with sales?

## Conclusion

This mini project demonstrates a complete data engineering workflow from raw CSV ingestion through data quality, transformation, warehouse modeling and analytical reporting. The star schema makes the resulting data suitable for BI tools such as Power BI as a reporting layer.
