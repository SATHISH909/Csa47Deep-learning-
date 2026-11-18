
# Gradient Descent Algorithm

# Define quadratic cost function
def cost_function(x):
    return x ** 2

# Define gradient of cost function
def gradient(x):
    return 2 * x

# Initialize parameters
x = 10
learning_rate = 0.1
iterations = 50

print("Initial Value of x:", x)
print("Initial Cost:", cost_function(x))

# Perform Gradient Descent
for i in range(iterations):
    grad = gradient(x)
    x = x - learning_rate * grad

    if (i + 1) % 10 == 0:
        print("Iteration", i + 1,
              "x =", round(x, 4),
              "Cost =", round(cost_function(x), 6))

# Display final result
print("\nFinal Value of x:", round(x, 6))
print("Minimum Cost:", round(cost_function(x), 8))

print("\nGradient Descent Completed Successfully")
