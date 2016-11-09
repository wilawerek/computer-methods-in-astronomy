#!/bin/usr/python
# Emil Wilawer 2016-11-09
# Plots temperature(time) for Poznan, Sept 2016
import datetime as dt
from matplotlib import pyplot as plt

file = open("meteo/data09-2016.csv", "r")
file.readline()
file.readline()
data = file.read().replace(";", " ").split()
file.close()
#
# create lists with date (0), time (1) and temperature (5)
# csv file has 13 parameters, I use 0, 1 and 5th
#
date = data[0::13]
time = data[1::13]
temp = map(float, data[5::13])
#
# table with date and time as datetime 
#
datetimetable = []
for i in range(0,len(date)):
	datetimetable.append(dt.datetime(int(date[i][6:]), int(date[i][3:5]), int(date[i][:2]),
                                     int(time[i][:2]), int(time[i][3:5]), int(time[i][6:])))
datetimetable.sort()

print "TEMPERATURE:"
print "\tMAX = {:5.1f};\t{}".format(max(temp), datetimetable[temp.index(max(temp))])
print "\tMAX = {:5.1f};\t{}".format(min(temp), datetimetable[temp.index(min(temp))])
#
# plot
#
plt.plot(datetimetable, temp, marker='o')
plt.title("METEO: September")
plt.xlabel("TIME")
plt.ylabel("TEMPERATURE")
plt.xticks(rotation='35')
plt.gca().yaxis.grid(True)
plt.show()
