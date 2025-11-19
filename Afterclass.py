class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.1416
    
r1 = Rectangle(22.35 , 3)
print(r1.area())
s1 = Square(34)
print(s1.area())
c1 = Circle(35)
print(c1.area())