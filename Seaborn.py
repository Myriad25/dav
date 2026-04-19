# -----------------------------
# 1. Import Libraries
# -----------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 2. Load Dataset
# -----------------------------
df = pd.read_csv("data.csv")

# Style
sns.set(style="whitegrid")

# -----------------------------
# 3. Histogram (Age)
# -----------------------------
plt.figure()
sns.histplot(df['age'], bins=5, kde=True)
plt.title("Age Distribution")
plt.show()

# -----------------------------
# 4. Bar Chart (Avg Income by Gender)
# -----------------------------
plt.figure()
sns.barplot(x='gender', y='income', data=df, estimator='mean')
plt.title("Average Income by Gender")
plt.show()

# -----------------------------
# 5. Pie Chart (Gender Distribution)
# -----------------------------
plt.figure()
df['gender'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# -----------------------------
# 6. Box Plot (Income by Gender)
# -----------------------------
plt.figure()
sns.boxplot(x='gender', y='income', data=df)
plt.title("Income Distribution by Gender")
plt.show()

# -----------------------------
# 7. Violin Plot (Income by Gender)
# -----------------------------
plt.figure()
sns.violinplot(x='gender', y='income', data=df)
plt.title("Income Distribution by Gender (Violin)")
plt.show()

# -----------------------------
# 8. Regression Plot (Age vs Income)
# -----------------------------
plt.figure()
sns.regplot(x='age', y='income', data=df)
plt.title("Age vs Income (Regression)")
plt.show()