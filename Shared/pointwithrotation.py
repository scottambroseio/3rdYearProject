class Point:
	def __init__(self, x, y, z, r):
		self.x = x
		self.y = y
		self.z = z
		self.r = r

	def __str__(self):
		return "X:{:.2f} Y:{:.2f} Z:{:.2f} R:{:.2f}".format(self.x, self.y, self.z, self.r)

	def copy(self):
		return Point(self.x, self.y, self.z, self.r)