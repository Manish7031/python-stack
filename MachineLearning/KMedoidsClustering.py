## clustering : K-Medoids clustering (Partition around Medoids)
## problem : Supply Chain Delivery hub optimization by grouping the assign stores to regional hub, reduce transportation cost, 
#            identify actual real stores based on stores Latitude, Longitude, Daily delivery volume.
## input parameters : Region Latitude, Longitude, Daily delivery volume
# K-Medoids Clustering Example
# Real-world scenario: Delivery hub optimization

import numpy as np
import pandas as pd
from sklearn_extra.cluster import KMedoids
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.default_rng(42)
# Region 1
region1 = np.random.normal(loc=[12.97, 77.59, 200], scale=[0.02, 0.02, 20], size=(100, 3))
# Region 2
region2 = np.random.normal(loc=[28.61, 77.20, 150], scale=[0.02, 0.02, 15], size=(100, 3))
# Region 3
region3 = np.random.normal(loc=[19.07, 72.87, 180], scale=[0.02, 0.02, 25], size=(100, 3))

data = np.vstack((region1, region2, region3))

df = pd.DataFrame(data, columns=["Latitude", "Longitude", "Daily_Volume"])

print("Raw_Data : ")
print(df.head())

X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)
# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
kmedoids = KMedoids(n_clusters=3, random_state=42, method='pam')
kmedoids.fit(X_train_scaled)

train_clusters = kmedoids.predict(X_train_scaled)
test_clusters = kmedoids.predict(X_test_scaled)

print("\nTest Cluster Predictions (first 10):")
print(test_clusters[:10])

# Identify Medoids
medoid_indices = kmedoids.medoid_indices_
print("\nMedoid Indices:", medoid_indices)
print("\nRepresentative Stores (Medoids):")
print(X_train.iloc[medoid_indices])

plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=train_clusters)
plt.title("K-Medoids Clustering (Latitude vs Longitude)")
plt.xlabel("Latitude scaled")
plt.ylabel("Longitude scaled")
plt.show()
