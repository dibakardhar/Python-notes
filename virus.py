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

import turtle as t

t.speed(10)
t.color('yellow')
t.bgcolor('black')
b = 200

while b > 0:
 	t.left(b)
 	t.forward(b * 3)
 	b = b - 1

t.done()