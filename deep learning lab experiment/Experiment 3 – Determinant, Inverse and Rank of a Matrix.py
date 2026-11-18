
import numpy as np

# Define encryption matrix
A = np.array([[2, 3, 1],
              [4, 1, 5],
              [7, 2, 3]])

print("Encryption Matrix:")
print(A)

# Calculate Determinant
det = np.linalg.det(A)
print("\nDeterminant:")
print(round(det, 2))

# Calculate Inverse
if round(det) != 0:
    inverse = np.linalg.inv(A)
    print("\nInverse Matrix:")
    print(np.round(inverse, 2))
else:
    print("\nInverse does not exist")

# Calculate Rank
rank = np.linalg.matrix_rank(A)
print("\nRank of Matrix:")
print(rank)

# Check suitability for encryption
if round(det) != 0 and rank == 3:
    print("\nMatrix is suitable for encryption")
else:
    print("\nMatrix is not suitable for encryption")
