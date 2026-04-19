# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 2. Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")

# -----------------------------
# 3. Histogram (Age)
# -----------------------------
plt.figure()
plt.hist(df['age'], edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 4. Bar Chart (Avg Income by Gender)
# -----------------------------
avg_income = df.groupby('gender')['income'].mean()

plt.figure()
plt.bar(avg_income.index, avg_income.values)
plt.title("Average Income by Gender")
plt.xlabel("Gender")
plt.ylabel("Income")
plt.show()

# -----------------------------
# 5. Pie Chart (Gender Count)
# -----------------------------
gender_count = df['gender'].value_counts()

plt.figure()
plt.pie(gender_count.values, labels=gender_count.index, autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.show()

# -----------------------------
# 6. Box Plot (Income)
# -----------------------------
plt.figure()
plt.boxplot(df['income'])
plt.title("Income Distribution")
plt.ylabel("Income")
plt.show()

# -----------------------------
# 7. Violin Plot (Income by Gender)
# -----------------------------
plt.figure()
sns.violinplot(x='gender', y='income', data=df)
plt.title("Income Distribution by Gender")
plt.show()

# -----------------------------
# 8. Regression Plot (Age vs Income)
# -----------------------------
plt.figure()
sns.regplot(x='age', y='income', data=df)
plt.title("Age vs Income (Regression)")
plt.show()