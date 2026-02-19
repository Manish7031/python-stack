## Regression : Ridge vs Lasso Regression
## problem : House Price Prediction with Many Correlated Features
## input data parameters: evaulation paramerter for real state model
# [House Area (sqft), 
# Number of bedrooms, 
# Number of bathrooms, 
# property age, 
# Distance from city, 
# Nearby school rating, 
# Near shopping centre, 
# Crime index, 
# Near Airport distance ]

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

np.random.default_rng(42)
n = 600

dataset = {
    "sqft": np.random.normal(1500, 400, n),
    "bedrooms": np.random.randint(1, 6, n),
    "bathrooms": np.random.randint(1, 4, n),
    "prop_age": np.random.randint(0, 30, n),
    "distance_city_center": np.random.normal(8, 4, n),
    "distance_airport": np.random.normal(12, 5, n),
    "distance_shopping_mall": np.random.normal(3, 2, n),
    "school_rating": np.random.randint(1, 10, n),
    "crime_index": np.random.normal(50, 15, n)
}
data =  pd.DataFrame(dataset)

# Target Variable (Price)
data["price"] = (
    4500 * data["sqft"] +
    18000 * data["bedrooms"] +
    12000 * data["bathrooms"] -
    2500 * data["prop_age"] -
    8000 * data["distance_city_center"] -
    4000 * data["distance_airport"] -
    6000 * data["distance_shopping_mall"] +
    22000 * data["school_rating"] -
    1500 * data["crime_index"] +
    np.random.normal(0, 40000, n)
)

X = data.drop("price", axis=1)
y = data["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Ridge & Lasso model
# Ridge Regression → Handles multicollinearity (L2 regularization)
# Lasso Regression → Performs feature selection (L1 regularization)
ridge = Ridge(alpha=20)
lasso = Lasso(alpha=2000)
ridge.fit(X_train_scaled, y_train)
lasso.fit(X_train_scaled, y_train)

#Prediction
ridge_pred = ridge.predict(X_test_scaled)
lasso_pred = lasso.predict(X_test_scaled)

## accuracy
print("Ridge R2 Score:", r2_score(y_test, ridge_pred))
print("Lasso R2 Score:", r2_score(y_test, lasso_pred))

print("\nRidge RMSE:", np.sqrt(mean_squared_error(y_test, ridge_pred)))
print("Lasso RMSE:", np.sqrt(mean_squared_error(y_test, lasso_pred)))

# Coefficient Comparison
coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Ridge Coefficient": ridge.coef_,
    "Lasso Coefficient": lasso.coef_
})

print("\nFeature Coefficients Comparison:")
print(coef_df.sort_values(by="Lasso Coefficient", key=abs, ascending=False))


