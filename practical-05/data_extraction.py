import pandas as pd
import requests


def extract_api_data(url):
    """Fetches data from a REST API and returns a DataFrame."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return pd.json_normalize(data)
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return pd.DataFrame()


def extract_csv_data(file_path):
    """Reads a flat CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"File Error: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"
    api_df = extract_api_data(api_url)

    if not api_df.empty:
        api_df = api_df[["id", "name", "email", "company.name"]]
        api_df.rename(columns={"company.name": "company"}, inplace=True)

    print("--- API Data ---")
    print(api_df.head())

    csv_df = extract_csv_data("locations.csv")

    print("\n--- CSV Data ---")
    print(csv_df.head())

    api_df.dropna(inplace=True)
    csv_df.dropna(inplace=True)
    api_df.drop_duplicates(inplace=True)
    csv_df.drop_duplicates(inplace=True)

    if not api_df.empty and not csv_df.empty:
        merged_df = pd.merge(api_df, csv_df, on="id", how="inner")
        print("\n--- Merged ETL Pipeline Data View ---")
        print(merged_df)
        merged_df.to_csv("cleaned_warehouse_profiles.csv", index=False)
        print("\nData successfully saved to 'cleaned_warehouse_profiles.csv'")
    else:
        print("\nUnable to complete the merge.")
