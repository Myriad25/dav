# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# Sample time series data (you can replace this with real data)
data = [100, 110, 108, 115, 120, 125, 130, 128, 135, 140,
        145, 150, 148, 155, 160]

# Convert to pandas series
ts = pd.Series(data)

# Plot original data
plt.plot(ts)
plt.title("Original Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# Create AR model (lag = 2 means using last 2 values)
model = AutoReg(ts, lags=2)

# Train model
model_fit = model.fit()

# Print coefficients
print("Coefficients:", model_fit.params)

# Make predictions
predictions = model_fit.predict(start=2, end=len(ts)-1)

# Plot actual vs predicted
plt.plot(ts, label="Actual")
plt.plot(predictions, color='red', label="Predicted")
plt.legend()
plt.title("AR Model Prediction")
plt.show()