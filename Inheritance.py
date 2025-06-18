class Vehicle():

    def __init__(self, fare):
        self.fare = fare

class Normal(Vehicle):

    def __init__(self, fare):
        super().__init__(fare)
        fare = 50
    def get_fare(self):
        return self.fare
print("Normal fare:", Normal(50).get_fare()) 
class Volvo(Vehicle):

    def __init__(self, fare):
        super().__init__(fare)
        fare = 100
    def get_fare(self):
        return self.fare + (self.fare * 0.2)
print("Volvo fare:", Volvo(100).get_fare())
