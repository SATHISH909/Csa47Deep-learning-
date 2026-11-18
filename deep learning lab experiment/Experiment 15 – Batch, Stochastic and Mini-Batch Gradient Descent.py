
import numpy as np

# Generate sample dataset
np.random.seed(42)
X = np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1) * 0.1

# Initialize parameters
learning_rate = 0.1
iterations = 100

# Batch Gradient Descent
def batch_gradient_descent(X, y):
    m = len(X)
    theta = np.zeros((2, 1))
    X_b = np.c_[np.ones((m, 1)), X]

    for i in range(iterations):
        gradients = (2/m) * X_b.T.dot(X_b.dot(theta) - y)
        theta = theta - learning_rate * gradients

    return theta

# Stochastic Gradient Descent
def stochastic_gradient_descent(X, y):
    m = len(X)
    theta = np.zeros((2, 1))
    X_b = np.c_[np.ones((m, 1)), X]

    for epoch in range(iterations):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X_b[random_index:random_index+1]
            yi = y[random_index:random_index+1]

            gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
            theta = theta - learning_rate * gradients

    return theta

# Mini-Batch Gradient Descent
def mini_batch_gradient_descent(X, y):
    m = len(X)
    theta = np.zeros((2, 1))
    X_b = np.c_[np.ones((m, 1)), X]
    batch_size = 10

    for epoch in range(iterations):
        indices = np.random.permutation(m)
        X_shuffled = X_b[indices]
        y_shuffled = y[indices]

        for i in range(0, m, batch_size):
            xi = X_shuffled[i:i+batch_size]
            yi = y_shuffled[i:i+batch_size]

            gradients = (2/len(xi)) * xi.T.dot(xi.dot(theta) - yi)
            theta = theta - learning_rate * gradients

    return theta

# Execute all methods
batch_theta = batch_gradient_descent(X, y)
stochastic_theta = stochastic_gradient_descent(X, y)
mini_batch_theta = mini_batch_gradient_descent(X, y)

# Display results
print("Batch Gradient Descent:")
print("Intercept:", round(batch_theta[0, 0], 4))
print("Slope:", round(batch_theta[1, 0], 4))

print("\nStochastic Gradient Descent:")
print("Intercept:", round(stochastic_theta[0, 0], 4))
print("Slope:", round(stochastic_theta[1, 0], 4))

print("\nMini-Batch Gradient Descent:")
print("Intercept:", round(mini_batch_theta[0, 0], 4))
print("Slope:", round(mini_batch_theta[1, 0], 4))

# Calculate Mean Squared Error
X_b = np.c_[np.ones((len(X), 1)), X]

for name, theta in [
    ("Batch", batch_theta),
    ("Stochastic", stochastic_theta),
    ("Mini-Batch", mini_batch_theta)
]:
    predictions = X_b.dot(theta)
    mse = np.mean((y - predictions) ** 2)
    print(name, "MSE:", round(mse, 4))

print("\nAll Gradient Descent Methods Completed Successfully")
