import numpy as np
from sklearn.datasets import load_iris

# 1. Load Iris (only Setosa=0 and Versicolor=1)
iris = load_iris()
mask = iris.target < 2
X, y = iris.data[mask], iris.target[mask]

# 2. Manual Standardization (no StandardScaler)
mean, std = X.mean(axis=0), X.std(axis=0)
X_std = (X - mean) / std

# 3. Manual Logistic Regression
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

w = np.zeros(X.shape[1])
b = 0.0
lr = 0.1

for _ in range(1000):
    h = sigmoid(np.dot(X_std, w) + b)
    w -= lr * np.dot(X_std.T, (h - y)) / len(y)
    b -= lr * np.mean(h - y)

# 4. Predict on User Input
user_x = np.array(list(map(float, input("Enter 4 features: ").split())))
user_std = (user_x - mean) / std
prob = sigmoid(np.dot(user_std, w) + b)

print("Versicolor" if prob >= 0.5 else "Setosa")