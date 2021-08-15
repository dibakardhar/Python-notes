#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DIBAKAR
#
# Created:     02-06-2020
# Copyright:   (c) DIBAKAR 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from math import*
a=float(input("Enter the first number= "))
b=float(input("Enter the second number= "))
print("------------------------------")
print("1.--Addition")
print("2.--Subtraction")
print("3.--Division")
print("4.--Multiplication")
print("_____________________________________")
c=int(input("Enter your choice="))

if c == 1 :
    d=a+b
    print("The addition is= %f"%d)
elif c == 2:
    e=a-b
    printf("The subtraction is= %f"%e)
elif c==3:
    f=a/b
    print("The division is= %0.3f"%f)
elif c==4:
    g=a*b
    print("The multiplication is= %0.3f"%g)
else:
    print("You entered a wrong choice")

print("thank you.....")

