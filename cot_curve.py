#cot_curve
import numpy as np
import matplotlib.pyplot as plt
x= np.linspace(0,10,50)
y= np.tan(x)
y=1/y
plt.plot(x,y)
plt.show()
