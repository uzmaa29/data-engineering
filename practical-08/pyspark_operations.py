from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, sum, count

spark = SparkSession.builder.appName("PySpark DataFrame Operations").getOrCreate()

# 1. Read CSV and display schema
sales_df = spark.read.csv("data/sales.csv", header=True, inferSchema=True)
print("\n--- Sales Dataset ---")
sales_df.show()
print("\n--- Dataset Schema ---")
sales_df.printSchema()

# 2. Filtering, grouping and aggregation
print("\n--- Filtered Sales (Sales > 1000) ---")
sales_df.filter(sales_df["Sales"] > 1000).show()

print("\n--- Sales Grouped by Category ---")
sales_df.groupBy("Category").agg(
    sum("Sales").alias("Total_Sales"),
    count("*").alias("Number_of_Records")
).show()

# 3. Remove duplicate records
print("\n--- Duplicate Removal ---")
print("Records before:", sales_df.count())
unique_df = sales_df.dropDuplicates()
print("Records after:", unique_df.count())
unique_df.show()

# 4. Join two datasets
products_df = spark.read.csv("data/products.csv", header=True, inferSchema=True)
print("\n--- Products Dataset ---")
products_df.show()

joined_df = sales_df.join(
    products_df,
    sales_df["ProductID"] == products_df["ProductID"],
    "inner"
)
print("\n--- Joined Dataset ---")
joined_df.show()

# 5. Average sales by product category
print("\n--- Average Sales by Category ---")
sales_df.groupBy("Category").agg(
    avg("Sales").alias("Average_Sales")
).show()

spark.stop()
