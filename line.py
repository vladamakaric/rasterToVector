class Line:
	def __init__(self, origin, normDir):
		self.dir = normDir
		self.origin = origin

	def __eq__(self, other):
		return self.origin == other.origin and self.dir == other.dir

	def __repr__(self):
		return "orig: " + str(self.origin) + " dir: " + str(self.dir)

	@staticmethod
	def createFrom2Endpoints(v1, v2):
		return Line(v1, (v2 - v1).normalize())
