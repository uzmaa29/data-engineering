# Data Warehouse Design

## Architecture

The project uses a **star schema**. `Fact_Sales` is the central fact table and the descriptive dimensions surround it.

```text
                 Dim_Customer
                      |
                      |
Dim_Date -----> Fact_Sales <----- Dim_Product
                      |
                      |
                Payment fields
```

## Fact Table

`Fact_Sales` stores measurable business events:
- OrderID
- CustomerKey
- ProductKey
- DateKey
- Quantity
- UnitPrice
- TotalAmount
- PaymentMethod
- PaymentStatus

## Dimensions

### Dim_Customer
Stores customer attributes such as name, email, city and signup date.

### Dim_Product
Stores product name, category and unit price.

### Dim_Date
Provides calendar attributes for time-based reporting such as year, month and quarter.

## ETL Layers

1. **Raw:** source CSV files.
2. **Cleaning:** standardized types, duplicates removed and invalid numeric records filtered.
3. **Transformation:** joins and derived `TotalAmount` metric.
4. **Warehouse:** dimensional model for analytics.
5. **Reporting:** summary, category and monthly sales reports.
