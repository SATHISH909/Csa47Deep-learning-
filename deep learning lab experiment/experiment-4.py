import numpy as np

week1 = np.array([100, 200, 150, 300, 250, 400, 350])
week2 = np.array([120, 180, 130, 320, 200, 450, 300])

total_week1 = np.sum(week1)
total_week2 = np.sum(week2)

change = week2 - week1

fallen_products = np.where(change < 0)[0] + 1

print("Week 1 Sales:", week1)
print("Week 2 Sales:", week2)
print("Week 1 Total:", total_week1)
print("Week 2 Total:", total_week2)
print("Change in Sales:", change)
print("Products Whose Sales Fell:", fallen_products)

print("Check:", np.array_equal(change, week2 - week1))
