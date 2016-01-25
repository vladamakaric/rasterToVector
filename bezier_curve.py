import math
from vec2 import *

def _bern3(i,t):
	threeChose_i = 6/(math.factorial(i)*math.factorial(3-i))
	return threeChose_i*( (t**i) * ( (1-t)**(3-i) ) )

def getPointOnCubicBezier(controlPoints, t):
	point = Vec2(0,0)

	for i, cp in enumerate(controlPoints):
		point+=controlPoints[i]*_bern3(i,t)

	return point







