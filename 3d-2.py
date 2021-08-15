from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation


fig = plt.figure()
ax = p3.Axes3D(fig)

q = [[-4.32, -2.17, -2.25, 4.72, 2.97, 1.74],
     [ 2.45, 9.73,  7.45,4.01,3.42,  1.80],[-1.40, -1.76, -3.08,-9.94,-3.13,-1.13]]
v = [[ 0.0068,0.024, -0.014,-0.013, -0.0068,-0.04],[ 0.012,
      0.056, -0.022,0.016,  0.0045, 0.039],
     [-0.0045,  0.031,  0.077,0.0016, -0.015,-0.00012]]

t=np.arange(0, 1000, 2)
x=q[0]
y=q[1]
z=q[2]
s=v[0]
u=v[1]
w=v[2]


points, = ax.plot(x, y, z, '*')

def update_points(t, x, y, z, points):
    point = []
    for i in range(0,len(x)-1,1):
        points.set_data(np.array([x[i]+s[i]*t*5, y[i]+u[i]*t*5]))
        points.set_3d_properties(z[i]+w[i]*t*5, 'z')
    return point

ani=animation.FuncAnimation(fig, update_points, 10, fargs=(x, y, z, points))

plt.show()