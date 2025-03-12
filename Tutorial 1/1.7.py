def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "The point lies in Quadrant 1."
    elif x < 0 and y > 0:
        return "The point lies in Quadrant 2."
    elif x < 0 and y < 0:
        return "The point lies in Quadrant 3."
    elif x > 0 and y < 0:
        return "The point lies in Quadrant 4."
    elif x == 0 and y != 0:
        return "The point lies on the Y-axis."
    elif y == 0 and x != 0:
        return "The point lies on the X-axis."
    else:
        return "The point lies at the origin."

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

print(find_quadrant(x, y))
