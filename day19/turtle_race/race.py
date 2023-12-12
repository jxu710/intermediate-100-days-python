from turtle import Turtle,Screen

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a clor:")
colors=["red","orange","yellow","green","blue","purple"]

#
# nick = Turtle(shape="turtle")
# nick.penup()
# nick.goto(x=-230,y=0)

position_x = -230
position_y = -150
for i in range (len(colors)):
    nick = Turtle(shape="turtle")
    nick.penup()
    nick.color(colors[i])
    nick.goto(position_x,position_y)
    position_y += 50



screen.exitonclick()


