def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return "Yes, it is a right-angled triangle." if sides[0]**2 + sides[1]**2 == sides[2]**2 else "No, it is not a right-angled triangle."

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print(is_right_triangle(a, b, c))
else:
    print("Invalid triangle. The sum of any two sides must be greater than the third side.")
