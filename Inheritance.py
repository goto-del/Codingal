class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display_info(self):
        return f"Name : {self.name}, ID Number : {self.idnumber}"
    
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)
        self.salary = salary
        self.post = post

    def display_info(self):
        person_info = super().display_info()
        return f"{person_info} Salary : {self.salary}, Post : {self.post}"
    
p1 = Employee("Ram", 1160033, "Rs. 1,00,000", "Senior Accountant")
p2 = Employee("Brian" , 110077, "Rs. 1,00,00,000", "Senior Manager")

print(p1.display_info())
print(p2.display_info())