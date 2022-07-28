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
import time

# create a screen
screen = turtle.getscreen()

# set background color of screen
screen.bgcolor("white")

# set tile of screen
screen.title("American Flag")

t = turtle.Turtle()
# set the cursor/turtle speed. Higher value, faster is the turtle
t.speed(100)
t.penup()

# decide the shape of cursor/turtle
t.shape("turtle")

# flag height to width ratio is 1:1.9
flag_height = 250
flag_width = 475

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -237
start_y = 125

# For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
stripe_height = flag_height/13
stripe_width = flag_width

# length of one arm of star
star_size = 10


def draw_fill_rectangle(x, y, height, width, color):
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.end_fill()
    t.penup()

def draw_star(x,y,color,length) :
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.color(color)
    for turn in range(0,5) :
        t.forward(length)
        t.right(144)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.penup()


# this function is used to create 13 red and white stripes of flag
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 13 stripes, 7 red and 6 white
    # so we first create, 6 red and 6 white stripes alternatively
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
            # decrease value of y by stripe_height
            y = y - stripe_height

    # create last red stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
    y = y - stripe_height


# this function create navy color square
# height = 7/13 of flag_height
# width = 0.76 * flag_height
# check references section for these values
def draw_square():
    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height
    draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')


def draw_six_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 112
    # create 5 rows of stars
    for row in range(0,5) :
        x = -222
        # create 6 stars in each row
        for star in range (0,6) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines


def draw_five_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        x = -206
        # create 5 stars in each row
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines

# start after 5 seconds.
time.sleep(5)
# draw 13 stripes
draw_stripes()
# draw squares to hold stars
draw_square()
# draw 30 stars, 6 * 5
draw_six_stars_rows()
# draw 20 stars, 5 * 4. total 50 stars representing 50 states of USA
draw_five_stars_rows()
# hide the cursor/turtle
t.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()