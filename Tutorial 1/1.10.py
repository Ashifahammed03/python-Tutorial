
def sum_of_even_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0: 
            total += number
    return total

N = int(input("Enter the number of elements: "))

numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

sum_even = sum_of_even_numbers(numbers)
print(f"The sum of even numbers is: {sum_even}")

