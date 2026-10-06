import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

DATA_PATH = Path("../data")
files = list(DATA_PATH.glob("customers_*.csv"))
frames = [pd.read_csv(file) for file in files]
combined_df = pd.concat(frames, ignore_index=True)
combined_df["Name"] = combined_df["Name"].str.strip()
combined_df["Email"] = combined_df["Email"].str.lower().str.strip()
combined_df["City"] = combined_df["City"].str.strip()
combined_df.drop_duplicates(subset=["CustomerID"], inplace=True)
combined_df.dropna(inplace=True)

SERVER = "localhost"
DATABASE = "Practical8_ETL"
DRIVER = "ODBC Driver 17 for SQL Server"
connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)
engine = create_engine(connection_string)
combined_df.to_sql("Customers_Combined", engine, if_exists="replace", index=False)
print("Multiple CSV files combined and loaded successfully.")
print(combined_df)
