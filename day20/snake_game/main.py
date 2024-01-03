from turtle import Turtle,Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nico's snake game")

for i in range(3):
    square = Turtle(shape="square")
    square.color("white")
    square.goto(x=(i*-20), y=0)





screen.exitonclick()