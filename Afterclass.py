#HELP me
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

rec1 = Rectangle(10, 5)
print("Area of Rectangle:", rec1.area())
sq1 = Square(4)
print("Area of Square:", sq1.area())
cir1 = Circle(3)
print("Area of Circle:", cir1.area())
tri1 = Triangle(6, 8)
print("Area of Triangle:", tri1.area())