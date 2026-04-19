# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'message': [
        "Win money now", "Hello friend", "Free entry in contest",
        "Call me later", "Congratulations you won prize",
        "Let's meet tomorrow"
    ],
    'label': [1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

# Features and target
X = df['message']
y = df['label']

# Convert text to numerical form
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.3, random_state=42
)

# Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test with new message
msg = ["Free money offer"]
msg_vec = vectorizer.transform(msg)
print("Spam Prediction (1=Spam):", model.predict(msg_vec)[0])