from math import *
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,24*np.pi,10000)
r=np.exp(np.cos(t))-2*np.cos(4*t) + (np.sin(t/12))**5
plt.polar(t,r,color='red')
plt.show()
x=r*np.cos(t)
y=r*np.sin(t)
plt.plot(x,y,color='blue')
plt.show()
