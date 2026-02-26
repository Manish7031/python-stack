# Clustering : Connectivity-Based Divisive Clustering(Top down)
# problem : Telecom Network Optimization, customer segmentation , identify balanced load distribution in regions and 
#           distinct customer groups based on usage patterns and demographics for targeted marketing strategies.
# input parameter : [ Data usage (GB/month), 
#                     Call duration (minutes/day), 
#                     Distance to nearest tower(km) ]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import kneighbors_graph
from sklearn.metrics import pairwise_distances_argmin

#np.random.seed(42)
np.random.default_rng(42)
cluster1 = np.random.normal(loc=[50, 200, 2], scale=[10, 30, 1], size=(200, 3))
cluster2 = np.random.normal(loc=[100, 400, 5], scale=[15, 40, 1], size=(200, 3))
cluster3 = np.random.normal(loc=[150, 600, 8], scale=[20, 50, 1], size=(200, 3))

data = np.vstack((cluster1, cluster2, cluster3))
df = pd.DataFrame(data, columns=["data_usage", "call_duration", "distance_tower"])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Connectivity Graph
connectivity = kneighbors_graph(scaled_data, n_neighbors=10, include_self=False)

# Divisive Clustering
n_clusters = 3
cluster_labels = np.zeros(len(scaled_data))
current_clusters = {0: scaled_data}
next_cluster_id = 1

while len(current_clusters) < n_clusters:
    
    # Find largest cluster
    largest_cluster_id = max(current_clusters, 
                             key=lambda k: len(current_clusters[k]))
    
    cluster_data = current_clusters.pop(largest_cluster_id)
    kmeans = KMeans(n_clusters=2, random_state=42)
    sub_labels = kmeans.fit_predict(cluster_data)
    
    # Store new clusters
    current_clusters[largest_cluster_id] = cluster_data[sub_labels == 0]
    current_clusters[next_cluster_id] = cluster_data[sub_labels == 1]
    
    next_cluster_id += 1

# Assign Final Labels
final_labels = np.zeros(len(scaled_data))

for cluster_id, cluster_data in current_clusters.items():
    indices = np.where(
        (scaled_data[:, None] == cluster_data).all(-1).any(1)
    )[0]
    final_labels[indices] = cluster_id

df["cluster"] = final_labels

# Centroids
centroids = []
for i in range(n_clusters):
    centroids.append(
        scaled_data[df["cluster"] == i].mean(axis=0)
    )
centroids = np.array(centroids)

# Predict New Telecom Users
new_users1 = np.array([
    [60, 220, 3],
    [140, 550, 7]
])

new_scaled = scaler.transform(new_users1)
predicted_clusters = pairwise_distances_argmin(
    new_scaled,
    centroids
)

print("Predicted clusters:", predicted_clusters)

plt.figure(figsize=(7,6))
plt.scatter(df["data_usage"], df["call_duration"], c=df["cluster"])
plt.xlabel("Data Usage (GB)")
plt.ylabel("Call Duration (min/day)")
plt.title("Connectivity-Based Divisive Clustering")
plt.show()