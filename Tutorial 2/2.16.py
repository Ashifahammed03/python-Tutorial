""" Write a menu driven program to implement the following
 i)check even or odd
 ii)check number is positive negative or zero
 iii) generate factors of a number"""

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def generate_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

while True:
    print("\nMenu:")
    print("1. Check if number is even or odd")
    print("2. Check if number is positive, negative, or zero")
    print("3. Generate factors of a number")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        num = int(input("Enter a number: "))
        print(f"{num} is {check_even_odd(num)}")
    elif choice == 2:
        num = int(input("Enter a number: "))
        print(f"{num} is {check_sign(num)}")
    elif choice == 3:
        num = int(input("Enter a number: "))
        print("Factors:", generate_factors(num))
    elif choice == 4:
        break
    else:
        print("Invalid choice, try again.")
