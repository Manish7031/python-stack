# clustering : Connectivity-Based Agglomerative Clustering(bottom up)
# problem : Retail Customer Segmentation for annual spending based on Annual Income, Spending Score, Distance from Store
# input parameter : Annual Income, Spending Score, Distance from Store

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances_argmin

np.random.seed(42)
# Cluster 1
cluster1 = np.random.normal(loc=[40, 60, 2], scale=[5, 10, 1], size=(150, 3))

# Cluster 2
cluster2 = np.random.normal(loc=[80, 30, 5], scale=[7, 8, 1], size=(150, 3))

# Cluster 3
cluster3 = np.random.normal(loc=[120, 80, 8], scale=[6, 12, 1], size=(150, 3))

data = np.vstack((cluster1, cluster2, cluster3))
df = pd.DataFrame(data, columns=["income", "spending_score", "distance_from_store"])

#Feature Scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Create Connectivity Graph
connectivity = kneighbors_graph(scaled_data, n_neighbors=10, include_self=False)

# Model
model = AgglomerativeClustering(
    n_clusters=3,
    connectivity=connectivity,
    linkage='ward'
)

clusters = model.fit_predict(scaled_data)
df["cluster"] = clusters

# Evaluation
centroids = []
for i in range(3):
    centroids.append(scaled_data[clusters == i].mean(axis=0))
centroids = np.array(centroids)

# Predict New Customers
new_customers = np.array([
    [50, 70, 3],
    [110, 75, 7]
])

new_scaled = scaler.transform(new_customers)
predicted_clusters = pairwise_distances_argmin(new_scaled, centroids)
print("Predicted clusters for new customers:", predicted_clusters)

plt.figure(figsize=(7,6))
plt.scatter(df["income"], df["spending_score"], c=df["cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Connectivity-Based Agglomerative Clustering")
plt.show()