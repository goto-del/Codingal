class Bird:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def display_info(self):
        print(f"Details of the bird is {self.name}, {self.color}, {self.age}")

bird1 = Bird("Parrot", "Greenish", 5)
bird1.display_info()
bird2 = Bird("Woodpecker", "Blackish", 6)
bird2.display_info()