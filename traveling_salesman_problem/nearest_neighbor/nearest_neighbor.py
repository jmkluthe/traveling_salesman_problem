import math
import string
import csv
import sys
import copy
import time

tnot = time.time()

#transform the input text file into a list
inputfilename = "../test-input-7.txt"

unvisited = []
with open(inputfilename, "r") as f:
    for row in f.readlines():
        if row:
            vals = row.strip().split()
            unvisited.append([vals[0], vals[1], vals[2]])
print(unvisited)


#cityCol = 0
#xCol = 1
#yCol = 2



def findClosest(currCity, unvisited):
	closestCity = None
	closestDistance = float("inf")
	for candCity in unvisited:
		distance = computeDistance(currCity[1], currCity[2], candCity[1], candCity[2])
		if distance < closestDistance:
			closestCityID = candCity[0]
			closestDistance = distance
	#closestData.city = closestCity
	#closestData.distance = closestDistance
	return closestCityID, closestDistance



def computeDistance(currX, currY, candX, candY):
	x = int(currX) - int(candX)
	y = int(currY) - int(candY)
	distance = float(math.sqrt(x*x + y*y))
	distance = int(round(distance))
	#print distance
	return distance



#make the first city in the unvisited list the current city, and remove it from unvisited
currCity = copy.deepcopy(unvisited[0])
#print currCity[0]
unvisited.remove(currCity)
pathLength = 0

#prepare output file
outputfilename = inputfilename + ".tour"
outputfile = open(outputfilename, 'w')
#create space for a pathlength at the top of the file, which will be added when the algorithm is complete
#outputfile.write('\n')

#repeat until all of the cities are visited
while len(unvisited) > 0:
	#find closest city
	closestData = findClosest(currCity, unvisited)
	#make closest city the current city
	currCityID = closestData[0]
	for city in unvisited:
		if city[0] == currCityID:
			currCity = copy.deepcopy(city)
	pathLength = pathLength + closestData[1]
	#add current city to the output tour file and remove it from unvisited list
	#print currCity[0]
	outputfile.write(currCity[0] + '\n')
	unvisited.remove(currCity)

#print pathLength
outputfile.seek(0,0)
outputfile.write(str(pathLength) + '\n')

print(time.time() - tnot)
print(pathLength)

