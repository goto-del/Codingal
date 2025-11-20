class Cat:
    def __init__(self,name , age):
        self.name = name 
        self.age = age

    def display_info(self):
        print(f"I am a Cat ,My name is {self.name}, My age is {self.age}")
    def sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"I am a Dog. My name is {self.name}, My age is {self.age}")

    def sound(self):
        print("Bow")

c1 = Cat("Rori", 5)
d1 = Dog("Leo", 1)
c1.display_info()
d1.display_info()
c1.sound()
d1.sound()