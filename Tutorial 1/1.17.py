
def print_multiplication_tables(n):
    for i in range(1, n + 1):
        print(f"Multiplication table of {i}:")
        for j in range(1, 11): 
            print(f"{i} x {j} = {i * j}")
        print()  
n = int(input("Enter a number n: "))

print_multiplication_tables(n)
