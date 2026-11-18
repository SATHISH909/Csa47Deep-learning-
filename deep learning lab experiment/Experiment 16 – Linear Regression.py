
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# House dataset
# Features: Area, Bedrooms, Location Score
X = np.array([
    [1000, 2, 1],
    [1500, 3, 2],
    [1800, 3, 2],
    [2000, 4, 3],
    [2500, 4, 3],
    [3000, 5, 4],
    [1200, 2, 1],
    [2200, 4, 2],
    [2800, 5, 3],
    [1600, 3, 1]
])

# House prices (in lakhs)
y = np.array([25, 35, 42, 50, 65, 80, 30, 55, 72, 38])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict house prices
predictions = model.predict(X)

# Display actual and predicted prices
print("Actual House Prices:")
print(y)

print("\nPredicted House Prices:")
print(np.round(predictions, 2))

# Predict price for a new house
new_house = np.array([[1700, 3, 2]])
new_prediction = model.predict(new_house)

print("\nNew House Details:")
print("Area: 1700 sq.ft")
print("Bedrooms: 3")
print("Location Score: 2")
print("Predicted House Price:", round(new_prediction[0], 2), "Lakhs")

# Evaluate model
mse = mean_squared_error(y, predictions)
mae = mean_absolute_error(y, predictions)
r2 = r2_score(y, predictions)

print("\nMean Squared Error:", round(mse, 2))
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 4))

print("\nLinear Regression Model Completed Successfully")
