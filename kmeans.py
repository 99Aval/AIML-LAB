import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 1. Load data
X = load_iris().data
k = 3

# 2. K-Means Clustering
centroids = X[:k].copy()
for _ in range(100):
    # Distance from every point to each centroid -> shape (150, 3)
    dists = np.linalg.norm(X[:, None] - centroids, axis=2)
    labels = np.argmin(dists, axis=1)
    centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

# 3. Plot Clusters & Centroids (using first 2 features)
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='red', s=100)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-Means on Iris')
plt.show()