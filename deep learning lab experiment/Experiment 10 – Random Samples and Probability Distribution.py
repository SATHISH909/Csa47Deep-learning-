
import numpy as np
import matplotlib.pyplot as plt

# Generate random temperature samples
np.random.seed(42)
temperatures = np.random.normal(loc=30, scale=5, size=1000)

# Display sample temperatures
print("First 10 Temperature Samples:")
print(np.round(temperatures[:10], 2))

# Calculate statistical values
mean = np.mean(temperatures)
variance = np.var(temperatures)
std_dev = np.std(temperatures)

print("\nMean Temperature:", round(mean, 2))
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std_dev, 2))

# Calculate probability distribution
hist, bins = np.histogram(temperatures, bins=10)
probability = hist / len(temperatures)

print("\nProbability Distribution:")
for i in range(len(probability)):
    print("Range", round(bins[i], 2), "to",
          round(bins[i+1], 2), ":", round(probability[i], 4))

# Plot histogram
plt.hist(temperatures, bins=20, density=True, edgecolor='black')
plt.title("Temperature Probability Distribution")
plt.xlabel("Temperature")
plt.ylabel("Probability Density")
plt.show()

# Analyse distribution
if 28 <= mean <= 32:
    print("\nGenerated observations follow the expected distribution.")
else:
    print("\nGenerated observations differ from the expected distribution.")
