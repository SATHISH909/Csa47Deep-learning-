
import numpy as np

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Display matrices
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication (A x B):")
print(multiplication)

# Transpose of Matrix A
transpose_A = np.transpose(A)
print("\nTranspose of Matrix A:")
print(transpose_A)

# Transpose of Matrix B
transpose_B = np.transpose(B)
print("\nTranspose of Matrix B:")
print(transpose_B)

# Analyse the resulting matrices
print("\nOriginal Matrix A Shape:", A.shape)
print("Transpose Matrix A Shape:", transpose_A.shape)
print("Original Matrix B Shape:", B.shape)
print("Transpose Matrix B Shape:", transpose_B.shape)
