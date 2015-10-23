class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "X:{:.2f} Y:{:.2f} Z:{:.2f}".format(self.x, self.y, self.z)

	def copy(self):
		return Point(self.x, self.y, self.z)