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

	for _ in range(0, steps):
		for key, i in zip(keys, range(0, 6)):
			if pointOne[key] < pointTwo[key]:
				interpolatedPoint[key] += distances[i]
			elif pointOne[key] > pointTwo[key]:
				interpolatedPoint[key] -= distances[i]	

		yield interpolatedPoint

	if startEndInclusive:
		yield pointTwo

for point in interpolate(Point(0, 0, 0, 0, 0, 0), Point(6, 6, 6, 180, -180, 180), 5, True):
	print(point)