def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10  
        number //= 10 
    return total

number = int(input("Enter a number: "))

print(f"The sum of the digits is: {sum_of_digits(abs(number))}")

