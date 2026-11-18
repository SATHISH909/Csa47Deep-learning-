
# Conditional Probability using Bayes' Theorem

# Probability of production by each machine
P_A = 0.60
P_B = 0.40

# Defect rates of machines
P_D_A = 0.02
P_D_B = 0.05

# Calculate total probability of defective products
P_D = (P_A * P_D_A) + (P_B * P_D_B)

# Calculate conditional probabilities
P_A_D = (P_A * P_D_A) / P_D
P_B_D = (P_B * P_D_B) / P_D

# Display results
print("Machine A Production Probability:", P_A)
print("Machine B Production Probability:", P_B)

print("\nMachine A Defect Rate:", P_D_A)
print("Machine B Defect Rate:", P_D_B)

print("\nTotal Probability of Defective Product:", round(P_D, 4))

print("\nProbability that defective product came from Machine A:")
print(round(P_A_D, 4))

print("\nProbability that defective product came from Machine B:")
print(round(P_B_D, 4))

print("\nPercentage of defective products from Machine A:",
      round(P_A_D * 100, 2), "%")

print("Percentage of defective products from Machine B:",
      round(P_B_D * 100, 2), "%")
