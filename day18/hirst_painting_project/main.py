# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# new_colors = []
# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r,g,b)
#     new_colors.append(color_tuple)
#     # or bew method works the same
#     # new_colors.append(color.rgb[:])

color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]
import turtle as t
import  random

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.goto(-300,-100)

num_of_dots = 100
for dot in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)













screen = t.Screen()
screen.exitonclick()
