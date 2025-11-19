class Parent:
    def __init__(self,name , age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name : {self.name}, Age : {self.age}"
    
class Child(Parent):
    def __init__(self, name, age, school):
        super().__init__(name,age)
        self.school = school
    
    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info}, School : {self.school}"
    
c1 = Child("Elias", 10 , "ITL Public School")
print(c1.display_info())