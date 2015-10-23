import sys
sys.path.insert(0, '../Shared')

from pointwithrotation import Point

def interpolate(pointOne, pointTwo, steps, startEndInclusive):
	# The distances between each point's coordinates in cartasian space
	xDistance = abs(pointOne.x - pointTwo.x)
	yDistance = abs(pointOne.y - pointTwo.y)
	zDistance = abs(pointOne.z - pointTwo.z)
	rDistance = abs(pointOne.r - pointTwo.r)
	intervals = steps + 1

	xDistancePerStep = xDistance / intervals
	yDistancePerStep = yDistance / intervals
	zDistancePerStep = zDistance / intervals
	rDistancePerStep = rDistance / intervals

	interpolatedPoint = pointOne.copy()

	if startEndInclusive:
		yield pointOne

	for index in range(0, steps):
		if pointOne.x < pointTwo.x:
			interpolatedPoint.x += xDistancePerStep
		elif pointOne.x > pointTwo.x:
			interpolatedPoint.x -= xDistancePerStep

		if pointOne.y < pointTwo.y:
			interpolatedPoint.y += yDistancePerStep
		elif pointOne.y > pointTwo.y:
			interpolatedPoint.y -= yDistancePerStep	

		if pointOne.z < pointTwo.z:
			interpolatedPoint.z += zDistancePerStep
		elif pointOne.z > pointTwo.z:
			interpolatedPoint.z -= zDistancePerStep	

		if pointOne.r < pointTwo.r:
			interpolatedPoint.r += rDistancePerStep
		elif pointOne.r > pointTwo.r:
			interpolatedPoint.r -= rDistancePerStep	

		yield interpolatedPoint

	if startEndInclusive:
		yield pointTwo

for point in interpolate(Point(0, 0, 0, 0), Point(6, 6, 6, -180), 5, True):
	print(point)