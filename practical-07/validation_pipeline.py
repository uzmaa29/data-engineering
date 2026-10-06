import pandas as pd

df = pd.read_csv("../data/customers_1.csv")
errors = []
if df["CustomerID"].isna().any():
    errors.append("CustomerID contains missing values.")
if df["CustomerID"].duplicated().any():
    errors.append("Duplicate CustomerID values found.")
if df["Email"].isna().any():
    errors.append("Email contains missing values.")
if not df["Email"].astype(str).str.contains("@", regex=False).all():
    errors.append("Invalid email format found.")
if errors:
    print("DATA VALIDATION FAILED")
    for error in errors:
        print("-", error)
else:
    print("DATA VALIDATION PASSED")
    print("Data is ready to be loaded into the target database.")
