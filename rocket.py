import numpy as np
#import matplotlib.pyplot as plt
import pylab


z = [(-4,-13), (-8,-13), (-3,-5), (-3,6), (0,10), (3,6), (3,-5), (8,-13), (4,-13), (3,-8), (1,-8), (2,-13), (-2,-13), (-1,-8), (-3,-8), (-3,-13), (-4,-13)]
x = []
y = []

for i, (q, v) in enumerate(z):
    x.append(q)
    y.append(v)

#plt.scatter(x, y)
#plt.show()

pylab.plot(x, y)
pylab.show()
