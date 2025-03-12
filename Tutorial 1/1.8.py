def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  # Add the last digit
        number //= 10  # Remove the last digit
    return total

number = int(input("Enter a number: "))

print(f"The sum of the digits is: {sum_of_digits(abs(number))}")

