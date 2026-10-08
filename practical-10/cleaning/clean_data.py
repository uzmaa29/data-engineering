from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
OUTPUT_DIR = DATA_DIR / "cleaned"
OUTPUT_DIR.mkdir(exist_ok=True)

def clean_data():
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    payments = pd.read_csv(DATA_DIR / "payments.csv")

    customers.drop_duplicates(subset=["CustomerID"], inplace=True)
    customers["Email"] = customers["Email"].str.lower().str.strip()
    customers["SignupDate"] = pd.to_datetime(customers["SignupDate"], errors="coerce")

    products.drop_duplicates(subset=["ProductID"], inplace=True)
    products["UnitPrice"] = pd.to_numeric(products["UnitPrice"], errors="coerce")
    products = products[products["UnitPrice"] >= 0]

    orders.drop_duplicates(subset=["OrderID"], inplace=True)
    orders["OrderDate"] = pd.to_datetime(orders["OrderDate"], errors="coerce")
    orders["Quantity"] = pd.to_numeric(orders["Quantity"], errors="coerce")
    orders["UnitPrice"] = pd.to_numeric(orders["UnitPrice"], errors="coerce")
    orders = orders[(orders["Quantity"] > 0) & (orders["UnitPrice"] >= 0)]

    payments.drop_duplicates(subset=["PaymentID"], inplace=True)
    payments["PaymentDate"] = pd.to_datetime(payments["PaymentDate"], errors="coerce")
    payments["Amount"] = pd.to_numeric(payments["Amount"], errors="coerce")
    payments = payments[payments["Amount"] >= 0]

    frames = {"customers": customers, "products": products, "orders": orders, "payments": payments}
    for name, df in frames.items():
        df.to_csv(OUTPUT_DIR / f"{name}_clean.csv", index=False)
    return frames

if __name__ == "__main__":
    clean_data()
    print("Cleaning completed.")
