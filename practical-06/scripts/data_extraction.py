import pandas as pd
import requests

def extract_api_data(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return pd.json_normalize(response.json())

def extract_csv_data(file_path):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/users"
    api_df = extract_api_data(api_url)
    api_df = api_df[["id", "name", "email", "company.name"]]
    api_df.rename(columns={"company.name": "company"}, inplace=True)
    csv_df = extract_csv_data("locations.csv")
    api_df.dropna(inplace=True); csv_df.dropna(inplace=True)
    api_df.drop_duplicates(inplace=True); csv_df.drop_duplicates(inplace=True)
    merged_df = pd.merge(api_df, csv_df, on="id", how="inner")
    merged_df.to_csv("cleaned_warehouse_profiles.csv", index=False)
    print("ETL extraction and merge completed successfully.")
    print(merged_df)
