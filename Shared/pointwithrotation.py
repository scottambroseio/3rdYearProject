class Point:
	def __init__(self, x, y, z, rx, ry, rz):
		self.x = x
		self.y = y
		self.z = z
		self.rx = rx
		self.ry = ry
		self.rz = rz

	def __str__(self):
		return "X:{:.2f} Y:{:.2f} Z:{:.2f} RX:{:.2f} RY:{:.2f} RZ:{:.2f}".format(self.x, self.y, self.z, self.rx, self.ry, self.rz)

	def copy(self):
		return Point(self.x, self.y, self.z, self.rx, self.ry, self.rz)

	def __getitem__(self, key):
		return getattr(self, key)

	def __setitem__(self, key, value):
		setattr(self, key, value)