import sys
sys.path.insert(0, '../Shared')

from pointwithrotation import Point

def interpolate(pointOne, pointTwo, steps, startEndInclusive):
	intervals = steps + 1

	keys = ["x", "y", "z", "rx", "ry", "rz"]

	distances = [abs(pointOne[key] - pointTwo[key]) / intervals for key in keys]

	interpolatedPoint = pointOne.copy()

	if startEndInclusive:
		yield pointOne

	for index in range(0, steps):
		for key in keys:
			if pointOne[key] < pointTwo[key]:
				interpolatedPoint[key] += distances[index]
			elif pointOne.x > pointTwo.x:
				interpolatedPoint[key] -= distances[index]	

		yield interpolatedPoint

	if startEndInclusive:
		yield pointTwo

for point in interpolate(Point(0, 0, 0, 0, 0, 0), Point(6, 6, 6, 180, -180, 180), 5, True):
	print(point)