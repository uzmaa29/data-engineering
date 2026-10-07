# Practical 9 – PySpark DataFrame Operations

## Objective
Perform common data processing operations using PySpark DataFrames.

## Requirements
1. Read a CSV dataset and display its schema.
2. Perform filtering, grouping, and aggregation.
3. Remove duplicate records.
4. Join two datasets using PySpark.
5. Calculate average sales by product category.

## Project Structure
```text
Practical-9-PySpark-DataFrame-Operations/
├── README.md
├── requirements.txt
├── pyspark_operations.py
└── data/
    ├── sales.csv
    └── products.csv
```

## Installation
```bash
pip install -r requirements.txt
```

Apache Spark and Java should be installed/configured for local execution.

## Run
```bash
python pyspark_operations.py
```
or:
```bash
spark-submit pyspark_operations.py
```

## Operations
- `printSchema()` displays the CSV schema.
- `filter()` selects records with Sales > 1000.
- `groupBy()` and `sum()` calculate total sales by category.
- `dropDuplicates()` removes the repeated OrderID 108 record.
- `join()` combines sales and product datasets using ProductID.
- `avg()` calculates average sales by category.

## Conclusion
This practical demonstrates reading, inspecting, filtering, grouping, aggregating, deduplicating, joining, and analyzing data with PySpark DataFrames.
