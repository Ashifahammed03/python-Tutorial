import math

def sin_series(x, n_terms):
    result = 0
    for n in range(n_terms):
        result += ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
    return result

x = float(input("Enter the value of x (in radians): "))
n_terms = int(input("Enter the number of terms: "))
print(f"sin({x}) up to {n_terms} terms is {sin_series(x, n_terms)}")
