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

from turtle import *

drawer = Turtle()
s = Screen()

s.bgcolor("black")

drawer.penup()
drawer.setposition(-20,-350)
drawer.pendown()
drawer.begin_fill()
drawer.color("red")
drawer.circle(300)
drawer.end_fill()
drawer.penup()
drawer.setposition(-20,-260)
drawer.pendown()
drawer.begin_fill()
drawer.color("black")
drawer.circle(230)
drawer.end_fill()
drawer.penup()
drawer.setposition(0,-100)
drawer.pendown()
drawer.begin_fill()
drawer.color("red")
drawer.pensize(2)
drawer.pencolor("grey")
drawer.backward(100)
drawer.left(60)
drawer.backward(200)
drawer.right(60)
drawer.backward(85)
drawer.right(115)
drawer.backward(600)
drawer.right(65)
drawer.backward(130)
drawer.right(90)
drawer.backward(440)
drawer.right(90)
drawer.backward(100)
drawer.right(90)

drawer.backward(65)
drawer.end_fill()
drawer.penup()
drawer.setposition(0,-50)
drawer.pendown()

drawer.pensize(2)


drawer.begin_fill()
drawer.color("black")
drawer.pencolor("grey")
drawer.right(90)

drawer.forward(90)
drawer.right(120)
drawer.forward(170)
drawer.right(150)
drawer.forward(150)
drawer.end_fill()

done()