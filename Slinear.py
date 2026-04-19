# Import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data (Age vs Income)
age = np.array([22, 25, 27, 29, 30, 31, 33, 35, 40]).reshape(-1, 1)
income = np.array([28000, 34000, 42000, 50000, 45000, 53000, 58000, 55000, 67000])

# Create model
model = LinearRegression()

# Train model
model.fit(age, income)

# Predict
predicted_income = model.predict(age)

# Print results
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

# Plot
plt.scatter(age, income)            # actual data
plt.plot(age, predicted_income)     # regression line
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Simple Linear Regression")
plt.show()