## Classification :  CatBoost gradient algorithm
## Problem : Telecom Customer churn out prediction based on features.=> Output {0-> customer not churn, 1-> customer churn}
## input parameter : {tenure, monthly_bill, support_calls, internet_type, contract_type, payment_method}

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

np.random.seed(42)
n = 5000
data = pd.DataFrame({

    "tenure": np.random.randint(1, 10, n),
    "monthly_bill": np.random.normal(70, 25, n),
    "support_calls": np.random.randint(0, 6, n),
    "internet_type": np.random.choice(["fiber","dsl"], n),
    "contract_type": np.random.choice(["monthly","yearly"], n),
    "payment_method": np.random.choice(["card","bank","cash"], n)
})

# Generate Churn Probability
prob = (
    0.03 * data["monthly_bill"] +
    0.5 * data["support_calls"] -
    0.2 * data["tenure"]
)

prob = prob / prob.max()
data["churn"] = (prob > 0.45).astype(int)

# Features and Target
X = data.drop("churn", axis=1)
y = data["churn"]

# Identify categorical features
cat_features = ["internet_type","contract_type","payment_method"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# CatBoost Model
model = CatBoostClassifier(

    iterations=300,
    depth=6,
    learning_rate=0.05,
    loss_function="Logloss",
    verbose=False
)

model.fit(
    X_train,
    y_train,
    cat_features=cat_features
)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Feature Importance Plot
importance = model.get_feature_importance()
features = X.columns

plt.figure(figsize=(8,5))
plt.barh(features, importance)
plt.title("CatBoost Feature Importance")
plt.xlabel("Importance Score")
plt.show()