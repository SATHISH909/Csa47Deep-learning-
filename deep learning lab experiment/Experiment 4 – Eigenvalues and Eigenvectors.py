
import numpy as np

# Create transition matrix
A = np.array([[0.5, 0.2, 0.3],
              [0.3, 0.4, 0.3],
              [0.2, 0.4, 0.4]])

# Display transition matrix
print("Transition Matrix:")
print(A)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(np.round(eigenvalues, 4))

print("\nEigenvectors:")
print(np.round(eigenvectors, 4))

# Identify the dominant eigenvalue
index = np.argmax(np.abs(eigenvalues))
print("\nDominant Eigenvalue:")
print(round(eigenvalues[index].real, 4))

# Identify the most important web page
importance = np.abs(eigenvectors[:, index].real)
importance = importance / np.sum(importance)

print("\nPage Importance Scores:")
for i, score in enumerate(importance):
    print("Web Page", i + 1, ":", round(score, 4))

print("\nMost Important Web Page:")
print("Web Page", np.argmax(importance) + 1)
