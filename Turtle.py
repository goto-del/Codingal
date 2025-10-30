import turtle

t = turtle.Turtle()
t.color("blue")
t.pensize(5)
t.speed(1)

board = turtle.Screen()

board.title("Turtle drawing a square")
board.bgcolor("lightblue")

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.penup()
t.left(90)
t.forward(50)
t.pendown()
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

turtle.done()

