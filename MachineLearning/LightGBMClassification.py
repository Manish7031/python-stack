## classification : light GBM (Light Gradient Boosting Machine) -> open source ensemble learning framework
## problem : Credit Card Fraud Detection model based on input parameter. output=> classify transaction :{ 0= Normal, 1= Fraud}
## input featues = [Transaction amount, Time of transaction, Distance from home location, Merchant category, Number of transactions in last hour]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

np.random.seed(42)
n = 5000

data = pd.DataFrame({
    "transaction_amount": np.random.normal(200, 150, n),
    "distance_from_home": np.random.normal(10, 5, n),
    "merchant_risk_score": np.random.uniform(0, 1, n),
    "transactions_last_hour": np.random.randint(0, 10, n),
    "card_age_years": np.random.randint(1, 10, n)
})

# Fraud probability rule
fraud_probability = (
    0.002 * data["transaction_amount"] +
    0.05 * data["distance_from_home"] +
    0.7 * data["merchant_risk_score"] +
    0.1 * data["transactions_last_hour"]
)

fraud_probability = fraud_probability / fraud_probability.max()
data["fraud"] = (fraud_probability > 0.55).astype(int)

# Feature / Target
X = data.drop("fraud", axis=1)
y = data["fraud"]

# split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train LightGBM Model
model = lgb.LGBMClassifier(
    
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("\nClassification Report")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# Feature Importance Plot

importance = model.feature_importances_
features = X.columns

plt.figure(figsize=(8,5))
plt.barh(features, importance)
plt.title("LightGBM Feature Importance")
plt.xlabel("Importance Score")
plt.show()