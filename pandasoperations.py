import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Ravi", "Sai", "Ram", "Kiran", "Arun"],
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
sorted_df = df.sort_values(by="Marks")
print("\nSorted DataFrame (by Marks):")
print(sorted_df)
print("\nFirst 3 rows:")
print(df.iloc[0:3])
print("\nSelected columns (Name, Marks):")
print(df[["Name", "Marks"]])