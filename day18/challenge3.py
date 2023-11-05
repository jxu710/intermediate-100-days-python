# Challenge 3 : draw different shapes
import random
from turtle import Turtle,Screen



arrow = Turtle()
color_list = ["red" , "green" , "blue","pink","salmon","purple"]
class move :
    def __init__(self, lines):
        self.lines = lines

    def draw(self):
        angle = 360 /self.lines
        self.color =random.choice(color_list)
        for _ in range(self.lines):
            arrow.forward(50)
            arrow.right(angle)
            arrow.color(self.color)
shape1 = move(3)
shape2 = move(4)
shape3 = move (5)
shape4 = move(6)
shape5 = move(7)
shape6 = move(8)

shapes = [shape1,shape2,shape3,shape4,shape5,shape6,]

for item in shapes:
    item.draw()


screen = Screen()
screen.exitonclick()