class car:
    def __init__ (self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        return f"Details of the car is {self.year} {self.color} {self.make} {self.model}"
    
c1 = car("Toyota", "Camry", 2020, "Red")
print(c1.display_info())