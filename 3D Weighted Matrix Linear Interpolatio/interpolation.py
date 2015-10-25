from sys import path, stderr
path.insert(0, '../Shared')

from point import Point
from statistics import mean
from collections import Sequence

def interpolate(pointOne, pointTwo, steps, startEndInclusive, weights):
	# The distances between each point's coordinates in cartasian space
	if isinstance(weights, Sequence) == False:
		print("The weights provided are not a sequence", file=stderr)
		return

	if validateWeights(weights) == False:
		print("Invalid weights provided", file=stderr)
		return

	intervals = steps + 1

	xDistance, yDistance, zDistance = getDistances(pointOne, pointTwo) 

	xDistancePerStep = xDistance / intervals
	yDistancePerStep = yDistance / intervals
	zDistancePerStep = zDistance / intervals

	interpolatedPoint = pointOne.copy()

	if startEndInclusive:
		yield pointOne

	for index in range(0, steps):
		if pointOne.x < pointTwo.x:
			interpolatedPoint.x += xDistancePerStep * weights[0][index]
		elif pointOne.x > pointTwo.x:
			interpolatedPoint.x -= xDistancePerStep * weights[0][index]

		if pointOne.y < pointTwo.y:
			interpolatedPoint.y += yDistancePerStep * weights[1][index]
		elif pointOne.y > pointTwo.y:
			interpolatedPoint.y -= yDistancePerStep	* weights[1][index]

		if pointOne.z < pointTwo.z:
			interpolatedPoint.z += zDistancePerStep * weights[2][index]
		elif pointOne.z > pointTwo.z:
			interpolatedPoint.z -= zDistancePerStep	* weights[2][index]

		yield interpolatedPoint

	if startEndInclusive:
		yield pointTwo

def getDistances(pointOne, pointTwo):
	return abs(pointOne.x - pointTwo.x), abs(pointOne.y - pointTwo.y), abs(pointOne.z - pointTwo.z)

def validateWeights(weightMatrix):
	return mean([mean(weights) for weights in weightMatrix]) == 1

weightMatrix = [
	[3, 0.5, 0.5, 0.5, 0.5],
	[1, 2, 1, 0.5, 0.5],
	[0.25, 0.25, 4, 0.25, 0.25]
]

for point in interpolate(Point(1, 1, 1), Point(6, 6, 6), 4, True, weightMatrix):
	print(point)




