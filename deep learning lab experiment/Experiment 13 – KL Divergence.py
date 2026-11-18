
import numpy as np

# Actual probability distribution
P = np.array([0.4, 0.3, 0.2, 0.1])

# Predicted probability distribution
Q = np.array([0.3, 0.4, 0.2, 0.1])

# Calculate KL Divergence
def kl_divergence(P, Q):
    return np.sum(P * np.log(P / Q))

# Display distributions
print("Actual Probability Distribution:")
print(P)

print("\nPredicted Probability Distribution:")
print(Q)

# Calculate KL Divergence
kl = kl_divergence(P, Q)

print("\nKL Divergence:")
print(round(kl, 4))

# Analyse the difference
if kl < 0.1:
    print("\nDistributions are very similar.")
elif kl < 0.5:
    print("\nDistributions have a small difference.")
else:
    print("\nDistributions have a large difference.")

print("\nInformation Loss:", round(kl, 4), "nats")
