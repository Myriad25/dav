import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
df = pd.DataFrame({
    'Hours Studied': [1,2,3,4,5,6,7,8,9,10],
    'Hours_Slept': [8,7,6,6,5,6,5,4,4,3],
    'Score': [12,20,28,35,45,50,60,62,70,78]
})

# Features and target
X = df[['Hours Studied', 'Hours_Slept']]
y = df['Score']

# Model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# ✅ 2D Visualization (Actual vs Predicted)
plt.scatter(y, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()])

plt.xlabel("Actual Score")
plt.ylabel("Predicted Score")
plt.title("Multiple Linear Regression (2D View)")
plt.grid(True)
plt.show()