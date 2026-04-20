# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Sample time series data (replace with real data if needed)
data = [100, 110, 108, 115, 120, 125, 130, 128, 135, 140,
        145, 150, 148, 155, 160]

ts = pd.Series(data)

# Plot original data
plt.plot(ts)
plt.title("Original Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# Build ARIMA model (p=2, d=1, q=2)
model = ARIMA(ts, order=(2, 1, 2))

# Train model
model_fit = model.fit()

# Summary
print(model_fit.summary())

# Make predictions (in-sample)
predictions = model_fit.predict(start=1, end=len(ts)-1)

# Plot actual vs predicted
plt.plot(ts, label="Actual")
plt.plot(predictions, color='red', label="Predicted")
plt.legend()
plt.title("ARIMA Model Prediction")
plt.show()

# Forecast future values
forecast = model_fit.forecast(steps=5)
print("Future Forecast:", forecast)