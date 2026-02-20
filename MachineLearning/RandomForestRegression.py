## Regression: Random Forest
## problem : Vehicle resale value price prediction based on input data.
## input data parameter : [
# engine_size in liter,
# engine HP,
# vehicle age (years),
# mileage (Kms)
# MPG,
# Brand,
# accident_records
# ]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

np.random.seed(42)
n = 1000

_raw_data = {
    "engine_size": np.random.normal(2.0, 0.5, n),        
    "horsepower": np.random.normal(150, 40, n),
    "age": np.random.randint(0, 15, n),                   
    "mileage": np.random.normal(60000, 20000, n),         
    "mpg": np.random.normal(25, 5, n),
    "brand_rating": np.random.randint(1, 10, n),
    "accident_history": np.random.randint(0, 3, n)
}
data = pd.DataFrame(_raw_data)
# Non-linear price function
data["price"] = (
    8000 * data["engine_size"] +
    150 * data["horsepower"] -
    1200 * data["age"] -
    0.05 * data["mileage"] +
    2000 * data["brand_rating"] -
    3000 * data["accident_history"] +
    1000 * np.sin(data["engine_size"]) +  # non-linear component
    np.random.normal(0, 2000, n)          # adding some random noise
)

X = data.drop("price", axis=1)
y = data["price"]
y_tolist = np.array(data['price'].tolist())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# model
rf = RandomForestRegressor(n_estimators=200, max_depth=None, random_state=42)
rf.fit(X_train, y_train)

#prediction
y_pred = rf.predict(X_test)

#evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("mean absolute error :", mean_absolute_error(y_test, y_pred))

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(importance)

# prediction
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Random Forest: Actual vs Predicted Price")
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()])
plt.show()
