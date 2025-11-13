class fruit:

    def __init__(self, color, name):
        self.color = color
        self.name = name
        print("Object Created")

    
    
    def __del__(self):
        print("Destructor called")

obj = fruit("Red", "Apple")
print(obj.name)
del obj