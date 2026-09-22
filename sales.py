import pandas as pd

df = pd.read_csv("sales_dataset_100_rows.csv")

columns = ["Sales", "Price", "Quantity", "Profit"]

for col in columns:
    print("\n", col)
    print("Mean:", df[col].mean())
    print("Median:", df[col].median())
    print("Minimum:", df[col].min())
    print("Maximum:", df[col].max())
    print("Sum:", df[col].sum())

city_sales = df.groupby("City")["Sales"].sum()
print("\n",city_sales)

category_sales = df.groupby("Category")["Sales"].mean()
print("\n",category_sales)

product_quantity = df.groupby("Product")["Quantity"].sum()
print("\n",product_quantity)

salespersons_profit = df.groupby("Salesperson")["Profit"].mean()
print("\n",salespersons_profit)

print("\n SORTING")
print("\nTop 5 Rows by sales")
top5_sales = df.sort_values("Sales",ascending=False).head(5)
print("\n",top5_sales)

print("\nBottom 5 Rows by sales")
bottom5_sales = df.sort_values("Sales",ascending=True).head(5)
print("\n",bottom5_sales)

sales_above_100000 = df[df["Sales"] > 100000]
print("\n",sales_above_100000)

profit_above_10000 = df[df["Profit"] > 10000]
print("\n",profit_above_10000)

quantity_above_15 = df[df["Quantity"] > 15]
print("\n",quantity_above_15)

result = df[
    (df["Sales"] > 10000) &
    (df["Profit"] > 2000)
]
print("\n",result)

result = df[
    (df["Sales"] > 100000) |
    (df["Profit"] > 20000)
]
print("\n",result)

result = df[~(df["City"] == "Chennai")]
print("\n",result)

result_1= df.groupby("Category").agg(
    {
        "Sales": ["sum", "mean"],
        "Quantity": ["sum", "mean"],
        "Profit": ["sum", "mean"]
    }
)
print("\n",result)

city_sales.to_csv("sales_by_city.csv")

category_sales.to_csv("average_sales_by_category.csv")

top5_sales.to_csv("top5_sales.csv", index=False)

bottom5_sales.to_csv("bottom5_sales.csv", index=False)

sales_above_100000.to_csv("sales_above_100000.csv", index=False)

profit_above_10000.to_csv("profit_above_10000.csv", index=False)

result_1.to_csv("category_aggregation.csv")

