import turtle
import random

t = turtle.Turtle()

color = ["red", "blue", "yellow", "green", "purple", "lightblue"]

screen = turtle.Screen()

screen.bgcolor("black")

t.speed(7)

t.hideturtle()

while True:
    for x in range(200):
        t.pencolor(random.choice(color))
        t.width(x/100+1)
        t.forward(x)
        t.left(59)

    t.right(239)
    for x in range(200, 0, -5):
        t.pencolor("black")
        t.width(x/100+7)
        t.forward(x)
        t.right(59)

turtle.done()    