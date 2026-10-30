import numpy as np

a = np.array([10, 20, 30, 40, 50])

mean = np.mean(a)
minimum = np.min(a)
maximum = np.max(a)
std_dev = np.std(a)
max_index = np.argmax(a)

# Manual scan to find maximum index
manual_index = 0
for i in range(1, len(a)):
    if a[i] > a[manual_index]:
        manual_index = i

print("Vector:", a)
print("Mean:", mean)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Standard Deviation:", std_dev)
print("NumPy Maximum Index:", max_index)
print("Manual Maximum Index:", manual_index)

print("Check:", max_index == manual_index)
