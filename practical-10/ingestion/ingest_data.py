from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def ingest():
    return {
        "customers": pd.read_csv(DATA_DIR / "customers.csv"),
        "products": pd.read_csv(DATA_DIR / "products.csv"),
        "orders": pd.read_csv(DATA_DIR / "orders.csv"),
        "payments": pd.read_csv(DATA_DIR / "payments.csv"),
    }

if __name__ == "__main__":
    data = ingest()
    for name, df in data.items():
        print(f"{name}: {len(df)} records")
