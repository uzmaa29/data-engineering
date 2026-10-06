import pandas as pd
from sqlalchemy import create_engine, text, inspect

SERVER = "localhost"
DATABASE = "Practical8_ETL"
DRIVER = "ODBC Driver 17 for SQL Server"
connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}&trusted_connection=yes"
)
engine = create_engine(connection_string)
source_df = pd.read_csv("../data/incremental_sales.csv")
source_df["LastUpdated"] = pd.to_datetime(source_df["LastUpdated"])

if not inspect(engine).has_table("Incremental_Sales"):
    source_df.to_sql("Incremental_Sales", engine, if_exists="replace", index=False)
    print("Initial full load completed.")
else:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT MAX(LastUpdated) FROM Incremental_Sales")).scalar()
    last_loaded = pd.Timestamp("1900-01-01") if result is None else pd.Timestamp(result)
    new_records = source_df[source_df["LastUpdated"] > last_loaded]
    if not new_records.empty:
        new_records.to_sql("Incremental_Sales", engine, if_exists="append", index=False)
        print(f"Incremental load completed: {len(new_records)} new record(s).")
    else:
        print("No new records found. Nothing loaded.")
