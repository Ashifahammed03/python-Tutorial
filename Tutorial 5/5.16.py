import numpy as np

# Create two random 3x3 matrices with integers between 0 and 20
matrix1 = np.random.randint(0, 21, (3, 3))
matrix2 = np.random.randint(0, 21, (3, 3))

# Perform matrix addition
addition_result = matrix1 + matrix2

# Perform matrix multiplication
multiplication_result = np.dot(matrix1, matrix2)

# Transpose of the product matrix
transpose_result = multiplication_result.T

# Print results
print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Matrix Addition Result:\n", addition_result)
print("Matrix Multiplication Result:\n", multiplication_result)
print("Transpose of Product Matrix:\n", transpose_result)
