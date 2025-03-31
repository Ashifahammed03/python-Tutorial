import numpy as np

# Generate two random 3x3 matrices
A = np.random.randint(0, 20, (3, 3))
B = np.random.randint(0, 20, (3, 3))

# Perform matrix addition
C = A + B

# Find the transpose of the result
C_transpose = C.T

# Display results
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Sum of Matrices:\n", C)
print("Transpose of the Sum:\n", C_transpose)
