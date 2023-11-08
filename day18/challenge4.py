# Challenge 4 : random walk
import random
import turtle

from turtle import Turtle,Screen

turtle.colormode(255)
line = Turtle()
line.pensize(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r,g,b)
    return my_color

directions = [0,90,180,270]

for i in range(50):
    line.color(random_color())
    line.setheading(random.choice(directions))
    line.fd(30)
    line.speed('fast')

screen = Screen()
screen.exitonclick()