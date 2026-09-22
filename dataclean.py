import pandas as pd

df = pd.read_csv("student_dataset_100_rows.csv")

print("Original Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

numeric_columns = ["Age", "Attendance", "Maths", "Python", "SQL", "CGPA"]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

categorical_columns = ["Student_ID", "Name", "Gender", "Department"]

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])


print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:", df.duplicated().sum())


df.to_csv("student_dataset_cleaned.csv", index=False)
print("\nCleaned dataset saved successfully!")