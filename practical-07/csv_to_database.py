import pandas as pd
from sqlalchemy import create_engine

SERVER = "localhost"
DATABASE = "Practical8_ETL"
DRIVER = "ODBC Driver 17 for SQL Server"

CONNECTION_STRING = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)

engine = create_engine(CONNECTION_STRING)
df = pd.read_csv("../data/customers_1.csv")
df["Name"] = df["Name"].str.strip()
df["Email"] = df["Email"].str.lower().str.strip()
df["City"] = df["City"].str.strip()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.to_sql("Customers_CSV", engine, if_exists="replace", index=False)
print("CSV data cleaned and loaded into SQL Server.")
print(df)
