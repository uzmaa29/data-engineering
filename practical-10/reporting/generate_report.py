from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "transformed"
OUT = ROOT / "reporting" / "reports"
OUT.mkdir(exist_ok=True)

fact = pd.read_csv(DATA / "fact_sales.csv", parse_dates=["OrderDate"])
products = pd.read_csv(DATA / "dim_product.csv")

fact = fact.merge(products[["ProductID", "ProductName", "Category"]], on="ProductID", how="left")

summary = pd.DataFrame({
    "Metric": ["Total Revenue", "Total Orders", "Total Units"],
    "Value": [fact["TotalAmount"].sum(), fact["OrderID"].nunique(), fact["Quantity"].sum()]
})
category = fact.groupby("Category", as_index=False)["TotalAmount"].sum().sort_values("TotalAmount", ascending=False)
monthly = fact.assign(Month=fact["OrderDate"].dt.to_period("M").astype(str)).groupby("Month", as_index=False)["TotalAmount"].sum()

with pd.ExcelWriter(OUT / "sales_report.xlsx", engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    category.to_excel(writer, sheet_name="By_Category", index=False)
    monthly.to_excel(writer, sheet_name="Monthly_Sales", index=False)

summary.to_csv(OUT / "summary_report.csv", index=False)
category.to_csv(OUT / "category_report.csv", index=False)
monthly.to_csv(OUT / "monthly_report.csv", index=False)
print(summary)
print("Reports generated in reporting/reports/")
