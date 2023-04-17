import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

from data_loader import Frame


def display_frames_path(frames):
    x = [0,1,2]
    y = [0,1,2]
    z = [0,1,2]
    for i in frames:
        x.append(i.pose[0])
        y.append(i.pose[1])
        z.append(i.pose[2])
    fig = plt.figure()
    ax1 = Axes3D(fig)
    fig.add_axes(ax1)
    ax1.scatter3D(x, y, z, c='g', s=2)
    # ax1.plot3D(np.array(x), np.array(y), np.array(z), 'gray')
    plt.axis('equal')
    plt.show()




