import math
def circle_properties(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference
radius = float(input("Enter the radius of the circle: "))
area, circumference = circle_properties(radius)

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
