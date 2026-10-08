from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
REPORTS = BASE / "reports"
REPORTS.mkdir(exist_ok=True)

SERVER = "localhost"
DATABASE = "Practical9_ECommerce"
DRIVER = "ODBC Driver 17 for SQL Server"
CONNECTION_STRING = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)


def load_data():
    customers = pd.read_csv(DATA / "customers.csv")
    products = pd.read_csv(DATA / "products.csv")
    orders = pd.read_csv(DATA / "orders.csv", parse_dates=["order_date"])
    payments = pd.read_csv(DATA / "payments.csv", parse_dates=["payment_date"])
    return customers, products, orders, payments


def clean_data(customers, products, orders, payments):
    customers = customers.drop_duplicates("customer_id").dropna(subset=["customer_id", "email"])
    products = products.drop_duplicates("product_id").dropna(subset=["product_id", "unit_price"])
    orders = orders.drop_duplicates("order_id").dropna(subset=["order_id", "customer_id", "product_id"])
    payments = payments.drop_duplicates("payment_id").dropna(subset=["payment_id", "order_id"])

    customers["email"] = customers["email"].str.lower().str.strip()
    customers["name"] = customers["name"].str.strip()
    products["category"] = products["category"].str.strip()
    orders["status"] = orders["status"].str.strip().str.title()
    payments["payment_status"] = payments["payment_status"].str.strip().str.title()

    orders = orders[orders["quantity"] > 0]
    products = products[products["unit_price"] >= 0]
    payments = payments[payments["payment_amount"] >= 0]
    return customers, products, orders, payments


def transform(customers, products, orders, payments):
    sales = orders.merge(products, on="product_id", how="left")
    sales["line_total"] = sales["quantity"] * sales["unit_price"]
    sales = sales.merge(customers[["customer_id", "name", "city"]], on="customer_id", how="left")
    sales = sales.merge(payments[["order_id", "payment_method", "payment_amount", "payment_status"]], on="order_id", how="left")
    return sales


def create_report(sales):
    completed = sales[sales["status"].eq("Completed")].copy()
    category_report = completed.groupby("category", as_index=False)["line_total"].sum()
    category_report.rename(columns={"line_total": "total_sales"}, inplace=True)

    city_report = completed.groupby("city", as_index=False)["line_total"].sum()
    city_report.rename(columns={"line_total": "total_sales"}, inplace=True)

    with pd.ExcelWriter(REPORTS / "ecommerce_report.xlsx", engine="openpyxl") as writer:
        sales.to_excel(writer, sheet_name="Sales_Detail", index=False)
        category_report.to_excel(writer, sheet_name="Category_Sales", index=False)
        city_report.to_excel(writer, sheet_name="City_Sales", index=False)

    category_report.to_csv(REPORTS / "category_sales.csv", index=False)
    return category_report


def load_to_sql(customers, products, orders, payments, sales):
    engine = create_engine(CONNECTION_STRING)
    customers.to_sql("Customers", engine, if_exists="replace", index=False)
    products.to_sql("Products", engine, if_exists="replace", index=False)
    orders.to_sql("Orders", engine, if_exists="replace", index=False)
    payments.to_sql("Payments", engine, if_exists="replace", index=False)
    sales.to_sql("Sales_Report", engine, if_exists="replace", index=False)


if __name__ == "__main__":
    customers, products, orders, payments = load_data()
    customers, products, orders, payments = clean_data(customers, products, orders, payments)
    sales = transform(customers, products, orders, payments)
    report = create_report(sales)
    load_to_sql(customers, products, orders, payments, sales)
    print("ETL completed successfully.")
    print("\nSales by category:")
    print(report)
