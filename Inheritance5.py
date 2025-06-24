from abc import ABC, abstractmethod
class Animal(ABC):


    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can crawl")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")


R = Human()
R.move()  # Output: I can walk and run

S = Snake()
S.move()  # Output: I can crawl

D = Dog()
D.move()  # Output: I can bark

L = Lion()
L.move()  # Output: I can roar