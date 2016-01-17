from line import *
from vec2 import *
import geometry


class LineSegment:
	def __init__(self, a, b):
		self.a = a
		self.b = b


	def isVecProjectionBetweenEndPoints(self, v):
		fromA = v - self.a
		fromB = v - self.b

		aToB = self.b - self.a

		return fromA*aToB >= 0 and fromB*aToB <= 0





