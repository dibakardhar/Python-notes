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

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)
turtle.bgcolor('black')

pen.color("#fff")
pen.pensize(7)
pen.circle(154)
pen.left(90)
pen.penup()
pen.pensize(15)
pen.forward(150)
pen.pendown()
pen.forward(150)
pen.penup()
pen.forward(-150)
pen.left(120)
pen.pendown()
pen.forward(150)
pen.penup()
pen.forward(-150)
pen.left(120)
pen.pendown()
pen.forward(150)
pen.penup()
pen.forward(-150)
pen.left(120)
pen.hideturtle()

turtle.done()