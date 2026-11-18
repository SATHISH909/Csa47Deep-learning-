
# Bayes' Theorem

# Given probabilities
prevalence = 0.01
sensitivity = 0.95
specificity = 0.90

# Calculate probability of false positive
false_positive = 1 - specificity

# Calculate probability of positive test
positive_probability = (sensitivity * prevalence) + (false_positive * (1 - prevalence))

# Apply Bayes' theorem
bayes_probability = (sensitivity * prevalence) / positive_probability

# Display results
print("Disease Prevalence:", prevalence)
print("Test Sensitivity:", sensitivity)
print("Test Specificity:", specificity)

print("\nFalse Positive Rate:", false_positive)
print("Probability of Positive Test:", round(positive_probability, 4))

print("\nProbability that patient has disease given positive test:")
print(round(bayes_probability, 4))

print("\nPercentage Probability:")
print(round(bayes_probability * 100, 2), "%")
