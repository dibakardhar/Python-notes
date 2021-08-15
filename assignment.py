import numpy as np
import matplotlib.pyplot as plt
# Create 10 random coordinates in cartesian coordinate

points = np.random.randint(-10, 10, size=(10, 2))
x, y = points[:, 0], points[:, 1]
# Coprdinate Transformation
'''
Function defination is not required, since, we have made use of numpy array vectorized opration
'''
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y,x)

# Plotting
fig = plt.figure(figsize=(9,5))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122, projection='polar')
ax1.scatter(x, y, c = theta, cmap='hsv', alpha=1)
ax1.title.set_text('Cartesian coordinate')
ax1.set_xlabel('$X$')
ax1.set_ylabel('$Y$')
ax1.grid()

ax2.scatter(theta, r, c= theta,cmap='hsv', alpha=0.75)
ax2.title.set_text('Polar coordinate')