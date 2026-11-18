
import numpy as np

# Actual labels (1 = Spam, 0 = Not Spam)
actual = np.array([1, 0, 1, 1, 0])

# Predicted probabilities
predicted = np.array([0.9, 0.2, 0.8, 0.7, 0.1])

# Calculate Cross-Entropy Loss
epsilon = 1e-15

predicted = np.clip(predicted, epsilon, 1 - epsilon)

loss = -np.mean(
    actual * np.log(predicted) +
    (1 - actual) * np.log(1 - predicted)
)

# Display results
print("Actual Values:", actual)
print("Predicted Probabilities:", predicted)

print("\nCross-Entropy Loss:", round(loss, 4))

# Predict spam or not spam
predicted_labels = (predicted >= 0.5).astype(int)

print("\nPredicted Labels:", predicted_labels)

# Calculate prediction errors
errors = np.abs(actual - predicted_labels)

print("\nPrediction Errors:", errors)
print("Total Prediction Errors:", np.sum(errors))

# Calculate accuracy
accuracy = np.mean(actual == predicted_labels) * 100

print("\nModel Accuracy:", round(accuracy, 2), "%")

if loss < 0.5:
    print("\nModel Prediction Performance: Good")
else:
    print("\nModel Prediction Performance: Needs Improvement")
