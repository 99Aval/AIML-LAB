import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load & split data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# 2. KNN Predict function
def knn(X_train, y_train, x, k=3):
    dists = np.linalg.norm(X_train - x, axis=1)      # Euclidean distance to all points
    k_labels = y_train[np.argsort(dists)[:k]]        # Labels of k nearest neighbors
    return np.bincount(k_labels).argmax()            # Most frequent class label

# 3. Evaluate accuracy
y_pred = [knn(X_train, y_train, x, k=3) for x in X_test]
print(f"Accuracy: {np.mean(y_pred == y_test):.2f}")