def sum_of_even_numbers(n):
    total = 0
    for _ in range(n):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            total += num
    return total

n = int(input("Enter the number of elements: "))
print("Sum of all even numbers:", sum_of_even_numbers(n))
