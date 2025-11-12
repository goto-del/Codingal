class Student:
    def __init__(self, name, age, DOB):
        self.name = name
        self.age = age
        self.DOB = DOB

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Date of Birth: {self.DOB}")
    
    
st1 = Student("Elias", 10, "2015/07/27")
st1.display_info()

st2 = Student("Anna", 16, "2009/02/17")
st2.display_info()