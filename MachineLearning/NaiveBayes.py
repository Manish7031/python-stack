## classification: Naive Bayes
## porblem: classifiy emails/text as SPAM(1) and not SPAM(0)
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


raw_data = {
    "email": [
        "Win money now",
        "Limited time offer",
        "Meeting scheduled tomorrow",
        "Project discussion update",
        "Claim your free prize",
        "Let's have lunch tomorrow",
        "Get cheap loans instantly",
        "Team meeting minutes attached",
        "claim your offer now",
        "claim discount to click link here"
    ],
    "label": [1, 1, 0, 0, 1, 0, 1, 0, 1, 1]   # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(raw_data)

X_train, X_test, y_train, y_test = train_test_split(
    df["email"], df["label"], test_size=0.3, random_state=42)

##Convert Text to TF-IDF Features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predictions
y_pred = model.predict(X_test_tfidf)

print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Predict on New Email
new_email = ["Congratulations! You won a free vacation"]
new_email_tfidf = vectorizer.transform(new_email)
prediction = model.predict(new_email_tfidf)

if prediction[0] == 1:
    print("\nPrediction: Spam")
else:
    print("\nPrediction: Not Spam")
