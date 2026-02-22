## Clustering : DBSCAN
## problem: credit card fraud transactions detections based on fraud pattern: Rare, Irregular, Do not form clear spherical clusters, isolated points.
## input transaction parameters: [Transaction amount, Transaction time gap, Distance from home location, Merchant risk score]
## assigns labels: 0, 1, 2 → clusters
## anomaly : -1 → noise

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
np.random.seed(42)

# Normal transactions cluster 1
cluster1 = np.random.normal(loc=[200, 2], scale=[50, 1], size=(300, 2))

# Normal transactions cluster 2
cluster2 = np.random.normal(loc=[500, 5], scale=[60, 1], size=(300, 2))

# Fraud transactions (outliers)
fraud = np.random.uniform(low=[1000, 10], high=[2000, 20], size=(30, 2))

data = np.vstack((cluster1, cluster2, fraud))
df = pd.DataFrame(data, columns=["transaction_amount", "distance_from_home"])

# Feature Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(scaled_data)

df["cluster"] = clusters

# Count Clusters
print("Unique cluster labels:", set(clusters))
print("Number of fraud (noise points):", list(clusters).count(-1))

plt.figure(figsize=(7,6))
plt.scatter(df["transaction_amount"], df["distance_from_home"], c=df["cluster"])
plt.xlabel("Transaction Amount")
plt.ylabel("Distance From Home")
plt.title("DBSCAN Clustering (Fraud Detection)")
plt.show()