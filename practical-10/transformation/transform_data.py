from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "cleaned"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "transformed"
OUTPUT_DIR.mkdir(exist_ok=True)

def transform():
    customers = pd.read_csv(DATA_DIR / "customers_clean.csv")
    products = pd.read_csv(DATA_DIR / "products_clean.csv")
    orders = pd.read_csv(DATA_DIR / "orders_clean.csv")
    payments = pd.read_csv(DATA_DIR / "payments_clean.csv")

    orders["TotalAmount"] = orders["Quantity"] * orders["UnitPrice"]
    orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
    orders["Year"] = orders["OrderDate"].dt.year
    orders["Month"] = orders["OrderDate"].dt.month

    fact = orders.merge(customers, on="CustomerID", how="left") \
                 .merge(products, on="ProductID", how="left", suffixes=("", "_Product")) \
                 .merge(payments[["OrderID", "PaymentMethod", "PaymentStatus", "Amount"]], on="OrderID", how="left")

    fact = fact[["OrderID", "CustomerID", "ProductID", "OrderDate", "Quantity", "UnitPrice", "TotalAmount", "PaymentMethod", "PaymentStatus"]]

    fact.to_csv(OUTPUT_DIR / "fact_sales.csv", index=False)
    customers.to_csv(OUTPUT_DIR / "dim_customer.csv", index=False)
    products.to_csv(OUTPUT_DIR / "dim_product.csv", index=False)

    dates = pd.DataFrame({"Date": pd.date_range(fact["OrderDate"].min(), fact["OrderDate"].max(), freq="D")})
    dates["Date"] = pd.to_datetime(dates["Date"])
    dates["Year"] = dates["Date"].dt.year
    dates["Month"] = dates["Date"].dt.month
    dates["MonthName"] = dates["Date"].dt.month_name()
    dates["Quarter"] = dates["Date"].dt.quarter
    dates.to_csv(OUTPUT_DIR / "dim_date.csv", index=False)
    return fact

if __name__ == "__main__":
    transform()
    print("Transformation completed.")
