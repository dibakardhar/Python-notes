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
from turtle import *
import math
window = turtle.Screen()
window.bgcolor("black")
color('orange', 'yellow')

begin_fill()

while True:
  forward(350)
  left(170)
  right(280)
  if abs(pos()) < 1:
    break

end_fill()
done()