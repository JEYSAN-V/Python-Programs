import turtle
import time
obj=turtle.Turtle()
obj.speed(100)
obj.color("white")
obj.backward(200)
obj.color("yellow")
obj.pensize(8)
obj.left(108)

def star():
    time.sleep(0.4)
    for _ in range(5):
        obj.forward(200)
        obj.left(144)

    obj.right(108)
    obj.penup()
    obj.forward(250)
    obj.pendown()
    obj.left(108)

def three_star():
    for _ in range(3):
        obj.fillcolor("yellow")
        obj.begin_fill()
        star()
        obj.end_fill()

three_star()

turtle.done()