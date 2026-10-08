from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data"
TARGET = DATA / "orders_historical_and_new.csv"

historical = pd.read_csv(DATA / "orders.csv", parse_dates=["order_date"])
new_data = pd.read_csv(DATA / "new_orders.csv", parse_dates=["order_date"])

if TARGET.exists():
    existing = pd.read_csv(TARGET, parse_dates=["order_date"])
else:
    existing = historical.copy()

combined = pd.concat([existing, new_data], ignore_index=True)
combined.drop_duplicates(subset=["order_id"], keep="last", inplace=True)
combined.sort_values("order_date", inplace=True)
combined.to_csv(TARGET, index=False)

print(f"Total records after incremental load: {len(combined)}")
print(combined.tail())
