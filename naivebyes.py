import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 1. Load & split data
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)

# 2. Fit: compute mean, variance, and prior for each class (0, 1, 2)
classes = np.unique(y_train)
mean = np.array([X_train[y_train == c].mean(axis=0) for c in classes])
var = np.array([X_train[y_train == c].var(axis=0) for c in classes])
priors = np.array([np.mean(y_train == c) for c in classes])

# 3. Predict: log-posterior = log(prior) + sum(log(Gaussian PDF))
def predict(x):
    log_pdf = -0.5 * np.log(2 * np.pi * var) - ((x - mean) ** 2) / (2 * var)
    posteriors = np.log(priors) + np.sum(log_pdf, axis=1)
    return classes[np.argmax(posteriors)]

y_pred = np.array([predict(x) for x in X_test])
print(f"Accuracy: {np.mean(y_pred == y_test):.4f}")
print("Predictions:", iris.target_names[y_pred])