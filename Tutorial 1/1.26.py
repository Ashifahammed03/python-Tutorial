import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = map(float, input("Enter the coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of the second point (x2 y2): ").split())

dist = distance(x1, y1, x2, y2)

print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {dist}")

