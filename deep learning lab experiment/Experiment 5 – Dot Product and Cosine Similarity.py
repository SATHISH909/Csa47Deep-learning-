
import numpy as np

# Customer preference vectors
customer1 = np.array([4, 3, 2, 5])
customer2 = np.array([3, 4, 2, 4])
customer3 = np.array([1, 2, 5, 3])

# Display customer vectors
print("Customer 1 Preferences:", customer1)
print("Customer 2 Preferences:", customer2)
print("Customer 3 Preferences:", customer3)

# Calculate Dot Products
dot12 = np.dot(customer1, customer2)
dot13 = np.dot(customer1, customer3)
dot23 = np.dot(customer2, customer3)

print("\nDot Product (Customer 1 and 2):", dot12)
print("Dot Product (Customer 1 and 3):", dot13)
print("Dot Product (Customer 2 and 3):", dot23)

# Function to calculate cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Calculate Cosine Similarity
sim12 = cosine_similarity(customer1, customer2)
sim13 = cosine_similarity(customer1, customer3)
sim23 = cosine_similarity(customer2, customer3)

print("\nCosine Similarity (Customer 1 and 2):", round(sim12, 4))
print("Cosine Similarity (Customer 1 and 3):", round(sim13, 4))
print("Cosine Similarity (Customer 2 and 3):", round(sim23, 4))

# Identify most similar customers
similarities = {
    "Customer 1 and 2": sim12,
    "Customer 1 and 3": sim13,
    "Customer 2 and 3": sim23
}

most_similar = max(similarities, key=similarities.get)

print("\nMost Similar Customers:", most_similar)
