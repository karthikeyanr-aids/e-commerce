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