from numpy import linspace, sin, cos
from pylab import figure, show
from mpl_toolkits.mplot3d import Axes3D

# generating some data
x = linspace(-10,10,100);
y = sin(x);
z = cos(x);

fig = figure()
 
ax = Axes3D(fig)

# plotting the stems
for i in range(len(x)):
  ax.plot([x[i], x[i]], [y[i], y[i]], [0, z[i]], 
          '--', linewidth=2, color='b', alpha=.5)

# plotting a circle on the top of each stem
ax.plot(x, y, z, 'o', markersize=8, 
        markerfacecolor='none', color='b',label='ib')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

show()