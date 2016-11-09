#!/bin/usr/python
# Emil Wilawer 2016-10-25
x='42'
try:
	x_new = int(x)
except ValueError:
	print "Ooops, could not convert to int"
else:
	print "Conversion succesfull: ---", x_new,"---"
finally:
	print "This is executted no matter what"
