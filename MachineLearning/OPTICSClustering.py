## Clustering : density based OPTICS (Ordering Points To Identify Clustering Structure)
## problem: Identify high crime hotspots in a city based on crime incident data: region coordinates, crime severity score.
## input parameters: [Latitude, Longitude, Crime severity score]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import OPTICS
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances_argmin

np.random.seed(42)
# High density crime zone
cluster1 = np.random.normal(loc=[19.07, 72.87], scale=[0.01, 0.01], size=(200, 2))

# Medium density crime zone
cluster2 = np.random.normal(loc=[19.10, 72.90], scale=[0.02, 0.02], size=(150, 2))

# Less crime zone
cluster3 = np.random.normal(loc=[19.15, 72.85], scale=[0.03, 0.03], size=(100, 2))

# Random noise (isolated crimes)
noise = np.random.uniform(low=[19.00, 72.80], high=[19.20, 73.00], size=(30, 2))

data = np.vstack((cluster1, cluster2, cluster3, noise))
df = pd.DataFrame(data, columns=["latitude", "longitude"])

# Feature Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# OPTICS Model
optics_model = OPTICS(min_samples=10, xi=0.05, min_cluster_size=0.05)
clusters = optics_model.fit_predict(scaled_data)
df["cluster"] = clusters
print("Unique cluster labels:", set(clusters))
print("Number of noise points:", list(clusters).count(-1))

# Compute Centroids
unique_clusters = [c for c in set(clusters) if c != -1]
centroids = []
for c in unique_clusters:
    centroids.append(
        scaled_data[clusters == c].mean(axis=0)
    )

centroids = np.array(centroids)

# Predict New Crime Events
new_crime1 = np.array([
    [19.08, 72.88],
    [19.18, 72.95]
])

new_scaled = scaler.transform(new_crime1)
predicted_clusters = pairwise_distances_argmin(
    new_scaled,
    centroids
)

print("Predicted cluster for new events:", predicted_clusters)

plt.figure(figsize=(7,6))
plt.scatter(df["latitude"], df["longitude"], c=df["cluster"])
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.title("OPTICS Crime Hotspot Clustering")
plt.plot(new_crime1[:, 0], new_crime1[:, 1], 'kx', markersize=10, label='New Crime Events', color='r')
plt.show()