#!/usr/bin/python
# Emil Wilawer 2016.10.19
# Counts quantity of every word in given text
text = open('cwiczenie1.txt', 'r').read()
words = text.split()
dictionary = {}
for word in words:
	if word in dictionary:
		dictionary[word]+=1
	else:
		dictionary[word]=1

result = sorted(dictionary.items(), key=lambda (k,v): v, reverse=True)

print "Most occuring words\n"
for word, quantity in result[:5]:
	print word,"-",quantity,"times"
text.close()
