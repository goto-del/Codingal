class Robot:
    def __init__(self,name,speed,madein,year,model):
        self.speed = speed
        self.madein = madein
        self.year = year
        self.model = model
        self.name = name

    def introduce(self):
        print(f"Hello My name is {self.name}, I am Made in {self.madein},My speed is {self.speed}, My model is {self.model}, I am made in year {self.year}")

robot1 = Robot("Roboxic", 11, "India", 2025, "Titanium")
robot2 = Robot("Robotic", 4 , "China", 2021, "HIGH-POWER")
robot1.introduce()
robot2.introduce()