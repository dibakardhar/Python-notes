from math import tan
from math import cos
g=9.8
print('The value of g=%0.2f meter/sec^2'%g)
v_0=float(input("The initial velocity is="))
print('The value of v_0=%0.2f meter/sec^2'%v_0)
y_0=float(input("The initial height is="))
print('The value of y_0=%0.2f meter'%y_0)
A=int(input("angle with x axis="))
print('The value of A=%0.2f rad'%A)
x=float(input("Value of x ="))
print('The value of x=%0.2f meter'%x)
y=(x*tan(A))-((1/(2*v_0**2))*((g*x**2)/(cos(A)**2)))+y_0
print('The value of y=%0.2f meter'%y)