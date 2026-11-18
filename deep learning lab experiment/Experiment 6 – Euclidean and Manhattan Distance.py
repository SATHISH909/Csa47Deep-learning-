
import numpy as np

# Customer purchasing behaviour data
customer1 = np.array([2, 3, 4])
customer2 = np.array([5, 7, 8])
customer3 = np.array([3, 4, 5])

# Display customer data
print("Customer 1:", customer1)
print("Customer 2:", customer2)
print("Customer 3:", customer3)

# Euclidean Distance Function
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# Manhattan Distance Function
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

# Calculate distances between Customer 1 and Customer 2
e1 = euclidean_distance(customer1, customer2)
m1 = manhattan_distance(customer1, customer2)

# Calculate distances between Customer 1 and Customer 3
e2 = euclidean_distance(customer1, customer3)
m2 = manhattan_distance(customer1, customer3)

# Display results
print("\nCustomer 1 and Customer 2:")
print("Euclidean Distance:", round(e1, 2))
print("Manhattan Distance:", m1)

print("\nCustomer 1 and Customer 3:")
print("Euclidean Distance:", round(e2, 2))
print("Manhattan Distance:", m2)

# Compare distances
print("\nDistance Comparison:")
if e2 < e1:
    print("Customer 1 and Customer 3 are more similar.")
else:
    print("Customer 1 and Customer 2 are more similar.")

print("\nConclusion:")
print("Euclidean Distance measures straight-line distance.")
print("Manhattan Distance measures absolute coordinate differences.")
