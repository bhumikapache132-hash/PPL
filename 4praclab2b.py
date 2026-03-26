import numpy as np

# Input for 5x3 matrix
print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)

# Input for 3x2 matrix
print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

# Convert to numpy arrays
A = np.array(A)
B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Multiplication
product = np.dot(A, B)

print("\nProduct Matrix (5x2):")
print(product)
