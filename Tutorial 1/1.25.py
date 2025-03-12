
def power(X, Y):
    result = 1
    for _ in range(Y):
        result *= X
    return result

X = int(input("Enter the base (X): "))
Y = int(input("Enter the exponent (Y): "))

result = power(X, Y)
print(f"{X} raised to the power {Y} is: {result}")
