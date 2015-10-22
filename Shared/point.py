class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "X:{:.2f} Y:{:.2f}".format(self.x, self.y)

	def copy(self):
		return Point(self.x, self.y)