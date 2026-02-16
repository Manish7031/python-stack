## classification: Logistic Regression
## problem: Customer churn and segmentation prediction analysis
## input parameters: customer tenure, monthly charge, total spend, customer calls

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


np.random.seed(42)
data = pd.DataFrame({
    "tenure": np.random.randint(1, 60, 100),
    "monthly_charges": np.random.randint(20, 120, 100),
    "total_spend": np.random.randint(100, 5000, 100),
    "support_calls": np.random.randint(0, 10, 100),
})

# Create target variable
data["churn"] = (
    (data["support_calls"] > 5) &
    (data["tenure"] < 12)
).astype(int)

# Separate Features and Target
X = data.drop("churn", axis=1)
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Logistic Regression Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predict New Customer
new_customer = pd.DataFrame({
    "tenure": [10],
    "monthly_charges": [399],
    "total_spend": [500],
    "support_calls": [5]
})

prediction = model.predict(new_customer)
probability = model.predict_proba(new_customer)

if prediction[0] == 1:
    print("\nPrediction: Customer Likely to Churn")
else:
    print("\nPrediction: Customer Likely to Stay")

print("Churn Probability:", probability[0][1])
