import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

###############################################################################
# Create helix:
def make_helix(n):
    theta_max = 8 * np.pi
    theta = np.linspace(0, theta_max, n)
    x, y, z = theta, np.sin(theta), np.cos(theta)
    helix = np.vstack((x, y, z))

    return helix

# Update AUV position for plotting:
def update_auv(num, dataLines, lines) :
    for line, data in zip(lines, dataLines) :
        line.set_data(data[0:2, num-1:num])
        line.set_3d_properties(data[2,num-1:num])
    return lines

# Update trajectory for plotting:
def update_trj(num, dataLines, lines) :
    for line, data in zip(lines, dataLines) :
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2,:num])
    return lines
###############################################################################

# Attach 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Define no. data points and create helix:
n = 100
data = [make_helix(n)]

# Create line objects:
auv = [ax.plot(data[0][0,0:1], data[0][1,0:1], data[0][2,0:1], 'ro')[0]]
trj = [ax.plot(data[0][0,0:1], data[0][1,0:1], data[0][2,0:1])[0]]

# Setthe axes properties
ax.set_xlim3d([0.0, 8*np.pi])
ax.set_xlabel('X')

ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-1.0, 1.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
ani_auv = animation.FuncAnimation(fig, update_auv, n, fargs=(data, auv),
                              interval=50, blit=False) #repeat=False,
ani_trj = animation.FuncAnimation(fig, update_trj, n, fargs=(data, trj),
                              interval=50, blit=False) #repeat=False,
plt.show()