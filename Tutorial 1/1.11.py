
def sum_of_cubes_of_even_numbers(n):
    total = 0
    for i in range(2, n+1, 2): 
        total += i**3  # Add the cube of the number
    return total

n = int(input("Enter a positive integer: "))

if n > 0:
    result = sum_of_cubes_of_even_numbers(n)
    print(f"The sum of cubes of all positive even numbers less than or equal to {n} is: {result}")
else:
    print("Please enter a positive integer.")
