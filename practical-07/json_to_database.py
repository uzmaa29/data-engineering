import json
import pandas as pd
from sqlalchemy import create_engine

with open("../data/sales.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.DataFrame(data)
df["total_amount"] = df["quantity"] * df["price"]
df["product"] = df["product"].str.upper()
df = df[["order_id", "customer_id", "product", "quantity", "price", "total_amount", "status"]]

SERVER = "localhost"
DATABASE = "Practical8_ETL"
DRIVER = "ODBC Driver 17 for SQL Server"
connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)
engine = create_engine(connection_string)
df.to_sql("Sales_JSON", engine, if_exists="replace", index=False)
print("JSON data transformed and loaded successfully.")
print(df)
