import pandas as pd
import numpy as np
df = pd.read_csv("ecommerce_data.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.isnull().sum())
print("\nDuplicate Rows:",df.duplicated().sum())
print(df[df.duplicated()])
print("\n",df.tail())
print("\n",df.describe())
prices = np.array(df["Price"].dropna())
print("Average Price:", np.mean(prices))
print("Minimum Price:", np.min(prices))
print("Maximum Price:", np.max(prices))

print("\nCLEANING DATA PROCESS")

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df["Price"] = df["Price"].fillna(df["Price"].median())
df["Customer_City"] = df["Customer_City"].fillna(df["Customer_City"].mode()[0])
df["Payment_Method"] = df["Payment_Method"].fillna(df["Payment_Method"].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df = df.drop_duplicates()
print("\nAfter removing duplicates:", df.duplicated().sum())

categorical_columns = ["Product", "Category", "Customer_City", "Payment_Method"]
for column in categorical_columns:
    df[column] = df[column].str.strip()

for column in categorical_columns:
    df[column]=df[column].str.title()  

print("\n")
print(df["Category"].unique())
print(df["Payment_Method"].unique())
print(df["Customer_City"].unique())
print(df["Product"].unique())

df["Quantity"] = df["Quantity"].astype(int)
print("\n",df.dtypes)

print("\nInvalid Prices:", np.sum(df["Price"] < 0))
print("\nInvalid Quantities:", np.sum(df["Quantity"] <= 0))

df.to_csv("cleaned_ecommerce_data.csv", index=False)

df = pd.read_csv("cleaned_ecommerce_data.csv")

print("\nDATA TRANSFORMATION PROCESS")

df["Total Sales"] = df["Quantity"] * df["Price"]
df["Discount %"] = np.where(df["Total Sales"] >= 50000, 10,np.where(df["Total Sales"] >= 20000, 5, 0))
df["Discount Amount"] = df["Total Sales"] * df["Discount %"] / 100
df["Net Sales"] = df["Total Sales"] - df["Discount Amount"]
df["Profit"] = df["Net Sales"] * 0.10
df["Profit Margin"] = df["Profit"] / df["Net Sales"] * 100

print("\n",df[[
    "Order_ID",
    "Quantity",
    "Price",
    "Total Sales",
    "Discount %",
    "Discount Amount",
    "Net Sales",
    "Profit",
    "Profit Margin"
]].head())
print(df[[
    "Total Sales",
    "Discount %",
    "Discount Amount",
    "Net Sales",
    "Profit",
    "Profit Margin"
]].isnull().sum())
print((df["Net Sales"] < 0).sum())
print((df["Profit"] < 0).sum())
print(df["Discount %"].unique())
print(df["Profit Margin"].unique())
print((df["Profit"] < 0).sum())
print((df["Net Sales"] < 0).sum())
df.to_csv("transformed-ecommerce-data.csv", index=False)

print("\nTransformed dataset saved successfully.")

df = pd.read_csv("transformed-ecommerce-data.csv")

print("\nDATA ANALYSIS PROCESS")

print("Dataset Shape:", df.shape)

print("\nTotal Sales:")
print(df["Total Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())

print("\nAverage Sales:")
print(df["Total Sales"].mean())

print("\nAverage Profit:")
print(df["Profit"].mean())

print("\nSales by Category:")
sales_by_category = df.groupby("Category")["Total Sales"].sum()
print(sales_by_category)

print("\nSales by City:")
print(df.groupby("Customer_City")["Total Sales"].sum())


print("\nProfit by Category:")
print(df.groupby("Category")["Profit"].sum())


print("\nQuantity by Category:")
print(df.groupby("Category")["Quantity"].sum())

print("\nTop 5 Products by Sales:")
top_products = (
    df.groupby("Product")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_products)

print("\nTop 5 Products by Quantity:")
top_quantity_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_quantity_products)

print("\nTop 5 Customers City:")
top_customers = (
    df.groupby("Customer_City")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_customers)

print("\nPayment Method Analysis:")
payment_analysis = df.groupby("Payment_Method")["Total Sales"].sum()
print(payment_analysis)

print("\nHighest Sale:")
print(df["Total Sales"].max())

print("\nLowest Sale:")
print(df["Total Sales"].min())

print("\nAverage Quantity per Order:")
print(df["Quantity"].mean())

print("\nProfit Margin:")
print(df["Profit Margin"].mean())

print("\nHighest profit:")
print(df["Profit"].max())

print("\nLowest profit:")
print(df["Profit"].min())

print("\nHighest Price:")
print(df["Price"].max())

print("\nLowest Price:")
print(df["Price"].min())

print("\nAverage Price:")
print(df["Price"].mean())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df["Profit Margin"] = df["Profit Margin"].astype(int)

print(df.dtypes)

print("\nAnalysis completed successfully.")

df.to_csv("processed-ecommerce-data.csv", index=False)

print("\nETL Pipeline completed successfully!")