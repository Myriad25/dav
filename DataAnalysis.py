# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import numpy as np

# -----------------------------
# 2. Import Dataset
# -----------------------------
df = pd.read_csv("data.csv")

# View data
print("First 5 rows:\n", df.head())

# -----------------------------
# 3. Basic Information
# -----------------------------
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# -----------------------------
# 4. Data Manipulation
# -----------------------------

# Add new column (example: yearly bonus = 10% of income)
df['bonus'] = df['income'] * 0.10

# Filter data (age > 30)
filtered = df[df['age'] > 30]
print("\nPeople with age > 30:\n", filtered)

# Group by gender and calculate average income
grouped = df.groupby('gender')['income'].mean()
print("\nAverage Income by Gender:\n", grouped)

# -----------------------------
# 5. Handling Missing Values
# -----------------------------
print("\nMissing Values:\n", df.isnull().sum())

# Example: fill missing income with mean
df['income'] = df['income'].fillna(df['income'].mean())

# -----------------------------
# 6. NumPy Operations
# -----------------------------
# Convert income column to numpy array
income_array = df['income'].values

print("\nNumPy Operations:")
print("Mean Income:", np.mean(income_array))
print("Max Income:", np.max(income_array))
print("Min Income:", np.min(income_array))
print("Standard Deviation:", np.std(income_array))

# -----------------------------
# 7. Sorting Data
# -----------------------------
sorted_df = df.sort_values(by='income', ascending=False)
print("\nSorted by Income:\n", sorted_df)

# -----------------------------
# 8. Unique Values
# -----------------------------
print("\nUnique Genders:", df['gender'].unique())