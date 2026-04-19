# Pandas
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
# Filter rows where Age > 25
filtered_df=df[df['Age'] > 25]
print(filtered_df)

# Numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
# Calculate the mean of the array
mean_value = np.mean(arr)
print(mean_value)

# Matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Seaborn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = {'A':[1, 2, 3, 4], 'B':[2, 3, 4, 5]}
df = pd.DataFrame(data)
sns.scatterplot(x='A', y='B', data=df)
plt.show()

# Scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1], [2], [3], [4]])
y = np.array([2.2, 4.3, 6.1, 8.0])
model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[5]])
print(prediction)

# SciPy
from scipy.stats import norm
x = 1
prob_density = norm.pdf(x, loc=0, scale=1)
print(prob_density)

# Plotly
import plotly.express as px
data = {'Name':['Alice', 'Bob', 'Charlie'], 'Score':[85, 90, 95]}
fig = px.bar(data, x='Name', y='Score', title='Student Scores')
fig.show()

# Statsmodels
import statsmodels.api as sm
X = [1, 2, 3, 4]
y = [2.2, 4.3, 6.1, 8.0]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

# TensorFlow
import tensorflow as tf
tensor = tf.constant([[1, 2], [3, 4]])
print(tensor)

# OpenCV
import cv2
image = cv2.imread('example.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
