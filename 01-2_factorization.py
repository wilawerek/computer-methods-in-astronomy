#!/usr/bin/python
# Emil Wilawer 2016.10.18
# Factorization of 123456
x, i, lista = 123456, 1, []
while len(lista) < 27:
	if x%i == 0:
		lista.append(i)
	i+=1
print lista 
