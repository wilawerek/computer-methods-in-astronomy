#!/usr/bin/python
# Emil Wilawer 2016.10.18
# Factorial of any number n>0
x, n = 1, int(raw_input("Factorial of which positive number you need?  "))
for i in range(1, n+1):
	x*=i
print x
