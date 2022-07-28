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

colors = ["cyan","yellow","blue","green","white","red"]

p = turtle.Pen()
turtle.bgcolor("black")

for i in range(300):
    p.pencolor(colors[i%6])
    p.width(i/100+2)
    p.forward(i)
    p.left(59)