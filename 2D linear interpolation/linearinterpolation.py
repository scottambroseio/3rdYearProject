class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "X:{:.2f} Y:{:.2f}".format(self.x, self.y)

	def copy(self):
		return Point(self.x, self.y)

def interpolate(pointOne, pointTwo, steps, startEndInclusive):
	# The distances between each point's coordinates in cartasian space
	xDistance = abs(pointOne.x - pointTwo.x)
	yDistance = abs(pointOne.y - pointTwo.y)
	intervals = steps + 1

	xDistancePerStep = xDistance / intervals
	yDistancePerStep = yDistance / intervals

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

		yield interpolatedPoint

	if startEndInclusive:
		yield pointTwo

for point in interpolate(Point(2,-2), Point(10, -10), 7, True):
	print(point)