## Clustering : Gaussian Mixture Model (probabilistic clustering)
## problem : Customers segmentation prediction analysis based on income and spending for target marketing.
## input parameters : Annual income, Spending score, Purchase frequency

import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.seed(42)
# Cluster 1 -> High income, High spending
cluster1 = np.random.normal(loc=[80, 85], scale=[5, 5], size=(100, 2))

# Cluster 2 -> High income, Low spending
cluster2 = np.random.normal(loc=[85, 30], scale=[5, 5], size=(100, 2))

# Cluster 3 -> Low income, High spending
cluster3 = np.random.normal(loc=[30, 75], scale=[5, 5], size=(100, 2))

data = np.vstack((cluster1, cluster2, cluster3))
df = pd.DataFrame(data, columns=["Annual_Income", "Spending_Score"])

print("Sample Data:")
print(df.head())

X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)
# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# model
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X_train_scaled)

# compare with K-means prediction
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train_scaled)

# prediction
train_clusters = gmm.predict(X_train_scaled)
test_clusters = gmm.predict(X_test_scaled)

kmeans_pred = kmeans.predict(X_test_scaled)
print("K-Means Predictions (first 10):")
print(kmeans_pred[:10])

print("\nGMM Cluster Predictions (first 10) :")
print(test_clusters[:10])

# Cluster Probabilities
test_probabilities = gmm.predict_proba(X_test_scaled)

print("\nCluster Membership Probabilities (First 5 Test) : ")
print(test_probabilities[:5])

plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], c=train_clusters, cmap='viridis')
plt.title("Gaussian Mixture Clustering")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()
