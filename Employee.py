class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        print("Object Created")

    def display_info(self):
        print(f"Name : {self.name} , Designation : {self.designation}")


    def __del__(self):
        print("Object Destroyed")

e1 = Employee("Raj", "Sales Associate")
e2 = Employee("Viraj" , "Clerk")

e1.display_info()
e2.display_info()

del e2