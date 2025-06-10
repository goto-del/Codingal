class fruit:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price



obj = fruit("Apple", "Red", 75)

print(obj.name)
print(obj.price)
print(obj.color)

obj1 = fruit("Banana", "Yellow", 50)

print(obj1.name)
print(obj1.price)
print(obj1.color)

obj2 = fruit("Grapes", "Green", 100)

print(obj2.name)
print(obj2.price)
print(obj2.color)