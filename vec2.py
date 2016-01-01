import math
import copy

class Vec2:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def norm(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		norm = self.norm()
		x = self.x/norm
		y = self.y/norm
		return Vec2(x,y)

	def inner(self, other):
		return self.x*other.x + self.y*other.y

	def __mul__(self, other):
		if type(other) == type(self):
			return self.inner(other)
		elif type(other) == type(1) or type(other) == type(1.0):
			return Vec2(self.x*other, self.y*other)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __div__(self, other):
		if type(other) == type(1) or type(other) == type(1.0):
			return Vec2(self.x/other, self.y/other)

	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		""" Returns the vector difference of self and other """
		return Vec2(self.x - other.x, self.y - other.y)

	def __repr__(self):
		return "x: " + str(self.x) + " y: " + str(self.y)

	def __eq__(self, other): 
			return self.x == other.x and self.y == other.y

	def __ne__(self, other): 
			return not self == other

