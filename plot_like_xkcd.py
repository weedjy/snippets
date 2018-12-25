from numpy import *
import math
import scipy.stats as ss
import pylab as plt

plt.xkcd()  #before all of the plots!

dt = 0.001
lx, ly = 1., 0.
x = [1.]
y = [0.]
for i in range(0,50000):
    dx = math.asin(ly/math.sqrt(ly*ly + lx*lx))*dt
    dy = -math.asin(lx/math.sqrt(ly*ly + lx*lx))*dt
    lx += dx
    ly += dy
    x.append(lx)
    y.append(ly)

plt.plot(x, y, color='red')
plt.show()
