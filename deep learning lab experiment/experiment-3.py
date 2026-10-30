import numpy as np

steps = np.array([
    3000, 4000, 5000, 6000, 7000,
    8000, 9000, 4500, 5500, 6500,
    7500, 8500, 9500, 3500, 4200,
    5200, 6200, 7200, 8200, 9200,
    4800, 5800, 6800, 7800, 8800,
    9800, 3900, 4900, 5900, 6900
])

first_week = steps[:7]
last_five = steps[-5:]
alternate_days = steps[::2]
reversed_steps = steps[::-1]

print("First Week:", first_week)
print("Last 5 Days:", last_five)
print("Alternate Days:", alternate_days)
print("Reversed Steps:", reversed_steps)

print("Lengths:",
      len(first_week),
      len(last_five),
      len(alternate_days),
      len(reversed_steps))

print("Check:",
      len(first_week) == 7 and
      len(last_five) == 5 and
      len(alternate_days) == 15 and
      len(reversed_steps) == 30)
