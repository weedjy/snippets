import math
from pylab import *
import numpy as np
from mpl_toolkits.mplot3d import axes3d 

fig = figure()
q = fig.gca(projection='3d')

x = []
y = []
z = []
i = 0

while i < 20000:
    t = 16.0*math.pi*i/10000.0
    x.append(math.cos(t))
    y.append(0.1*t)
    z.append(math.sin(t))
    i += 1

q.plot(x, y, z)
show()
