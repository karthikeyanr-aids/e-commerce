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
print(df["Discount %"].unique())
df.to_csv("transformed-ecommerce-data.csv", index=False)
print("\nTransformed dataset saved successfully.")