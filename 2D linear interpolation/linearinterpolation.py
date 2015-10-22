class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "X:{:.2f} Y:{:.2f}".format(self.x, self.y)

	def copy(self):
		return Point(self.x, self.y)

def interpolate(pointOne, pointTwo, steps):
	xDistance = abs(pointOne.x - pointTwo.x)
	yDistance = abs(pointOne.y - pointTwo.y)
	intervals = steps +1

	xDistancePerStep = xDistance / intervals
	yDistancePerStep = yDistance / intervals

	interpolatedPoint = pointOne.copy()

	print(pointOne)

	for x in range(0, steps):
		interpolatedPoint.x += xDistancePerStep
		interpolatedPoint.y += yDistancePerStep
		print(interpolatedPoint)

	print(pointTwo)

pointOne = Point(0,0) 
pointTwo = Point(3,4)
interpolate(pointOne, pointTwo, 2);