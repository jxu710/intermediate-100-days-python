import random
import turtle

from turtle import Turtle,Screen

circle = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r,g,b)
    return my_color

turtle.colormode(255)

for item in range (36):
    circle.color(random_color())
    circle.circle(100)
    circle.setheading(item*10)
    circle.speed('fastest')





screen = Screen()
screen.exitonclick()