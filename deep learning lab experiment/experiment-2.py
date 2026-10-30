import numpy as np

roll_numbers = np.arange(1, 61)
time_points = np.linspace(0, 1, 50)
zeros = np.zeros(8)
ones = np.ones(8)

vectors = [roll_numbers, time_points, zeros, ones]

names = ["Roll Numbers", "Time Points", "Zeros", "Ones"]

for name, vector in zip(names, vectors):
    print(name, "Length:", len(vector))
    print(name, "Data Type:", vector.dtype)

print("Check:", len(roll_numbers) == 60)
print("Check:", len(time_points) == 50)
print("Check:", len(zeros) == 8)
print("Check:", len(ones) == 8)
