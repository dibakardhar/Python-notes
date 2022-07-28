#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wolverine
#
# Created:     28-07-2022
# Copyright:   (c) Wolverine 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
turtle.title('Sixteen Petals Flower')
turtle.setworldcoordinates(-2000,-2000,2000,2000)

def draw_flower(x,y,tilt,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)

for tilt in range(0,360,30):
    draw_flower(0,0,tilt,1000)