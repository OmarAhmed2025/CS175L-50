'''
Omar Ahmed
Turtle Graphics Stop Sign
CS175-50L
Spring 2022
'''
import math
import turtle
WINDOW_WIDTH= 400
WINDOW_HEIGHT= 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
MYCOLOR= 'red'
# size the window
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Finding Diameter of Octagon
#s^2 = x^2 + x^2
#s^2 = 2*x^2
LENGTH= 100
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)



#Initialize Turtle
one_turt=turtle.Turtle()
one_turt.fillcolor('red')
one_turt.color('black')
one_turt.penup()
one_turt.goto(-49, 120)
one_turt.pendown()
one_turt.color(MYCOLOR)
one_turt.begin_fill()



for i in range(8):
    one_turt.forward(100)
    one_turt.right(45)

one_turt.end_fill()
one_turt.hideturtle()
#stop text
one_turt.penup()
one_turt.goto(-37.35,-21)
one_turt.color('white')
one_turt.write("STOP", font=("Arial", 30, "normal"))

