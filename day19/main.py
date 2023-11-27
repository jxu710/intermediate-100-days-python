from turtle import Turtle,Screen

josh = Turtle()
screen = Screen()

def move_forward():
    josh.forward(10)

screen.listen()
screen.onkey(key='space',fun = move_forward)

screen.exitonclick()