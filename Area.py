def square_area(side_length):
    return side_length * side_length
def rectangle_area(length, width):
    return length * width
def circle_area(radius):
    import math
    return math.pi * radius * radius
def triangle_area(base, height):
    return 0.5 * base * height

print("Choose the shape to calculate area:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")
choice = input("Enter the number corresponding to the shape: ")
if choice == "1":
    Side = int(input("Enter the side Length of the square: "))
    area = square_area(Side)
    print(f"The area of the square is: {area}")

if choice == "2":
    l = float(input("Enter the side length of the square: "))
    b = float(input("Enter the breadth of the square: "))
    area2 = rectangle_area(l, b)
    print(f"The area of the rectangle is: {area2}")
if choice == "3":
    circle_area = float(input("Enter the radius of the circle: "))
    area3 = circle_area(circle_area)
    print(f"The area of the circle is: {area3}")
if choice == "4":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area4 = triangle_area(base, height)
    print(f"The area of the triangle is: {area4}")
