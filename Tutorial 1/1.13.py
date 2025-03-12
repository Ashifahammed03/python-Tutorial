
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_num = reversed_num * 10 + digit 
        number //= 10  # Remove the last digit
    return reversed_num

num = int(input("Enter a number: "))

reversed_num = reverse_number(num)
print(f"The reversed number is: {reversed_num}")
