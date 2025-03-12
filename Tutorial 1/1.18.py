def is_armstrong_number(number):
    num_str = str(number)
    n = len(num_str)  

    sum_of_powers = sum(int(digit) ** n for digit in num_str)
    return sum_of_powers == number

number = int(input("Enter a number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
