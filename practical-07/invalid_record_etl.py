import re
import pandas as pd

df = pd.read_csv("../data/invalid_records.csv")

def valid_email(email):
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(email)))

valid = (
    df["Name"].notna()
    & df["Email"].apply(valid_email)
    & df["Age"].between(1, 100)
)
invalid_df = df[~valid].copy()
clean_df = df[valid].copy()
invalid_df.to_csv("../data/invalid_records_found.csv", index=False)
clean_df.to_csv("../data/valid_records.csv", index=False)
print("Invalid records:")
print(invalid_df)
print("\nValid records:")
print(clean_df)
