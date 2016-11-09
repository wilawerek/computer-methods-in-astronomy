#!/usr/bin/python
# Emil Wilawer 2016.10.19
# Prints n smallest prime numbers
n = int(raw_input("How many prime numbers: "))
prime, number = [2], 3
while len(prime)<n:
	for div in prime:
		if number%div == 0:
			break
		elif div==prime[-1]:
			prime.append(number)
	number+=1			
print prime, len(prime)
