
import numpy as np

# Student examination marks
marks = np.array([75, 80, 85, 90, 70, 95, 88, 78, 82, 92])

# Display student marks
print("Student Marks:")
print(marks)

# Calculate Mean
mean = np.mean(marks)
print("\nMean:", mean)

# Calculate Variance
variance = np.var(marks)
print("Variance:", variance)

# Calculate Standard Deviation
std_deviation = np.std(marks)
print("Standard Deviation:", round(std_deviation, 2))

# Find minimum and maximum marks
print("\nHighest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))

# Analyse student performance
if std_deviation < 10:
    print("\nStudent Performance is Consistent")
else:
    print("\nStudent Performance is Not Consistent")
