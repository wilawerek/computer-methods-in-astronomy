#!/usr/bin/python
# Emil Wilawer 2016-10-25
# my first plot
from matplotlib import pyplot as plt
import random

x,y = random.sample(xrange(25), 10), random.sample(xrange(25), 10)
print "X:",x
print "Y:",y

plt.plot(x,y, marker='o')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("PLOT: 02-1")
plt.show() 
