# Challenge 4 : random walk
import random

from turtle import Turtle,Screen

line = Turtle()
line.pensize(10)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]

for i in range(50):
    line.color(random.choice(colours))
    line.setheading(random.choice(directions))
    line.fd(30)
    line.speed('fast')

screen = Screen()
screen.exitonclick()