## classification: XGBoost
## problem: financial analysis to predict Risk for customer loan defaulter. 1 : Default on loan |0 : Not default
# input parameter: income, credit score, age, loan amount
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

np.random.seed(42)
data = pd.DataFrame({
    "income": np.random.randint(20000, 120000, 100),
    "credit_score": np.random.randint(300, 850, 100),
    "age": np.random.randint(21, 65, 100),
    "loan_amount": np.random.randint(5000, 500000, 100),
})

#Create target variable
data["default"] = (
    (data["credit_score"] < 500) &
    (data["loan_amount"] > 30000)
).astype(int)

#Split Features & Target
X = data.drop("default", axis=1)
y = data["default"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#XGBoost Model
model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss'
)

model.fit(X_train, y_train)

#Prediction
y_pred = model.predict(X_test)

#accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Predict on New Customer
new_customer = pd.DataFrame({
    "income": [40000],
    "credit_score": [500],
    "age": [30],
    "loan_amount": [50000]
})

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("\nPrediction: High Risk (Likely to Default)")
else:
    print("\nPrediction: Low Risk (No default Customer)")
