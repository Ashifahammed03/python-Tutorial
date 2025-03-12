def compare_numbers(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 < num2:
        return f"{num1} is smaller than {num2}"
    else:
        return f"{num1} is equal to {num2}"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = compare_numbers(num1, num2)
print(result)
