## Clustering : FCM - Fuzzy C-Means clustering -> Soft (probability-like membership)
## problem: Patients risk segmentation into health risk categories based on: BMI, Blood Pressure, Cholesterol Level.
## Patients can belong to multiple risk categories with varying degrees of membership (low, medium, high risk).
## input parameters: [BMI, Blood Pressure, Cholesterol Level]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from sklearn.preprocessing import StandardScaler
np.random.seed(42)
n_clusters = 3

# Low Risk
cluster1 = np.random.normal(loc=[22, 120, 180], scale=[2, 10, 15], size=(150, 3))

# Medium Risk
cluster2 = np.random.normal(loc=[27, 140, 220], scale=[2, 10, 15], size=(150, 3))

# High Risk
cluster3 = np.random.normal(loc=[32, 160, 260], scale=[2, 10, 15], size=(150, 3))

data = np.vstack((cluster1, cluster2, cluster3))
df = pd.DataFrame(data, columns=["BMI", "Blood_Pressure", "Cholesterol"])

# Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# transpose format
scaled_data = scaled_data.T
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(
    scaled_data,
    c=n_clusters,
    m=2,
    error=0.005,
    maxiter=1000,
    init=None
)

# Hard labels (highest membership)
cluster_membership = np.argmax(u, axis=0)

df["cluster"] = cluster_membership
print("Fuzzy Partition Coefficient (FPC):", fpc)

# Predict New Patients
new_patients = np.array([
    [25, 135, 210],
    [30, 155, 250]
])

new_scaled = scaler.transform(new_patients).T
u_new, _, _, _, _, _ = fuzz.cluster.cmeans_predict(
    new_scaled,
    cntr,
    m=2,
    error=0.005,
    maxiter=1000
)

predicted_cluster = np.argmax(u_new, axis=0)
print("Predicted clusters:", predicted_cluster)
print("Patient risk probabilities:\n", u_new)

plt.figure(figsize=(7,6))
plt.scatter(df["BMI"], df["Blood_Pressure"], c=df["cluster"])
plt.xlabel("BMI")
plt.ylabel("Blood Pressure")
plt.title("Fuzzy C-Means Clustering")
plt.show()