from turtle import *

josh = Turtle()
screen = Screen()

def move_forward():
    josh.forward(10)

def move_backward():
    josh.backward(10)

def move_right():
    josh.right(10)

def move_left():
    josh.left(10)

def clear():
    josh.clear()
    josh.penup()
    josh.home()
    josh.pendown()




screen.listen()
screen.onkey(key='w',fun = move_forward)
screen.onkey(key='s',fun = move_backward)
screen.onkey(key='d',fun = move_right)
screen.onkey(key='a',fun = move_left)
screen.onkey(key='c',fun = clear)

screen.exitonclick()