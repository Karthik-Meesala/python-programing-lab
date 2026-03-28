import pandas as pd
df = pd.read_csv("students.csv")

print("First 5 rows of data:")
print(df.head())

print("\nLast 5 rows of data:")
print(df.tail())

print("\nInformation about DataFrame:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())