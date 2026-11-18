
import numpy as np

# Create two 3D vectors
vector1 = np.array([2, 3, 4])
vector2 = np.array([1, 2, 3])

# Display original vectors
print("First Vector:", vector1)
print("Second Vector:", vector2)

# Vector Addition
addition = np.add(vector1, vector2)
print("\nVector Addition:", addition)

# Vector Subtraction
subtraction = np.subtract(vector1, vector2)
print("Vector Subtraction:", subtraction)

# Scalar Multiplication
scalar = 2
multiplication = np.multiply(vector1, scalar)
print("Scalar Multiplication:", multiplication)

# Calculate new robot position
new_position = vector1 + vector2
print("New Robot Position:", new_position)
