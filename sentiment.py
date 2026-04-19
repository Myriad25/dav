# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'review': [
        "I love this product",
        "This is terrible",
        "Awesome Product",
        "Worst service ever",
        "Very happy with purchase",
        "I hate it"
    ],
    'sentiment': [1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative
}

df = pd.DataFrame(data)

# Features and target
X = df['review']
y = df['sentiment']

# Convert text to numerical form
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.3, random_state=42
)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test with new review
review = ["This product is awesome"]
review_vec = vectorizer.transform(review)
print("Sentiment (1=Positive):", model.predict(review_vec)[0])